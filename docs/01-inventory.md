# 01 — Inventory of the Sinhala Writing System

Scope: the **inventory** of the Sinhala writing system — what symbols exist, what they are called, how they are classified, and which ones are live, rare or obsolete — together with how they are encoded in Unicode and SLS 1134. Spelling rules, sandhi, and the design of romanization schemes are out of scope except for the closing "Implications for romanization and transliteration" section.

Compiled October 2026.

Letter IDs (used throughout this repository):
consonants `ka kha ga gha nga nnga(ඟ) ca cha ja jha nya(ඤ) jnya(ඥ) nyja(ඦ) tta ttha dda ddha nna nndda(ඬ) ta tha da dha na nda(ඳ) pa pha ba bha ma mba(ඹ) ya ra la va sha(ශ) ssa(ෂ) sa ha lla(ළ) fa`;
vowels `a aa ae aee i ii u uu ru ruu ilu iluu e ee ai o oo au`; `hal` = al-lakuna.

---

## 0. Summary

- The Unicode **Sinhala block (U+0D80–U+0DFF)** encodes 3 "various signs" (ඁ ං ඃ), 18 independent vowels, 41 consonants, 1 al-lakuna, 19 dependent vowel signs (17 in the main run + 2 "additional"), 10 Lith digits and 1 punctuation mark (෴). **Sinhala Archaic Numbers (U+111E1–U+111F4)** adds 20 historical numerals. ZWJ (U+200D) is mandatory for every conjunct, yansaya, rakaransaya and repaya; ZWNJ (U+200C) has only marginal, display-oriented roles.
- The **"60-letter" modern alphabet** (NIE 1989: 18 vowels + 42 "consonants", the 42 including ං and ඃ) is the school standard. **SLS 1134** counts **61** (18 vowels + 41 consonants + 2 semi-consonants) because it adds **ඥ** (jnya), which the 1989 NIE list lacks.
- Historically: Sidat Sangarā (13th c.) 30 letters → Eḷu / Śuddha 32 (adds ඇ ඈ) → Vadan-kavi 50 → Miśra 54 → NIE 1989 60 (adds ෆ + five sanyaka) → SLS/Unicode 61 (adds ඥ). Counts and what was added at each stage differ between sources (see §11).
- In modern use, **ඏ ඐ ඎ ෟ(alone) ෳ ඁ ඦ** are effectively dead; **ඞ ඣ ඪ** are Pali/Sanskrit-only rarities; **ෆ** and **ඇ/ඈ** do most of the work for English sounds; there is **no letter for /z/**.

---

## 1. Sources (cited by key in the tables)

| Key | Source | Notes |
|---|---|---|
| U-CH | Unicode 18.0 code chart, Sinhala — https://www.unicode.org/charts/PDF/U0D80.pdf | Normative names, aliases, decompositions. Read directly. |
| U-AN | Unicode 18.0 code chart, Sinhala Archaic Numbers — https://www.unicode.org/charts/PDF/U111E0.pdf | Read directly. |
| U-SP | Unicode Core Spec ch. 13 (v16.0), §13.2 Sinhala — https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-13/ | ZWJ rules, u/uu contextual forms, candrabindu, kunddaliya. Read via summarizer. |
| U-NS | Unicode NamedSequences.txt — https://www.unicode.org/Public/UCD/latest/ucd/NamedSequences.txt | Yansaya / rakaransaya / repaya sequences. Read directly. |
| U-L2 | L2/08-105, J. B. Disanayaka for ICTA & SLSI, "Observations on the Encoding of Archaic Sinhala Numerals", Feb 2008 — https://www.unicode.org/L2/L2008/08105-sinhala.pdf | Read directly. |
| CP | codepoints.net (Unicode version of first encoding) — https://codepoints.net/U+0D81 , https://codepoints.net/U+0DE6 , https://codepoints.net/U+0DC6 | Secondary, derived from UCD DerivedAge. |
| SLS | SLS 1134 Draft, 2nd revision (SLSI, draft dated 2004-04-26) — https://sinhala.sourceforge.net/archive/akuru.org/att-0028/sls1134.pdf | Read directly (pages 1–20). **The final published SLS 1134:2004 / :2011 texts were not available**; the draft may differ. |
| WP-EN | Wikipedia, "Sinhala script" — https://en.wikipedia.org/wiki/Sinhala_script | Lead only. |
| WP-SI | සිංහල විකිපීඩියා, "සිංහල හෝඩි" — https://si.wikipedia.org/wiki/සිංහල_හෝඩි | Lead only; read via summarizer. |
| WP-NUM | Wikipedia, "Sinhala numerals" — https://en.wikipedia.org/wiki/Sinhala_numerals | Lead only. |
| KLN | University of Kelaniya, නෙමඩල, "සිංහල හෝඩියේ උත්පත්තිය", බී. ලක්ෂිකා මදුශානි, 2022-07-11 — https://units.kln.ac.lk/nemadala/index.php/visheshanga/gaweshana/295-2022-07-11-03-29-22 | University student-research portal; best Sinhala-language source found for alphabet history. |
| LD | Lankadeepa, "'ෆ' අක්ෂරය සිංහල හෝඩියට ආ හැටි" — https://www.lankadeepa.lk/mathaka_ha_mathaka/ෆ-අකෂරය-සහල-හඩයට-ආ-හට/287-656225 | Newspaper; history of ෆ. |
| B-AK | akurusinhala.blogspot.com, "සිංහල අක්‍ෂර වර්ගීකරණය" (2016) — http://akurusinhala.blogspot.com/2016/10/blog-post.html | Blog; classification tables (corroborative only). |
| B-BN | bingunada.blogspot.com, "සිංහල භාෂාවේ පිලි" (2014) — http://bingunada.blogspot.com/2014/09/blog-post.html | Blog; pili names (corroborative only). |
| B-IH | ihhodiya.blogspot.com, "අපේ සිංහල හෝඩිය" (2018) — http://ihhodiya.blogspot.com/2018/09/2.html | Blog; alphabet history. |
| B-S4 | sinhala4all.weebly.com, "අක්ෂර මාලාව" — https://sinhala4all.weebly.com/34613482353035223515-35123535351735353520.html | Teacher site; alphabet history. |
| YM | Yamu.lk, "සිංහල හෝඩිය ගැන හැංගුණු කතාවක්" (2019-11-22) — https://www.yamu.lk/trending/sinhala-alphabet-doubts/ | Popular article; ඥ/z commentary. |
| ST | Sunday Times (LK), 1998-10-04 — https://www.sundaytimes.lk/981004/plus2.html | Disanayaka interview: "from around 37 letters… up to 60". |

**Not reached:** the NIE / Educational Publications Department Grade 6 textbook lesson "අක්ෂරමාලාව හා පිල්ලම්" (listed at https://govdoc.lk/lesson-view?id=3986&fid=62e8a270be286 but not fetched as text), and the Sri Lanka Sinhala Encyclopedia article "අක්ෂරමාලාව (සිංහල)" at encyclopedia.gov.lk (connection refused). Anything attributed below to "school grammar" is therefore corroborated only by secondary Sinhala sources. **Treat it as medium confidence until someone checks the textbook.**

---

## 2. Table 1 — Unicode Sinhala block, complete (U+0D80–U+0DFF)

Columns: **ID** = letter ID used in this repository. **Unicode name** is the normative name (with its `=` alias). **Sinhala name** is the traditional name. For letters these follow the "-යන්න" pattern the Unicode names were built from (WP-EN, SLS Table 4). The Sinhala spelling is my own rendering of the Unicode/SLS romanized name; where B-BN/B-AK give a different everyday form, that form is shown too. **Cat.**: SIGN = ayogavaha/various sign; IV = independent vowel; C = consonant; VS = dependent vowel sign; D = digit; P = punctuation. **Set**: Ś = in the Śuddha (Eḷu) set, M = Miśra-only, N = added in the modern/NIE era. **Status**: live / rare / obsolete. "Since" = first Unicode version (CP, U-SP).

Unassigned in the block: 0D80, 0D84, 0D97–0D99, 0DB2, 0DBC, 0DBE–0DBF, 0DC7–0DC9, 0DCB–0DCE, 0DD5, 0DD7, 0DE0–0DE5, 0DF0–0DF1, 0DF5–0DFF (U-CH). SLS says 0D97–0D99 and 0DC7–0DC9 were held back deliberately for future vowels and consonants.

### 2a. Various signs (ayogavaha)

| CP | Glyph | ID | Unicode name (= alias) | Sinhala name | Cat. | Set | Status |
|---|---|---|---|---|---|---|---|
| 0D81 | ඁ | — | SINHALA SIGN CANDRABINDU | චන්ද්‍රබින්දු (candrabindu) | SIGN | — | obsolete; Unicode 13.0 (2020). Spec says it is for archaic Sanskrit texts only, **not modern Sinhala** (U-SP). |
| 0D82 | ං | — | SINHALA SIGN ANUSVARAYA (= anusvara) | අනුස්වාරය / බින්දුව | SIGN | Ś | live (very common: සිංහල, ලංකාව) |
| 0D83 | ඃ | — | SINHALA SIGN VISARGAYA (= visarga) | විසර්ගය | SIGN | M | rare (Sanskrit loans: දුඃඛ, පුනඃ) |

### 2b. Independent vowels (ස්වර / ප්‍රාණාක්ෂර)

| CP | Glyph | ID | Unicode name (= alias) | Sinhala name | Set | Status |
|---|---|---|---|---|---|---|
| 0D85 | අ | a | SINHALA LETTER AYANNA (= a) | අයන්න | Ś | live |
| 0D86 | ආ | aa | AAYANNA (= aa) | ආයන්න | Ś | live |
| 0D87 | ඇ | ae | AEYANNA (= ae) | ඇයන්න | Ś (post-Sidat-Sangarā) | live |
| 0D88 | ඈ | aee | AEEYANNA (= aae) | ඈයන්න | Ś (post-Sidat-Sangarā) | live |
| 0D89 | ඉ | i | IYANNA (= i) | ඉයන්න | Ś | live |
| 0D8A | ඊ | ii | IIYANNA (= ii) | ඊයන්න | Ś | live |
| 0D8B | උ | u | UYANNA (= u) | උයන්න | Ś | live |
| 0D8C | ඌ | uu | UUYANNA (= uu) | ඌයන්න | Ś | live |
| 0D8D | ඍ | ru | IRUYANNA (= vocalic r) | ඉරුයන්න | M | live-rare (ඍතුව, ඍෂි) |
| 0D8E | ඎ | ruu | IRUUYANNA (= vocalic rr) | ඉරූයන්න | M | obsolete as a letter. Its sign ෲ survives (SLS note 3). |
| 0D8F | ඏ | ilu | ILUYANNA (= vocalic l) | ඉලුයන්න | M | obsolete (SLS: "do not occur in present usage") |
| 0D90 | ඐ | iluu | ILUUYANNA (= vocalic ll) | ඉලූයන්න | M | obsolete |
| 0D91 | එ | e | EYANNA (= e) | එයන්න | Ś | live |
| 0D92 | ඒ | ee | EEYANNA (= ee) | ඒයන්න | Ś | live |
| 0D93 | ඓ | ai | AIYANNA (= ai) | ඓයන්න | M | live-rare (ඓතිහාසික) |
| 0D94 | ඔ | o | OYANNA (= o) | ඔයන්න | Ś | live |
| 0D95 | ඕ | oo | OOYANNA (= oo) | ඕයන්න | Ś | live |
| 0D96 | ඖ | au | AUYANNA (= au) | ඖයන්න | M | live-rare (ඖෂධ) |

### 2c. Consonants (ව්‍යඤ්ජන / ගාත්‍රාක්ෂර)

| CP | Glyph | ID | Unicode name (= alias) | Sinhala name | Set | Status |
|---|---|---|---|---|---|---|
| 0D9A | ක | ka | ALPAPRAANA KAYANNA (= ka) | අල්පප්‍රාණ කයන්න | Ś | live |
| 0D9B | ඛ | kha | MAHAAPRAANA KAYANNA (= kha) | මහාප්‍රාණ කයන්න (also "බයානු කයන්න", WP-EN) | M | live (loans) |
| 0D9C | ග | ga | ALPAPRAANA GAYANNA (= ga) | අල්පප්‍රාණ ගයන්න | Ś | live |
| 0D9D | ඝ | gha | MAHAAPRAANA GAYANNA (= gha) | මහාප්‍රාණ ගයන්න | M | live (loans: සංඝ, මේඝ) |
| 0D9E | ඞ | nga | KANTAJA NAASIKYAYA (= nga) | කණ්ඨජ නාසිකය | M | rare. SLS: never takes a vowel, appears only as ඞ්. |
| 0D9F | ඟ | nnga | SANYAKA GAYANNA (= nnga) | සඤ්ඤක ගයන්න | Ś (sanyaka) | live (අඟල, හඟින) |
| 0DA0 | ච | ca | ALPAPRAANA CAYANNA (= ca) | අල්පප්‍රාණ චයන්න | Ś (modern); **absent from Sidat Sangarā list** | live |
| 0DA1 | ඡ | cha | MAHAAPRAANA CAYANNA (= cha) | මහාප්‍රාණ චයන්න | M | live (loans: ඡායා) |
| 0DA2 | ජ | ja | ALPAPRAANA JAYANNA (= ja) | අල්පප්‍රාණ ජයන්න | Ś | live |
| 0DA3 | ඣ | jha | MAHAAPRAANA JAYANNA (= jha) | මහාප්‍රාණ ජයන්න | M | very rare (Pali ඣාන) |
| 0DA4 | ඤ | nya | TAALUJA NAASIKYAYA (= nya) | තාලුජ නාසිකය | M | live (ඤාණ, සඤ්ඤා) |
| 0DA5 | ඥ | jnya | TAALUJA SANYOOGA NAAKSIKYAYA (= jnya) | තාලුජ සංයෝග නාසිකය | M (not in NIE 1989 list; in SLS/Unicode) | live (ඥාති, විශේෂඥ, ප්‍රඥා) |
| 0DA6 | ඦ | nyja | SANYAKA JAYANNA (= nyja) | සඤ්ඤක ජයන්න | N (sanyaka) | **obsolete/never used** (SLS: not in contemporary writing) |
| 0DA7 | ට | tta | ALPAPRAANA TTAYANNA (= tta) | අල්පප්‍රාණ ටයන්න | Ś | live |
| 0DA8 | ඨ | ttha | MAHAAPRAANA TTAYANNA (= ttha) | මහාප්‍රාණ ටයන්න | M | rare (ශ්‍රේෂ්ඨ) |
| 0DA9 | ඩ | dda | ALPAPRAANA DDAYANNA (= dda) | අල්පප්‍රාණ ඩයන්න | Ś | live |
| 0DAA | ඪ | ddha | MAHAAPRAANA DDAYANNA (= ddha) | මහාප්‍රාණ ඩයන්න | M | very rare |
| 0DAB | ණ | nna | MUURDHAJA NAYANNA (= nna) | මූර්ධජ ණයන්න | Ś | live (spelling-only distinction from න) |
| 0DAC | ඬ | nndda | SANYAKA DDAYANNA (= nndda) | සඤ්ඤක ඩයන්න | Ś (sanyaka) | live (කඬ, හඬ) |
| 0DAD | ත | ta | ALPAPRAANA TAYANNA (= ta) | අල්පප්‍රාණ තයන්න | Ś | live |
| 0DAE | ථ | tha | MAHAAPRAANA TAYANNA (= tha) | මහාප්‍රාණ තයන්න | M | live (loans: ස්ථාන, කථා) |
| 0DAF | ද | da | ALPAPRAANA DAYANNA (= da) | අල්පප්‍රාණ දයන්න | Ś | live |
| 0DB0 | ධ | dha | MAHAAPRAANA DAYANNA (= dha) | මහාප්‍රාණ දයන්න | M | live (loans: ධර්ම, බුද්ධ) |
| 0DB1 | න | na | DANTAJA NAYANNA (= na) | දන්තජ නයන්න | Ś | live |
| 0DB3 | ඳ | nda | SANYAKA DAYANNA (= nda) | සඤ්ඤක දයන්න | Ś (sanyaka) | live (සඳ, ඳ is very frequent) |
| 0DB4 | ප | pa | ALPAPRAANA PAYANNA (= pa) | අල්පප්‍රාණ පයන්න | Ś | live |
| 0DB5 | ඵ | pha | MAHAAPRAANA PAYANNA (= pha) | මහාප්‍රාණ පයන්න | M | live-rare (ඵල) |
| 0DB6 | බ | ba | ALPAPRAANA BAYANNA (= ba) | අල්පප්‍රාණ බයන්න | Ś | live |
| 0DB7 | භ | bha | MAHAAPRAANA BAYANNA (= bha) | මහාප්‍රාණ බයන්න | M | live (භාෂාව) |
| 0DB8 | ම | ma | MAYANNA (= ma) | මයන්න | Ś | live |
| 0DB9 | ඹ | mba | AMBA BAYANNA (= mba) | අඹ බයන්න / සඤ්ඤක බයන්න | Ś (sanyaka) | live (අඹ, තඹ) |
| 0DBA | ය | ya | YAYANNA (= ya) | යයන්න | Ś | live |
| 0DBB | ර | ra | RAYANNA (= ra) | රයන්න | Ś | live |
| 0DBD | ල | la | DANTAJA LAYANNA (= la; dental) | දන්තජ ලයන්න | Ś | live |
| 0DC0 | ව | va | VAYANNA (= va) | වයන්න | Ś | live |
| 0DC1 | ශ | sha | TAALUJA SAYANNA (= sha) | තාලුජ ශයන්න | M | live (ශ්‍රී, ශාලා) |
| 0DC2 | ෂ | ssa | MUURDHAJA SAYANNA (= ssa; retroflex) | මූර්ධජ ෂයන්න | M | live (භාෂා; English "sh": ෂෝ) |
| 0DC3 | ස | sa | DANTAJA SAYANNA (= sa; dental) | දන්තජ සයන්න | Ś | live |
| 0DC4 | හ | ha | HAYANNA (= ha) | හයන්න | Ś | live |
| 0DC5 | ළ | lla | MUURDHAJA LAYANNA (= lla; retroflex) | මූර්ධජ ළයන්න | Ś | live (spelling-only distinction from ල) |
| 0DC6 | ෆ | fa | FAYANNA (= fa) | ෆයන්න | N (1989) | live (English loans). Unicode 3.0 (1999). |

### 2d. Al-lakuna and dependent vowel signs (පිලි / පිල්ලම්). See §6 for names.

| CP | Glyph | ID | Unicode name (= alias) | Decomposition (U-CH) |
|---|---|---|---|---|
| 0DCA | ් | hal | SINHALA SIGN AL-LAKUNA (= virama) | — |
| 0DCF | ා | aa | VOWEL SIGN AELA-PILLA (= aa) | — |
| 0DD0 | ැ | ae | VOWEL SIGN KETTI AEDA-PILLA (= ae) | — |
| 0DD1 | ෑ | aee | VOWEL SIGN DIGA AEDA-PILLA (= aae) | — |
| 0DD2 | ි | i | VOWEL SIGN KETTI IS-PILLA (= i) | — |
| 0DD3 | ී | ii | VOWEL SIGN DIGA IS-PILLA (= ii) | — |
| 0DD4 | ු | u | VOWEL SIGN KETTI PAA-PILLA (= u) | — |
| 0DD6 | ූ | uu | VOWEL SIGN DIGA PAA-PILLA (= uu) | — |
| 0DD8 | ෘ | ru | VOWEL SIGN GAETTA-PILLA (= vocalic r) | — |
| 0DD9 | ෙ | e | VOWEL SIGN KOMBUVA (= e) | — (pre-base glyph) |
| 0DDA | ේ | ee | VOWEL SIGN DIGA KOMBUVA (= ee) | ≡ 0DD9 0DCA |
| 0DDB | ෛ | ai | VOWEL SIGN KOMBU DEKA (= ai) | **none** (not ≡ ෙ+ෙ) |
| 0DDC | ො | o | VOWEL SIGN KOMBUVA HAA AELA-PILLA (= o) | ≡ 0DD9 0DCF |
| 0DDD | ෝ | oo | VOWEL SIGN KOMBUVA HAA DIGA AELA-PILLA (= oo) | ≡ 0DDC 0DCA |
| 0DDE | ෞ | au | VOWEL SIGN KOMBUVA HAA GAYANUKITTA (= au) | ≡ 0DD9 0DDF |
| 0DDF | ෟ | ilu | VOWEL SIGN GAYANUKITTA (= vocalic l) | — |
| 0DF2 | ෲ | ruu | VOWEL SIGN DIGA GAETTA-PILLA (= vocalic rr) | — |
| 0DF3 | ෳ | iluu | VOWEL SIGN DIGA GAYANUKITTA (= vocalic ll) | — |

### 2e. Digits and punctuation

| CP | Glyph | Unicode name | Notes |
|---|---|---|---|
| 0DE6–0DEF | ෦ ෧ ෨ ෩ ෪ ෫ ෬ ෭ ෮ ෯ | SINHALA LITH DIGIT ZERO … NINE | Astrological ("Lith Illakkam"), positional, has a zero. Unicode 7.0 (2014). |
| 0DF4 | ෴ | SINHALA PUNCTUATION KUNDDALIYA | කුණ්ඩලිය. Cross-ref U+11FFF TAMIL PUNCTUATION END OF TEXT. |

### 2f. Characters outside the block that Sinhala needs

| CP | Name | Sinhala role (U-SP, U-NS, SLS §4.3/§5) |
|---|---|---|
| 200D | ZERO WIDTH JOINER | **Required** to form any conjunct (bandi akuru), yansaya, rakaransaya, repaya, or touching letter. Without ZWJ, al-lakuna is always visible. |
| 200C | ZERO WIDTH NON-JOINER | SLS only: ZWNJ + vowel sign shows a sign on its own (`‌ා`). ZWNJ ් ZWJ ය gives a stand-alone yansaya. ර ් ZWJ ZWNJ gives a stand-alone repaya. The Unicode Sinhala section does not mention ZWNJ (U-SP). |
| 00A0 | NO-BREAK SPACE | SLS lists it. The Unicode convention is NBSP or dotted circle as the base for showing a lone combining mark. |
| 0964/0965 | DEVANAGARI DANDA / DOUBLE DANDA | Not Sinhala-specific. Sometimes seen in Pali texts. **Unverified for Sinhala** and not encoded in the Sinhala block. |

---

## 3. Table 2 — Sinhala Archaic Numbers (U+111E0–U+111FF), "Sinhala Illakkam"

Non-positional, **no zero** (U-AN). 111E0 and 111F5–111FF are unassigned. Unicode 7.0 (2014) per WP-EN (CP not checked for this block).

| CP | Name | CP | Name |
|---|---|---|---|
| 111E1 | SINHALA ARCHAIC DIGIT ONE | 111EA | SINHALA ARCHAIC NUMBER TEN |
| 111E2 | … DIGIT TWO | 111EB | … NUMBER TWENTY |
| 111E3 | … DIGIT THREE | 111EC | … NUMBER THIRTY |
| 111E4 | … DIGIT FOUR | 111ED | … NUMBER FORTY |
| 111E5 | … DIGIT FIVE | 111EE | … NUMBER FIFTY |
| 111E6 | … DIGIT SIX | 111EF | … NUMBER SIXTY |
| 111E7 | … DIGIT SEVEN | 111F0 | … NUMBER SEVENTY |
| 111E8 | … DIGIT EIGHT | 111F1 | … NUMBER EIGHTY |
| 111E9 | … DIGIT NINE | 111F2 | … NUMBER NINETY |
| | | 111F3 | … NUMBER ONE HUNDRED |
| | | 111F4 | … NUMBER ONE THOUSAND |

---

## 4. Rules and facts: inventory and encoding (INV-001 … INV-014)

**INV-001 — Unicode letter inventory**
- **Statement:** The Sinhala block encodes 18 independent vowels (0D85–0D96) and 41 consonants (0D9A–0DC6, with gaps). Every consonant is one code point, including the 5 sanyaka letters, ඥ, and ෆ.
- **Examples:** ඟ = U+0D9F (not ඞ්+ග); ඥ = U+0DA5 (not ඤ්‍ජ).
- **Exceptions:** None.
- **Confidence:** high. **Sources:** U-CH, SLS §5.2.

**INV-002 — Independent vowels are atomic**
- **Statement:** An independent vowel must be stored as its own code point, never as අ + vowel sign.
- **Examples:** ආ is U+0D86, **not** 0D85 0DCF. ඒ is U+0D92, not එ + ්.
- **Exceptions:** SLS describes ආ as අ + ා and ඒ as එ + ් in terms of how the letters are written. This is writing order only; the stored form must be the atomic code point.
- **Confidence:** high. **Sources:** SLS §5.1 note, §6.2.

**INV-003 — Composite vowel signs and normalization**
- **Statement:** ේ ො ෝ ෞ have canonical decompositions (table 2d), so NFC and NFD differ for them. Store the single precomposed sign.
- **Examples:** කෝ = 0D9A 0DDD. The sequence 0D9A 0DD9 0DCF 0DCA is permitted by Unicode but SLS discourages it.
- **Exceptions:** ෛ (0DDB) has **no** decomposition. Two kombuvas (ෙෙ) are *not* canonically equal to ෛ, so any conversion or normalization step must map "kombuva twice" to 0DDB itself.
- **Confidence:** high. **Sources:** U-CH, SLS §5.4 note 2.

**INV-004 — Al-lakuna and conjunct formation**
- **Statement:** Al-lakuna (්, 0DCA) is always visible and does **not** by itself form a conjunct. A consonant cluster becomes a ligature or reduced form only with **C + ් + ZWJ + C**.
- **Examples:** ක්‍ෂ = ක ් ZWJ ෂ (kssa). න්‍ද = න ් ZWJ ද. ක්‍ව = ක ් ZWJ ව.
- **Exceptions:** Touching letters use a different order (INV-005).
- **Confidence:** high. **Sources:** U-SP §13.2, SLS §5.8.

**INV-005 — Touching letters (bandi akuru, Pali style)**
- **Statement:** Unicode encodes a touching conjunct as **C + ZWJ + ් + C**, with ZWJ *before* al-lakuna.
- **Examples:** Pali text written in Sinhala script, e.g. a ka touching a ka in ධම්මචක්ක (glyph only).
- **Exceptions:** **Conflict:** the 2004 SLS draft says touching letters use 0DCA 200D, the same order as conjuncts.
- **Confidence:** medium (Unicode high; SLS final text not seen). **Sources:** U-SP, SLS §5.8 note.

**INV-006 — Named sequences for yansaya, rakaransaya, repaya**
- **Statement:** Three reduced forms have fixed sequences:
  - yansaya (ය after a consonant) = **0DCA 200D 0DBA**
  - rakaransaya (ර after a consonant) = **0DCA 200D 0DBB**
  - repaya (ර before a consonant) = **0DBB 0DCA 200D**, placed before the following consonant
- **Examples:** ක්‍ය kya. ක්‍ර kra. ක්‍රෙ kre. කර්‍ම karma (repaya form).
- **Exceptions:**
  - Repaya is optional: කර්ම and කර්‍ම are both valid (SLS §3.5).
  - SLS says yansaya is **not** written after ර; it marks its own example spelling with ර + yansaya incorrect.
- **Confidence:** high. **Sources:** U-NS, SLS §5.6–5.7.

**INV-007 — ZWJ omission is meaningful**
- **Statement:** Leaving out the ZWJ gives an explicit-hal spelling. This is a legitimate spelling choice, not an error.
- **Examples:** ක්ය (no ZWJ) vs ක්‍ය.
- **Exceptions:** None.
- **Confidence:** high. **Sources:** SLS §5.6 note 2.

**INV-008 — Ayogavaha are trailing combining marks**
- **Statement:** ං and ඃ are combining marks. They follow a vowel, a consonant with its inherent a, or a vowel sign, and they are always the **last** character of the cluster.
- **Examples:**
  - අං = 0D85 0D82
  - කං = 0D9A 0D82
  - කොං = 0D9A 0DDD 0D82 (SLS's own example)
  - කුඃ = 0D9A 0DD4 0D83
- **Exceptions:** They never follow a pure (hal) consonant.
- **Confidence:** high. **Sources:** SLS §3.3, §5.5.

**INV-009 — Contextual vowel-sign shapes share one code**
- **Statement:** Shape variants of al-lakuna and of the u/uu signs are all encoded with the same code point.
- **Examples:**
  - The hal on ක් looks different from the hal on ට, but both are 0DCA.
  - කු (0D9A 0DD4) has a different u-shape from නු (0DB1 0DD4).
  - u/uu take alternative forms after ක ග ඟ ත භ ශ, and again after a rakaransaya.
- **Exceptions:** None.
- **Confidence:** high. **Sources:** SLS §5.4, U-SP.

**INV-010 — Irregular ligatures are ordinary sequences**
- **Statement:** ර and ළ have irregular ligatures with the u and ae signs, but they are still stored as plain consonant + sign.
- **Examples:** රු = 0DBB 0DD4. රූ = 0DBB 0DD6. රැ = 0DBB 0DD0. ළු = 0DC5 0DD4.
- **Exceptions:** SLS lists ළු ("muurdhaja lu") as a distinct form for convenience, but there is no separate code for it.
- **Confidence:** high. **Sources:** SLS §5.4, §6.1.

**INV-011 — Candrabindu is not modern Sinhala**
- **Statement:** U+0D81 is used only for archaic Sanskrit texts. Transliteration of ordinary modern text should not produce it.
- **Examples:** —
- **Exceptions:** None.
- **Confidence:** high. **Sources:** U-SP, CP.

**INV-012 — Two numeral systems; modern text uses European digits**
- **Statement:**
  - **Sinhala Illakkam** (111E1–111F4): archaic, no zero, separate signs for 10–90, 100 and 1000. Used before 1815; the Kandyan Convention clause numbers are an example.
  - **Sinhala Lith Illakkam** (0DE6–0DEF): astrological, positional, has a zero. Used for horoscopes into the 20th century.
  - Everyday Sinhala uses 0–9.
- **Examples:** —
- **Exceptions:** Disanayaka (for ICTA/SLSI, 2008) argued that the "archaic" numerals also had a zero and a place-holder concept, and opposed encoding the 11 compound numerals (10…1000). Unicode encoded them anyway.
- **Confidence:** high (encoding); medium (historical claims). **Sources:** U-CH, U-AN, U-L2, WP-NUM.

**INV-013 — Kunddaliya**
- **Statement:** ෴ (කුණ්ඩලිය, 0DF4) is a historical full stop or ornament. Today it appears mainly to close a paragraph or as decoration, including on social media. Modern punctuation is Western (. , ? !).
- **Examples:** —
- **Exceptions:** None.
- **Confidence:** high. **Sources:** U-SP, SLS §4.2, WP-EN.

**INV-014 — Unicode history**
- **Statement:**
  - Sinhala block (incl. ෆ and ෴): Unicode 3.0 (1999)
  - Lith digits 0DE6–0DEF and the Archaic Numbers block: Unicode 7.0 (2014)
  - Candrabindu 0D81: Unicode 13.0 (2020)
  - SLS 1134 and its 2001 revision were the basis for ISO/IEC 10646 Sinhala.
- **Examples:** —
- **Exceptions:** None.
- **Confidence:** high (CP for 0D81/0DE6/0DC6); medium (archaic block). **Sources:** CP, SLS Foreword.

---

## 5. Table 3 — Hodiya: alphabets through history

| Stage | Name | Vowels | Consonants | Total | What changed | Sources | Conf. |
|---|---|---|---|---|---|---|---|
| 13th c. (Dambadeniya) | සිදත් සඟරා හෝඩිය | 10: අ ආ ඉ ඊ උ ඌ එ ඒ ඔ ඕ | 20: ක ග ජ ට ඩ ණ ත ද න ප බ ම ය ර ල ව ස හ ළ **අං** | 30 | Classical Eḷu. No ඇ ඈ, no ච, ං counted as a consonant. | KLN, WP-SI, B-IH, B-S4 | high |
| (later) | එළු හෝඩිය / ශුද්ධ සිංහල (අමිශ්‍ර) හෝඩිය | 12 (adds ඇ ඈ) | 20 | 32 | Adds ඇ ඈ. **KLN** says ඇ ඈ were added but still gives 30 (internal inconsistency). | B-IH, B-S4, WP-SI; KLN conflicting | medium |
| Kandyan (Mahanuwara) period | වදන් කවි (වඩන කවි) හෝඩිය | 16 | 34 | 50 | Adds Pali/Sanskrit letters. Used in temple teaching ("pansal hodiya") into the 20th c. | KLN, B-IH | medium |
| 1891 (A. M. Gunasekara, *Comprehensive Grammar*) | මිශ්‍ර සිංහල හෝඩිය | 18 | 36 | 54 | Adds 4 to Vadan-kavi (ඍ ඎ ඏ ඐ ඓ ඖ ශ ෂ … per KLN). Gunasekara also proposed ෆ. | KLN, LD, WP-SI | medium |
| 1989 (NIE, Maharagama; *Sinhala Lekhana Rītiya* committee) | නූතන / සම්මත සිංහල හෝඩිය | 18 | 42 | **60** | Adds **ෆ** and **five sanyaka (ඟ ඦ ඬ ඳ ඹ)**. ං ඃ written අං අඃ. **ඥ not included.** | KLN, WP-SI, B-S4, LD, YM, ST | medium-high |
| 1990 (J. B. Disanayaka) | සමකාලීන සිංහල හෝඩිය | — | — | (≈60) | Drops ඏ ඐ and ඦ; adds ඥ; KLN also mentions new "closed" vowel notations. Details unclear. | KLN, WP-SI | low |
| 2004 (SLS 1134 rev. 2) / Unicode | encoding standard | 18 | 41 + 2 semi-consonants | **61** | All 41 Unicode consonants, incl. both ඥ and ඦ. | SLS §3 | high |

**INV-015 — Śuddha vs Miśra (modern definition)**
- **Statement:** "Śuddha" (Eḷu) letters are enough for native Sinhala words. "Miśra" adds letters needed only for tatsama (Sanskrit/Pali) or English loans: the aspirates, extra sibilants, ඍ-series and ඏ-series, ඓ ඖ, ඃ, ඞ ඤ ඥ, and ෆ.
  - Śuddha (modern sense) = අ ආ ඇ ඈ ඉ ඊ උ ඌ එ ඒ ඔ ඕ + ක ග ච ජ ට ඩ ණ ත ද න ප බ ම ය ර ල ව ස හ ළ + ඟ ඬ ඳ ඹ + ං
  - Miśra = the 60/61-letter set
- **Examples:** Native ගඟ (ganga, "river") uses only Śuddha letters. Tatsama ගංගා (gangaa) uses ං. Loan ධර්මය (dharmaya) needs Miśra ධ.
- **Exceptions:**
  - The classical Sidat Sangarā list has **no ච and no sanyaka letters**. WP-EN's "Śuddha" includes ච and the 4 sanyaka, because it describes modern phonemes.
  - ණ and ළ are Śuddha even though they are no longer distinct phonemes.
  - Using Miśra letters is partly a matter of prestige or etymology (WP-EN).
- **Confidence:** medium. **Sources:** WP-EN, WP-SI, KLN.

**INV-016 — Why "60 vs 61"**
- **Statement:** The modern count is reconciled as follows:
  - **NIE 60** = 18 vowels + 42 consonants, where the 42 are 40 consonant letters (25 varga + 5 sanyaka + ය ර ල ව + ශ ෂ ස හ ළ ෆ) **plus ං and ඃ**.
  - **SLS 61** = 18 vowels + 41 consonants (the same 40 + ඥ) + 2 semi-consonants.
  - So SLS 61 = NIE 60 + ඥ.
- **Examples:** —
- **Exceptions:**
  - WP-SI's 42-list, as read through a summarizer, came back one letter short. ඦ was assumed missing because KLN says 1989 added ඦ.
  - Some sources say "18 + 42" while also listing ඥ.
- **Confidence:** medium. **Sources:** SLS §3, KLN, WP-SI, YM.

**INV-017 — Alphabet order**
- **Statement:** Traditional order (followed by Unicode/SLS):
  1. Vowels: අ ආ ඇ ඈ ඉ ඊ උ ඌ ඍ ඎ ඏ ඐ එ ඒ ඓ ඔ ඕ ඖ
  2. Ayogavaha: ං ඃ (NIE places them after the vowels as අං අඃ)
  3. Varga rows, each followed by its sanyaka: ක ඛ ග ඝ ඞ ඟ / ච ඡ ජ ඣ ඤ ඥ ඦ / ට ඨ ඩ ඪ ණ ඬ / ත ථ ද ධ න ඳ / ප ඵ බ භ ම ඹ
  4. ය ර ල ව ශ ෂ ස හ ළ ෆ
- **Examples:** SLS put ං ඃ at the *start* of the code page (0D82–0D83) to help collation.
- **Exceptions:** SLS warns that sorting still needs a dedicated collation algorithm.
- **Confidence:** high. **Sources:** U-CH, SLS §3.3 note 2, §4.

---

## 6. Table 4 — Pili (vowel signs and other strokes): names

Every vowel sign is written after the consonant in memory, even when it is drawn before it (ෙ). The Sinhala names come from SLS Table 1 and §6.1 (romanized), Unicode names, and B-BN. Alternate everyday names are separated by "/".

| CP | Sign | Vowel ID | Sinhala name(s) | Romanized (SLS/Unicode) | Position | Notes |
|---|---|---|---|---|---|---|
| 0DCA | ් | hal | හල් ලකුණ / හල් කිරීම / ඇල (al) | al-lakuna (virama) | above / attached | "Hal kirīma" names the *act* of removing the vowel; the sign is the *al/hal lakuna*. There are two glyph forms (on ක vs on ට), but one code. |
| 0DCF | ා | aa | ඇලපිල්ල | aela-pilla | right | |
| 0DD0 | ැ | ae | කෙටි ඇදය / කෙටි ඇදපිල්ල | ketti aeda-pilla | right-lower | |
| 0DD1 | ෑ | aee | දිග ඇදය / දිග (දික්) ඇදපිල්ල | diga aeda-pilla | right-lower | |
| 0DD2 | ි | i | කෙටි ඉස්පිල්ල | ketti is-pilla | above | |
| 0DD3 | ී | ii | දිග (දික්) ඉස්පිල්ල | diga is-pilla | above | |
| 0DD4 | ු | u | කෙටි පාපිල්ල (the hooked form: කෙටි වක් පාපිල්ල) | ketti paa-pilla 1 / 2 | below | SLS lists two shapes (7, 7a). B-BN uses "වක් පාපිල්ල" for the hooked form after ක ග ත … |
| 0DD6 | ූ | uu | දිග පාපිල්ල (hooked: දිග වක් පාපිල්ල) | diga paa-pilla 1 / 2 | below | |
| 0DD8 | ෘ | ru | ගැටපිල්ල / කෙටි ගැටපිල්ල | gaetta-pilla | right | |
| 0DF2 | ෲ | ruu | දිග ගැටපිල්ල / ගැටපිලි දෙක | diga gaetta-pilla | right | Rare (පිතෲ). |
| 0DD9 | ෙ | e | කොම්බුව | kombuva | left (pre-base) | Written before the consonant but stored after it. |
| 0DDA | ේ | ee | කොම්බුව හා හල් ලකුණ / දිග කොම්බුව (B-BN: කොම්බුව හා උස්පිල්ල) | diga kombuva | left + above | ≡ ෙ + ් |
| 0DDB | ෛ | ai | කොම්බු දෙක (ද්විත්ව කොම්බුව) | kombu deka | left | |
| 0DDC | ො | o | කොම්බුව හා ඇලපිල්ල | kombuva haa aela-pilla | two-part | ≡ ෙ + ා |
| 0DDD | ෝ | oo | කොම්බුව හා දිග ඇලපිල්ල | kombuva haa diga aela-pilla | two-part | ≡ ො + ් |
| 0DDE | ෞ | au | කොම්බුව හා ගයනුකිත්ත | kombuva haa gayanukitta | two-part | ≡ ෙ + ෟ |
| 0DDF | ෟ | ilu | ගයනුකිත්ත | gayanukitta | right | Alone it means vocalic l (obsolete). It **is** used as part of ෞ and ඖ. |
| 0DF3 | ෳ | iluu | දිග ගයනුකිත්ත / ගයනුකිති දෙක | diga gayanukitta | right | Unused (SLS note 4). |
| 0D82 | ං | — | බින්දුව / අනුස්වාරය | anusvaraya | right | ayogavaha |
| 0D83 | ඃ | — | විසර්ගය | visargaya | right | ayogavaha |
| (seq.) | ්‍ය | — | යංශය | yansaya | right | "non-vocalic stroke" (SLS) |
| (seq.) | ්‍ර | — | රකාරාංශය | rakaransaya | below | |
| (seq.) | ර්‍ | — | රේඵය | repaya | above next consonant | |

**INV-018 — Pili in SLS table 2**
- **Statement:** Each consonant can combine with 17 vocalic forms: hal, inherent a, and 15 vowel signs. ෟ and ෳ are excluded as obsolete.
  - With yansaya: 8 valid vowel combinations. With rakaransaya: 12.
  - Adding ං or ඃ gives SLS's figure of "109 possible letters" per consonant.
- **Examples:** ක් ක කා කැ කෑ කි කී කු කූ කෘ කෲ කෙ කේ කෛ කො කෝ කෞ. Yansaya set: ක්‍ය ක්‍යා ක්‍යු ක්‍යූ ක්‍යෙ ක්‍යේ ක්‍යො ක්‍යෝ.
- **Exceptions:**
  - SLS: not every combination is valid for every consonant. ඞ appears only as ඞ්.
  - SLS's own yansaya table lists kyu/kyuu, which are rare in practice.
- **Confidence:** high (as SLS defines it). **Sources:** SLS §3.4–3.5, Tables 1–3.

---

## 7. Table 5 — Classification of letters

### 7a. Vowels (ස්වර)

| Class | Sinhala term | Members (IDs) | Conf. |
|---|---|---|---|
| Short | හ්‍රස්ව | අ ඇ ඉ උ ඍ ඏ එ ඔ (a ae i u ru ilu e o) | high |
| Long | දීර්ඝ | ආ ඈ ඊ ඌ ඎ ඐ ඒ ඕ (aa aee ii uu ruu iluu ee oo) | high |
| Diphthong | සන්ධ්‍යක්ෂර / සංයුක්ත ස්වර | ඓ ඖ (ai au). Usually counted with the long vowels. | medium |
| Unique to Sinhala among Indic scripts | — | ඇ ඈ (ae aee). SLS: "unique to the Sinhala language… since the 7th century". | high (SLS) |
| Sounds vs letters | — | SLS: the 61 symbols represent **40 sounds** (14 vowel + 26 consonant). | high (as claim) |

### 7b. Consonants: varga grid (place × manner)

| Varga (Sinhala) | Place (Sinhala) | aghosha alpaprana | aghosha mahaprana | ghosha alpaprana | ghosha mahaprana | nasal (වර්ගාන්ත / අනුනාසික) | sanyaka (prenasalised) |
|---|---|---|---|---|---|---|---|
| ක වර්ගය | කණ්ඨජ (velar) | ක ka | ඛ kha | ග ga | ඝ gha | ඞ nga | ඟ nnga |
| ච වර්ගය | තාලුජ (palatal) | ච ca | ඡ cha | ජ ja | ඣ jha | ඤ nya | ඦ nyja |
| ට වර්ගය | මූර්ධජ (retroflex) | ට tta | ඨ ttha | ඩ dda | ඪ ddha | ණ nna | ඬ nndda |
| ත වර්ගය | දන්තජ (dental) | ත ta | ථ tha | ද da | ධ dha | න na | ඳ nda |
| ප වර්ගය | ඕෂ්ඨජ (labial) | ප pa | ඵ pha | බ ba | භ bha | ම ma | ඹ mba |

Non-varga consonants:

| Class | Sinhala term | Members | Place | Conf. |
|---|---|---|---|---|
| Semivowels / liquids | අන්තස්ථ | ය ya (palatal), ර ra (retroflex/alveolar), ල la (dental), ව va (dento-labial) | — | high |
| Sibilants / fricatives | ඌෂ්ම | ශ sha (palatal), ෂ ssa (retroflex), ස sa (dental), හ ha (velar/glottal). B-AK also lists **ඃ and ෆ** (6 in all). | — | medium (4-member list high; 6-member list from one blog) |
| Retroflex lateral | — | ළ lla (මූර්ධජ). Traditionally grouped apart from the varga letters. | මූර්ධජ | high |
| Dento-labial | දන්තෝෂ්ඨජ | ව va, ෆ fa | — | medium |
| Velar-palatal / velar-labial vowels | කණ්ඨතාලුජ / කණ්ඨෝෂ්ඨජ | එ ඒ ඓ / ඔ ඕ ඖ (Sanskrit tradition) | — | medium |
| ඥ jnya | තාලුජ සංයෝග නාසිකය | Historically the cluster ජ්+ඤ. Pronounced [gn]/[gɲ] in modern speech. | palatal | medium |

**INV-019 — Alpaprana / mahaprana**
- **Statement:** Each varga has two unaspirated (අල්පප්‍රාණ) and two aspirated (මහාප්‍රාණ) stops.
  - Mahaprana = ඛ ඝ ඡ ඣ ඨ ඪ ථ ධ ඵ භ (10)
  - Alpaprana = ක ග ච ජ ට ඩ ත ද ප බ (10)
  - Modern Sinhala does **not** pronounce aspiration. The choice of letter is etymological (spelling only).
- **Examples:** ධර්මය is pronounced like *darmaya*. කථාව and කතාව are both seen; the spelling is debated.
- **Exceptions:** Nasals, semivowels, sibilants and ha are classified as neither (or as alpaprana in some grammars).
- **Confidence:** high (classes); high (no phonemic aspiration, WP-EN). **Sources:** B-AK, U-CH names, WP-EN.

**INV-020 — Ghosha / aghosha (voicing)**
- **Statement:**
  - Aghosha (voiceless) = the first two letters of each varga (ක ඛ ච ඡ ට ඨ ත ථ ප ඵ) + ශ ෂ ස (+ ෆ, ඃ by extension)
  - Ghosha (voiced) = the remaining varga letters, the nasals, the sanyaka letters, ය ර ල ව, හ, ළ, and all vowels
- **Examples:** —
- **Exceptions:** හ is traditionally ghosha in Sanskrit phonetics; Sinhala sources follow that. **Unverified** in a primary Sinhala textbook.
- **Confidence:** medium. **Sources:** search summary of letslearnsinhala/akurusinhala; Sanskrit tradition.

**INV-021 — Sanyaka (සඤ්ඤක / අර්ධ නාසික) letters**
- **Statement:** There are 5 prenasalised stops: ඟ ඦ ඬ ඳ ඹ ("half-nasal", romanized by SLS as nng, ndj, nnd, nd, mb). Each is a single letter and a single code point. Sinhala treats them as one segment, distinct from a full nasal plus a stop.
- **Examples:**
  - අඟල (anngala) vs අංග (anga)
  - සඳ (sanda, "moon") vs සන්ද (sanda, a name)
  - කඬ / හඬ (hanndda); අඹ (amba)
- **Exceptions:** ඦ is never used. Native spellings use ඳ etc.; tatsama words use න්ද etc.
- **Confidence:** high. **Sources:** SLS §3, U-CH, WP-EN.

---

## 8. Table 6 — Rare, obsolete, Pali/Sanskrit-only, and foreign-sound letters

| Letter | ID | Status | Typical domain | Example | Conf. | Source |
|---|---|---|---|---|---|---|
| ඏ ඐ | ilu iluu | obsolete; SLS keeps them only "for completeness"; Disanayaka 1990 dropped them | Sanskrit grammar | (ඏකාරය as a citation only) | high | SLS, KLN, YM |
| ෟ (alone), ෳ | ilu iluu signs | obsolete (ෟ survives inside ෞ/ඖ) | — | — | high | SLS note 4 |
| ඎ | ruu | letter obsolete; sign ෲ used in a handful of Sanskrit words | Sanskrit | පිතෲ (unverified example) | medium | SLS note 3 |
| ඍ / ෘ | ru | live in tatsama words | Sanskrit | ඍතුව, කෘෂිකර්ම, වෘක්ෂ, ගෘහ | high | SLS, WP-EN |
| ඓ ඖ / ෛ ෞ | ai au | live, low frequency | Sanskrit | ඓතිහාසික, වෛද්‍ය, ඖෂධ, පෞද්ගලික | high | — |
| ඃ | — | rare | Sanskrit | දුඃඛ, අතඃපුර | medium | — |
| ඁ | — | not for modern Sinhala | archaic Sanskrit | — | high | U-SP |
| ඞ | nga | rare; only as ඞ් before a velar | Pali/Sanskrit | වාඞ්මය, සඞ්ඝ (Pali) | medium | SLS |
| ඤ | nya | live | Pali/Sanskrit + native | ඤාණ, සඤ්ඤා | high | SLS |
| ඥ | jnya | live (high frequency in -ඥ "expert" words) | Sanskrit | ඥාති, විශේෂඥ, නීතිඥ, ප්‍රඥා | high | SLS, YM |
| ඦ | nyja | **never used** | — | — | high | SLS, WP-EN |
| ඣ ඪ | jha ddha | very rare | Pali/Sanskrit | ඣාන (jhāna) | medium | — |
| ඨ ඵ | ttha pha | rare | Sanskrit | ශ්‍රේෂ්ඨ, ඵල | high | — |
| ෆ | fa | live; English/foreign /f/ | English | ෆැෂන්, ෆ්‍රාන්සය | high | LD, WP-EN |
| ඇ ඈ / ැ ෑ | ae aee | native vowels, also the default for English /æ/ | English loans | බැංකුව (bank), කැෆේ | high | SLS §3 |
| ෂ | ssa | in loans; also the usual letter for English /ʃ/ | English | ෂෝ (show), ෂර්ට් (shirt) | medium | (common practice; unverified in a standard) |
| (none) | z | **no letter for /z/**. Usually written with ස (sometimes ශ/ජ). | English | සූ (zoo), සීරෝ (zero) | medium | YM, Lankadeepa search summary |

**INV-022 — History of ෆ**
- **Statement:** A. M. Gunasekara first proposed ෆ in his 1891 grammar and used it in print in 1897. The NIE writing-rules committee formally adopted it in 1989. Before that, writers used ප.
- **Examples:** ප්‍රැන්සිස් → ෆ්‍රැන්සිස් (Francis).
- **Exceptions:** One Lankadeepa commenter claims government offices still do not recognize ෆ in official documents. **Unverified.**
- **Confidence:** medium-high. **Sources:** LD, KLN, WP-SI.

**INV-023 — Pronunciation mergers among letters**
- **Statement:** Several letter pairs sound the same in modern Sinhala; only the spelling differs:
  - **ණ/න** and **ළ/ල** are pronounced alike
  - **ශ/ෂ** are both pronounced [ʃ]
  - each **mahaprana** letter is pronounced like its alpaprana partner
  - **ඤ/ඥ** sound the same only word-initially. Elsewhere ඥ behaves as two consonant sounds (SLS).
- **Examples:** ඥාන ~ ඤාණ (word-initial). ප්‍රඥා (non-initial).
- **Exceptions:** None.
- **Confidence:** high (ණ/ළ/aspirates, WP-EN, YM, SLS). **Sources:** SLS §3.2 note 2, WP-EN, YM.

---

## 9. Numerals and punctuation (summary)

| System | Range | Zero | Positional | Period of use | Status |
|---|---|---|---|---|---|
| Sinhala Illakkam (archaic) | 111E1–111F4 | no (Unicode). Disanayaka 2008 disputed this. | no | to 1815 and some palm-leaf use | historical |
| Sinhala Lith Illakkam | 0DE6–0DEF | yes (the glyph resembles hal lakuna) | yes | horoscopes into the 20th c. | specialist |
| European digits | 0030–0039 | yes | yes | modern | **default** |
| Kunddaliya ෴ | 0DF4 | — | — | historical full stop | decorative |

---

## 10. Implications for romanization and transliteration

These points apply to anyone converting between a Latin-script romanization and Sinhala script, or validating stored Sinhala text.

1. **Use atomic code points.**
   - Independent vowels, the composite signs ේ ො ෝ ෞ ෛ, and sanyaka consonants should each be produced and stored as their single code point (INV-002, INV-003).
   - අ+ා, ෙ+ා, ෙ+ෙ and ඞ්+ග are not correct stored forms.
   - Normalize to NFC; this composes ෙ+ා into ො, etc. It does **not** fix ෙ+ෙ.
2. **ZWJ is part of spelling.**
   - A romanization needs explicit, predictable correspondences for:
     - conjuncts (C ් ZWJ C)
     - yansaya (C ් ZWJ ය)
     - rakaransaya (C ් ZWJ ර)
     - repaya (ර ් ZWJ C)
     - optionally touching letters (C ZWJ ් C)
   - Common modern practice: use ZWJ for `C+ya`/`C+ra` and for ක්‍ෂ, but **not** for arbitrary clusters.
   - An explicit-hal spelling (no ZWJ) must remain representable (INV-007).
3. **Sanyaka vs nasal+stop is a real contrast.**
   - `nnga`, `nndda`, `nda`, `mba` must be kept distinct from `n+g`, `n+d`, `m+b` (INV-021).
   - For example, a romanization must distinguish අඟල from අංගය, and සඳ from සන්ද.
4. **Ayogavaha ං comes after the vowel.** `aṁ` corresponds to ං after any vowel sign. ං and ඃ never follow a hal consonant (INV-008). ං is very frequent; ඃ is rare.
5. **Many letters are spelling-only distinctions** (INV-019, INV-023): aspirates, ණ/න, ළ/ල, ශ/ෂ.
   - A romanization that is to be reversible needs distinct symbols for them (e.g. `kh`, `N`, `L`, `sh`/`Sh`); otherwise converting to Sinhala requires a dictionary.
   - Pure phonetics cannot recover them.
6. **Tier the inventory.** The live set covers ordinary modern text.
   - Low frequency: ඍ/ෘ, ඓ ඖ, ඃ, ඞ, ඣ ඪ, ෲ.
   - ඏ ඐ ෟ(alone) ෳ ඁ ඦ should not appear in transliterations of ordinary modern text (INV-011, Table 6); they belong to archaic or Sanskrit material.
7. **Foreign sounds.**
   - /f/ → ෆ
   - English /æ/ → ඇ ඈ / ැ ෑ
   - `sh` → ෂ or ශ, decided per word
   - /z/ has no target letter. A romanization must state its policy (e.g. map to ස). Note that some existing romanization schemes use `z` for ඇ.
8. **Irregular glyphs are ordinary sequences.** රු රූ රැ ළු need no special codes; the font handles them (INV-010).
9. **Kombuva is written first but stored after.** A romanization is naturally in logical order (`ke` = ක + ෙ), which matches storage order.
10. **Digits.** Modern text uses European digits. Lith digits and ෴ are specialist or decorative characters.

---

## 11. Open questions / conflicting sources

| # | Issue | Sources in conflict | Status |
|---|---|---|---|
| Q1 | Is the modern alphabet **60 or 61** letters, and is ඥ part of it? | NIE 1989 = 60 (no ඥ, per KLN/WP-SI/YM) vs SLS 1134 = 61 (with ඥ) | Reconciled hypothesis INV-016. **Verify against the NIE Grade 6 textbook.** |
| Q2 | Is **ඦ** in the 60? | KLN: added by NIE 1989 as one of five sanyaka; WP-SI 42-list (via summarizer) omitted it; Disanayaka 1990 reportedly removed it | Unverified |
| Q3 | Śuddha / Eḷu count: 30 or 32? Does it include **ච** and the sanyaka? | Sidat Sangarā list has no ච/sanyaka (WP-SI, KLN). WP-EN's "śuddha" includes ච and ඟ ඬ ඳ ඹ. KLN says Eḷu = 30 even after adding ඇ ඈ; B-IH/B-S4 say 32. | Medium. Different definitions: classical vs phonemic. |
| Q4 | Mishra 54: did it already contain the sanyaka letters? | B-IH: yes (ඟ ඦ ඬ ඳ ඹ). KLN: sanyaka added only in 1989. | Unverified |
| Q5 | Vadan-kavi hodiya letter list (16 + 34) | Only counts found, no list | Unverified |
| Q6 | Touching-letter encoding: ZWJ before or after al-lakuna | Unicode: `C ZWJ ් C`. SLS 2004 draft: `C ් ZWJ C` | Unicode governs. Final SLS text unseen. |
| Q7 | Disanayaka 1990 "samakaleena" alphabet: exact contents and the "closed vowel" additions | KLN only; summarizer output garbled | Low confidence |
| Q8 | Ushma set: 4 (ශ ෂ ස හ) or 6 (+ ඃ ෆ)? | Sanskrit tradition: 4. B-AK blog: 6 | Unverified in a textbook |
| Q9 | Place of articulation for **ඇ ඈ**, and whether ය ර ල ව have assigned places in school grammar | Not found | Open |
| Q10 | ghosha/aghosha membership of හ, sanyaka letters, and nasals in Sinhala school grammar | Inferred from the Sanskrit system | Unverified |
| Q11 | Sinhala-script traditional names (e.g. "මහාප්‍රාණ කයන්න" vs "බයානු කයන්න"; "තාලුජ නාසිකය" vs "තාලුජ නාසික්‍යය") | Unicode/SLS give only romanized forms; the Sinhala spellings in Table 1 are my renderings | Medium |
| Q12 | Pili alternate names: ඇදය vs ඇදපිල්ල; දිග vs දික්; whether ේ is "කොම්බුව හා හල් ලකුණ" or "දිග කොම්බුව" in textbooks | SLS/Unicode vs B-BN | Medium |
| Q13 | Did archaic Illakkam have a zero? | Unicode chart: no. Disanayaka/ICTA 2008: yes (palm-leaf evidence) | Historical dispute; encoding is settled |
| Q14 | Unicode version for the Archaic Numbers block (7.0?) | WP-EN only; not checked against DerivedAge | Likely 7.0 |
| Q15 | Common orthography for English /z/ and /ʃ/ | Only popular sources; no standard | Open. Needs corpus check. |
| Q16 | Whether `ර ් ZWJ ය` renders as repaya + ya or as ra + yansaya, and which is correct for words like කාර්‍ය | SLS: yansaya not used after ර, and gives a special ZWNJ sequence for repaya + yansaya. Font behaviour varies. | Needs font testing (Noto Sinhala, Iskoola Pota) |
