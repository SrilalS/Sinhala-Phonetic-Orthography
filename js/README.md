# sinhala-orthography

[![npm](https://img.shields.io/npm/v/sinhala-orthography)](https://www.npmjs.com/package/sinhala-orthography)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23244126.svg)](https://doi.org/10.5281/zenodo.23244126)

Sinhala phonetic romanization, letter inventory and spelling disambiguation for JavaScript and
TypeScript. No dependencies; works in Node.js and the browser.

This is a port of the Python package of the same name, which is the reference implementation of
[Sinhala Phonetic Orthography](https://srilals.github.io/Sinhala-Phonetic-Orthography/), a sourced
study of Sinhala orthography. Both packages read the same sequence tables, and a golden test
checks that this port gives exactly the Python output for more than 50,000 inputs.

```sh
npm install sinhala-orthography
```

## Converting romanization

```js
import { toSinhala } from "sinhala-orthography";

toSinhala("lankaava");                          // 'ලංකාව'
toSinhala("kruura");                            // 'කෲර'
toSinhala("kruura", { rakaransayaU: true });    // 'ක්‍රූර'
toSinhala("lait");                              // 'ලයිට්'
toSinhala("akShara", { classical: true });      // 'අක්‍ෂර'
toSinhala("karma", { repayaZwj: true });        // 'කර්‍ම'
```

Characters outside the sequence tables (spaces, digits, punctuation) pass through unchanged.
Every output obeys the hard rules of the
[rule set](https://srilals.github.io/Sinhala-Phonetic-Orthography/rules), checked exhaustively
over every input of up to three sequences.

| Option | Effect | Convention |
|---|---|---|
| `archaic` | Allow ඏ ඐ ෟ ෳ, standalone ඎ, ඁ, ඦ and touching letters | R-14 |
| `repayaZwj` | Write repaya as ර්‍ + C instead of plain ර් + C | R-08 |
| `classical` | ZWJ conjuncts for the classical bandi akuru pairs, and rakaransaya after ම න ල | R-07, R-10 |
| `rakaransayaU` | Write C + r + u/uu as rakaransaya + ු/ූ (ක්‍රූර) instead of the usual C + ෘ/ෲ (කෲර) | R-06 |
| `retroflexD` | `d` types ඩ and `dh` types ද (`D` ඪ, `Dh` ධ), the older keyboard convention | R-01 |

The romanization (sequence tables, conversion rules, conventions) is specified in
[07 · Phonetic romanization](https://srilals.github.io/Sinhala-Phonetic-Orthography/research/phonetic-romanization).
Try it in the [playground](https://srilals.github.io/Sinhala-Phonetic-Orthography/playground).

`tokenize(text, archaic?)` returns the longest-match tokens with the Latin sequence of each, and
`TABLES` holds the sequence tables, for building cheat sheets.

## Disambiguating with a word list

About 14 groups of Sinhala letters sound alike, so one romanization can't always pick the
standard spelling. `Lexicon` indexes a word-frequency list by sound key, and `candidates()` ranks
the words that share the input's key.

```js
import { Lexicon, candidates } from "sinhala-orthography";
import { readFileSync } from "node:fs";

const lex = new Lexicon(readFileSync("word-frequency-list.tsv", "utf-8")); // "word<TAB>count" lines
candidates(lex, "honda");                   // ['හොඳ', …]
candidates(lex, "hon", { partial: true });  // completions of a word prefix
```

| Export | What |
|---|---|
| `new Lexicon(source)` | `source` is the text of a "word<TAB>count" list, or `[word, count]` pairs. `.count` (Map word → frequency), `.exact(key)`, `.prefix(key, limit = 200)` |
| `candidates(lex, roman, { limit = 5, partial = false, ...options })` | Ranked spellings. The converter's own spelling is always included; when the romanization has an explicit marker (a capital, a `z` prefix, a doubled vowel …) and that spelling is a word or a lone vowel letter (`R` ඍ, `E` ඓ), it comes first |
| `soundKey(text)` | The text folded so sound-alike spellings match. `soundKey("හොඳ")` is `'හොන්ද'` |
| `normalize(word)` | Restores the mandatory ZWJ in C ් ය and C ් ර (never after ර), for word lists that dropped it |
| `restyle(word, options)` | A word in the style of the converter options (ක්‍රූර for කෲර with `rakaransayaU` …). `candidates()` applies it, so the word list never undoes an option |

## Letter inventory

```js
import { VOWELS, CONSONANTS, SIGNS, entries } from "sinhala-orthography";

entries().length;   // 923
entries()[30];      // { id: 'ka.ru', kind: 'syllable', text: 'කෘ', consonant: 'ka', vowel: 'ru',
                    //   codepoints: ['U+0D9A', 'U+0DD8'] }
```

## Development

The package lives in `js/` of the
[research repository](https://github.com/SrilalS/Sinhala-Phonetic-Orthography). The Python package
in `src/sinhala_orthography/` is the reference: change it (and its tables) first, then run
`python tools/build_js_golden.py` and make `npm test` pass here.

```sh
npm install
npm test    # builds, then runs the API and golden tests
```

## License

MIT
