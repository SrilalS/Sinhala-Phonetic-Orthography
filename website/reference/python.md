# Python and JavaScript packages

`sinhala_orthography` holds the letter inventory, the romanization converter and a
frequency-based disambiguator. It needs Python 3.9 or later and has no dependencies.

## Install

Clone the repository and import from `src/`, or install it:

```sh
git clone https://github.com/SrilalS/Sinhala-Phonetic-Orthography
cd Sinhala-Phonetic-Orthography
pip install .
```

::: tip Windows consoles
Set `PYTHONIOENCODING=utf-8` before printing Sinhala text.
:::

## Converting romanization

```python
from sinhala_orthography import to_sinhala

to_sinhala("lankaava")                  # 'ලංකාව'
to_sinhala("kruura")                    # 'කෲර'
to_sinhala("kruura", rakaransaya_u=True)  # 'ක්‍රූර'
to_sinhala("lait")                      # 'ලයිට්'
to_sinhala("akShara", classical=True)   # 'අක්‍ෂර'
to_sinhala("karma", repaya_zwj=True)    # 'කර්‍ම'
```

### `to_sinhala(source, archaic=False, repaya_zwj=False, classical=False, rakaransaya_u=False)`

Converts a romanized word or text to Sinhala script. Characters outside the sequence tables
(spaces, digits, punctuation) pass through unchanged. Every output obeys the HARD rules of the
[rule set](/rules). This is checked over every input of up to three sequences (see
[Verification](/reference/verification)).

| Option | Effect | Convention |
|---|---|---|
| `archaic` | Allow ඏ ඐ ෟ ෳ, standalone ඎ, ඁ, ඦ and touching letters | R-14 |
| `repaya_zwj` | Write repaya as ර්‍ + C instead of plain ර් + C | R-08 |
| `classical` | ZWJ conjuncts for the classical bandi akuru pairs, and rakaransaya after ම න ල | R-07, R-10 |
| `rakaransaya_u` | Write C + r + u/uu as rakaransaya + ු/ූ (ක්‍රූර) instead of the usual C + ෘ/ෲ (කෲර) | R-06 |

`transliterate()` is the same function under its original name. The sequence tables live in
`src/sinhala_orthography/data/` (`consonants.json`, `vowels.json`, `specials.json`), and the
romanization is specified in [07 · Phonetic romanization](/research/phonetic-romanization).
Try it in the [playground](/playground).

## Disambiguating with a word list

About 14 groups of letters sound alike (G-SP-01), so one romanization can't always pick
the standard spelling. `Lexicon` indexes a word-frequency list by *sound key*, and
`candidates()` ranks the words that share the input's key.

```python
from sinhala_orthography import Lexicon, candidates

lex = Lexicon("word-frequency-list.tsv")   # one "word<TAB>count" per line
candidates(lex, "honda")                   # ['හොඳ', ...]
candidates(lex, "hon", partial=True)       # completions of a word prefix
```

| Function | Returns |
|---|---|
| `candidates(lex, roman, limit=5, partial=False, **options)` | Ranked spellings. The converter's own spelling is always included. When the romanization has an explicit marker (a capital, a `z` prefix, a doubled vowel …) and that spelling is a word, it comes first |
| `sound_key(text)` | The text folded so sound-alike spellings match: aspirates → plain, ණ → න, ළ → ල, ශ/ෂ → ස, vowel length dropped, sanyaka → nasal + stop. `sound_key("හොඳ")` is `'හොන්ද'` |
| `normalize(word)` | Restores the mandatory ZWJ in C ් ය and C ් ර (never after ර), for word lists that dropped it |
| `restyle(word, **options)` | A word in the style of the converter options (ක්‍රූර for කෲර with `rakaransaya_u` …). `candidates()` applies it, so the word list never undoes an option |
| `Lexicon(path)` | `.count` (word → frequency), `.exact(key)`, `.prefix(key, limit=200)` |

The evaluation in [07](/research/phonetic-romanization#_4-disambiguation-with-a-lexicon) used the
University of Moratuwa NLPC
[Word Frequency List for Sinhala](https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala),
which isn't redistributed here.

## Letter inventory

```python
from sinhala_orthography import VOWELS, CONSONANTS, SIGNS, entries

len(entries())   # 923
entries()[30]    # {'id': 'ka.ru', 'kind': 'syllable', 'text': 'කෘ', 'consonant': 'ka',
                 #  'vowel': 'ru', 'codepoints': ['U+0D9A', 'U+0DD8']}
```

| Name | What |
|---|---|
| `VOWELS` | `(id, independent letter, dependent sign)` for hal, the inherent a and the 17 signs |
| `CONSONANTS` | `(id, letter)` for the 41 consonants in Unicode order |
| `SIGNS` | ං ඃ ඁ |
| `entries()` | Every letter form, as in [`data/letters.json`](/reference/data) |

## JavaScript and TypeScript

The same package is available for JavaScript and TypeScript, for Node.js and the browser, with no
dependencies. It lives in [`js/`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/tree/main/js)
and reads the same sequence tables. A golden test checks that it gives exactly the Python output for
more than 50,000 inputs, and the [playground](/playground) runs on it.

```js
import { toSinhala, Lexicon, candidates } from "sinhala-orthography";

toSinhala("kruura");                          // 'කෲර'
toSinhala("kruura", { rakaransayaU: true });  // 'ක්‍රූර'
const lex = new Lexicon(wordListText);        // "word<TAB>count" lines, or [word, count] pairs
candidates(lex, "honda", { limit: 5 });
```

| Python | JavaScript |
|---|---|
| `to_sinhala(s, repaya_zwj=True)` | `toSinhala(s, { repayaZwj: true })` (also `archaic`, `classical`, `rakaransayaU`) |
| `Lexicon(path)` | `new Lexicon(text)` or `new Lexicon(pairs)`: no file access, so it also runs in a browser |
| `candidates(lex, roman, limit=5, partial=False)` | `candidates(lex, roman, { limit, partial })` |
| `sound_key`, `normalize`, `entries`, `VOWELS`, `CONSONANTS`, `SIGNS` | `soundKey`, `normalize`, `entries`, `VOWELS`, `CONSONANTS`, `SIGNS` |

The Python package stays the reference: change it first, run `python tools/build_js_golden.py`, then
make `npm test` in `js/` pass.

## Tools

```sh
python tools/build_data.py            # data/letters.json, data/validity.json
python tools/check_romanization.py    # coverage + exhaustive safety (about 20 s)
python tools/build_spec_tables.py     # tables in docs/07
python tools/check_translations.py    # Sinhala translations whose English source changed
python -m unittest discover tests     # set SINHALA_WORD_LIST to also run the lexicon tests
```
