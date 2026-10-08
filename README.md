# Sinhala Phonetic Orthography

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23244126.svg)](https://doi.org/10.5281/zenodo.23244126)
[![npm](https://img.shields.io/npm/v/sinhala-orthography)](https://www.npmjs.com/package/sinhala-orthography)

A sourced study of how Sinhala words are built in writing, from the letter inventory and
vowel signs to conjuncts, nasals, phonotactics and sandhi. It also covers how Sinhala is
romanized, and specifies a phonetic romanization whose output provably obeys the
orthographic rules.

- 📚 **Research:** seven topic studies with about 250 numbered rules, each citing its sources
  (Unicode, SLS 1134, the ICANN Sinhala script panel, peer-reviewed linguistics and NLP papers,
  and school-level grammar material).
- 🧾 **Rule set:** the studies merged into one deduplicated list of 88 rules, each marked
  HARD (invariant), SOFT (tendency) or STYLE (accepted variants).
- 🔤 **Data:** all 923 Sinhala letter forms, each with a validity status and the rules behind it.
- 🧪 **Reference code:** a romanization-to-Sinhala converter and a frequency-based
  disambiguator, verified against the rules over 3.98 million inputs, in Python and in TypeScript.
- 🌐 **Website:** <https://srilals.github.io/Sinhala-Phonetic-Orthography/>: the studies, a playground
  that runs the converter in the browser, and an explorer for all 923 letter forms. In English
  and [Sinhala](https://srilals.github.io/Sinhala-Phonetic-Orthography/si/) (සිංහලෙන්).

---

## Contributions

The individual facts about Sinhala spelling are known; what this work adds is putting them together
in a form that can be checked:

1. **A sourced, consolidated rule set.** Seven topic studies merged into 88 rules, each marked HARD
   (invariant), SOFT (tendency) or STYLE (accepted variant) and traced to its sources.
2. **A validity status for all 923 Sinhala letter forms**, with the rules behind each, and the
   ෘ / ෲ columns checked against a 2.1M-word frequency list.
3. **A phonetic romanization with machine-checked guarantees.** Every letter form the rules allow
   can be typed (791 / 791), and no input of up to three sequences produces a form the rules
   forbid: 0 violations over 3.98 million inputs, under each of the six option sets.
4. **Measured, reproducible evidence.** How Sinhala is written and romanized, counted from pinned
   public sources (the NLPC 2.1M-word list, the Dakshina corpus, a dated Sinhala Wikipedia dump).
   One script recomputes every number quoted in the studies.
5. **Open reference implementations** in Python and TypeScript, golden-tested against each other,
   with a frequency lexicon that resolves the ~14 groups of sound-alike letters: 27 of 27
   everyday words come out right, against 9 of 27 for the rules alone.

---

## Contents

| | Path | What |
|---|---|---|
| 🧾 | [docs/00-rules.md](docs/00-rules.md) | **Start here.** The consolidated rule set (G-* rules) |
| 🔤 | [docs/01-inventory.md](docs/01-inventory.md) | Letter inventory: Unicode block, alphabets through history, classification, numerals |
| 🅰️ | [docs/02-vowel-signs.md](docs/02-vowel-signs.md) | Vowel signs, normalization, consonant × vowel validity, glides, length |
| 🔗 | [docs/03-hal-conjuncts.md](docs/03-hal-conjuncts.md) | Hal, ZWJ, yansaya / rakaransaya / repaya, bandi akuru, touching letters, clusters |
| 👃 | [docs/04-nasals-and-spelling-distinctions.md](docs/04-nasals-and-spelling-distinctions.md) | ං ඃ ඁ, sanyaka letters, nasal consonants, ණ/න, ළ/ල, ශ/ෂ/ස |
| 📏 | [docs/05-phonotactics-sandhi-spelling.md](docs/05-phonotactics-sandhi-spelling.md) | Syllable structure, sandhi, schwa (letter-to-sound) rules, spelling conventions, loanwords |
| 🌐 | [docs/06-romanization.md](docs/06-romanization.md) | Formal romanizations (ISO 15919, Sri Lanka national system, ALA-LC …) and measured informal romanization |
| ✍️ | [docs/07-phonetic-romanization.md](docs/07-phonetic-romanization.md) | A grammar-correct phonetic romanization: tables, conversion rules, conventions, evaluation |
| 🇱🇰 | [docs/si/](docs/si) | Sinhala translations of 00 to 07 (සිංහල පරිවර්තනය), with the translation glossary. English is authoritative |
| 📊 | [data/letters.json](data/letters.json) | 923 letter forms: 18 vowels, 3 signs, 41 × 19 consonant forms, 41 × 3 conjuncts |
| ✅ | [data/validity.json](data/validity.json) | Status of each form: `valid` · `loan` · `rare` · `unattested` · `never`, with rule IDs |
| 🗺️ | [data/romanization-coverage.json](data/romanization-coverage.json) | Romanizations that produce each form, per option set |
| 📖 | [data/examples.json](data/examples.json) | A few frequent words that contain each form, from a word-frequency list |
| 🐍 | [src/sinhala_orthography/](src/sinhala_orthography) | Inventory, converter (`to_sinhala`), sound key and disambiguator (`Lexicon`, `candidates`) |
| 🟦 | [js/](js) | The same package in TypeScript (`toSinhala`, `Lexicon`, `candidates` …), golden-tested against the Python |
| 🛠️ | [tools/](tools) | Builders and the exhaustive rule checker |
| 📈 | [reports/romanization-check.md](reports/romanization-check.md) | Coverage and safety results ([සිංහලෙන්](reports/romanization-check.si.md)) |
| 🔢 | [reports/corpus-counts.md](reports/corpus-counts.md) | Every corpus number in the studies (claims CC-01…), with its source and definition |
| 🌐 | [website/](website) | The documentation site (VitePress). `npm install`, then `npm run dev` |

---

## Key findings

1. **ZWJ is spelling, not rendering.** Yansaya and rakaransaya need ZWJ, and its position
   picks conjunct vs touching style. Repaya and other conjuncts are optional (G-EN-07…09, G-HC-11…15).
2. **ෛ has no canonical decomposition.** ෙ + ෙ is a different, silently wrong string (G-EN-03).
3. **Sanyaka letters (ඟ ඦ ඬ ඳ ඹ) never take hal and never start a word.** Whether a word uses
   one or a nasal cluster is lexical: කඳ "trunk" ≠ කන්ද "hill" (G-HC-06, G-NS-07/08).
4. **About 14 letter groups are pronounced alike** (aspirates, ණ/න, ළ/ල, ශ/ෂ/ස …). No rule
   can recover their spelling from sound; a frequency lexicon must (G-SP-01).
5. **Two vowels are never written side by side.** Hiatus takes a ය / ව glide: "ai" is අයි, not
   අඉ, and ෛ / ෞ belong to Sanskrit loans (G-VS-03, G-VS-06, G-VS-11).
6. **/kru/ is written කෘ, not ක්‍රු.** Rakaransaya + ු/ූ is the Unicode illustration of
   *krūra*, but writers use C + ෘ/ෲ (කෲර 1,667 vs ක්‍රූර 9 in a 2.1M-word list), or the
   wrong look-alike ක්‍රෑර. Several fonts don't draw the rakaransaya + ූ shape at all (G-VS-15).
7. **Informal romanization differs from formal systems.** `d` is ද 99% of the time,
   `ee` means ී 38% of the time, and vowel length is rarely marked (G-TY-01…10).

---

## Quick start

JavaScript and TypeScript ([npm](https://www.npmjs.com/package/sinhala-orthography), no dependencies):

```sh
npm install sinhala-orthography
```

```js
import { toSinhala } from "sinhala-orthography";
toSinhala("lankaava");   // 'ලංකාව'
```

Python: requires Python 3.9 or later. No dependencies.

```python
import sys; sys.path.insert(0, "src")
from sinhala_orthography import to_sinhala, Lexicon, candidates

to_sinhala("lankaava")   # 'ලංකාව'
to_sinhala("kruura")     # 'කෲර'
to_sinhala("lait")       # 'ලයිට්'

lex = Lexicon("path/to/word-frequency-list.tsv")    # "word<TAB>count" per line
candidates(lex, "honda")                            # ['හොඳ', ...]
```

Rebuild the data and run the checks:

```sh
python tools/build_data.py            # data/letters.json, data/validity.json
python tools/check_romanization.py    # coverage + exhaustive safety (about 20 s)
python tools/build_examples.py LIST   # data/examples.json from a "word<TAB>count" list
python tools/build_spec_tables.py     # tables in docs/07
python tools/check_translations.py    # Sinhala translations whose English source changed
python tools/build_js_golden.py       # golden files for the TypeScript port; then `npm test` in js/
python -m unittest discover tests     # set SINHALA_WORD_LIST to also run the lexicon tests
python tools/corpus_counts.py         # every corpus number in docs/ (downloads the sources once)
```

On Windows consoles, set `PYTHONIOENCODING=utf-8` first.

### Reproducing the corpus numbers

`tools/corpus_counts.py` downloads three public sources once into `.cache/corpus/` (about 2 GB to
download, 300 MB kept), checks them against pinned hashes, and writes
[reports/corpus-counts.md](reports/corpus-counts.md). The studies cite its claim ids (CC-02 …) for
aggregate numbers, and write a single word's count as "NLPC n".
The sources are not redistributed here and keep their own licenses:

| Source | Pinned at | Used for |
|---|---|---|
| University of Moratuwa NLPC [Word Frequency List for Sinhala](https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala) (Fernando and Dias, ICON 2021) | commit `1283550a3389` | spelling frequencies, the lexicon evaluation |
| [Dakshina dataset](https://github.com/google-research-datasets/dakshina) v1.0, Sinhala (Roark et al., LREC 2020) | release v1.0 | how native speakers romanize each letter |
| [Sinhala Wikipedia](https://dumps.wikimedia.org/siwiki/20261001/) pages-articles dump | 2026-10-01 | article counts of competing spellings |

`python tools/corpus_counts.py --lookup WORD …` prints the NLPC count of any word.

---

## Status and limitations

- School textbooks (NIE), the final SLS 1134:2004/2011 texts and the 1989 *Sinhala Lekhana Rīthiya*
  could not be consulted. School-level spelling rules rest on agreeing secondary sources and are
  marked with their confidence.
- The consonant × vowel validity table is a synthesis of the sources, not a corpus count, except
  for the ෘ / ෲ columns (CC-04).
- The corpus counts come from news text (NLPC), carefully romanized Wikipedia sentences
  (Dakshina) and Wikipedia. Chat and other informal registers may differ.
- Every topic file ends with its open questions and conflicting sources. Corrections are welcome.

---

## Citation

Archived on Zenodo: [doi:10.5281/zenodo.23244126](https://doi.org/10.5281/zenodo.23244126) (all versions; v0.2.0 is
[doi:10.5281/zenodo.23244127](https://doi.org/10.5281/zenodo.23244127)). See [CITATION.cff](CITATION.cff).

```bibtex
@software{siriwardhana_sinhala_phonetic_orthography,
  author    = {Siriwardhana, Srilal},
  title     = {Sinhala Phonetic Orthography: a sourced rule set for Sinhala word
               construction and phonetic romanization},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23244126},
  url       = {https://doi.org/10.5281/zenodo.23244126}
}
```

## License

[MIT](LICENSE). Quoted source material remains under its original terms; quotations are
kept under 15 words and every source is cited.
