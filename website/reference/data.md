# Data files

Three JSON files in `data/` describe all 923 Sinhala letter forms. They share one `id` per form,
so they join on it. Browse them in the [letter explorer](/explorer).

| File | Built by | What |
|---|---|---|
| [`letters.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/letters.json) | `tools/build_data.py` | The inventory: text and code points of each form |
| [`validity.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/validity.json) | `tools/build_data.py` | Status of each form and the rules behind it |
| [`romanization-coverage.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/romanization-coverage.json) | `tools/check_romanization.py` | The romanizations that produce each form, per option set |

## IDs

| Kind | Count | ID | Example |
|---|---:|---|---|
| Independent vowel | 18 | `vowel.<vowel>` | `vowel.aa` ආ |
| Sign | 3 | `sign.<name>` | `sign.anusvara` ං |
| Consonant form | 41 × 19 | `<consonant>.<vowel>` | `ka.hal` ක්, `ka.a` ක, `ka.ru` කෘ |
| Conjunct | 41 × 3 | `<consonant>.<conjunct>` | `ka.yansaya` ක්‍ය, `ka.rakaransaya` ක්‍ර, `ka.repaya` ර්‍ක |

Vowel IDs: `hal` `a` `aa` `ae` `aee` `i` `ii` `u` `uu` `ru` `ruu` `ilu` `iluu` `e` `ee` `ai` `o` `oo` `au`.
Consonant IDs follow [01 · Letter inventory](/research/inventory), in Unicode order from `ka` ක to `fa` ෆ.

## `letters.json`

```json
{ "id": "ka.ru", "kind": "syllable", "text": "කෘ", "consonant": "ka", "vowel": "ru",
  "codepoints": ["U+0D9A", "U+0DD8"] }
```

`kind` is `vowel`, `sign`, `syllable` or `conjunct`. Conjuncts carry `conjunct` instead of `vowel`.

## `validity.json`

```json
{ "id": "ka.u", "text": "කු", "status": "valid", "shape": "hook-u", "rules": ["G-VS-13"] }
```

| `status` | Count | Meaning |
|---|---:|---|
| `valid` | 380 | In ordinary use |
| `loan` | 193 | Valid, but in practice only in Sanskrit or Pali (tatsama) words |
| `rare` | 101 | A valid encoding that is marginal or archaic in use |
| `unattested` | 117 | No known word uses it, but no rule forbids it |
| `never` | 132 | Forbidden by a hard rule (G-HC-06, G-HC-07, G-HC-08, G-HC-14, G-VS-08) |

`shape` flags a glyph that is drawn specially. The encoding is unchanged (G-EN-11):
`hook-u`, `irregular` (ර and ළ with u/uu, ර with ae/aee), `tail-loss` and `alt-hal`. It is
`null` for the other 897 forms.

Consonant × vowel statuses come from the 41 × 17 table in
[02 · Vowel signs §8](/research/vowel-signs). They are a synthesis of the sources, not a corpus count,
except the ෘ / ෲ columns, which were checked against a 2.1M-word list (VS-035).

## `romanization-coverage.json`

```json
{ "id": "ka.repaya", "text": "ර්‍ක", "status": "valid",
  "default": [], "repaya_zwj": ["rka", "rca"], "classical": [], "archaic": [],
  "rakaransaya_u": [] }
```

Each option set lists up to four romanizations that produce the form, shortest first. Signs are
written after ක (`kax` → කං), and letters that can't start a word are written after අ
(`azda` → අඳ). An empty list means that option set can't produce the form. ZWJ repaya needs `repaya_zwj`, and archaic letters
need `archaic`. All 791 forms that aren't `never` are producible under some option set.
