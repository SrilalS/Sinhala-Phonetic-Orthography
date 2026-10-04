// Runs the converter for the playground with the TypeScript package in js/, which is
// golden-tested against the Python reference (src/sinhala_orthography), so the playground
// behaves exactly like both packages.
import { TABLES as SEQUENCE_TABLES, toSinhala, tokenize } from "../../../../js/src/index";
import { charName } from "./unicode-names";

export const TABLES = SEQUENCE_TABLES;

export type Token = { seq: string; kind: string; letter: string; sign?: string; vowel?: string };
export type Explained = {
  output: string;
  words: { input: string; output: string; tokens: Token[]; chars: { ch: string; cp: string; name: string }[] }[];
};
/** The option names as they appear in the playground URL (?o=repaya_zwj,…), like the Python package. */
export type Options = { archaic: boolean; repaya_zwj: boolean; classical: boolean; rakaransaya_u: boolean };

function convertOptions(o: Options) {
  return { archaic: o.archaic, repayaZwj: o.repaya_zwj, classical: o.classical, rakaransayaU: o.rakaransaya_u };
}

/** The tokens of one word for display, including the characters the converter drops (a stray z). */
function tokens(word: string, archaic: boolean): Token[] {
  const out: Token[] = [];
  let i = 0;
  const dropped = (ch: string) => out.push({ seq: ch, kind: "dropped", letter: ch });
  for (const t of tokenize(word, archaic)) {
    while (!word.startsWith(t.seq, i)) dropped(word[i++]);
    i += t.seq.length;
    if (t.kind === "C") out.push({ seq: t.seq, kind: "consonant", letter: t.letter });
    else if (t.kind === "V") out.push({ seq: t.seq, kind: "vowel", letter: t.independent, sign: t.sign, vowel: t.vowel });
    else if (t.kind === "LIT") out.push({ seq: t.seq, kind: "literal", letter: t.seq });
    else out.push({ seq: t.seq, kind: "sign", letter: t.output });
  }
  while (i < word.length) dropped(word[i++]);
  return out;
}

function chars(text: string) {
  return [...text].map((ch) => ({
    ch,
    cp: "U+" + ch.codePointAt(0)!.toString(16).toUpperCase().padStart(4, "0"),
    name: charName(ch),
  }));
}

/** Convert a text and explain each word: its tokens and the code points of its output. */
export function explain(text: string, o: Options): Explained {
  const opts = convertOptions(o);
  const words = text.split(/\s+/).filter(Boolean).map((w) => {
    const output = toSinhala(w, opts);
    return { input: w, output, tokens: tokens(w, o.archaic), chars: chars(output) };
  });
  return { output: toSinhala(text, opts), words };
}
