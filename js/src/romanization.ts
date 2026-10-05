// Phonetic romanization → Sinhala script. A port of src/sinhala_orthography/romanization.py,
// which is the reference: the output must match it exactly (test/golden.test.mjs).
//
// The romanization is defined by the sequence tables (data.ts) and specified in
// docs/07-phonetic-romanization.md. The converter is a longest-match tokenizer followed by one
// left-to-right pass that decides vowel signs, hal, ZWJ joins, glides and nasal assimilation.
// Every output satisfies the hard orthographic rules of docs/00-rules.md.
import { CONSONANT_TABLE, SPECIAL_TABLE, VOWEL_TABLE } from "./data.js";

export interface Options {
  /** Allow ඏ ඐ ෟ ෳ ඎ ඁ ඦ and touching letters (R-14). */
  archaic?: boolean;
  /** Write repaya as ර්‍ + C instead of plain ර් + C (R-08). */
  repayaZwj?: boolean;
  /** ZWJ conjuncts for the classical bandi akuru pairs (R-10), and rakaransaya after ම න ල (R-07). */
  classical?: boolean;
  /** Write C + r + u/uu as rakaransaya + ු/ූ (ක්‍රූර) instead of the usual ෘ/ෲ (කෲර) (R-06). */
  rakaransayaU?: boolean;
}

const HAL = "්";
const ZWJ = "‍";
const ANUSVARA = "ං";
const SANYAKA = new Set("ඟඦඬඳඹ");
const NO_HAL = new Set([...SANYAKA, "ළ"]); // G-HC-06, G-HC-07
const NGA = "ඞ"; // G-HC-08: only as ඞ්
const PLAIN: Record<string, string> = { ඟ: "ග", ඦ: "ජ", ඬ: "ඩ", ඳ: "ද", ඹ: "බ" }; // G-PH-01
const PLAIN_BEFORE_RA = new Set("මනල"); // R-07: C ් ර after ම න ල is plain hal (දුම්රිය, හෙන්රි)
const VELARS = new Set("කඛගඝ"); // R-11: n + velar → ං
const GAETTA: Record<string, string> = { u: "ෘ", uu: "ෲ" }; // R-06, G-VS-15
// C-13: ෘ / ෲ only after the consonants where the form is attested (validity.json: valid, loan or rare)
const GAETTA_AFTER: Record<string, Set<string>> = { u: new Set("කගඝජටඩතදධනපබභමවශසහෆ"), uu: new Set("කගටඩතදපබම") };
const FRONT = new Set(["i", "ii", "e", "ee", "ae", "aee", "ai"]);
const BACK = new Set(["u", "uu", "o", "oo", "au"]);
/** The classical bandi akuru pairs (first + second consonant). */
export const BANDI: ReadonlySet<string> = new Set(["කෂ", "කව", "ගධ", "ටඨ", "තථ", "තව", "දධ", "දව", "නථ", "නද", "නධ", "නව", "ඤච"]); // G-HC-15

export type Token =
  | { kind: "C"; seq: string; letter: string }
  | { kind: "V"; seq: string; vowel: string; independent: string; sign: string }
  | { kind: "ANUS" | "VIS" | "CANDRA" | "TOUCH"; seq: string; output: string }
  | { kind: "LIT"; seq: string };

const has = (o: object, k: string) => Object.prototype.hasOwnProperty.call(o, k);

const SPECIAL_KIND: Record<string, "ANUS" | "VIS" | "CANDRA" | "TOUCH"> = {
  "ං": "ANUS", "ඃ": "VIS", "ඁ": "CANDRA", touch: "TOUCH",
};

/** All sequences for this mode, longest first (ties keep table order). */
function sequences(archaic: boolean): [string, Token][] {
  const seqs: [string, Token][] = [];
  for (const [seq, letter, mode] of CONSONANT_TABLE)
    if (mode === "normal" || archaic) seqs.push([seq, { kind: "C", seq, letter }]);
  for (const [seq, vowel, independent, sign, mode] of VOWEL_TABLE)
    if (mode === "normal" || archaic) seqs.push([seq, { kind: "V", seq, vowel, independent, sign }]);
  for (const [seq, output, mode] of SPECIAL_TABLE)
    if (mode === "normal" || archaic) seqs.push([seq, { kind: SPECIAL_KIND[output], seq, output }]);
  const order = new Map(seqs.map(([k], n) => [k, n]));
  return seqs.sort((a, b) => b[0].length - a[0].length || order.get(a[0])! - order.get(b[0])!);
}

const SEQUENCES = { false: sequences(false), true: sequences(true) };

/**
 * Split a romanization into the longest matching sequences. Characters outside the tables
 * become LIT tokens, except a stray "z" (an unknown z-combination), which is dropped.
 */
export function tokenize(source: string, archaic = false): Token[] {
  const table = SEQUENCES[archaic ? "true" : "false"];
  const toks: Token[] = [];
  let i = 0;
  outer: while (i < source.length) {
    for (const [seq, tok] of table) {
      if (source.startsWith(seq, i)) {
        toks.push(tok);
        i += seq.length;
        continue outer;
      }
    }
    const ch = source[i];
    if (ch !== "z") toks.push({ kind: "LIT", seq: ch });
    i += 1;
  }
  return toks;
}

/** G-VS-06: ය after front vowels, ව after back; after a/aa, decided by the next vowel. */
function glide(prevVowel: string | null, vowel: string) {
  if (prevVowel !== null && FRONT.has(prevVowel)) return "ය";
  if (prevVowel !== null && BACK.has(prevVowel)) return "ව";
  return FRONT.has(vowel) ? "ය" : "ව";
}

/** Convert a romanized word or text to Sinhala script. */
export function toSinhala(source: string, options: Options = {}): string {
  const { archaic = false, repayaZwj = false, classical = false, rakaransayaU = false } = options;
  const toks = tokenize(source, archaic);
  const out: string[] = [];
  // state: null (word start), "V" (ends in a vowel; prevVowel set), "ANUS", "HAL"
  let state: null | "V" | "ANUS" | "HAL" = null;
  let prevVowel: string | null = null;
  let j = 0;
  while (j < toks.length) {
    const tok = toks[j];
    const nxt = j + 1 < toks.length ? toks[j + 1] : null;
    const nk = nxt ? nxt.kind : null;

    if (tok.kind === "C") {
      let letter = tok.letter;
      const seq = tok.seq;
      const after = j + 2 < toks.length ? toks[j + 2] : null;
      if (state === null && has(PLAIN, letter)) letter = PLAIN[letter];
      if (letter === NGA && nk === "V") {
        if (state === null) { // G-PH-01: ඞ never starts a word
          out.push(seq); state = null; j += 1; continue;
        }
        letter = "ඟ"; // G-HC-08: /ŋ/ + vowel is written ඟ
      }
      if (letter === NGA && state === null) { out.push(seq); j += 1; continue; }
      // R-11: n + velar after a vowel → ං; word-final "ng" → ං
      if (letter === "න" && seq === "n" && state === "V" && nxt?.kind === "C" && VELARS.has(nxt.letter)) {
        out.push(ANUSVARA); state = "ANUS";
        if (nxt.seq === "g" && (after === null || after.kind === "LIT")) { j += 2; continue; }
        j += 1; continue;
      }
      out.push(letter);
      if (nxt?.kind === "V") {
        out.push(nxt.sign); state = "V"; prevVowel = nxt.vowel;
        j += 2; continue;
      }
      if (nk === "ANUS" || nk === "VIS" || nk === "CANDRA") {
        state = "V"; prevVowel = "a"; // ං/ඃ need a vowel base: keep inherent a
        j += 1; continue;
      }
      if (nxt?.kind === "C") {
        const nl = nxt.letter;
        if (NO_HAL.has(letter) || SANYAKA.has(nl)) { // no hal here: keep inherent a
          state = "V"; prevVowel = "a"; j += 1; continue;
        }
        if (letter === NGA) {
          out.push(HAL);
        } else if (nl === "ය") {
          out.push(letter !== "ර" || repayaZwj ? HAL + ZWJ : HAL); // G-HC-11, G-HC-14, R-09
        } else if (nl === "ර") {
          const vowel = after?.kind === "V" ? after.vowel : null;
          const ru = vowel !== null && has(GAETTA, vowel);
          const attested = ru && GAETTA_AFTER[vowel].has(letter); // C-13: මෘ, not ලෘ
          if (attested && !rakaransayaU) {
            out.push(GAETTA[vowel]); // G-VS-15, R-06
            state = "V"; prevVowel = vowel;
            j += 3; continue;
          }
          // R-07: plain hal after ම න ල (දුම්රිය, දිල්රුක්ෂි), except a rakaransaya that stands for an
          // attested ෘ (rakaransayaU: ම්‍රුදු) or, without u, under classical (තාම්‍ර)
          const plain = letter === "ර" || (PLAIN_BEFORE_RA.has(letter) && !attested && !(classical && !ru));
          out.push(plain ? HAL : HAL + ZWJ); // G-HC-12, R-07
        } else if (letter === "ර") {
          out.push(repayaZwj ? HAL + ZWJ : HAL); // R-08
        } else if (classical && BANDI.has(letter + nl)) {
          out.push(HAL + ZWJ); // R-10
        } else {
          out.push(HAL);
        }
        state = "HAL"; j += 1; continue;
      }
      if (nk === "TOUCH" && after?.kind === "C" && !NO_HAL.has(letter)) {
        out.push(ZWJ + HAL); state = "HAL"; j += 2; continue;
      }
      // end of word
      if (NO_HAL.has(letter)) {
        state = "V"; prevVowel = "a";
      } else {
        out.push(HAL); state = "HAL";
      }
      j += 1; continue;
    }

    if (tok.kind === "V") {
      const { vowel, sign } = tok;
      if (state === "V") {
        out.push(glide(prevVowel, vowel) + sign);
        state = "V"; prevVowel = vowel;
      } else if (state === "ANUS") {
        out[out.length - 1] = "ම" + sign; // G-NS-04: ං never before a vowel
        state = "V"; prevVowel = vowel;
      } else {
        // G-VS-08: ඎ is archaic
        out.push(vowel === "ruu" && !archaic ? "ඍ" : tok.independent);
        state = "V"; prevVowel = vowel;
      }
      j += 1; continue;
    }

    if (tok.kind === "ANUS" || tok.kind === "VIS" || tok.kind === "CANDRA") {
      if (tok.kind === "ANUS" && nxt?.kind === "C" && SANYAKA.has(nxt.letter)) {
        j += 1; continue; // G-NS-09: the sanyaka already carries the nasal
      }
      if (state === "V") {
        out.push(tok.output); state = tok.kind === "ANUS" ? "ANUS" : "V";
      } else {
        out.push(tok.seq); state = null; // no base: leave the romanization as written
      }
      j += 1; continue;
    }

    if (tok.kind === "TOUCH") {
      out.push("+"); state = null; j += 1; continue;
    }

    out.push(tok.seq); state = null; prevVowel = null; // LIT
    j += 1;
  }
  return out.join("");
}

/** The sequence tables, for building cheat sheets. */
export const TABLES = { consonants: CONSONANT_TABLE, vowels: VOWEL_TABLE, specials: SPECIAL_TABLE };
