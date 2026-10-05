// Disambiguating sound-alike spellings with a word-frequency list. A port of
// src/sinhala_orthography/lexicon.py.
//
// The converter produces one spelling per input. Several Sinhala letter groups are pronounced
// alike (G-SP-01), and some choices are lexical (sanyaka vs nasal cluster, ං vs න්, ෛ vs අයි …),
// so a romanization alone cannot always pick the standard spelling. This module:
//
// 1. folds words to a *sound key* that erases the distinctions speakers do not hear or do not
//    write in Latin script (aspiration, ණ/න, ළ/ල, ශ/ෂ/ස, ද/ඩ, vowel length, sanyaka vs cluster …);
// 2. returns the words of a frequency list that share the input's sound key, most frequent first;
// 3. keeps the converter's own spelling first when the romanization contains an explicit marker
//    for a distinction (a capital, a z- prefix, a doubled vowel …) and that spelling is a word;
// 4. writes the words in the style the converter options ask for (restyle()), so a word list in
//    the usual style (කෲර, කර්ම) does not undo rakaransayaU, repayaZwj or classical (ක්‍රූර, කර්‍ම).
import { BANDI, toSinhala, type Options } from "./romanization.js";

const HAL = "්";
const ZWJ = "‍";

// --- 1. normalisation of lexicon spellings ----------------------------------------------------

const JOIN = new RegExp(`([ක-ෆ])${HAL}(?!${ZWJ})(?=([යර]))`, "g"); // lookahead: ය/ර may start the next join

/** C ් ය / C ් ර takes ZWJ, except after ර (G-HC-14, R-09) and C ් ර after ම න ල (R-07). */
const joins = (c: string, next: string): boolean => c !== "ර" && !(next === "ර" && "මනල".includes(c));

/** Restore the mandatory ZWJ in yansaya and rakaransaya, for word lists that dropped it. */
export function normalize(word: string): string {
  return word.replace(JOIN, (_, c: string, next: string) => c + HAL + (joins(c, next) ? ZWJ : ""));
}

// --- 1b. converter options applied to lexicon spellings ----------------------------------------

const GAETTA = /([ක-ෆ])([ෘෲ])/g;
const REPAYA = new RegExp(`ර${HAL}(?!${ZWJ})(?=[ක-ෆ])`, "g");
const CLUSTER = new RegExp(`([ක-ෆ])${HAL}(?!${ZWJ})(?=([ක-ෆ]))`, "g");

/**
 * Write a word in the style the converter options choose, as toSinhala() would: rakaransaya + u
 * for C + ෘ/ෲ except after ර (R-06), ZWJ repaya (R-08), the classical bandi akuru pairs (R-10).
 * `archaic` changes no spelling. With no options the word is returned unchanged.
 */
export function restyle(word: string, options: Options = {}): string {
  if (options.rakaransayaU)
    word = word.replace(GAETTA, (m, c: string, sign: string) =>
      c === "ර" ? m : c + HAL + ZWJ + "ර" + (sign === "ෘ" ? "ු" : "ූ"));
  if (options.repayaZwj) word = word.replace(REPAYA, "ර" + HAL + ZWJ);
  if (options.classical)
    word = word.replace(CLUSTER, (_, c: string, next: string) => c + HAL + (BANDI.has(c + next) ? ZWJ : ""));
  return word;
}

const unique = (words: string[]) => [...new Set(words)];

// --- 2. sound key --------------------------------------------------------------------------------

const FOLD_SEQ: [string, string][] = [
  // composite vowels first
  ["ෛ", "යි"], ["ඓ", "අයි"], ["ෞ", "වු"], ["ඖ", "අවු"],
  ["ෘ", HAL + "රු"], ["ෲ", HAL + "රු"], ["ඍ", "රු"], ["ඎ", "රු"],
  ["ඥ", "ග" + HAL + "න"], // G-NS-12: gn
  // sanyaka → nasal + stop (R-03)
  ["ඟ", "න" + HAL + "ග"], ["ඦ", "න" + HAL + "ජ"], ["ඬ", "න" + HAL + "ද"], ["ඳ", "න" + HAL + "ද"], ["ඹ", "ම" + HAL + "බ"],
  ["ං", "න" + HAL], ["ඞ" + HAL, "න" + HAL], // R-11
];
const FOLD_CHAR: Record<string, string> = {
  // aspirates → plain (G-SP-01, G-SP-06)
  ඛ: "ක", ඝ: "ග", ඡ: "ච", ඣ: "ජ", ඨ: "ට", ඪ: "ද", ථ: "ත", ධ: "ද", ඵ: "ප", භ: "බ",
  ඩ: "ද", // R-01: d is written for both in informal romanization
  ණ: "න", ළ: "ල", ශ: "ස", ෂ: "ස", ඤ: "න", // G-SP-02…05, G-NS-13
  // vowel length and ae/e (G-SP-07, G-TY-04, G-TY-07)
  ආ: "අ", ඊ: "ඉ", ඌ: "උ", ඒ: "එ", ඕ: "ඔ", ඇ: "එ", ඈ: "එ",
  "ා": "", "ී": "ි", "ූ": "ු", "ේ": "ෙ", "ෝ": "ො", "ැ": "ෙ", "ෑ": "ෙ",
  [ZWJ]: "",
};

/** Fold a Sinhala word so that spellings which sound alike get the same key. */
export function soundKey(text: string): string {
  for (const [a, b] of FOLD_SEQ) text = text.split(a).join(b);
  let out = "";
  for (const ch of text) out += Object.prototype.hasOwnProperty.call(FOLD_CHAR, ch) ? FOLD_CHAR[ch] : ch;
  return out;
}

// --- 3. lexicon ------------------------------------------------------------------------------------

const LINE_BREAK = /\r\n|[\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029]/;
const byCode = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

/**
 * A word-frequency list indexed by sound key. Pass the text of a "word<TAB>count" file, or
 * [word, count] pairs. Copies of a list without ZWJ are repaired on load (see normalize()).
 */
export class Lexicon {
  /** word → frequency */
  readonly count = new Map<string, number>();
  readonly byKey = new Map<string, string[]>();
  readonly keys: string[];

  constructor(source: string | Iterable<readonly [string, number]>) {
    const add = (word: string, n: number) => {
      const w = normalize(word);
      this.count.set(w, (this.count.get(w) ?? 0) + n);
    };
    if (typeof source === "string") {
      for (const line of source.split(LINE_BREAK)) {
        const tab = line.indexOf("\t");
        const word = tab < 0 ? line : line.slice(0, tab);
        const n = tab < 0 ? "" : line.slice(tab + 1);
        if (word && /^[0-9]+$/.test(n)) add(word, parseInt(n, 10));
      }
    } else {
      for (const [word, n] of source) if (word) add(word, n);
    }
    for (const w of this.count.keys()) {
      const k = soundKey(w);
      const list = this.byKey.get(k);
      if (list) list.push(w);
      else this.byKey.set(k, [w]);
    }
    for (const ws of this.byKey.values()) ws.sort((a, b) => this.count.get(b)! - this.count.get(a)!);
    this.keys = [...this.byKey.keys()].sort(byCode);
  }

  /** Words whose sound key is exactly `key`, most frequent first. */
  exact(key: string): string[] {
    return this.byKey.get(key) ?? [];
  }

  /** Words whose sound key starts with `key`, in key order. */
  prefix(key: string, limit = 200): string[] {
    let lo = 0;
    let hi = this.keys.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (this.keys[mid] < key) lo = mid + 1;
      else hi = mid;
    }
    const out: string[] = [];
    for (let i = lo; i < this.keys.length && this.keys[i].startsWith(key) && out.length < limit; i++)
      out.push(...this.byKey.get(this.keys[i])!);
    return out;
  }
}

// Romanization markers that pin down a distinction the sound key erases. When one is present
// and the converter's spelling is a word, that spelling outranks frequency.
const EXPLICIT = /[KCGJTDNLPBSWVUIEOAXRMH]|z[a-zA-Z]|aa|ii|uu|ee|oo|ae|thh|dh|kh|gh|chh|jh|ph|bh|x/;

export interface CandidateOptions extends Options {
  /** Maximum number of spellings (default 5). */
  limit?: number;
  /** Treat the input as an incomplete word and return completions. */
  partial?: boolean;
}

/**
 * Ranked Sinhala spellings for a romanized word (or a word prefix with partial: true). Words are
 * ranked by frequency, then written in the style of the options (restyle()).
 */
export function candidates(lex: Lexicon, roman: string, options: CandidateOptions = {}): string[] {
  const { limit = 5, partial = false, ...convert } = options;
  const spelled = toSinhala(roman, convert);
  const key = soundKey(spelled);
  const rank = (ws: string[]) =>
    [...new Set(ws)].sort((a, b) => lex.count.get(b)! - lex.count.get(a)! || byCode(a, b));
  if (partial) {
    // An incomplete word: its last consonant may still take a vowel, so drop a trailing hal.
    const words = rank(lex.prefix(key.endsWith(HAL) ? key.slice(0, -HAL.length) : key));
    return unique(words.map((w) => restyle(w, convert))).slice(0, limit);
  }
  let ranked = unique(rank(lex.exact(key)).map((w) => restyle(w, convert)));
  if (ranked.includes(spelled) && EXPLICIT.test(roman)) {
    ranked = [spelled, ...ranked.filter((w) => w !== spelled)]; // explicit markers beat frequency
  } else if (!ranked.includes(spelled)) {
    ranked.push(spelled); // the rule-based spelling is always included
  }
  return ranked.slice(0, limit);
}
