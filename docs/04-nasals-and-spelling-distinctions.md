# 04: Nasals, ayogavaha signs, and the ණ/න · ළ/ල · ශ/ෂ/ස spelling distinctions

Scope: the nasal and nasal-related signs of Sinhala (anusvara (ං), visarga (ඃ), candrabindu (ඁ), the prenasalised ("sanyaka") letters ඟ ඦ ඬ ඳ ඹ and the nasal consonants ඞ ඤ ඥ ණ න ම) together with the spelling distinctions that sound alone cannot decide: ණ/න, ළ/ල and ස/ශ/ෂ. For each, the file gives where the sign may occur, how it is pronounced, and the orthographic rules (mostly from school grammar and Sanskrit/Pali etymology) that choose between homophonous letters. A closing section draws out the consequences for romanization and transliteration.

Compiled October 2026. All rules are summarised in my own words. Short quotes are marked.

---

## 0. How to read this file

| Field | Meaning |
|---|---|
| **ID** | `NS-nnn`. Stable, so later docs can refer to it. |
| **Statement** | The rule. |
| **Examples** | Sinhala + romanisation. The romanisation is ISO 15919-style (ṃ = ං, ḥ = ඃ, n̆g/n̆ḍ/n̆d/m̆b = sanyaka, ṇ = ණ, ḷ = ළ, ś = ශ, ṣ = ෂ). |
| **Exceptions** | Known counter-cases. |
| **Applies-to** | Letter IDs (used throughout this repository). `anusvara`, `visarga` and `candrabindu` are used for the signs. |
| **Confidence** | high = two or more independent sources, or one normative source (Unicode, ICANN LGR, SLS). medium = one good source, or several informal sources that agree. low = inferred or a single informal source. |
| **Sources** | URLs (see the full list in §11). |

**UNVERIFIED** marks a claim that rests on my general knowledge of Sinhala and Sanskrit, or that I could not confirm in a fetched source.

### Source shorthand

| Key | Source |
|---|---|
| [UNI] | Unicode Standard, ch. 13.2 Sinhala (v15.0 PDF, also the v18.0 HTML) |
| [ICANN-P] | Sinhala Generation Panel, *Proposal for a Sinhala Script Root Zone LGR* (22 Apr 2019) |
| [ICANN-LGR] | Root Zone LGR for Sinhala (rz-lgr-6, Sep 2025) |
| [WG2] | ISO/IEC JTC1/SC2/WG2 N1473R (the Sinhala encoding proposal, derived from SLS 1134) |
| [UD-AV] | Usgoda Dhammagaru, *සිංහල භාෂාවේ අක්ෂර වින්‍යාසය* (archive.org, Index_201704/dhgra002.pdf). A Sinhala teaching handout on orthography. It is the most systematic rule list I found. |
| [UD-AM] | Usgoda Dhammagaru, *සිංහල අක්ෂරමාලාව* (archive.org, dhgra001.pdf). Covers the history of the alphabet: Sidat Sangarava, NIE 60-letter alphabet, J.B. Disanayaka 1990, Unicode. |
| [ASSAJ] | Ven. K. Assajithissa (2021), "Sources of Sinhala Retroflex Lateral /ḷ/", *Journal of Humanities* 28, Univ. of Kelaniya |
| [BAND] | S. Bandarage, "Loss and re-introduction of nasals in Sinhalese", *Ceylon Journal of the Humanities* (Peradeniya IR) |
| [MADD] | I. Maddieson (1989), "Prenasalized stops and speech timing", *JIPA* |
| [FEIN] | M. Feinstein (1977/1979), *Linguistic nature of prenasalization*; "Prenasalization and syllable structure", *LI* 10 |
| [SIWIKI-AV] | si.wikipedia, සිංහල අක්ෂර වින්‍යාසය |
| [WP-SCRIPT] / [WP-LANG] / [WP-PNC] | en.wikipedia: Sinhala script / Sinhala language / Prenasalized consonant (used only as leads) |
| [UNGEGN] | UNGEGN Romanization report: Sinhala (Sri Lanka Survey Dept system, Cabinet-approved 2018) |
| [KS-NN] | ketisatahan.online.lk, "ණ,න අක්ෂර වින්‍යාසය රීති" |
| [KS-NGA] | ketisatahan.online.lk, traditional ඞ/ඤ words now written with ං |
| [UTH] | uthmax.blogspot.com, මූර්ධජ 'ණ' යන්න පිළිබඳ සම්මතයන් |
| [SANH] | sanhindha.blogspot.com, සිංහලයේ න ණ ල ළ වහර. Cites Kudatihi 2000, Senadheera 1999, and Sumanajothi & Paññāloka 1999. |
| [LLS] | letslearnsinhala.blogspot.com, අක්ෂර වින්‍යාසය |
| [TI943] | throughinternet943.blogspot.com, දන්තජ න හා මූර්ධජ ණ |
| [SDVP] | sdvp10.blogspot.com, a Grade-10/11 Sinhala lesson (16 පාඩම II) |
| [ADYA] | adyapanika01.blogspot.com, සඤ්ඤක අක්ෂර |
| [SLAK] | sundaralakdiwa.blogspot.com, සඤ්ඤක අක්ෂර |
| [GG-SAN] | Google Groups sinhala-bloggers, "සඤ්ඥක අකුරු සහිත වචන" |
| [GG-UNI] | Google Groups sinhala-unicode, "අක්ෂර වින්‍යාසය සහ ණ, න සහ ළ, ල භේදය" (2006) |
| [GANESAN] | N. Ganesan, unicode-ml post, July 2006, on U+0DA5 |
| [NLPC] | A. Fernando and G. Dias (2021), "Building a Linguistic Resource: A Word Frequency List for Sinhala", ICON 2021 (University of Moratuwa NLPC; github.com/nlpcuom/Word-Frequency-List-for-Sinhala) |

> **Coverage gap.** I could not reach the NIE / educationpublications.gov.lk textbooks or the SLS 1134 text online. [UD-AV], [UD-AM] and the school-lesson blogs ([SDVP], [KS-NN], [LLS]) appear to reproduce the school rule set; their wording matches each other closely. Treat them as secondary until someone checks them against an NIE Grade 6–11 Sinhala textbook.

---

## ⚠️ Things that will bite you (front-loaded)

For anyone converting between romanized and Sinhala text, checking spelling, or analysing the orthography.

1. **"ng" has at least four spellings**, and they are not interchangeable:
   - ං (`anusvara`): අංගය *aṃgaya* 'component'
   - ඟ (`nnga`): අඟල *an̆gala* 'inch'
   - ඞ් + ග (Pali/archaic): සඞ්ඝ
   - ං word-finally with no g: සුළං *suḷaṃ* 'wind'

   See NS-005, NS-030 and NS-033.
2. **"nd" and "mb" are lexical, not rule-driven.** Compare කඳ *kan̆da* 'trunk' with කන්ද *kanda* 'hill'. Both are native words. No orthographic rule picks the right one (NS-033), so a dictionary is needed.
3. **Romanized *nda* and *nya* are ambiguous.** The letter ID `nda` = ඳ, but plain Latin-script *nda* more often stands for න්ද. Likewise `nya` = ඤ collides with න්‍ය (ධන්‍ය, අන්‍ය, ශූන්‍ය), which is far more common (NS-047).
4. **`gn` is not always ඥ.** Compare අග්නි *agni* 'fire' and නග්න *nagna* 'naked' with ඥානය *jñānaya* (NS-046).
5. **ණ/න and ළ/ල are pronounced the same** in modern Sinhala (NS-050, NS-070). A sound-based romanization cannot recover them. Only morphology and etymology can, and the rules are mostly about Sanskrit-origin words plus a few native suffixes.
6. **Retroflexion after ර is reversed in native verbs.** Tatsama මරණ *maraṇa* 'death' takes ණ, but the native participle මරන *marana* 'killing' takes න (NS-051, NS-061).
7. **ං never takes a vowel sign, and nothing can follow a hal** (al-lakuna). Sanyaka letters can never take hal (NS-002, NS-031).
8. **ශ and ෂ are both pronounced [ʃ].** Choosing between them depends on the neighbouring consonant (NS-081 to NS-086).
9. **ඞ, ඩ and ඬ look alike.** A ඞ in modern text is nearly always a mistyped ඩ (කොවිඞ් for කොවිඩ්), and a word-initial ඬ is too (NS-048).

---

## 1. Anusvara / binduva: ං (U+0D82)

Names: *anusvāraya*, *binduva* ("zero"), *nāsikya* [WG2].

### NS-001: Position: always after a base, never word-initial, never after hal
- **Statement.** ං is a combining sign. It must follow one of these bases:
  - an independent vowel (V)
  - a consonant with its inherent *a* (C)
  - a consonant plus a vowel sign (C+M)
  - a sanyaka letter (J)

  It cannot follow al-lakuna (්). It cannot start a word or stand alone.
- **Examples.**
  - අං *aṃ* 'horn' (V+ං)
  - කං *kaṃ* (C+ං)
  - පිං *piṃ* (C+M+ං; the ICANN example)
  - ඳං *n̆daṃ* (J+ං; allowed by the LGR but practically unattested)
- **Exceptions.** None. ් + ං is invalid.
- **Applies-to.** anusvara, hal, all vowels, all consonants, nnga nyja nndda nda mba.
- **Confidence.** high.
- **Sources.** [ICANN-P] §3.3.4 and §5.6.3–5.6.5; [ICANN-LGR].

### NS-002: ං carries no vowel sign of its own
- **Statement.** The vowel belongs to the preceding base, so the encoding order is base + vowel sign + ං. ං cannot be "killed" with hal and cannot be followed by a vowel sign. In speech it closes the syllable.
- **Examples.**
  - පුංචි *puṃci* 'small'
  - සිංහල *siṃhala*
  - කෝං *kōṃ* (ICANN example, C+ෝ+ං)
  - ඉංග්‍රීසි *iṃgrīsi* 'English'
- **Exceptions.** None.
- **Applies-to.** anusvara, all vowels.
- **Confidence.** high.
- **Sources.** [ICANN-P] Table 7.

### NS-003: Phonetic value: [ŋ]
- **Statement.** ං is pronounced as the velar nasal [ŋ]. The Sinhala GP describes it as representing "a general nasal sound" (short quote).
- **Examples.**
  - ලංකා *laṃkā* [laŋkaː]
  - සිංහ *siṃha* [siŋhə]
- **Exceptions.** In Sanskrit, anusvara before a stop is often read as the homorganic nasal. In Sinhala, the spelling itself switches to ණ්/න්/ම් in those cases (NS-005). **UNVERIFIED:** whether ං before ව/ස/හ is still a full [ŋ] or partly a nasalised vowel.
- **Applies-to.** anusvara, nga.
- **Confidence.** high for [ŋ].
- **Sources.** [ICANN-P] §3.3.4; [ICANN-LGR]; [UNGEGN] romanises ං as **ṅ**.

### NS-004: ං has replaced ඞ් (and often ඤ්) in modern spelling
- **Statement.** Words traditionally spelled with a velar nasal hal (ඞ්), and some with a palatal one (ඤ්), are now written with ං. ඞ් is the same sound as ං but is now archaic or Pali-only (NS-040).
- **Examples.**
  - මඞ්ගල → මංගල *maṃgala* 'auspicious'
  - ලඞ්කාව → ලංකාව *laṃkāva*
  - වඤ්චාව → වංචාව *vaṃcāva* 'fraud'
- **Exceptions.** Pali texts in Sinhala script keep ඞ්/ඤ් (e.g. සඞ්ඝ), and also use ං for *niggahīta* (බුද්ධං සරණං). **UNVERIFIED** for specific editions.
- **Applies-to.** anusvara, nga, nya.
- **Confidence.** medium.
- **Sources.** [KS-NGA]; [GG-UNI] (a commenter notes binduva can stand for ඤ medially, but only as a lead); [UD-AM] (the Sidat Sangarava alphabet lists අං among its consonants).

### NS-005: Choosing ං vs a nasal + hal before a consonant (tatsama words)
- **Statement.** Spelling follows Sanskrit/Pali practice for the nasal before a consonant:

| Following consonant | Spelling | Examples |
|---|---|---|
| Velar ක ඛ ග ඝ | **ං** | අංකය *aṃkaya*, සංඛ්‍යාව *saṃkhyāva*, අංගය *aṃgaya*, සංඝයා *saṃghayā*, මංගල |
| Palatal ච ඡ ජ ඣ | **ං** in modern spelling; **ඤ්** in Pali and older spelling | වංචාව / Pali වඤ්චා; සංචාරය *saṃcāraya*; පංච ~ පඤ්ච *pañca* |
| Retroflex ට ඨ ඩ ඪ | **ණ්** (never ං) | කණ්ටකය *kaṇṭakaya*, කණ්ඨය, මණ්ඩලය *maṇḍalaya*, පණ්ඩිත *paṇḍita*, ආණ්ඩුව *āṇḍuva* |
| Dental ත ථ ද ධ | **න්** (normally) | සන්තෝෂය *santōṣaya*, ග්‍රන්ථය *granthaya*, සන්දේශය *sandēśaya*, සන්ධිය *sandhiya*, චන්ද්‍ර *candra* |
| Labial ප ඵ බ භ ම | **ම්** | සම්පත *sampata*, සම්බන්ධය *sambandhaya*, සම්භාවනා, සම්මතය *sammataya*, සම්පූර්ණ |
| Semivowels, sibilants and h: ය ර ල ව ශ ෂ ස හ | **ං** (always) | සංයෝගය *saṃyōgaya*, සංරක්ෂණය *saṃrakṣaṇaya*, සංවාදය *saṃvādaya*, සංශෝධනය *saṃśōdhanaya*, සංස්කෘතිය *saṃskṛtiya*, සංහාරය *saṃhāraya*, සිංහ, හංස, වංශ, මාංශ |

- **Exceptions.**
  - Before dentals, learned coinages with the prefix *saṃ-* often keep ං: සංදර්ශනය ~ සන්දර්ශනය, සංතෘප්ත 'saturated'. **UNVERIFIED** as a rule; I found no official statement.
  - Before palatals, usage varies (NS-043).
- **Applies-to.** anusvara, nga nya nna na ma; ka kha ga gha ca cha ja jha tta ttha dda ddha ta tha da dha pa pha ba bha ma ya ra la va sha ssa sa ha.
- **Confidence.**
  - high: retroflex → ණ් ([UD-AV]: a retroflex consonant is preceded by ණ්; [KS-NN]; [TI943])
  - high: dental → න් ([TI943]: න් before ත ථ ද ධ)
  - medium: velar → ං, labial → ම්, and ං before ය ර ල ව ශ ස හ. A search snippet from a Sinhala lesson page said binduva stays unchanged before ය් ර් ල් ව් ශ් ස් හ්, but I could not open that page. The rest is Sanskrit sandhi and well-attested spellings.
- **Sources.** [UD-AV]; [KS-NN]; [TI943]; [UNI] (shows අඬ vs අණ්ඩ, i.e. ණ්ඩ written with a full nasal plus hal).

### NS-006: *saṃ-* / *sam-* before a vowel → ම + vowel sign (no ං)
- **Statement.** In Sanskrit compounds, prefix-final *m* before a vowel is written as ම carrying that vowel. ං is not written before a vowel inside a word.
- **Examples.**
  - සමාගම *samāgama* (sam+āgama)
  - සමාලෝචනය *samālōcanaya*
  - සමූපකාර / සමුපකාර *samūpakāra* (sam+upakāra; both spellings occur on government sites)
  - සමීක්ෂණය *samīkṣaṇaya*
- **Exceptions.** **UNVERIFIED:** whether colloquial or compound spellings like ගංඉවුර ever write ං directly before an independent vowel. Normally such compounds are written as two words (ගං ඉවුර).
- **Applies-to.** anusvara, ma, all vowels.
- **Confidence.** medium (Sanskrit sandhi; examples are standard words).
- **Sources.** General Sanskrit grammar. Examples checked against usage (coop.gov.lk uses සමූපකාර / සමුපකාර).

### NS-007: Native words: ං alternates with ඟ (and other sanyaka) at stem or compound boundaries
- **Statement.** Several native nouns that end in a sanyaka syllable use a ං-final stem in compounds and in some inflections.
- **Examples.**
  - ගඟ *gan̆ga* 'river' → ගංවතුර *gaṃvatura* 'flood', ගංතෙර
  - මඟ *man̆ga* 'road' → මංසන්ධිය *maṃsandhiya* 'junction', මංමාවත්
  - අඟ *an̆ga* 'horn' ~ අං *aṃ*
- **Exceptions.** Not a documented rule. These are lexical patterns.
- **Applies-to.** anusvara, nnga.
- **Confidence.** low–medium. **UNVERIFIED** as a stated rule; the example words are standard.
- **Sources.** None found that state this rule.

### NS-008: Word-final ං in native words and in colloquial writing
- **Statement.** ං is common word-finally:
  - in native lexemes: සුළං *suḷaṃ* 'wind', which [ASSAJ] cites from Disanayaka as an indigenous ḷ-word
  - in informal or colloquial spellings that stand for a final nasal

  Formal written Sinhala usually has ම් or න් in the colloquial cases.
- **Examples.**
  - මං *maṃ* 'I' (formal මම)
  - එහෙනං *ehenaṃ* 'then' (formal එසේ නම් / එහෙනම්)
  - මෙහෙං / එහෙං / කොහෙං 'from here / there / where' (formal -න්)
  - උං *uṃ* 'they' (coarse)
- **Exceptions.** In formal writing these are written ම් / න්. [GG-UNI] notes that ං use belongs to folk and verse registers.
- **Applies-to.** anusvara, ma, na, hal.
- **Confidence.** medium. The colloquial examples are **UNVERIFIED** against a written-grammar source; [GG-UNI] supports the general point.
- **Sources.** [ASSAJ]; [GG-UNI].

### NS-009: Contrast: final ං vs final ම් / න්
- **Statement.** Word-final ං [ŋ] contrasts with ම් [m] and න් [n], so the three are different words.
- **Examples.**
  - දං *daṃ* 'jambu fruit' vs දන් *dan* 'alms' (දන්සැල) ([GG-UNI])
  - ගං- 'river (stem)' vs ගම් *gam* 'villages' (**UNVERIFIED** pairing)
- **Exceptions.** None.
- **Applies-to.** anusvara, ma, na.
- **Confidence.** medium.
- **Sources.** [GG-UNI].

### NS-010: ං after independent vowels
- **Statement.** ං may follow any independent vowel letter.
- **Examples.**
  - අං *aṃ*
  - ඉංග්‍රීසි *iṃgrīsi*
  - උං *uṃ*
- **Exceptions.** None known.
- **Applies-to.** anusvara, a aa ae aee i ii u uu e ee o oo.
- **Confidence.** high (structure); medium (examples).
- **Sources.** [ICANN-P] Table 6.

### NS-011: ං in English and other recent loans (before k/g)
- **Statement.** Loanwords with [ŋk] or [ŋg] use ං.
- **Examples.**
  - බැංකුව *bæṃkuva* 'bank'
  - ටැංකිය *ṭæṃkiya* 'tank'
  - කොංක්‍රීට් *koṃkrīṭ* 'concrete'
  - ඉංජිනේරු *iṃjinēru* 'engineer' (before j)
- **Exceptions.** None known.
- **Applies-to.** anusvara.
- **Confidence.** medium (**UNVERIFIED** in a cited source; standard spellings).
- **Sources.** None.

### NS-012: ං vs ඟ: two different sequences
See NS-030 to NS-033. ං+ග is [ŋ.g], heavy and heterosyllabic, as in අංගය. ඟ is [ᵑg], a light onset, as in අඟල.

---

## 2. Visarga: ඃ (U+0D83)

Names: *visargaya*, *visarjanīya* [WG2].

### NS-020: Rare, Sanskrit-only, pronounced [h]
- **Statement.** ඃ is rarely used. It occurs almost only in Sanskrit borrowings and is read as [h].
- **Examples.**
  - අන්තඃපුරය *antaḥpuraya* 'harem' (the ICANN example)
  - දුඃඛ *duḥkha* 'suffering' (Pali form දුක්ඛ, native දුක)
  - මනඃකල්පිත *manaḥkalpita* 'imaginary' (**UNVERIFIED** in a fetched source)
  - අතඃ *ataḥ*, පුනඃ *punaḥ* (literary only; **UNVERIFIED** in a fetched source)
- **Exceptions.** See NS-024 (a colloquial case).
- **Applies-to.** visarga.
- **Confidence.** high.
- **Sources.** [ICANN-P] §3.3.5; [ICANN-LGR].

### NS-021: Position: after a vowel, a consonant, or a consonant + vowel sign; never after hal
- **Statement.** Same constraint as ං, except that sanyaka letters are not listed as valid bases (see NS-024).
- **Examples.**
  - අඃ (V+ඃ)
  - කඃ (C+ඃ)
  - කිඃ *kiḥ* (C+M+ඃ)
- **Exceptions.** Never after ්.
- **Applies-to.** visarga, hal.
- **Confidence.** high.
- **Sources.** [ICANN-P] Tables 6–7; [ICANN-LGR].

### NS-022: Visarga sandhi in tatsama words (where ඃ disappears into another letter)
- **Statement.** Most Sanskrit visarga in Sinhala vocabulary shows up as a sandhi result, not as ඃ:

| Context | Result | Examples |
|---|---|---|
| -aḥ + voiced consonant | **-o** (ෝ) | මනෝවිද්‍යාව *manōvidyāva*, මනෝරථ, යශෝධරා |
| -iḥ / -uḥ + vowel or voiced consonant | **-r** (ර්, or ර + vowel) | නිර්මාණ *nirmāṇa*, නිරෝගී, දුර්වල *durvala*, පුනර්ජීවනය, පුනරුදය |
| before ච / ඡ | **ශ්** | නිශ්චල *niścala*, දුශ්චරිත *duścarita* |
| before ත / ථ, and namas-/manas- before k | **ස්** | මනස්තාපය, නමස්කාරය *namaskāraya*, මනස්කාන්ත |
| before k / p after i or u | **ෂ්** | දුෂ්කර *duṣkara*, නිෂ්පාදනය *niṣpādanaya*, නිෂ්ඵල |
| before ශ / ස | doubled sibilant | නිශ්ශබ්ද *niśśabda*, නිස්සාර (**UNVERIFIED**) |

- **Exceptions.** None noted.
- **Applies-to.** visarga, ra, sha, ssa, sa, o oo.
- **Confidence.** medium. The sandhi pattern is standard Sanskrit. The Sinhala examples for ශ්/ෂ්/ස් come from [UD-AV] and [SIWIKI-AV]. The ෝ and ර් examples are standard spellings, **UNVERIFIED** in a fetched Sinhala grammar.
- **Sources.** [UD-AV]; [SIWIKI-AV]; en.wikipedia Visarga (lead only).

### NS-023: Not part of the native (*śuddha*) alphabet
- **Statement.** Visarga is technically a *miśra* (mixed, Sanskrit) sign:
  - The Sidat Sangarava (13th c.) alphabet left it out.
  - The NIE 60-letter alphabet and Unicode include it.
  - The proposed "spoken Sinhala" (භාෂණ) 40-letter alphabet drops both ඃ and ං.
- **Examples.** -
- **Exceptions.** -
- **Applies-to.** visarga, anusvara.
- **Confidence.** high.
- **Sources.** [UD-AM]; [WP-SCRIPT].

### NS-024: Colloquial ඃ after a sanyaka
- **Statement.** The Sinhala GP notes that a few colloquial words put ඃ after a sanyaka, e.g. ඉඳඃ *in̆daḥ*. Standard writing has no such sequence.
- **Examples.** ඉඳඃ.
- **Exceptions.** -
- **Applies-to.** visarga, nnga nyja nndda nda mba.
- **Confidence.** low (single source).
- **Sources.** [ICANN-P] §5.6.5.

---

## 3. Candrabindu: ඁ (U+0D81)

### NS-025: Not used in modern Sinhala
- **Statement.** Unicode reserves ඁ for "some archaic Sanskrit texts" (short quote) and says it is not for modern Sinhala. The ICANN repertoire does not include it. It does not appear in any school alphabet: not Sidat Sangarava, NIE-60, Disanayaka-60 or Unicode-61.
- **Examples.** None in modern text.
- **Exceptions.** Specialist Sanskrit editions only. [GANESAN] mentions candrabindu as one way to render Sinhala half-nasals in *other* Indic scripts. That is not a Sinhala use.
- **Applies-to.** candrabindu.
- **Confidence.** high.
- **Sources.** [UNI]; [ICANN-LGR]; [UD-AM]; [GANESAN].

---

## 4. Sanyaka (prenasalised) letters: ඟ ඦ ඬ ඳ ඹ

Names: *sañ​ñaka akuru*, *ardha-nāsikya* / *ardhānunāsika* ("half-nasal").

### NS-030: Inventory and make-up
- **Statement.** There are five letters. Each is a short homorganic nasal fused to a voiced unaspirated stop:

| Letter | Letter ID | Parts | IPA |
|---|---|---|---|
| ඟ | nnga | ඞ+ග | [ᵑɡ] |
| ඦ | nyja | ඤ+ජ | [ⁿdʒ] |
| ඬ | nndda | ණ+ඩ | [ᶯɖ] |
| ඳ | nda | න+ද | [ⁿd̪] |
| ඹ | mba | ම+බ | [ᵐb] |

  Only voiced stops (ග ජ ඩ ද බ) have sanyaka forms.
- **Examples.**
  - ගඟ *gan̆ga*
  - හොඬ *hon̆ḍa*
  - ඇඳ *æn̆da* 'bed'
  - අඹ *am̆ba* 'mango'
- **Exceptions.** -
- **Applies-to.** nnga nyja nndda nda mba.
- **Confidence.** high.
- **Sources.** [ADYA]; [SLAK]; [WP-SCRIPT]; [UNI].

### NS-031: Never with hal; never word-initial
- **Statement.**
  - A sanyaka letter cannot take al-lakuna, so it never closes a syllable or ends a word as a dead consonant.
  - It does not occur word-initially. It appears word-medially (intervocalically) or as the last syllable of a word with a vowel.
- **Examples.**
  - අඹ, හඳ, ගඟ, තරඟ, සුරඹ (final syllable, with a vowel)
  - ඳ් and ඹ් are impossible
- **Exceptions.** None attested for word-initial position in native vocabulary. **UNVERIFIED** for onomatopoeia and very recent loans.
- **Applies-to.** nnga nyja nndda nda mba, hal.
- **Confidence.** high (hal, from the normative ICANN rule); high (initial, from several school sources).
- **Sources.** [ICANN-P] §3.3.6; [ICANN-LGR]; [ADYA]; a Sinhala lesson-site search snippet (lead).

### NS-032: Phonetics: short nasal onset vs nasal + stop cluster
- **Statement.**
  - **Sanyaka:** the nasal part is very short and never makes the preceding syllable heavy. Stress or accent does not fall before it.
  - **Nasal + stop** (න්ද, ම්බ, ං+ග): a full nasal that closes the preceding syllable, which is therefore heavy.

  Sinhala is one of only three languages reported to contrast the two, with Fula and Selayarese. Some phonologists analyse the contrast as one versus two nasal timing units (geminate-like vs single nasal) rather than unit vs cluster.
- **Examples.**
  - කද *kada* 'carrying pole' / කන *kana* 'ear' / කඳ *kan̆da* 'trunk' / කන්ද *kanda* 'hill'
  - අඬ *an̆ḍa* 'cry, sound' vs අණ්ඩ *aṇḍa* 'egg' (Sanskrit; Unicode's example)
- **Exceptions.** -
- **Applies-to.** nnga nndda nda mba, na, nna, ma, anusvara.
- **Confidence.** high.
- **Sources.** [UNI]; [WP-PNC]; [BAND]; [MADD]; [FEIN].

### NS-033: Choosing a sanyaka vs ං/nasal + hal + stop: a lexical choice
- **Statement.** There is no phonological rule that predicts the spelling. Practical guidance:
  - **Tatsama** (direct Sanskrit or Pali) words never use a sanyaka. They use ං before velars, and ණ්/න්/ම් before the other stops (NS-005). Examples: අංගය, ගංගාව, චන්ද්‍ර, සුන්දර, ආනන්ද, සම්බන්ධ.
  - **Native and tadbhava** (evolved) words often have a sanyaka where the Sanskrit source had a nasal cluster. Examples: අඟ / අඟල (< aṅga), ගඟ (< gaṅgā), සඳ (< candra), කඳ (< skandha), බඹ (< brahma; **UNVERIFIED** etymology).
  - **Native words can also have a real cluster.** Examples: කන්ද 'hill', හන්දිය 'junction' (**UNVERIFIED** etymology), මන්දා.
  - **English and other modern loans** use a cluster. Examples: ලන්ඩන්, කැලැන්ඩර්, සිලින්ඩර්.
- **Examples.** අඟල vs අංගය; ගඟ vs ගංගාව; හඳ / සඳ vs චන්ද්‍රයා; කඳ vs කන්ද.
- **Exceptions.** See NS-034 (optional variants).
- **Applies-to.** nnga nndda nda mba, anusvara, na, nna, ma, ga, dda, da, ba.
- **Confidence.** medium. The tatsama/native split is a strong tendency, not a stated rule. [BAND] documents that many sanyaka continue Old Indo-Aryan nasal + stop clusters, and that others arose from secondary nasalisation.
- **Sources.** [BAND]; [UNI]; [UTH] (loans with න්ඩ).

### NS-034: Some words allow a sanyaka or a plain stop
- **Statement.** A set of words is written either with a sanyaka or with the plain voiced stop. Both spellings are accepted.
- **Examples.**
  - උරග / උරඟ 'serpent'
  - මග / මඟ 'road'
  - නගියි / නඟියි
  - මගුල් / මඟුල් 'wedding'
  - මඩුව / මඬුව
  - නිදි / නිඳි
  - කලබ / කලඹ
- **Exceptions.** -
- **Applies-to.** nnga nndda nda mba, ga dda da ba.
- **Confidence.** medium.
- **Sources.** [SLAK]; [ADYA].

### NS-035: Vowel signs on sanyaka letters
- **Statement.** Sanyaka letters take every dependent vowel sign, and can be followed by ං (rare). Rendering note: ු and ූ take special forms on ඟ, as they do on ක, ග, ත, භ and ශ.
- **Examples.**
  - ඟු *n̆gu* (in මඟුල්)
  - ඳි *n̆di* (in ඉඳි)
  - ඹු *m̆bu* (in අඹුව *am̆buva* "wife"; **UNVERIFIED** in a fetched source)
  - ඬු *n̆ḍu* (in මඬුව)
  - ඳෙ *n̆de* (in වෙළෙඳ)
- **Exceptions.** No hal (NS-031). Visarga only colloquially (NS-024).
- **Applies-to.** nnga nyja nndda nda mba, all vowels.
- **Confidence.** high.
- **Sources.** [ICANN-P] Table 8; [UNI] (vowel-sign alternates).

### NS-036: ඦ is (almost) never used
- **Statement.** ඦ is part of the NIE alphabet and of Unicode, but it is extremely rare:
  - The ICANN LGR leaves it out as "not frequently used".
  - J.B. Disanayaka's 1990 alphabet dropped it in favour of ඥ.
  - The one word usually cited is the dog-call ඉඦු (attributed to Disanayaka).
- **Examples.** ඉඦු *in̆ju*.
- **Exceptions.** See §10 for the conflict.
- **Applies-to.** nyja.
- **Confidence.** high for "rare". Whether it is ever used is disputed.
- **Sources.** [ICANN-P] §3.3.6; [ICANN-LGR]; [UD-AM]; [ADYA]; [GG-SAN]; [WP-SCRIPT].

### NS-037: Nothing nasal precedes a sanyaka
- **Statement.** A sanyaka already contains its nasal, so ං+ඟ or න්+ඳ is redundant and not written.
- **Examples.** අඹ, never අංඹ.
- **Exceptions.** -
- **Applies-to.** nnga nyja nndda nda mba, anusvara.
- **Confidence.** medium (follows from the structure; no source states it).
- **Sources.** -

---

## 5. The nasal consonants ඞ ඤ ඥ ණ න ම

### NS-040: ඞ (*kaṇṭhaja nāsikyaya*, velar nasal)
- **Statement.** ඞ is rare in modern Sinhala and almost never occurs as a live syllable. Its hal form ඞ් appears in Pali written in Sinhala script and in a few learned Sanskrit words. Elsewhere it has been replaced by ං (NS-004).
- **Examples.**
  - Pali සඞ්ඝ *saṅgha* vs modern සංඝයා
  - වාඞ්මය *vāṅmaya* 'literature' (learned; **UNVERIFIED** current frequency)
- **Exceptions.** -
- **Applies-to.** nga, hal.
- **Confidence.** medium.
- **Sources.** [KS-NGA]; [UD-AM] (Sidat Sangarava left out the class-final nasals ඞ and ඤ).

### NS-041: ඤ (*tāluja nāsikyaya*, palatal nasal)
- **Statement.** ඤ is used:
  - word-initially in a handful of Pali-derived words
  - as a geminate ඤ්ඤ in Pali words and a few native or loan words
  - before ච/ජ in Pali and older spellings

  In modern Sinhala the hal form before a palatal is often replaced by ං (NS-043).
- **Examples.**
  - ඤාතියා *ñātiyā* 'relative' (also ඥාතියා; see §10)
  - Pali ඤාණ *ñāṇa*
  - සඤ්ඤා *saññā*, පඤ්ඤා *paññā*
  - මඤ්ඤොක්කා *maññokkā* 'manioc' (**UNVERIFIED** in a fetched source)
  - පඤ්ච *pañca*, අඤ්ජන *añjana*, කුඤ්ජර
- **Exceptions.** -
- **Applies-to.** nya, hal.
- **Confidence.** medium.
- **Sources.** [KS-NGA]; [UD-AM].

### NS-042: ඥ (*tāluja sanyōga nāsikyaya*): the ජ්+ඤ conjunct
- **Statement.**
  - **Encoding.** ඥ is a single code point, U+0DA5. It represents the Sanskrit conjunct *jñ* (ජ්+ඤ). Unicode says it is "atomically encoded" (short quote).
  - **Pronunciation.** Sri Lankan speech is commonly *gn* / *gny*. The Survey Dept romanisation is **gna**, and personal names use *Gnana-* and *Pragna*. Wikipedia gives [dʒɲ], which is the Sanskrit value.
  - **Usage.** Only in tatsama words with *jñ*, including the agent suffix *-jña* 'knower, expert'.
- **Examples.**
  - ඥානය *jñānaya* 'knowledge'
  - ප්‍රඥාව *prajñāva* 'wisdom'
  - ආඥාව *ājñāva* 'command'
  - යඥය *yajñaya* 'sacrifice'
  - සංඥාව *saṃjñāva* 'signal'
  - ඥාතියා *jñātiyā*
  - විද්‍යාඥයා *vidyājñayā* 'scientist'
  - ශාස්ත්‍රඥ *śāstrajña*
  - නීතිඥ *nītijña* 'lawyer' (also seen as නීතීඥ)
  - කෘතඥ *kṛtajña* 'grateful'
- **Exceptions.** Not every *gn* is ඥ (NS-046).
- **Applies-to.** jnya, ja, nya.
- **Confidence.** high (encoding, usage); medium (pronunciation).
- **Sources.** [UNI]; [ICANN-P] §3.3.1; [UNGEGN]; [GANESAN]; [WP-SCRIPT]; [UD-AM] (Disanayaka added ඥ as a letter of its own in 1990).

### NS-043: Palatal-nasal spellings vary
- **Statement.** Before ච/ජ, and in the *saṃ+jñ* prefix, both ං and ඤ් spellings occur. Modern general writing leans towards ං.
- **Examples.**
  - පංච ~ පඤ්ච
  - වංචා ~ වඤ්චා
  - සංඥා ~ සඤ්ඥා (**UNVERIFIED**)
  - සංජානනය
- **Exceptions.** -
- **Applies-to.** anusvara, nya, ca, ja, jnya.
- **Confidence.** low–medium.
- **Sources.** [KS-NGA]; [GG-UNI].

### NS-044: ම: no special rule
- **Statement.** ම behaves like any other consonant. Before labials, ම් is the nasal hal (NS-005), and *sam-* plus a vowel gives ම (NS-006).
- **Examples.** සම්පත, සම්බන්ධ, සමාගම.
- **Exceptions.** -
- **Applies-to.** ma.
- **Confidence.** high.
- **Sources.** -

### NS-045: න / ණ: see §6 (NS-050 to NS-066).

### NS-046: Gotcha: ග්න ≠ ඥ
- **Statement.** Sanskrit *gn* (ග්න) is a separate cluster from *jñ* (ඥ).
- **Examples.**
  - අග්නි *agni* 'fire'
  - නග්න *nagna* 'naked'
  - ලග්න *lagna* 'ascendant'
- **Exceptions.** -
- **Applies-to.** ga, na, jnya, hal.
- **Confidence.** medium (standard spellings; **UNVERIFIED** in a fetched source).
- **Sources.** -

### NS-047: Gotcha: ඤ ≠ න්‍ය
- **Statement.** *nya* in tatsama words is very often න + yansaya (න්‍ය), not ඤ.
- **Examples.**
  - අන්‍ය *anya* 'other'
  - ධන්‍ය *dhanya*
  - ශූන්‍ය *śūnya* 'zero'
  - මාන්‍ය *mānya*
  - වන්‍ය *vanya* 'wild'
- **Exceptions.** -
- **Applies-to.** nya, na, ya.
- **Confidence.** high.
- **Sources.** [UNI] (yansaya = ්+ZWJ+ය).

### NS-048: Gotcha: ඞ in a word is almost always a typo for ඩ
- **Statement.** ඞ (U+0D9E, nga) and ඩ (U+0DA9, dda) look almost the same in many fonts, and ඬ (U+0DAC, nndda) looks like ඩ too. In digital text, a ඞ that is not ඞ් before a velar (NS-040) is a mistyped ඩ, and a word-initial ඬ (banned by NS-031) is a mistyped ඩ. A ඞ or ඞ් right before a velar stands for the modern ං (NS-004).
- **Examples** (wrong → right, from [NLPC]):
  - කොවිඞ් → කොවිඩ් 'COVID', මොහොමඞ් → මොහොමඩ්, රිමාන්ඞ් → රිමාන්ඩ් 'remand', ඩොනල්ඞ් → ඩොනල්ඩ්
  - ඞීසල් → ඩීසල් 'diesel', ක්‍රීඞා → ක්‍රීඩා 'sports', ෆීල්ඞ් → ෆීල්ඩ් 'field'
  - ඬේවිඞ් → ඩේවිඩ් 'David' (initial ඬ and final ඞ් in one word)
  - සඞඝයා → සංඝයා, අස්තඞගමයද → අස්තංගමයද (ඞ before a velar, hal missing)
- **Evidence.** In a 37,547-word excerpt of [NLPC], all 15 words containing ඞ were typos of this kind: the correct ඩ spelling of each was also in the list and more frequent, usually 3 to 10 times (කොවිඩ් 2,328 vs කොවිඞ් 333). The 16th entry was a run-together token. No ඞ word in it was a correct modern spelling.
- **Exceptions.** Pali and a few learned words written with ඞ් before a velar (NS-040).
- **Applies-to.** nga, dda, nndda.
- **Confidence.** high (for modern prose).
- **Sources.** [NLPC]; [UNI] (code points).

---

## 6. ණ / න භේදය (retroflex vs dental n)

Background. ණ (*mūrdhaja*) and න (*dantaja*) are both pronounced [n] in modern Sinhala, so the difference is purely orthographic. It still separates meanings:
- කන *kana* 'ear (organ)' vs කණ *kaṇa* 'blind (in one eye)'
- දන *dana* 'people' vs දණ *daṇa* 'knee'
- වන *vana* 'forest' vs වණ *vaṇa* 'wound'
- also නුවන/නුවණ, ගන/ගණ, පහන/පහණ

Sources: [UD-AV]; [UTH]; [LLS]; [WP-SCRIPT].

### NS-050: ණ and න are homophones in modern Sinhala
- **Statement.** The retroflex nasal is not a separate phoneme in modern Sinhala.
- **Examples.** As above.
- **Exceptions.** -
- **Applies-to.** nna, na.
- **Confidence.** high.
- **Sources.** [WP-SCRIPT]; [WP-LANG]; [UD-AV].

### NS-051: After ර in Sanskrit/Pali words → ණ
- **Statement.** In tatsama words, an n that follows ර takes ණ.
- **Examples.**
  - සරණ *saraṇa* 'refuge'
  - ධාරණ *dhāraṇa*
  - කාරණ *kāraṇa*
  - විවරණ *vivaraṇa*
  - මරණ *maraṇa* 'death'
  - රණ *raṇa*
  - වාරණ *vāraṇa*
  - පරිහරණය, තරණය, තරුණයා *taruṇayā* 'youth'
- **Exceptions.** NS-061 (native verbs), NS-063 (compound boundary).
- **Applies-to.** nna, ra.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [LLS]; [TI943].

### NS-052: After repaya (ර්) or rakaransaya (්‍ර) → ණ
- **Statement.** An r that is part of a cluster (written as repaya or rakaransaya) also triggers ණ.
- **Examples.**
  - මන්ත්‍රණ *mantraṇa*
  - ප්‍රාණ *prāṇa*
  - වර්ණ *varṇa*
  - සම්පූර්ණ *sampūrṇa*
  - මිශ්‍රණය *miśraṇaya*
  - ශ්‍රේණිය *śrēṇiya*
  - ප්‍රණාමය *praṇāmaya*
  - ආමන්ත්‍රණය, චිත්‍රණ, ප්‍රවීණ, ග්‍රහණය, සංක්‍රමණ, අරණ්‍ය
- **Exceptions.** -
- **Applies-to.** nna, ra.
- **Confidence.** high.
- **Sources.** [UD-AV]; [KS-NN]; [TI943].

### NS-053: After ෂ or ඍ/ෘ → ණ
- **Statement.** ෂ and the vowel ඍ (or its sign ෘ) also trigger ණ.
- **Examples.**
  - දූෂණය *dūṣaṇaya*
  - රක්ෂණය *rakṣaṇaya*
  - නිරීක්ෂණ *nirīkṣaṇa*
  - භීෂණය, පාෂාණ
  - තෘෂ්ණා *tṛṣṇā*
  - තෘණ *tṛṇa*
  - ඍණ *ṛṇa*
  - විෂ්ණු *viṣṇu*
  - උෂ්ණ *uṣṇa*
  - දක්ෂිණ *dakṣiṇa*
- **Exceptions.** -
- **Applies-to.** nna, ssa, ru, ruu.
- **Confidence.** high.
- **Sources.** [UD-AV]; [KS-NN]; [UTH]; [TI943].

### NS-054: Which sounds block the trigger (the Sanskrit *ṇatva* rule)
- **Statement.** The trigger (ර / ෂ / ඍ) still causes ණ when only vowels, velars (ක-group), labials (ප-group), or ය / ව / හ come in between. Any other consonant in between, such as a dental, palatal, retroflex, ල or ශ/ස, blocks it, and the n stays න.
- **Examples.**
  - Trigger still works:
    - තර්කණ *tarkaṇa*
    - දර්පණ *darpaṇa*
    - නිර්මාණ *nirmāṇa*
    - බ්‍රාහ්මණ *brāhmaṇa*
    - ග්‍රහණ *grahaṇa*
    - ප්‍රමාණ *pramāṇa*
    - නිරූපණ *nirūpaṇa*
  - Trigger blocked (න):
    - මර්දනය *mardanaya*
    - නර්තනය *nartanaya*
    - ආරාධනා *ārādhanā*
    - දර්ශනය *darśanaya*
    - ප්‍රශ්නය *praśnaya*
    - ප්‍රකාශන *prakāśana*
    - විදර්ශන
- **Exceptions.** -
- **Applies-to.** nna, na, ra, ssa, ru.
- **Confidence.** high for the Sinhala statement ([LLS]; [SDVP]). Mapping it to Pāṇini 8.4.1–2 is medium (general knowledge).
- **Sources.** [LLS]; [SDVP]; [KS-NN].

### NS-055: Before retroflex stops → ණ් (ණ්ට, ණ්ඨ, ණ්ඩ, ණ්ඪ)
- **Statement.** A nasal hal before a retroflex stop is always ණ්.
- **Examples.**
  - කණ්ටක *kaṇṭaka*
  - මණ්ඩලය *maṇḍalaya*
  - කණ්ඨජ *kaṇṭhaja*
  - සණ්ඨාව / ඝණ්ඨාව
  - කාණ්ඩය *kāṇḍaya*
  - භාණ්ඩ *bhāṇḍa*
  - පණ්ඩිත *paṇḍita*
  - දණ්ඩ, චණ්ඩ
  - ආණ්ඩුව *āṇḍuva* 'government' (native, from this rule)
- **Exceptions.** English loans and colloquial infinitives use න්ඩ:
  - කැලැන්ඩර්, සිලින්ඩර්, බ්‍රැන්ඩි
  - කන්ඩ, බොන්ඩ, දෙන්ඩ, ලියන්ඩ ([UTH])
- **Applies-to.** nna, tta, ttha, dda, ddha, hal.
- **Confidence.** high.
- **Sources.** [UD-AV]; [UTH]; [KS-NN]; [SANH].

### NS-056: Before dentals, and after ස or ශ → න
- **Statement.** A nasal next to a dental consonant, or after ස or ශ, is න.
- **Examples.**
  - Before dentals (න්ත, න්ථ, න්ද, න්ධ):
    - දන්ත *danta*
    - ප්‍රාන්තය *prāntaya*
    - ග්‍රන්ථය *granthaya*
    - වින්දනය *vindanaya*
    - අන්ධ *andha*
    - වන්දනාව *vandanāva*
    - චන්දන *candana*
  - After ස: ලස්සන *lassana*, අත්සන *atsana*
  - After ශ: ප්‍රශ්නය, දේශනය *dēśanaya*
- **Exceptions.** -
- **Applies-to.** na, ta, tha, da, dha, sa, sha.
- **Confidence.** high.
- **Sources.** [TI943]; [KS-NN].

### NS-057: Word-initial ණ: practically only ණය
- **Statement.** In modern usage only ණය *ṇaya* 'debt' begins with ණ. [UD-AV] also lists ණිහ 'dog' and ණිහිය 'daughter-in-law', which are archaic or literary.
- **Examples.** ණය.
- **Exceptions.** ණිහ, ණිහිය (archaic).
- **Applies-to.** nna.
- **Confidence.** high.
- **Sources.** [KS-NN]; [UD-AV]; ketisatahan "ණ යන්නෙන් ඇරැඹී…" (ketapathpawra).

### NS-058: Stem-final ණ is never written with hal
- **Statement.** ණ at the end of a stem is never written with hal. [UD-AV] says the stem-final letters ණ and ළ "are not hal" (short paraphrase). When a form needs a final consonant, it usually surfaces as න්.
- **Examples.**
  - තොරණ, සෙවණ, බණ, පහණ
  - කණ 'ear' → plural කන් *kan* (**UNVERIFIED** in a fetched source)
- **Exceptions.** ණ් inside clusters is fine: ණ්ඩ, ණ්ට, ණ්‍ය (NS-055).
- **Applies-to.** nna, hal.
- **Confidence.** medium.
- **Sources.** [UD-AV].

### NS-059: Root-derived native nouns ending in ණ (or ළ)
- **Statement.** A group of native nouns built from roots ends in ණ or ළ.
- **Examples.** දණ, බණ, පණ, අණ, වළ, බළ.
- **Exceptions.** -
- **Applies-to.** nna, lla.
- **Confidence.** medium.
- **Sources.** [UD-AV].

### NS-060: Honorific suffixes -ආණ, -අණි, -අණු, -අණ්ඩි → ණ
- **Statement.** Honorific suffixes are written with ණ.
- **Examples.**
  - පියාණෝ / පියාණන් *piyāṇō*
  - දියණිය *diyaṇiya*
  - පුතණුවෝ
  - මැණි
  - මාමණ්ඩි, අයියණ්ඩි, මලයණ්ඩි
- **Exceptions.** -
- **Applies-to.** nna.
- **Confidence.** high.
- **Sources.** [UD-AV]; [KS-NN]; [LLS]; [TI943]; [SANH].

### NS-061: Native verbs: past and passive forms take ණ; present forms take න
- **Statement.**
  - **ණ:** involitive/passive past forms in -ඉණි / -ඉණ, and past participles in -උණු / -උණ / -උණේ.
  - **න:** present participles and present-tense verbs, even after ර. This overrides NS-051.
- **Examples.**
  - ණ:
    - බැලිණි *bæliṇi*
    - හෙලිණි, වැටිණි, දැවිණි
    - බැලුණු *bæluṇu*
    - විසිරුණු, බිඳුණු, වැටුණු, කැඩුණු, නැමුණු
    - වැටුණේ ය
    - මැරුණි
  - න:
    - කරන *karana*
    - හදාරන, මරන, මතුරන, බලන
    - කරනු
    - කරනවා, හදාරනවා, මෝරනවා
- **Exceptions.** -
- **Applies-to.** nna, na, ra.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [KS-NN]; [SANH]; [SDVP]; [TI943].

### NS-062: Other native suffixes take න
- **Statement.** These suffixes are written with dental න:
  - nouns ending in -න්න
  - the -නි vocative/locative plural
  - the feminine -ඉනි
- **Examples.**
  - ඉන්න, දුන්න, ගින්න, ඔටුන්න
  - උතුමනි, මිනිසුනි, ළමයිනි
  - යකිනි, මැතිනි, කෙකිනි
- **Exceptions.** -
- **Applies-to.** na.
- **Confidence.** medium–high.
- **Sources.** [KS-NN]; [TI943].

### NS-063: Compound boundary blocks retroflexion
- **Statement.** A ර at the end of the first member of a compound does not turn an n at the start of the second member into ණ.
- **Examples.**
  - ධාරානිපාත
  - සුරනර
  - බණ්ඩාරනායක
  - පිරිනමනවා
- **Exceptions.** -
- **Applies-to.** na, ra.
- **Confidence.** medium.
- **Sources.** [KS-NN].

### NS-064: When Sanskrit and Pali disagree, Sinhala follows Pali ණ
- **Statement.** Where Pali has ṇ but Sanskrit has n, the Sinhala word takes ණ.
- **Examples.**
  - පෙණ *peṇa* 'foam' (Pali pheṇa, Sanskrit phena)
  - Native forms that keep ණ: බමුණු (< brāhmaṇa), වෙණ (< vīṇā), දෙරණ (< dharaṇī), ලුණු (< lavaṇa)
- **Exceptions.** -
- **Applies-to.** nna.
- **Confidence.** medium (single source with citations).
- **Sources.** [SANH].

### NS-065: Native and loan words outside the rules must be memorised
- **Statement.** Some words do not follow any rule and must be learned as they are.
- **Examples.**
  - ගණිතය, මැණික, මුහුණ (ණ)
  - ඉරානය, කුරානය (න despite ර)
- **Exceptions.** -
- **Applies-to.** nna, na.
- **Confidence.** medium.
- **Sources.** [UTH].

### NS-066: Rare word-medial ණ before a vowel
- **Statement.** ණ also appears between vowels in non-trigger contexts. These cases are etymological.
- **Examples.** කිංකිණි, රෙහෙණ, ආභරණ.
- **Exceptions.** -
- **Applies-to.** nna.
- **Confidence.** medium.
- **Sources.** [SANH].

---

## 7. ල / ළ භේදය (dental vs retroflex l)

### NS-070: ළ and ල are homophones in modern Sinhala
- **Statement.** The difference is written only. Spoken Sinhala lost /ḷ/, around the 16th century according to [ASSAJ]. Inflection still shows an older difference: ල doubles before case endings, ළ does not.
- **Examples.** balu+ā → ballā, but nalu+ā → naluvā.
- **Exceptions.** -
- **Applies-to.** la, lla.
- **Confidence.** high.
- **Sources.** [ASSAJ]; [WP-SCRIPT].

### NS-071: Past tense of ර-final roots: ර → ළ
- **Statement.** In the past tense of verbs whose root ends in ර, the ර becomes ළ.
- **Examples.**
  - කර → කළ *kaḷa* 'did'
  - මර → මළ
  - හදාර → හදාළ
  - වදාර → වදාළ
  - ගුගුර → ගුගුළ
  - වගුර → වගුළ
  - පතුර → පතුළ
  - කොඳුර → කොඳුළ
  - මතුර → මතුළ
  - හර → හළ
  - විසුර → විසුළ
- **Exceptions.** -
- **Applies-to.** lla, ra.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [LLS]; [SDVP].

### NS-072: A Pali/Sanskrit retroflex (ට ඨ ඩ ඪ ණ) becomes ළ in Sinhala
- **Statement.** When a word with one of these retroflex consonants passes into Sinhala, that consonant is written ළ.
- **Examples.**
  - දාඨා → දළ 'tusk'
  - පඨවි → පොළොව 'earth'
  - පටිපාටි → පිළිවෙළ
  - සාටක → සළු
  - බිඩාල → බළලා 'cat'
  - වාණිජ → වෙළෙඳ 'trade'
  - ක්‍රීඩා → කෙළි
  - Tamil loans: අගළ, ආඬපාළි
- **Exceptions.** -
- **Applies-to.** lla, tta, ttha, dda, ddha, nna.
- **Confidence.** high.
- **Sources.** [UD-AV]; [ASSAJ]; [LLS]; [SDVP].

### NS-073: Meaning "small / young / near / tender" → initial ළ
- **Statement.** Words carrying this meaning begin with ළ.
- **Examples.**
  - ළපටි *ḷapaṭi*
  - ළමා, ළමයා
  - ළය
  - ළමැද
  - ළසඳ
  - ළහිරු
  - ළඳරු
- **Exceptions.** -
- **Applies-to.** lla.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV].

### NS-074: Two l's in one noun: the first is usually ළ
- **Statement.** When a noun contains two l-sounds, the first is usually written ළ.
- **Examples.**
  - සළෙල
  - උළෙල
  - වළලු
  - නළල 'forehead'
  - පළල 'width'
  - අළලනවා
  - කළල
- **Exceptions.** [UD-AV] says this holds "mostly".
- **Applies-to.** lla, la.
- **Confidence.** medium.
- **Sources.** [UD-AV]; [LLS].

### NS-075: ළ is never doubled and never hal; geminates are ල්ල
- **Statement.** A doubled l is always ල්ල. A singular in -ල්ල has a plural in -ලු. A singular with medial ළ keeps ළ in the plural.
- **Examples.**
  - සියල්ල, මල්ල, පොල්ල
  - සියල්ල > සියලු, බල්ලා > බලු, වල්ල > වලු, කොල්ලා > කොලු, ගාල්ල > ගාලු, මහල්ලා > මහලු
  - සළුව > සළු, සිළුව > සිළු, මළුව > මළු
- **Exceptions.** -
- **Applies-to.** lla, la, hal.
- **Confidence.** high.
- **Sources.** [UD-AV]; [LLS]; [SDVP].

### NS-076: Stem-final ළ is not hal
- **Statement.** See NS-058.
- **Examples.** දළ, නළ 'wind', බළ, කොළ, පොළ.
- **Exceptions.** -
- **Applies-to.** lla, hal.
- **Confidence.** medium.
- **Sources.** [UD-AV].

### NS-077: The prefix පිළි- always takes ළ
- **Statement.** Words built with the prefix පිළි- are always written with ළ.
- **Examples.**
  - පිළිතුර
  - පිළිගත්
  - පිළිබඳ
  - පිළිමය
  - පිළිරුව
  - පිළිවෙළ
  - පිළිකුල්
- **Exceptions.** -
- **Applies-to.** lla.
- **Confidence.** high.
- **Sources.** [SIWIKI-AV].

### NS-078: ළ before a sanyaka
- **Statement.** An l-sound directly before a sanyaka letter is written ළ.
- **Examples.**
  - වෙළඳ / වෙළෙඳ
  - කොළඹ *koḷam̆ba*
  - කැළඹීම
  - ළිඳ 'well'
- **Exceptions.** -
- **Applies-to.** lla, nnga nndda nda mba.
- **Confidence.** medium. Two informal sources state it ([LLS]; a YouTube lesson title by kinki). There may be counter-examples. **UNVERIFIED** exhaustively.
- **Sources.** [LLS]; YouTube "කිංකිගේ ඉස්කෝලේ … ඟ ඳ ඹ සඤ්ඤක අකුරුවලට පෙර ළ යෙදීම".

### NS-079: Indigenous ළ-words (memorise)
- **Statement.** Some native words have ළ without any rule-based reason and must be memorised.
- **Examples.**
  - මාළු 'fish'
  - රිළා 'monkey'
  - ඔළුව 'head'
  - සුළං 'wind'
  - කළව, කොළඹ, කරළු
- **Exceptions.** -
- **Applies-to.** lla.
- **Confidence.** high.
- **Sources.** [ASSAJ] (citing J.B. Disanayaka and W.S. Karunatillake).

---

## 8. ස / ශ / ෂ භේදය (sibilants)

### NS-080: Native Sinhala uses only ස; ශ and ෂ are for loans
- **Statement.** ශ and ෂ belong to the *miśra* set. They are used for Sanskrit/Pali tatsama and for foreign loans. In modern speech ශ and ෂ are both [ʃ] and ස is [s].
- **Examples.** -
- **Exceptions.** -
- **Applies-to.** sa, sha, ssa.
- **Confidence.** high for the distribution; medium for the [ʃ] merger.
- **Sources.** [WP-SCRIPT]; [WP-LANG]; [UD-AM].

### NS-081: ශ with palatal consonants
- **Statement.** ශ is the sibilant used in clusters with palatals (ච ඡ ජ ඣ ඤ) and in ශ්ශ.
- **Examples.**
  - දුශ්චරිත *duścarita*
  - ආශ්චර්ය *āścarya*
  - නිශ්ශබ්ද, නිශ්ශංක
  - දුශ්ශීල
  - දෘශ්‍යාබාධ
- **Exceptions.** -
- **Applies-to.** sha, ca, cha, ja, jha, nya.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [SDVP].

### NS-082: ශ before ව and ර, and without a cluster
- **Statement.** ශ is used before ව, in ශ්‍ර, and in many words with no cluster at all.
- **Examples.**
  - Before ව: විශ්වාස, ඊශ්වර, විශ්වය, අශ්වයා
  - ශ්‍ර: ශ්‍රී, ශ්‍රවණ, ශ්‍රේණිය
  - No cluster: අනුශාසනා, විශාරද, ක්ලේශ
- **Exceptions.** -
- **Applies-to.** sha, va, ra.
- **Confidence.** high.
- **Sources.** [SIWIKI-AV].

### NS-083: Word with two sibilants: ශ comes first
- **Statement.** In words with ශ+ස or ශ+ෂ, the ශ comes first.
- **Examples.**
  - ප්‍රශස්ති, ශාස්ත්‍රය, ශාසනය
  - ශිෂ්ටාචාරය, විශේෂ, විශිෂ්ට, ශිෂ්‍යයා
- **Exceptions.** -
- **Applies-to.** sha, sa, ssa.
- **Confidence.** medium–high.
- **Sources.** [SIWIKI-AV]; [UD-AV].

### NS-084: ෂ with retroflex consonants
- **Statement.** ෂ is the sibilant used before retroflex consonants (ෂ්ට, ෂ්ඨ, ෂ්ණ).
- **Examples.**
  - විෂ්ණු, කෘෂ්ණ
  - දෘෂ්ටි, අෂ්ටලෝක
  - ශිෂ්ටාචාරය
  - ජ්‍යෙෂ්ඨ, ධර්මිෂ්ඨ
  - නෂ්ට
- **Exceptions.** -
- **Applies-to.** ssa, tta, ttha, nna.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [SDVP].

### NS-085: ෂ in ක්ෂ, and after vowels other than a/ā before velars and labials (the *ruki* rule)
- **Statement.**
  - ක්ෂ (also written ක්‍ෂ) always takes ෂ.
  - After any vowel other than අ/ආ, a sibilant before a velar or labial is ෂ.
- **Examples.**
  - ක්ෂ:
    - අක්ෂර / අක්‍ෂර
    - පරීක්ෂණ, තීක්ෂණ, රක්ෂණ, දක්ෂ
  - After a vowel other than අ/ආ:
    - දූෂණය
    - දුෂ්කර
    - නිෂ්පාදනය
    - අභිනිෂ්ක්‍රමණය
    - නිෂ්ඵල
    - ද්වේෂ
- **Exceptions.** -
- **Applies-to.** ssa, ka, pa, pha.
- **Confidence.** high.
- **Sources.** [UD-AV]; [SIWIKI-AV]; [SDVP].

### NS-086: Morphophonemic ෂ
- **Statement.** Two processes produce ෂ:
  - **Root + ත / ති:** a root ending in ශ, ෂ or ස, plus the suffix ත or ති, gives ෂ්ට / ෂ්ටි.
  - **Superlative -ඉෂ්ඨ:** keeps ෂ්ඨ.
- **Examples.**
  - නශ්+ත → නෂ්ට
  - දෘශ්+ති → දෘෂ්ටි
  - ශිස්+ත → ශිෂ්ට
  - පාපිෂ්ඨ, ධර්මිෂ්ඨ, ජ්‍යෙෂ්ඨ, කනිෂ්ඨ, ශ්‍රේෂ්ඨ
- **Exceptions.** -
- **Applies-to.** ssa, sha, sa, ta, tta, ttha.
- **Confidence.** high.
- **Sources.** [UD-AV].

### NS-087: ස with dental consonants
- **Statement.** ස is the sibilant used before dentals, and in *namas-* / *manas-* + k.
- **Examples.**
  - Before dentals:
    - විස්තර, ස්තන
    - ප්‍රස්තාර, ප්‍රස්තාවනා
    - ස්තූප
    - ශාස්ත්‍රය
    - ලස්සන
  - namas- / manas- + k: නමස්කාරය, මනස්කාන්ත
- **Exceptions.** [UD-AV] lists ස්ථාවර, ස්ථවිර, ස්ථීර, ස්ථානය, ස්ථූල as cases "where it is not so", but these also have dental ස. The intended contrast is unclear (see §10).
- **Applies-to.** sa, ta, tha, ka.
- **Confidence.** high (main rule).
- **Sources.** [UD-AV].

### NS-088: English /ʃ/ in loanwords
- **Statement.** English /ʃ/ is usually written ෂ, e.g. ෂර්ට් *shirt* and ෂෝ *show*. ශ also occurs in some loans and names.
- **Examples.** ෂර්ට්, ෂෝ.
- **Exceptions.** -
- **Applies-to.** ssa, sha.
- **Confidence.** low (**UNVERIFIED**).
- **Sources.** -

---

## 9. Implications for romanization and transliteration

Guidance for anyone converting between Latin-script romanizations and Sinhala script, building a spelling checker, or validating Sinhala text. These points follow from the rules above; they add no new rules.

```
         ┌──── romanized "n"/"m" + consonant ────┐
         │                                        │
    velar k/g ──► ං        retroflex ṭ/ḍ ──► ණ්     │
    palatal c/j ──► ං (or ඤ්)   dental t/d ──► න්  │
    labial p/b ──► ම්      y r l v ś ṣ s h ──► ං (tatsama)
         └────────────────────────────────────────┘
     BUT: native kan̆da/kanda, an̆gala/aṃgaya → lexical; needs a dictionary
          or a romanization that marks prenasalisation (n̆)
```

1. **Sanyaka cannot be recovered by rule.** Nothing predicts a sanyaka versus ං or nasal + hal + stop (NS-033). A romanization that does not mark prenasalisation (as the n̆ / m̆ convention of this file does) loses the distinction, and a converter must fall back on a dictionary. Because sanyaka are never word-initial and never take hal (NS-031), a romanized `ng`, `nd` or `mb` at the start of a word, or followed by hal or a consonant, cannot be a sanyaka.
2. **Where ං is predictable.** A nasal + hal before these contexts is written ං:
   - k / g / kh / gh (ලංකා, බැංකුව)
   - y / r / l / v / ś / ṣ / s / h (සංවාද, සිංහ, හංස)
   - end of word, in colloquial writing (මං, එහෙනං)

   ම් stays before labials and න් before dentals. Pali spellings (ඞ් / ඤ්; NS-004, NS-040) and formal final ම් / න් (NS-008) are legitimate exceptions, so a converter should not force ං in those cases.
3. **Retroflex nasal before retroflex stops is predictable.** `n` + `ṭ` / `ḍ` (ට ඩ) is ණ් (NS-055), except in English loans and colloquial -න්ඩ (කැලැන්ඩර්, කන්ඩ). ණ්ඩ is the default reading; න්ඩ is the loanword and colloquial alternative.
4. **The *ṇatva* rule is a ranking cue, not a hard rule.** For `n` after r / ṣ / ṛ (with only vowels, k-group, p-group, y, v or h in between), ණ is the likely spelling (NS-051 to NS-054). The cue does not apply when:
   - the word ends in the native present morphology -nawā / -na / -nu (NS-061)
   - the n is at a compound boundary (NS-063)
   - the word is an English loan
5. **Morphology cues for ණ.** The endings -iṇi / -iṇa / -uṇu / -uṇa / -uṇē (past participle and passive) and the honorifics -āṇō / -aṇi / -aṇu / -aṇḍi (NS-060, NS-061) predict ණ reliably. They are worth a suffix table.
6. **ළ cues.** Reliable indicators of ළ:
   - past tense of ර-roots: kala → කළ, mala → මළ, hadāḷa (NS-071)
   - the prefix piḷi- (NS-077)
   - the ḷa- "small / young" words (NS-073)
   - l directly before a sanyaka (NS-078)
   - the first l of an l…l noun (NS-074)

   Well-formed text never has ළ්, ළ්ළ, or ණ් at the end of a word (NS-058, NS-075).
7. **Choosing the sibilant for romanized *sh* / *s*.**

| Romanized context | Likely letter | Rule |
|---|---|---|
| `sh` + c / ch / j / v / r, or word-initial `shr` | ශ | NS-081, NS-082 |
| `sh` + ṭ / ṭh / ṇ, `ksh`, or after i / u / e before k / p | ෂ | NS-084, NS-085 |
| plain `s` + t / th / n | ස | NS-087 |
| first of two sibilants in a word | ශ | NS-083 |

   Word-initial `sh` is ambiguous: ශ (ශ්‍රී, ශාන්ත, ශිෂ්‍ය) vs ෂ (English loans, NS-088). Only a dictionary resolves it.
8. **ඥ.** Romanized `gn` / `gny` / `jn` / `jny` corresponds to ඥ only before a vowel, and only in words a dictionary confirms. Plain `gn` may also be ග්න (අග්නි, නග්න, ලග්න) (NS-046). The suffix -ඥ / -ඥයා (විද්‍යාඥයා, නීතිඥ) is a strong cue.
9. **The `nya` ambiguity.** Romanized *nya* (the letter ID for ඤ) usually stands for the very common න්‍ය (NS-047). ඤ is rare, so න්‍ය is the safer default unless the romanization marks the palatal nasal explicitly.
10. **ඃ and ඁ.**
    - ඃ should come only from an explicit *ḥ* in the source romanization. Most Sanskrit visarga already surface as ෝ / ර් / ශ් / ස් / ෂ් (NS-022).
    - ඁ has no modern correspondence (NS-025).
11. **Validity guards.** Well-formed Sinhala text never contains:
    - ් + ං
    - ් + ඃ
    - sanyaka + ්
    - ං as the first character of a word
    - ං + vowel sign
    - ං / න් directly before a sanyaka (NS-001, NS-002, NS-021, NS-031, NS-037)
12. **ඦ.** It is a valid letter (`nyja`), but it should never be inferred automatically from a romanization (NS-036).

---

## 10. Open questions / conflicting sources

| # | Topic | Conflict / gap |
|---|---|---|
| 1 | ඦ usage | [WP-SCRIPT] says it is used nowhere, ancient or modern. [ADYA] and [GG-SAN] cite ඉඦු (dog call). [ICANN-P] says "not frequently used". [UD-AM] says Disanayaka removed it in 1990. The NIE-60 and Unicode alphabets still include it. |
| 2 | ඥ pronunciation | [WP-SCRIPT] gives [dʒɲa]. The Sri Lanka Survey Dept romanises it **gna** [UNGEGN]. Everyday speech seems to be [gn] or [gɲ]: **UNVERIFIED** by phonetic study. [GANESAN] argues it is only a conjunct, not a letter. |
| 3 | Distribution of /ŋ/ | [WP-LANG] says [ŋ] occurs only word-finally and before velars. But spelling puts ං before ය ර ල ව ශ ස හ too. How those are pronounced is **UNVERIFIED**. |
| 4 | ං vs න් before dentals in *saṃ-* words | සංදර්ශනය vs සන්දර්ශනය, සංතෘප්ත. I found no official rule. |
| 5 | ං vs ඤ් before palatals and *jñ* | පංච / පඤ්ච, සංඥා / සඤ්ඥා, වංචා / වඤ්චා. Modern usage is variable; no NIE ruling found. |
| 6 | ඤාති vs ඥාති | Pali-based vs Sanskrit-based spelling of 'relative'. Both occur. |
| 7 | Optional sanyaka (මග / මඟ etc.) | It is unclear which form school or NIE material prefers. |
| 8 | Word-initial ණ | [KS-NN]: only ණය. [UD-AV] adds ණිහ and ණිහිය. Probably archaic, but unconfirmed. |
| 9 | [SANH] "Rule 6" | The fetched summary contradicted itself ("never end in ණ/ළ" while listing අණ, දළ…). I used [UD-AV]'s reading instead: stem-final ණ/ළ is not *hal*. Needs checking against the original page. |
| 10 | [UD-AV] ස exception list | ස්ථාවර, ස්ථවිර, ස්ථීර, ස්ථානය, ස්ථූල, ස්ථාන are listed as "not following the rule", but they also have dental ස before a dental. Possibly a PDF font/encoding issue, or a rule about ථ vs ත. Unresolved. |
| 11 | Sanyaka + ඃ | Attested only in [ICANN-P] (ඉඳඃ, colloquial). |
| 12 | ං directly before a vowel letter | Whether forms like ගංඉවුර are ever written as one word. **UNVERIFIED.** |
| 13 | ළ before sanyaka (NS-078) | Comes only from informal lesson sources. No exhaustive check for counter-examples. |
| 14 | Phonological analysis of sanyaka | Unit segment ([BAND], [UNI]) vs sequence plus syllabification ([FEIN]) vs single/geminate nasal ([MADD]). This does not affect spelling, but matters if a romanisation tries to be "phonetic". |
| 15 | Authoritative primary sources not reached | NIE textbooks (educationpublications.gov.lk), the SLS 1134:2004 text, Gair & Paolillo 1997, Karunatillake's grammar, and Geiger's grammar were not fetched. Rules here rest on Unicode, the ICANN GP, two academic papers, and teaching handouts or blogs that agree with each other. |

---

## 11. Source URLs

- [UNI] https://www.unicode.org/versions/Unicode15.0.0/ch13.pdf · https://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/
- [ICANN-P] https://www.icann.org/en/system/files/files/proposal-sinhala-lgr-22apr19-en.pdf · https://www.icann.org/sites/default/files/packages/lgr/proposal-sinhala-lgr-22apr19-en.xml
- [ICANN-LGR] https://www.icann.org/sites/default/files/packages/lgr/rz-lgr-6-sinhala-script-23sep25-en.htm
- [WG2] https://www.evertype.com/standards/si/si.html
- [UD-AV] https://ia601404.us.archive.org/21/items/Index_201704/dhgra002.pdf
- [UD-AM] https://ia601404.us.archive.org/21/items/Index_201704/dhgra001.pdf
- [ASSAJ] https://journals.kln.ac.lk/jhu/media/attachments/2021/12/02/chapter-06.pdf
- [BAND] https://ir.lib.pdn.ac.lk/bitstreams/ce2591e7-7369-43d6-84a4-bb5068fd4597/download
- [MADD] https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/abs/prenasalized-stops-and-speech-timing1/63ACDDDEA90F550BB3DD8F38FA128B7C
- [FEIN] https://academicworks.cuny.edu/gc_etds/2207
- [UNGEGN] https://arhiiv.eki.ee/wgrs/rom2_si.pdf
- [GANESAN] https://unicode.org/mail-arch/unicode-ml/y2006-m07/0010.html
- [NLPC] https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala
- [SIWIKI-AV] https://si.wikipedia.org/wiki/සිංහල_අක්ෂර_වින්‍යාසය
- [WP-SCRIPT] https://en.wikipedia.org/wiki/Sinhala_script
- [WP-LANG] https://en.wikipedia.org/wiki/Sinhala_language
- [WP-PNC] https://en.wikipedia.org/wiki/Prenasalized_consonant
- [KS-NN] https://ketisatahan.online.lk/ණන-අක්ෂර-වින්යාසය-රීත/
- [KS-NGA] https://ketisatahan.online.lk/සාම්ප්රදායිකව-ඞ-ඤ-අ/
- [UTH] https://uthmax.blogspot.com/2009/06/01.html
- [SANH] http://sanhindha.blogspot.com/2009/07/blog-post.html
- [LLS] http://letslearnsinhala.blogspot.com/2012/03/blog-post.html
- [TI943] https://throughinternet943.blogspot.com/2020/10/blog-post_20.html
- [SDVP] https://sdvp10.blogspot.com/2020/06/16-ii.html
- [ADYA] https://adyapanika01.blogspot.com/p/blog-page.html
- [SLAK] http://sundaralakdiwa.blogspot.com/2015/08/blog-post_76.html
- [GG-SAN] https://groups.google.com/g/sinhala-bloggers/c/29KvFUBElp8
- [GG-UNI] https://groups.google.com/g/sinhala-unicode/c/GJfUKz8i0is
- YouTube lesson (ළ before sanyaka, ණ after ර): https://www.youtube.com/watch?v=JaRN8rU677c
- ketapathpawra (word-initial ණ): http://www.ketapathpawra.com/?p=1396
