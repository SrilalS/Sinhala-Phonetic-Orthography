// Sinhala orthography and phonetic romanization: inventory, rules, conversion, disambiguation.
// A port of the Python package sinhala_orthography (the reference implementation).
export { toSinhala, tokenize, TABLES, type Options, type Token } from "./romanization.js";
export { Lexicon, candidates, normalize, restyle, soundKey, type CandidateOptions } from "./lexicon.js";
export { CONSONANTS, SIGNS, VOWELS, codepoints, entries, type Entry } from "./inventory.js";

export const VERSION = "0.1.0";
