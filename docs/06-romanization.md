# 06: Romanization of Sinhala

This document surveys how Sinhala is written in Latin script. It covers (a) the formal romanization systems (ISO 15919 and its 7-bit ASCII form, the Sri Lanka national system, the UN 1972 table, ALA-LC and KNAB) and (b) informal romanized Sinhala ("Singlish") as people actually write it, measured from the Sinhala portion of the Dakshina corpus and described in the published research on Singlish back-transliteration. It closes with a per-letter comparison, a set of conventions (RS-xxx) and recommendations for a phonetic romanization of Sinhala.

Compiled October 2026.

## Legend

| Mark | Meaning |
|---|---|
| ✅ | Taken from a primary source (the standard, an official report, or a published mapping table) |
| 🧪 | Measured from a corpus (the Dakshina Sinhala data, §2a) |
| ❓ | Unverified. The source says nothing, or the value is an inference. Don't treat it as a mapping |
| - | No value recorded for this letter in the sources used here |

Confidence for each RS convention: **H** means several primary sources agree, **M** means one primary source or an inference, **L** means a guess.

Letter IDs follow the rest of this repository: consonants `ka kha ga gha nga(ඞ) nnga(ඟ) ca cha ja jha nya(ඤ) jnya(ඥ) nyja(ඦ) tta ttha dda ddha nna nndda(ඬ) ta tha da dha na nda(ඳ) pa pha ba bha ma mba(ඹ) ya ra la va sha(ශ) ssa(ෂ) sa ha lla(ළ) fa`; vowels `a aa ae aee i ii u uu ru ruu ilu iluu e ee ai o oo au`; signs `hal anusvara visarga yansaya rakaransaya repaya`.

---

## Summary

- **Informal writing uses `th` = ත and `t` = ට.** ත is written `th` 93% of the time and ට is `t` 99%. ISO 15919 does the opposite (`t` = ත, `ṭ` = ට) (RS-001).
- **Informal `d` is ද first.** People write `d` for both ද (99%) and ඩ (100%), and keep `dh` for ධ (68%), which agrees with ISO (RS-002, RS-003).
- **Informal `ee`/`oo` mean ī/ū, not ē/ō.** ී is written `ee` 40% of the time, ේ almost never. ISO's 7-bit form uses `ee`/`oo` for ē/ō (RS-006, RS-007).
- **Vowel length is rarely marked.** ා is written `a` 97% of the time, and ී is `i` 57% (RS-009).
- **The formal systems disagree on the nasals.** ISO, the Sri Lanka national system and ALA-LC each romanize ං and ඞ differently (RS-029).

---

## ⚠️ Things that will bite you

| # | Gotcha | Rule |
|---|---|---|
| 1 | Informal `kohomada` means කොහොමද: `d` is ද, not ඩ. Reading `d` as ඩ gives the wrong word | RS-002 |
| 2 | Informal `ee` is ඊ/ී (`kireemata`, `pawathee`), not ඒ as in ISO 7-bit | RS-006 |
| 3 | Informal `oo` is ඌ/ූ (`soodanam`), not ඕ as in ISO 7-bit | RS-007 |
| 4 | Plain `nd`, `mb`, `ng` are ambiguous: න්ද or ඳ, ම්බ or ඹ, න්ග or ඟ or ංග. Informal writing uses them for the prenasalized letters (ඳ is `nd` 90% of the time) | RS-012 |
| 5 | Informal `n` for ං (92%) can't be told apart from න් | RS-014 |
| 6 | `c` is ච in ISO, but informal writing uses `ch` for ච (95%) | RS-005 |
| 7 | Chat-style Singlish drops vowels (`nthi`, `mta`, `kynna`), so one spelling can stand for several words | RS-010 |
| 8 | ඏ ඐ ෟ ෳ have values only in the formal systems; there is no informal data for them | RS-018 |

---

## 1. Formal romanizations ✅

### 1a. ISO 15919 (2001), with its 7-bit ASCII form
**Source:** the ISO 15919 table on Wikipedia, read from the page source. <https://en.wikipedia.org/wiki/ISO_15919>. The 7-bit ASCII form is given in brackets.

- **Vowels:** අ a · ආ ā (aa) · ඇ æ (ae) · ඈ ǣ (aee) · ඉ i · ඊ ī (ii) · උ u · ඌ ū (uu) · ඍ r̥ (,r) · ඎ r̥̄ (,rr) · ඏ l̥ (,l) · ඐ l̥̄ (,ll) · එ e · ඒ ē (ee) · ඓ ai · ඔ o · ඕ ō (oo) · ඖ au
- **Consonants:** ක k · ඛ kh · ග g · ඝ gh · ඞ ṅ (;n) · ඟ n̆g (^ng) · ච c · ඡ ch · ජ j · ඣ jh · ඤ ñ (~n) · ඦ n̆j (^nj) · ට ṭ (.t) · ඨ ṭh · ඩ ḍ · ඪ ḍh · ණ ṇ · ඬ n̆ḍ (^n.d) · ත t · ථ th · ද d · ධ dh · න n · ඳ n̆d (^nd) · ප p · ඵ ph · බ b · භ bh · ම m · ඹ m̆b (^mb) · ය y · ර r · ල l · ළ ḷ (.l) · ව v · ශ ś (sh) · ෂ ṣ (.s) · ස s · හ h · ෆ f
- **Signs:** ං ṁ (;m) · ඃ ḥ (.h) · ් has no symbol
- ඥ isn't listed separately. It's normally romanized as the conjunct jñ ❓.

### 1b. Sri Lanka national system (Survey Department, Cabinet-approved 4 Sep 2018, amended later)
**Source:** UNGEGN Working Group on Romanization Systems report, v5.0, Oct 2021. <https://arhiiv.eki.ee/wgrs/rom2_si.htm>. The report states there is still **no UN-approved system** for Sinhala.

- **Based on ISO, but these values differ:**
  - ඞ = **ṁa** and ං = **ṅ** (ISO has these the other way round)
  - ඓ = **ĩ** (it was ai in 2018)
  - ඣ = **qa** (it was jha)
  - ඨ = **ṯa** (it was ṭha)
  - ෂ = **sha**, ශ = ś
  - ඥ = **gna**
  - ඹ = **ḅa** (it was m̆ba)
  - ඦ = n̆ǰa
- **Other listed values:** ඟ n̆ga · ඬ n̆ḍa · ඳ n̆da · ඇ æ · ඈ ǣ · ඏ ḷ · ඐ ḹ · ඍ ṛ · ඎ ṝ
- **Ligatures:** ර්‍ is r-, ්‍ර is -r, ්‍ය is -y. The Survey Department's online converter is at <https://www.survey.gov.lk/RomanizationConverter/>.

### 1c. UN 1972 "Sharma" table (never approved)
**Source:** interscript map `un-sin-Sinh-Latn-1972`, citing the 1972 UN conference papers. <https://github.com/interscript/maps>

- Short vowels carry a breve: ඇ æ̆ · ඈ æ · එ ĕ · ඒ e · ඔ ŏ · ඕ o
- ච ch · ඡ chh · ශ sh · ෂ ṣh · ං ṁ · ඞ ṅ

### 1d. ALA-LC (Library of Congress) Sinhalese
**Source:** interscript maps `alalc-sin-Sinh-Latn-1997` and `-2011`. The LoC PDF itself failed to load (HTTP 520), so this is medium confidence.

| Area | ALA-LC 1997 |
|---|---|
| Vowels | ඇ ă · ඈ â · ඏ ḷ · ඐ ḹ · ෟ ḷ · ෳ ḹ · ē / ō for the long forms |
| Consonants | ච **ca** · ඡ **cha** · ශ ś · ෂ ṣ |
| Anusvara | ං ṃ |
| Prenasalized | ඟ ṅga · ඦ ñja · ඬ ṇḍa · ඳ nda · ඹ ṃba |

**Rules:**
- ALA-LC writes anusvara as the nasal of the following consonant's class: ṅ, ñ, ṇ, n or m.
- A sanyaka (prenasalized) letter followed by an aspirate is written as unaspirated + aspirate.

The 2011 test strings use ă / â for ඇ / ඈ.

### 1e. KNAB (Estonian place-name database), 1989
**Source:** <https://arhiiv.eki.ee/knab/lat/kblsi1.pdf>

- Vowels: ඇ è · ඈ ê · එ ĕ · ඒ e
- Consonants: ච cha · ශ sha · ෂ ṣha
- ං ṁ (ń)
- It marks prenasalized letters with a middle dot (·mba).
- It notes that in local practice è / ê are written e, and v is written **w**.

---

## 2. Informal Singlish: how people actually write Sinhala in Latin script

### 2a. Measured: the Dakshina corpus, Sinhala portion 🧪
**Corpus:** 10,000 Wikipedia sentences romanized by native speakers (Roark et al., LREC 2020), plus a lexicon of attested variants. The data used is a third-party mirror on Hugging Face: `Anvesh-Lankala/Copy_Dakshina_Google_research_dataset`, `si` split. It has not been checked byte-for-byte against the official release ❓.

**Method:** each Sinhala word was aligned to its romanization with a small dynamic-programming aligner, and the spelling chosen for each letter was counted.
- "Sentences" = sentence tokens: 127,701 of 141,995 tokens aligned.
- "Lexicon" = lexicon variants: 116,349 of 120,258 aligned.

| Letter | Sentences | Lexicon variants |
|---|---|---|
| ක | k 99%, c 1% | k 99% |
| ඛ / ඝ | kh 69% / gh 70% (rest: k, g) | kh 88% / gh 89% |
| ඟ | ng 51%, g 48% | ng 62%, g 38% |
| ච / ඡ | ch 95%, c 5% / ch 98% | ch 56%, c 44% / ch 100% |
| ජ | j 99% | j 99% |
| ඤ / ඥ | n 63%, gn 37% / **gn 98%** | n 55%, kn 45% / gn 74%, ny 12% |
| ට / ඨ | **t 99%** / t 92% | t 100% / th 77% |
| ඩ / ඪ | **d 100%** / d 73% | d 99% / dh 73% |
| ණ | n 100% | n 100% |
| ඬ | nd 81%, d 19% | nd 65%, d 33% |
| ත / ථ | **th 93%**, t 7% / th 99% | th 54%, t 46% / th 94% |
| ද / ධ | **d 99%**, dh 1% / **dh 68%**, d 32% | d 94% / dh 90% |
| ඳ | **nd 90%**, d 9% | nd 58%, dh 31% |
| ඵ / භ | p 57%, ph 43% / bh 91% | ph 80% / bh 78% |
| ඹ | **mb 88%**, b 11% | mb 84% |
| ව | **w 73%**, v 27% | v 74%, w 26% |
| ශ / ෂ | sh 85% / sh 91% | s 53%, sh 47% / sh 55%, s 45% |
| ළ | l 100% | l 100% |
| ෆ | f 86%, ph 13% | f 94% |
| inherent a | a 99% (rarely dropped in this corpus) | a 100% |
| ා | **a 97%**, aa 3% | a 91%, aa 8% |
| ැ / ඇ | e 62%, a 38%, ae ≈0% / a 60%, e 40% | ae 44%, a 43%, e 14% |
| ෑ | e 68%, a 29%, aa 3% | a 52%, ae 34% |
| ී / ඊ | i 57%, **ee 40%**, ii 2% / i 69%, ee 30% | i 69%, ee 30% |
| ූ / ඌ | u 72%, **oo 23%**, uu 5% / u 94% | u 83%, oo 14% |
| ේ / ඒ | e 99%, ee ≈0% / e 98% | e 98% |
| ෝ / ඕ | o 97%, oo 2% / o 97% | o 99% |
| ෘ | ru 93%, r 7% | ru 53%, r 46% |
| ෛ / ඓ | ai 94% / ai 89% | ai 95% |
| ෞ / ඖ | au 97% / au 93% | au 92% |
| ං | **n 92%**, ng 4%, m 3% | n 59%, m 34% |

**Caveats:**
- These are Wikipedia sentences romanized carefully on request, not chat. Chat drops vowels much more (§2b).
- In the lexicon, ත splits th/t about 50/50, so some annotators used ISO-like plain `t` for ත.

### 2b. Papers on Singlish back-transliteration
1. **Athukorala & Sumanathilaka, "Swa Bhasha: Message-Based Singlish to Sinhala Transliteration"** (2022 / 2024). <https://arxiv.org/abs/2404.13350>
   - Writers drop vowels. One word appears as kiyanna, kianna, kynna, kynn and kiynna.
   - The authors handle this with numeric letter codes and fuzzy matching.
   - They note that rule-based converters need vowels to be written, and they compare their system against existing tools.
2. **Perera, Prabhath, Sumanathilaka, Anuradha, "IndoNLP 2025 Shared Task: Romanized Sinhala to Sinhala Reverse Transliteration Using BERT"** (2025). <https://aclanthology.org/2025.indonlp-1.16.pdf>
   - Romanization is "ad-hoc" in their terms, with vowels omitted. For example, තාත්තා is written Thaaththaa, Thaththa, Thattha, Thatta or Tatta.
   - Their system combines a dictionary, rules for out-of-vocabulary words, and BERT for ambiguity.
   - Test set 2 is mostly vowel-less input.
3. **Perera & Sumanathilaka, "Evaluating Transliteration Ambiguity in Adhoc Romanized Sinhala"** (RANLP 2025). <https://aclanthology.org/2025.ranlp-1.107.pdf>
   - 22 romanized words that each map to two Sinhala words.
   - Examples: `nthi` නීති/නැති · `mta` මට/මීට · `es` ඇස/එසේ · `eda` ඇද/එදා · `bala` බල/බාල · `badu` බඩු/බදු · `ud` උඩ/උදේ · `dnna` දන්නා/දෙන්නා · `oya` ඔය/ඔයා.
   - These show three things: length isn't marked, ඇ and එ collapse into one spelling, and `d` is ambiguous between ඩ and ද.
4. **Sumanathilaka et al., "Swa-bhasha Resource Hub"** (arXiv 2507.09245, 2025). <https://arxiv.org/abs/2507.09245>
   - A survey of 2020–2025 systems and datasets.
   - Singlish isn't standardised and often drops vowels.
   - Swa Bhasha does better than existing tools and rule-based converters on vowel-less input.

### 2c. Everyday spellings
`mama`, `oya`/`oyaa`, `kohomada` (d for ද), `ayubowan`, `ganna`, `thiyenawa` (th for ත, no length mark), `amma`/`ammaa`, `thaththa`, `api`, `eka`, `ekka`, `mokada`, `honda` (nd for ඳ), `lassana`, `sinhala`/`lanka` (n for ං), `wenawa`/`venava`, `karanna`, `kiyanna`.

---

## 3. Per-letter comparison

Notes on the columns:
- Consonants are shown without the inherent vowel (the national system and ALA-LC sources write it, e.g. **ṁa**, **ca**).
- **ISO 7-bit:** the bracketed values from §1a. Where the ISO value is already plain ASCII, the 7-bit form is the same.
- **Sri Lanka national** and **ALA-LC:** only the values the sources list (§1b, §1d). "-" means the source excerpt used here gives no value, not that the letter is absent.
- **Informal:** the top spelling in the Dakshina sentences (§2a) and its share. Where no share is given, the spelling comes from the per-letter summary without a published percentage. `n = …` marks very small counts.

### Consonants

| ID | Sinhala | ISO 15919 | ISO 7-bit | Sri Lanka national | ALA-LC | Informal 🧪 |
|---|---|---|---|---|---|---|
| ka | ක | k | k | - | - | k 99% |
| kha | ඛ | kh | kh | - | - | kh 69% |
| ga | ග | g | g | - | - | g |
| gha | ඝ | gh | gh | - | - | gh 70% |
| nga | ඞ | ṅ | ;n | ṁ | - | - (no data) |
| nnga | ඟ | n̆g | ^ng | n̆g | ṅg | ng 51% (g 48%) |
| ca | ච | c | c | - | c | ch 95% |
| cha | ඡ | ch | ch | - | ch | ch 98% |
| ja | ජ | j | j | - | - | j 99% |
| jha | ඣ | jh | jh | q | - | jh (n = 4) |
| nya | ඤ | ñ | ~n | - | - | n 63% (gn 37%) |
| jnya | ඥ | jñ ❓ | - | gn | - | gn 98% |
| nyja | ඦ | n̆j | ^nj | n̆ǰ | ñj | - (no data) |
| tta | ට | ṭ | .t | - | - | t 99% |
| ttha | ඨ | ṭh | - | ṯ | - | t 92% |
| dda | ඩ | ḍ | - | - | - | d 100% |
| ddha | ඪ | ḍh | - | - | - | d 73% |
| nna | ණ | ṇ | - | - | - | n 100% |
| nndda | ඬ | n̆ḍ | ^n.d | n̆ḍ | ṇḍ | nd 81% |
| ta | ත | t | t | - | - | th 93% |
| tha | ථ | th | th | - | - | th 99% |
| da | ද | d | d | - | - | d 99% |
| dha | ධ | dh | dh | - | - | dh 68% |
| na | න | n | n | - | - | n |
| nda | ඳ | n̆d | ^nd | n̆d | nd | nd 90% |
| pa | ප | p | p | - | - | p |
| pha | ඵ | ph | ph | - | - | p 57% (ph 43%) |
| ba | බ | b | b | - | - | b |
| bha | භ | bh | bh | - | - | bh 91% |
| ma | ම | m | m | - | - | m |
| mba | ඹ | m̆b | ^mb | ḅ | ṃb | mb 88% |
| ya | ය | y | y | - | - | y |
| ra | ර | r | r | - | - | r |
| la | ල | l | l | - | - | l |
| va | ව | v | v | - | - | w 73% (v 27%) |
| sha | ශ | ś | sh | ś | ś | sh 85% |
| ssa | ෂ | ṣ | .s | sh | ṣ | sh 91% |
| sa | ස | s | s | - | - | s |
| ha | හ | h | h | - | - | h |
| lla | ළ | ḷ | .l | - | - | l 100% |
| fa | ෆ | f | f | - | - | f 86% |

### Vowels (independent / sign) and signs

| ID | Sinhala | ISO 15919 | ISO 7-bit | Sri Lanka national | ALA-LC | Informal 🧪 |
|---|---|---|---|---|---|---|
| a | අ / (inherent) | a | a | - | - | a 99% |
| aa | ආ / ා | ā | aa | - | - | a 97% (aa 3%) |
| ae | ඇ / ැ | æ | ae | æ | ă | ැ e 62%; ඇ a 60% |
| aee | ඈ / ෑ | ǣ | aee | ǣ | â | e 68% (a 29%) |
| i | ඉ / ි | i | i | - | - | i |
| ii | ඊ / ී | ī | ii | - | - | i 57% (**ee 40%**) |
| u | උ / ු | u | u | - | - | u |
| uu | ඌ / ූ | ū | uu | - | - | u 72% (**oo 23%**) |
| ru | ඍ / ෘ | r̥ | ,r | ṛ | - | ru 93% |
| ruu | ඎ / ෲ | r̥̄ | ,rr | ṝ | - | ru (n = 7) |
| ilu | ඏ / ෟ | l̥ | ,l | ḷ | ḷ | - (no data) |
| iluu | ඐ / ෳ | l̥̄ | ,ll | ḹ | ḹ | - (no data) |
| e | එ / ෙ | e | e | - | - | e |
| ee | ඒ / ේ | ē | ee | - | ē | e 99% |
| ai | ඓ / ෛ | ai | ai | ĩ | - | ai 94% |
| o | ඔ / ො | o | o | - | - | o |
| oo | ඕ / ෝ | ō | oo | - | ō | o 97% |
| au | ඖ / ෞ | au | au | - | - | au 97% |
| hal | ් | (none) | (none) | - | - | not written (implied at end of word) |
| anusvara | ං | ṁ | ;m | ṅ | ṃ (class nasal) | n 92% |
| visarga | ඃ | ḥ | .h | - | - | h (n = 1) |
| yansaya | ්‍ය | -y | -y | -y | - | y |
| rakaransaya | ්‍ර | -r | -r | -r | - | r |
| repaya | ර්‍ | r- | r- | r- | - | r |

---

## 4. Conventions (RS-xxx)

| ID | Convention / conflict | Evidence | Conf. |
|---|---|---|---|
| RS-001 | Informal writing uses `th` = ත and `t` = ට: ත is `th` 93%, ට is `t` 99%. ISO 15919 uses plain `t` = ත and `ṭ` = ට, and some lexicon annotators follow it (ත splits th/t about 50/50 in the lexicon) | §1a, §2a | H |
| RS-002 | **`d` is ambiguous in informal writing.** People write `d` for both ද (99%) and ඩ (100%). ISO separates them (d = ද, ḍ = ඩ). The RANLP pair `badu` බඩු/බදු shows the ambiguity in practice | §1a, §2a, §2b | H |
| RS-003 | **`dh` = ධ.** ISO uses dh = ධ, and informal writing agrees (68% in sentences, 90% in the lexicon) | §1a, §2a | H |
| RS-004 | ISO marks aspirates by adding h to the base letter (`ch` = ඡ, `th` = ථ). Informal writing barely separates aspirates from their plain letters: ථ and ත are both `th`, ඨ is mostly `t`, ඪ mostly `d` | §1a, §2a | H |
| RS-005 | `c`: ISO and ALA-LC use c = ච. Informal writing uses `ch` for ච (95%), `c` only 5%; ක is `c` 1% | §1a, §1d, §2a | M |
| RS-006 | `ee`: in ISO 7-bit, `ee` = ē (ඒ). In informal writing `ee` is a common spelling of ī (ී = `ee` 40%), and almost never of ē (ේ = `ee` ≈0%) | §1a, §2a | H |
| RS-007 | `oo`: in ISO 7-bit, `oo` = ō (ඕ). In informal writing `oo` is a spelling of ū (ූ = `oo` 23%), rarely of ō (ෝ = `oo` 2%) | §1a, §2a | H |
| RS-008 | ඇ: ISO is æ, with `ae` as its 7-bit form; UN 1972 æ̆, ALA-LC ă, KNAB è. Informal writing mostly uses `e` or `a`, rarely `ae` (ැ = `ae` ≈0% in sentences) | §1, §2a | H |
| RS-009 | Informal writing rarely marks vowel length (ා = `a` 97%, ී = `i` 57%). Length has to be recovered from context or a dictionary | §2a, §2b | H |
| RS-010 | Chat-style Singlish drops vowels heavily (`nthi`, `mta`, `kynna`). The published systems cope with dictionaries, fuzzy matching or BERT | §2b | H |
| RS-011 | ව: the formal systems use `v`. KNAB notes that local practice writes `w`, and informal writing prefers `w` in sentences (73%) | §1e, §2a | H |
| RS-012 | Prenasalized letters: ISO and the national system mark them with a breve (n̆d, m̆b, n̆g), KNAB with a middle dot (·mba), ALA-LC writes nda / ṃba / ṅga. Informal writing uses a plain cluster (`nd` 90%, `mb` 88%, `ng` 51%), which is ambiguous with න්ද, ම්බ, න්ග | §1, §2a | H |
| RS-014 | ං: ISO ṁ, national system ṅ, ALA-LC the class nasal, KNAB ṁ (ń). Informal writing uses `n` (92%), which can't be told apart from න් | §1, §2a | H |
| RS-017 | ෘ is written `ru` informally (93%, `r` 7%); ISO uses r̥. A romanization that writes ෘ as `ru` cannot distinguish කෘ from ක්‍රු (both `kru`) | §1a, §2a | H |
| RS-018 | ඏ ඐ ෟ ෳ have values only in the formal systems (ISO l̥ / l̥̄, national and ALA-LC ḷ / ḹ). There is no informal data for them | §1, §2a | H |
| RS-019 | Hal is not written. ISO has no symbol for ්, and informal writing leaves a consonant with no following vowel bare (hal implied, especially at the end of a word) | §1a, §2a | H |
| RS-020 | The inherent vowel is written as `a` in ISO and in informal writing (99% in Dakshina). Chat breaks this (RS-010) | §1a, §2a | H |
| RS-024 | ශ / ෂ: ISO ś / ṣ, national ś / sh, UN 1972 sh / ṣh, KNAB sha / ṣha. Informal writing uses `sh` for both (85% / 91%) | §1, §2a | H |
| RS-025 | The formal systems mark retroflex letters with an underdot (ṭ ḍ ṇ ḷ). Informal writing does not distinguish them at all for the nasal and lateral (ණ = `n` 100%, ළ = `l` 100%) | §1a, §2a | H |
| RS-026 | `ai` = ඓ and `au` = ඖ in ISO, and in informal writing (ai 94%, au 97%). The national system now uses ĩ for ඓ | §1a, §1b, §2a | H |
| RS-029 | The formal systems disagree with each other on the nasals. ISO: ං = ṁ, ඞ = ṅ. Sri Lanka 2018+: ං = ṅ, ඞ = ṁ. ALA-LC: ං takes the class nasal | §1 | H |

---

## 5. Where conventions agree: recommendations for a phonetic romanization

1. **Use the values that formal and informal practice already share:**
   - `k g j p b m y r l s h f n` as the base consonants
   - `kh gh bh` as aspirates, and `dh` = ධ
   - `d` = ද (ISO and informal agree)
   - `a i u e o` short vowels and `ai` = ඓ, `au` = ඖ
   - the inherent vowel written as `a`, hal left unwritten
2. **Where informal practice departs from ISO, decide and state it.** The clearest cases:
   - `th` = ත and `t` = ට (informal) vs `t` / `ṭ` (ISO)
   - `ch` = ච (informal) vs `c` (ISO)
   - `w` (informal, KNAB's local practice) vs `v` (formal) for ව
   - `sh` for both ශ and ෂ (informal) vs ś / ṣ (formal)
3. **Mark vowel length explicitly, and avoid `ee`/`oo` for it.** Use `aa ii uu` (ISO 7-bit) for ā ī ū. `ee` and `oo` mean ī/ū to informal writers but ē/ō in ISO 7-bit, so they are ambiguous.
4. **Use `ae` / `aee` for ඇ / ඈ**, matching the ISO 7-bit form. Informal `e`/`a` collapses ඇ with එ and අ.
5. **Mark the prenasalized letters and anusvara explicitly** if the romanization must round-trip. Plain `nd`, `mb`, `ng` and `n` are ambiguous with න්ද, ම්බ, න්ග and න්. Prior art: the ISO breve and KNAB's middle dot.
6. **Pick one convention for ං and ඞ and document it**, since ISO and the national system swap ṁ and ṅ.
7. **Cover the gaps informal writing ignores:** a distinction between ෘ and ්‍රු, and values for ඏ ඐ ෟ ෳ (ISO and ALA-LC are the only prior art).

---

## 6. Open questions

1. How long-vowel and ඇ use differs between real chat text (social media) and the careful Dakshina romanizations. No chat-corpus counts per letter are published ❓.
2. Is the Dakshina Hugging Face mirror identical to the official release? ❓
3. The ALA-LC table is from interscript, not the LoC PDF (which failed to load). The 2011 ඇ value (ă vs æ) still needs checking ❓.

---

## Removed RS conventions

Removed: out of scope: RS-013, RS-015, RS-016, RS-021, RS-022, RS-023, RS-027, RS-028, RS-030, RS-031.

---

## Sources

- ISO 15919: <https://en.wikipedia.org/wiki/ISO_15919>
- UNGEGN WGRS Sinhala report v5.0 (2021): <https://arhiiv.eki.ee/wgrs/rom2_si.htm> · Survey Department converter: <https://www.survey.gov.lk/RomanizationConverter/>
- Interscript maps (UN 1972, ALA-LC 1997 / 2011): <https://github.com/interscript/maps>
- KNAB 1989: <https://arhiiv.eki.ee/knab/lat/kblsi1.pdf>
- Dakshina (Roark et al., LREC 2020), Hugging Face mirror: <https://huggingface.co/datasets/Anvesh-Lankala/Copy_Dakshina_Google_research_dataset>
- Athukorala & Sumanathilaka, Swa Bhasha: <https://arxiv.org/abs/2404.13350>
- Perera, Prabhath, Sumanathilaka & Anuradha, IndoNLP 2025: <https://aclanthology.org/2025.indonlp-1.16.pdf>
- Perera & Sumanathilaka, RANLP 2025: <https://aclanthology.org/2025.ranlp-1.107.pdf>
- Sumanathilaka et al., Swa-bhasha Resource Hub: <https://arxiv.org/abs/2507.09245>
