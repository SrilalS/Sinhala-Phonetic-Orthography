// The Sinhala letter inventory: independent vowels, signs, consonants, vowel forms, conjuncts.
// A port of src/sinhala_orthography/inventory.py. IDs follow docs/01-inventory.md; consonants
// are in Unicode (alphabet) order, U+0D9A to U+0DC6.

const HAL = "්";
const ZWJ = "‍";

/** [id, independent vowel, dependent sign]. "" = inherent a; HAL = no vowel. */
export const VOWELS: readonly (readonly [string, string | null, string])[] = [
  ["hal", null, HAL], ["a", "අ", ""], ["aa", "ආ", "ා"], ["ae", "ඇ", "ැ"], ["aee", "ඈ", "ෑ"],
  ["i", "ඉ", "ි"], ["ii", "ඊ", "ී"], ["u", "උ", "ු"], ["uu", "ඌ", "ූ"],
  ["ru", "ඍ", "ෘ"], ["ruu", "ඎ", "ෲ"], ["ilu", "ඏ", "ෟ"], ["iluu", "ඐ", "ෳ"],
  ["e", "එ", "ෙ"], ["ee", "ඒ", "ේ"], ["ai", "ඓ", "ෛ"],
  ["o", "ඔ", "ො"], ["oo", "ඕ", "ෝ"], ["au", "ඖ", "ෞ"],
];

/** [id, letter] for the 41 consonants. */
export const CONSONANTS: readonly (readonly [string, string])[] = [
  ["ka", "ක"], ["kha", "ඛ"], ["ga", "ග"], ["gha", "ඝ"], ["nga", "ඞ"], ["nnga", "ඟ"],
  ["ca", "ච"], ["cha", "ඡ"], ["ja", "ජ"], ["jha", "ඣ"], ["nya", "ඤ"], ["jnya", "ඥ"], ["nyja", "ඦ"],
  ["tta", "ට"], ["ttha", "ඨ"], ["dda", "ඩ"], ["ddha", "ඪ"], ["nna", "ණ"], ["nndda", "ඬ"],
  ["ta", "ත"], ["tha", "ථ"], ["da", "ද"], ["dha", "ධ"], ["na", "න"], ["nda", "ඳ"],
  ["pa", "ප"], ["pha", "ඵ"], ["ba", "බ"], ["bha", "භ"], ["ma", "ම"], ["mba", "ඹ"],
  ["ya", "ය"], ["ra", "ර"], ["la", "ල"], ["va", "ව"],
  ["sha", "ශ"], ["ssa", "ෂ"], ["sa", "ස"], ["ha", "හ"], ["lla", "ළ"], ["fa", "ෆ"],
];

/** [id, sign] */
export const SIGNS: readonly (readonly [string, string])[] = [["anusvara", "ං"], ["visarga", "ඃ"], ["candrabindu", "ඁ"]];

export interface Entry {
  id: string;
  kind: "vowel" | "sign" | "syllable" | "conjunct";
  text: string;
  vowel?: string;
  consonant?: string;
  conjunct?: "yansaya" | "rakaransaya" | "repaya";
  codepoints: string[];
}

export function codepoints(text: string): string[] {
  return [...text].map((ch) => "U+" + ch.codePointAt(0)!.toString(16).toUpperCase().padStart(4, "0"));
}

/** Every letter form: 18 vowels, 3 signs, 41 × 19 syllables, 41 × 3 conjuncts (923). */
export function entries(): Entry[] {
  const rows: Omit<Entry, "codepoints">[] = [];
  for (const [vid, independent] of VOWELS)
    if (independent) rows.push({ id: `vowel.${vid}`, kind: "vowel", text: independent, vowel: vid });
  for (const [sid, text] of SIGNS) rows.push({ id: `sign.${sid}`, kind: "sign", text });
  for (const [cid, letter] of CONSONANTS)
    for (const [vid, , sign] of VOWELS)
      rows.push({ id: `${cid}.${vid}`, kind: "syllable", text: letter + sign, consonant: cid, vowel: vid });
  for (const [cid, letter] of CONSONANTS) {
    rows.push({ id: `${cid}.yansaya`, kind: "conjunct", text: letter + HAL + ZWJ + "ය", consonant: cid, conjunct: "yansaya" });
    rows.push({ id: `${cid}.rakaransaya`, kind: "conjunct", text: letter + HAL + ZWJ + "ර", consonant: cid, conjunct: "rakaransaya" });
    rows.push({ id: `${cid}.repaya`, kind: "conjunct", text: "ර" + HAL + ZWJ + letter, consonant: cid, conjunct: "repaya" });
  }
  return rows.map((r) => ({ ...r, codepoints: codepoints(r.text) }));
}
