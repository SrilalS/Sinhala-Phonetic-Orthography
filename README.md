# Sinhala Phonetic Orthography

A sourced study of how Sinhala words are built in writing, from the letter inventory and
vowel signs to conjuncts, nasals, phonotactics and sandhi. It also covers how Sinhala is
romanized, and specifies a phonetic romanization whose output provably obeys the
orthographic rules.

- 📚 **Research:** seven topic studies with about 250 numbered rules, each citing its sources
  (Unicode, SLS 1134, the ICANN Sinhala script panel, peer-reviewed linguistics and NLP papers,
  and school-level grammar material).
- 🧾 **Rule set:** the studies merged into one deduplicated list of 87 rules, each marked
  HARD (invariant), SOFT (tendency) or STYLE (accepted variants).
- 🔤 **Data:** all 923 Sinhala letter forms, each with a validity status and the rules behind it.
- 🧪 **Reference code:** a romanization-to-Sinhala converter and a frequency-based
  disambiguator, verified against the rules over 2.69 million inputs.

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
| 📊 | [data/letters.json](data/letters.json) | 923 letter forms: 18 vowels, 3 signs, 41 × 19 consonant forms, 41 × 3 conjuncts |
| ✅ | [data/validity.json](data/validity.json) | Status of each form: `valid` · `loan` · `rare` · `unattested` · `never`, with rule IDs |
| 🗺️ | [data/romanization-coverage.json](data/romanization-coverage.json) | Romanizations that produce each form, per option set |
| 🐍 | [src/sinhala_orthography/](src/sinhala_orthography) | Inventory, converter (`to_sinhala`), sound key and disambiguator (`Lexicon`, `candidates`) |
| 🛠️ | [tools/](tools) | Builders and the exhaustive rule checker |
| 📈 | [reports/romanization-check.md](reports/romanization-check.md) | Coverage and safety results |

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
6. **Informal romanization differs from formal systems.** `d` is ද 99% of the time,
   `ee` means ී 40% of the time, and vowel length is rarely marked (G-TY-01…10).

---

## Quick start

Requires Python 3.9 or later. No dependencies.

```python
import sys; sys.path.insert(0, "src")
from sinhala_orthography import to_sinhala, Lexicon, candidates

to_sinhala("lankaava")   # 'ලංකාව'
to_sinhala("kruura")     # 'ක්‍රූර'
to_sinhala("lait")       # 'ලයිට්'

lex = Lexicon("path/to/word-frequency-list.tsv")    # "word<TAB>count" per line
candidates(lex, "honda")                            # ['හොඳ', ...]
```

Rebuild the data and run the checks:

```sh
python tools/build_data.py            # data/letters.json, data/validity.json
python tools/check_romanization.py    # coverage + exhaustive safety (about 20 s)
python tools/build_spec_tables.py     # tables in docs/07
python -m unittest discover tests     # set SINHALA_WORD_LIST to also run the lexicon tests
```

On Windows consoles, set `PYTHONIOENCODING=utf-8` first.

The lexicon tests and the evaluation in `docs/07` use the University of Moratuwa NLPC
[Word Frequency List for Sinhala](https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala),
which is not redistributed here.

---

## Status and limitations

- School textbooks (NIE), the final SLS 1134:2004/2011 texts and the 1989 *Sinhala Lekhana Rīthiya*
  could not be consulted. School-level spelling rules rest on agreeing secondary sources and are
  marked with their confidence.
- The consonant × vowel validity table is a synthesis of the sources, not a corpus count.
- Every topic file ends with its open questions and conflicting sources. Corrections are welcome.

---

## Citation

See [CITATION.cff](CITATION.cff).

## License

[MIT](LICENSE). Quoted source material remains under its original terms; quotations are
kept under 15 words and every source is cited.
