# 07: A grammar-correct phonetic romanization of Sinhala

This document specifies a phonetic romanization of Sinhala: a set of Latin-letter sequences
and conversion rules that turn romanized text into Sinhala script. It is designed so that
every result obeys the orthographic rules in `00-rules.md`, while staying close to how
Sinhala is informally written in Latin script (`06-romanization.md`). Compiled October 2026.

The reference implementation is `src/sinhala_orthography/romanization.py`. The sequence
tables are `src/sinhala_orthography/data/{consonants,vowels,specials}.json`.

---

## ⚠️ Things that will surprise you

| | Convention | Example |
|---|---|---|
| 1 | Lower-case `t` is retroflex but lower-case `d` is dental, matching informal usage | `t` ට, `th` ත · `d` ද, `D` ඩ |
| 2 | `ai` and `au` are written with a glide, not as ෛ / ෞ | `lait` → ලයිට්, `kauda` → කවුද |
| 3 | `ru` / `ruu` straight after a consonant is written with ෘ / ෲ, the usual spelling; rakaransaya + ු / ූ is an option | `kruura` → කෲර, `mrudu` → මෘදු, `karu` → කරු |
| 4 | Lower-case `n` before a velar becomes ං | `lankaava` → ලංකාව |
| 5 | Repaya is plain ර් by default | `karma` → කර්ම, `kaarya` → කාර්ය |
| 6 | A rule-forbidden form is never produced; a valid fallback is used instead | `kazd` → කඳ (no hal on ඳ), `Ba` → බ (no word-initial ඹ) |
| 7 | Case is significant: capitals mark retroflex, aspirate, ඇ/ඈ and diphthong letters | `N` ණ, `L` ළ, `A` ඇ, `E` ෛ |

---

## 1. Design principles

1. **Never produce a forbidden sequence.** All HARD rules in `00-rules.md` hold for every
   output. This is checked exhaustively (§5).
2. **Every allowed letter form is producible.** All 791 forms that `data/validity.json`
   allows can be written.
3. **Follow majority informal usage where it is unambiguous** (`06-romanization.md`):
   `th` ත, `t` ට, `d` ද, `w`/`v` ව, `ee` for long e.
4. **Mark spelling-only distinctions explicitly.** Distinctions speakers do not hear
   (aspiration, ණ/න, ළ/ල, ශ/ෂ, sanyaka) get an explicit marker: a capital, an `h`, or a
   `z` prefix. Without the marker, the plain letter is written, and a lexicon can recover
   the standard spelling (§4).
5. **Logical order.** Romanization is written in pronunciation order, which is also Unicode
   storage order, so pre-base signs (ෙ, ෛ, ො…) need no reordering.

---

## 2. Sequence tables

Generated from the JSON tables by `tools/build_spec_tables.py`. The Notes column cites the
convention (R-*) or rule (G-*) behind a row. Matching is case-sensitive and longest-first.

<!-- tables:start -->

### Consonants

A consonant written without a following vowel takes hal (්): `k` → ක්, `ka` → ක.

| Letter | Romanization | Notes |
|:-:|---|---|
| **ක** | `k` · `c` | alias |
| **ඛ** | `kh` · `K` · `C` | alias |
| **ග** | `g` |  |
| **ඝ** | `gh` · `G` |  |
| **ඞ** | `X` | G-HC-08: hal only |
| **ඟ** | `zg` | sanyaka |
| **ච** | `ch` |  |
| **ඡ** | `chh` |  |
| **ජ** | `j` |  |
| **ඣ** | `jh` · `J` |  |
| **ඤ** | `zk` | R-12 |
| **ඥ** | `zh` | R-12 |
| **ඦ** | `zj` | R-14; archaic option |
| **ට** | `t` |  |
| **ඨ** | `T` |  |
| **ඩ** | `D` | R-01 |
| **ඪ** | `Dh` | R-01 |
| **ණ** | `N` |  |
| **ඬ** | `zD` | R-01 sanyaka |
| **ත** | `th` |  |
| **ථ** | `thh` |  |
| **ද** | `d` · `q` | R-01; alias |
| **ධ** | `dh` · `dhh` | R-01; alias |
| **න** | `n` |  |
| **ඳ** | `zd` · `zdh` · `zq` | R-01 sanyaka; alias |
| **ප** | `p` |  |
| **ඵ** | `ph` · `P` |  |
| **බ** | `b` |  |
| **භ** | `bh` |  |
| **ම** | `m` |  |
| **ඹ** | `B` | sanyaka |
| **ය** | `y` |  |
| **ර** | `r` |  |
| **ල** | `l` |  |
| **ව** | `w` · `v` · `W` · `V` |  |
| **ශ** | `sh` |  |
| **ෂ** | `Sh` · `S` |  |
| **ස** | `s` |  |
| **හ** | `h` |  |
| **ළ** | `L` |  |
| **ෆ** | `f` |  |

### Vowels

The independent letter is used at the start of a word; after a consonant the vowel is written as a sign.

| Vowel | Independent | Sign | Romanization | Notes |
|---|:-:|:-:|---|---|
| a | අ | *(inherent)* | `a` |  |
| aa | ආ | ◌ා | `aa` |  |
| ae | ඇ | ◌ැ | `A` · `ae` | R-04 |
| aee | ඈ | ◌ෑ | `Aa` · `AA` · `aee` | R-04 |
| i | ඉ | ◌ි | `i` |  |
| ii | ඊ | ◌ී | `ii` · `I` | R-02 |
| u | උ | ◌ු | `u` · `U` |  |
| uu | ඌ | ◌ූ | `uu` · `UU` · `Uu` | R-02 |
| ru | ඍ | ◌ෘ | `R` | R-06 |
| ruu | ඎ | ◌ෲ | `RR` | R-06 (independent ඎ archaic only) |
| e | එ | ◌ෙ | `e` |  |
| ee | ඒ | ◌ේ | `ee` | R-02 |
| ai | ඓ | ◌ෛ | `E` | R-05b |
| o | ඔ | ◌ො | `o` · `O` |  |
| oo | ඕ | ◌ෝ | `oo` · `OO` · `Oo` | R-02 |
| au | ඖ | ◌ෞ | `Au` · `AU` | R-05b |
| ilu | ඏ | ◌ෟ | `~l` | R-14; archaic option |
| iluu | ඐ | ◌ෳ | `~ll` | R-14; archaic option |

### Signs and joins

| Output | Romanization | Notes |
|:-:|---|---|
| ං | `x` | G-NS-01: needs a vowel base |
| ං | `zn` | G-NS-01 |
| ං | `M` | G-NS-01 |
| ඃ | `H` | G-NS-05 |
| ඁ | `~n` | R-14 / G-NS-06; archaic option |
| touching letters (C ZWJ ් C) | `+` | R-14 / G-HC-17: C ZWJ ් C; archaic option |

<!-- tables:end -->

---

## 3. Conversion rules

| # | Rule | Example | Basis |
|---|---|---|---|
| C-1 | A consonant with no following vowel takes hal | `pin` → පින් | G-HC-01 |
| C-2 | C + `y` → yansaya (C ් ZWJ ය), except after ර | `vaakya` → වාක්‍ය | G-HC-11, G-HC-14 |
| C-3 | C + `r` → rakaransaya (C ් ZWJ ර) for every consonant that takes hal, except ම න ල (plain hal; rakaransaya under `classical`) | `kramaya` → ක්‍රමය, `dumriya` → දුම්රිය | G-HC-12, R-07 |
| C-4 | ර + C → plain ර් (repaya with ZWJ under `repaya_zwj`) | `karma` → කර්ම | G-HC-13, R-08 |
| C-5 | Geminates and other clusters use plain hal (ZWJ conjuncts under `classical`) | `amma` → අම්ම, `akShara` → අක්ෂර | G-HC-03, R-10 |
| C-6 | A vowel after a vowel is joined by a glide: ය after front vowels, ව after back vowels; after a / aa the following vowel decides | `toppia` → ටොප්පිය, `dua` → දුව, `ai` → අයි | G-VS-06, R-05 |
| C-7 | `n` + k / kh / g / gh after a vowel → ං; word-final `ng` → ං | `ingriisi` → ඉංග්‍රීසි, `sing` → සිං | G-NS-03, R-11 |
| C-8 | ං needs a vowel base: a consonant before `x` keeps its inherent a; a vowel after ං turns it into ම + sign | `kx` → කං | G-NS-01, G-NS-04 |
| C-9 | Sanyaka and ළ never take hal: without a vowel they keep the inherent a | `kaL` → කළ | G-HC-06, G-HC-07 |
| C-10 | No sanyaka at the start of a word: the plain stop is written | `zda` → ද | G-PH-01 |
| C-11 | ඞ only as ඞ් before a consonant; ඞ + vowel → ඟ + sign; ං before a sanyaka is dropped | `aXa` → අඟ, `axzda` → අඳ | G-HC-08, G-NS-09 |
| C-12 | A sequence that cannot be written is left in Latin script | `x` (no base) → x | G-NS-01 |
| C-13 | C + `r` + `u` / `uu` → C + ෘ / ෲ where that form is attested (`valid`, `loan` or `rare` in validity.json: මෘ, not ලෘ); otherwise C-3 applies (rakaransaya + ු / ූ, plain hal after ම න ල). Rakaransaya + ු / ූ throughout under `rakaransaya_u`; `R` / `RR` always write ෘ / ෲ | `kruura` → කෲර, `mrudu` → මෘදු, `gruup` → ගෲප්, `dilrukshi` → දිල්රුක්ශි | G-VS-15, R-06 |

### Options

| Option | Effect | Convention |
|---|---|---|
| `repaya_zwj` | ර්‍ + C instead of ර් + C | R-08 |
| `classical` | ZWJ conjuncts for ක්‍ෂ ක්‍ව ග්‍ධ ට්‍ඨ ත්‍ථ ත්‍ව ද්‍ධ ද්‍ව න්‍ථ න්‍ද න්‍ධ න්‍ව ඤ්‍ච, and rakaransaya after ම න ල (ම්‍ර න්‍ර ල්‍ර) | R-10, G-HC-15, R-07 |
| `archaic` | ඏ ඐ ෟ ෳ (`~l`, `~ll`), standalone ඎ (`RR`), ඁ (`~n`), ඦ (`zj`), touching letters (`+`) | R-14 |
| `rakaransaya_u` | C + `r` + `u` / `uu` as rakaransaya + ු / ූ (ක්‍රු, ක්‍රූ) instead of C + ෘ / ෲ. The name means "rakaransaya + u": the `u` is the vowel sign ු. Rakaransaya itself is always written; the option changes only C + `ru` / `ruu` | R-06 |
| `retroflex_d` | `d` ඩ · `dh` ද · `D` ඪ · `Dh` ධ · `zd` ඬ, the older keyboard convention (`dhh` ධ, `zdh` ඳ, `q` ද keep their letters) | R-01 |

---

## 4. Disambiguation with a lexicon

A romanization fixes one spelling, but about 14 groups of Sinhala letters are pronounced
alike (G-SP-01). People rarely mark vowel length or aspiration in Latin script, so the
standard spelling often needs a word list. `src/sinhala_orthography/lexicon.py`:

```
romanized ──► conversion (§3) ──► one spelling ──► sound key ──► words of a frequency list
                                                       │            with the same key,
                                                       │            most frequent first
                                                       └─ explicit marker present and the
                                                          spelling is a word, or a lone
                                                          vowel letter → it stays first
```

The **sound key** erases: aspiration, ණ/න, ළ/ල, ශ/ෂ/ස, ද/ඩ, ඤ/න, ඥ/ග්න, sanyaka vs
nasal + stop, ං/න්, vowel length, ඇ/එ, ෛ/යි, ෞ/වු, ෘ/්‍රු and ZWJ.

**A lone vowel letter keeps its spelling.** When an input with an explicit marker converts
to a single independent vowel (`A` ඇ, `Aa` ඈ, `R` ඍ, `E` ඓ, `Au` ඖ), that letter stays first
although the list has no such word: a letter typed on its own is meant as that letter, and
frequency would otherwise turn it into a sound-alike word (ඍ → රු, ඓ → අයි). Unmarked vowels
are still matched by sound (`e` → ඒ).

**Options apply to the words too.** A word list is written in the usual style (කෲර, කර්ම), so
`candidates()` rewrites each word in the style of the converter options before returning it
(`restyle()`): `rakaransaya_u` turns C + ෘ/ෲ into rakaransaya + ු/ූ (ක්‍රූර), `repaya_zwj` joins
repaya with ZWJ (කර්‍ම) and `classical` joins the bandi akuru pairs (අක්‍ෂර). Otherwise the
lexicon would undo the options on every word. With no options nothing changes.

**Evaluation.** 27 everyday words, written as people informally romanize them, with the
University of Moratuwa NLPC frequency list (2.1M words, pinned; CC-14 in `reports/corpus-counts.md`).
The list is not included here: `tools/corpus_counts.py` downloads it, and `tests/test_lexicon.py`
runs the same words against any list.

| | Correct spelling ranked first |
|---|---:|
| Conversion rules alone | 9 / 27 |
| Rules + lexicon | **27 / 27** |

| Romanized | Rules alone | Rules + lexicon |
|---|---|---|
| `honda` | හොන්ද | හොඳ |
| `sinhala` | සින්හල | සිංහල |
| `thiyenawa` | තියෙනව | තියෙනවා |
| `bada` | බද | බඩ |
| `vaidya` | වයිද්‍ය | වෛද්‍ය |
| `krushi` | කෘශි | කෘෂි |
| `lamaya` | ලමය | ළමයා |

17.7% of the list's sound keys are shared by two or more words (e.g. කළ කල කාල කලා; CC-15), so
frequency alone cannot always choose. Context from the previous word would help.

---

## 5. Verification

`tools/check_romanization.py` (report: `reports/romanization-check.md`):

| Check | Result |
|---|---|
| Coverage: letter forms allowed by `data/validity.json` that can be produced | **791 / 791** |
| Safety: inputs of 1–3 sequences (plus space), all six option sets | **3.98 million inputs, 0 violations** of 14 forbidden patterns |
| Fixtures: `tests/test_romanization.py` | all pass |

---

## 6. Conventions and their rationale

| ID | Convention | Rationale |
|---|---|---|
| R-01 | `d` ද · `dh` ධ · `D` ඩ · `Dh` ඪ; sanyaka `zd` ඳ, `zD` ඬ; `q` = ද alias | Informal writing uses `d` for ද 99% of the time and `dh` for ධ (G-TY-02). Capitals mark retroflex letters, as with `N` ණ and `L` ළ. ද is also 5 times as frequent as ඩ in running text (74% vs 15% of d-letters, CC-12), so the unmarked key goes to the common letter. Older keyboard schemes write `d` ඩ / `dh` ද, mirroring `t` ට / `th` ත (06:RS-030); `retroflex_d` offers that convention |
| R-02 | `ee` ඒ · `oo` ඕ · `ii` ඊ · `uu` ඌ | Consistent doubling for length. Informal `ee` = ී (G-TY-03) is recovered by the lexicon |
| R-03 | `nd` / `mb` / `ng` + vowel are written as clusters; the lexicon chooses sanyaka (ඳ ඹ ඟ) or cluster | Sanyaka vs cluster is lexical (G-NS-08), and informal writing uses `nd`/`mb`/`ng` for both (G-TY-06) |
| R-04 | `A` / `ae` ඇ · `Aa` / `AA` / `aee` ඈ | `ae` matches ISO 15919 7-bit; `A` keeps a one-letter form |
| R-05 | `ai` / `au` → glide spelling (අයි / අවු, C + යි / C + වු); ෛ ඓ via `E`, ෞ ඖ via `Au` | Two vowels are never written side by side (G-VS-03, G-VS-06). In the NLPC list, words with C + යි outnumber C + ෛ 11:1 and C + වු outnumber C + ෞ 1.7:1 (CC-05). A word that has ෛ or ෞ is nearly always written with it (වෛද්‍ය 46,508 vs වයිද්‍ය 142, CC-06), and the lexicon restores it |
| R-06 | C + `ru` / `ruu` = C + ෘ / ෲ; `R` / `RR` also write ෘ / ෲ; `rakaransaya_u` gives ක්‍රු / ක්‍රූ instead; standalone `R` = ඍ; `ru` after a vowel = ර + ු | ෘ / ෲ is the usual spelling of /Cru(ː)/ in Sanskrit and English loans alike (G-VS-15): in the NLPC list it is the most frequent spelling in 155 of 205 words written more than one way (කෲර 1,667, ක්‍රූර 9; CC-02, CC-03). ගෘහ and ග්‍රහ stay distinct (G-VS-12) |
| R-07 | Rakaransaya after every consonant that takes hal, except ම න ල: there ර starts a new syllable and takes plain hal (දුම්රිය, හෙන්රි); `classical` writes ම්‍ර (තාම්‍ර) | Running text writes ම්ර / න්ර plain (දුම්රිය 30,800 vs දුම්‍රිය 82; 03:HC-052, CC-10); a ZWJ would draw a rakaransaya under ම. ම්‍ර is attested only for Sanskrit tatsama words |
| R-08 | Repaya defaults to plain ර් + C | Both forms are standard (G-HC-13); the plain form dominates the NLPC list (2,182,087 vs 26,785 tokens, CC-07) |
| R-09 | *kārya* → කාර්ය | Follows from R-08; 18,722 occurrences in the NLPC list (CC-08) |
| R-10 | ක්ෂ and other bandi akuru default to plain hal; ZWJ conjuncts are optional | Conjuncts other than yansaya/rakaransaya are optional and mostly classical (G-HC-15/16) |
| R-11 | `n` + velar → ං automatically; before h s sh y r l v the lexicon chooses ං or න් | G-NS-03; native and Sanskrit words differ before ස (පන්සල vs සංසාරය) |
| R-12 | `ny` → න්‍ය; `gn` → ග්න; ඥ = `zh`; ඤ = `zk` | න්‍ය and ග්න are the common readings (G-NS-12/13); ඥ and ඤ are recovered by the lexicon |
| R-13 | Case-sensitive | Capitals carry the spelling-only distinctions (principle 4) |
| R-14 | Archaic letters and touching letters only under the `archaic` option | Not used in modern Sinhala (G-VS-08, G-HC-17, G-NS-06) |
| R-15 | Spelling-only distinctions are resolved by a frequency lexicon | G-SP-01: sound cannot decide them |

---

## 7. Limitations

- Disambiguation quality depends on the word list. The NLPC list is drawn from news text,
  so formal words outrank colloquial ones (ඔය before ඔයා). Some copies of it have lost
  their ZWJs; `normalize()` repairs yansaya and rakaransaya on load. It runs only on a list
  with no ZWJ at all, because it cannot see word boundaries and also joins බවත් + ය → බවත්‍ය.
- The per-consonant validity table (`data/validity.json`) is a synthesis of the sources,
  not a corpus count (`00-rules.md` §10).
- Informal romanization often drops vowels altogether (G-TY-05). Recovering those needs
  fuzzy matching, which is out of scope here.
