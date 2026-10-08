# 02: Vowel signs (pili) and vowel attachment

Scope: every Sinhala dependent vowel sign (U+0DCF–U+0DDF, U+0DF2, U+0DF3) plus al-lakuna
(U+0DCA): how they attach to consonants, which consonant + sign pairs occur, independent vs
dependent vowel use, hiatus and glides, vowel length, and the relation between writing order,
storage order and rendering.

Compiled October 2026.

All text is paraphrased. Rules carry a confidence level, and claims that no consulted source
confirms are marked **[open]** and listed in §10. Counts such as "(NLPC 829)" are token counts in the
NLPC 2.1M-word list (S17); "rare" means fewer than 20 tokens. "Local test" means the compiler checked behaviour locally: Python `unicodedata` (UCD 16.0), HarfBuzz via `uharfbuzz`
0.56.2 with the Windows *Nirmala UI* font, and Chromium rendering of all 41 consonants × signs.
A second local test (October 2026) rendered rakaransaya + u/uu in seven fonts: Noto Sans Sinhala,
Noto Serif Sinhala, Abhaya Libre, Yaldevi, Gemunu Libre, Nirmala UI and Iskoola Pota.

---

## 0. Sources

| ID | Source | URL |
|----|--------|-----|
| S1 | Unicode Standard 18.0, ch. 13, §13.2 Sinhala | http://www.unicode.org/versions/Unicode18.0.0/core-spec/chapter-13/ |
| S2 | Unicode code chart U+0D80–0DFF (names, aliases, ≡ decompositions, block notes) | https://www.unicode.org/charts/PDF/U0D80.pdf |
| S3 | UCD IndicPositionalCategory.txt / IndicSyllabicCategory.txt | https://www.unicode.org/Public/UCD/latest/ucd/IndicPositionalCategory.txt , https://www.unicode.org/Public/UCD/latest/ucd/IndicSyllabicCategory.txt |
| S4 | UCD DoNotEmit.txt (Sinhala vowel-letter entries) | https://www.unicode.org/Public/UCD/latest/ucd/DoNotEmit.txt |
| S5 | SLS 1134:2004 draft (2nd revision), Sri Lanka Standards Institution, with ICTA input | https://sinhala.sourceforge.net/archive/akuru.org/att-0028/sls1134.pdf (also WG2 N2737) |
| S6 | SLSI working group decisions 2004-06-09 (Unicode doc L2/04-231) | https://www.unicode.org/L2/L2004/04231-sinhala-rep.pdf |
| S7 | Microsoft, *Creating and Supporting OpenType Fonts for Sinhala Script* | https://learn.microsoft.com/en-us/typography/script-development/sinhala |
| S8 | HarfBuzz `hb-ot-shaper-vowel-constraints.cc` (Sinhala block) | https://github.com/harfbuzz/harfbuzz/blob/main/src/hb-ot-shaper-vowel-constraints.cc |
| S9 | Sinhala Generation Panel, *Proposal for a Sinhala Script Root Zone LGR* v3.0 (2019, ICANN). Panel includes Prof. J.B. Dissanayake | https://www.icann.org/en/system/files/files/proposal-sinhala-lgr-22apr19-en.pdf |
| S10 | H. Jayasuriya (UCSC LTRL), *Sinhala Orthography: Ola Leaf to the Computer* (2007) | https://ftp3.gwdg.de/pub/gnu/www/savannah-checkouts/non-gnu/sinhala/doc/presentations/sinhala-orthography-hj-20070212.pdf |
| S11 | A. Wasala & K. Gamage (UCSC), *Research Report on Phonetics and Phonology of Sinhala* | http://www.columbia.edu/~kf2119/SPLTE1014/Day%203%20slides%20and%20readings/SinhalaPhoneticsandPhonology.pdf |
| S12 | M. Żygis, *Typology of Consonantal Insertions*, ZAS Papers in Linguistics 52 (2010), citing Smith (2001:63) on Sinhala | https://d-nb.info/1096751291/34 |
| S13 | Sinhala Wikipedia, සන්ධි (sandhi types incl. ආගම සන්ධි): lead only | https://si.wikipedia.org/wiki/සන්ධි |
| S14 | English Wikipedia, *Sinhala script*: lead only (cites Gair & Paolillo 1997, Fairbanks/Gair/Silva 1968) | https://en.wikipedia.org/wiki/Sinhala_script |
| S15 | Liyanapathirana, Gunasinghe, Dias, *SinSpell* (2021) | https://arxiv.org/abs/2107.02983 |
| S16 | Local test (see header) | - |
| S17 | University of Moratuwa NLPC, *Word Frequency List for Sinhala*: the 2.1M-word list (`word_frequency_list_2M`) | https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala |
| S18 | Sinhala Wikipedia, articles in the pages-articles dump of 2026-10-01 (`tools/corpus_counts.py`) | https://dumps.wikimedia.org/siwiki/20261001/ |

Gap: no NIE / educationpublications.gov.lk grammar textbook could be found through web search,
so the native pili names below come from S2/S5 (Unicode names follow the traditional Sinhala
names). They are not confirmed in a Sinhala grammar textbook, so their confidence is lowered
(§10, item 10).

---

## 1. Things that will bite you

1. **Kombu deka (ෛ U+0DDB) has NO decomposition.** ෙ+ෙ is a different string that *looks*
   almost the same. NFC will never turn ෙෙ into ෛ, so text written as "kombuva twice" must be
   mapped to U+0DDB explicitly by whatever produces or cleans the text (VS-004).
2. **The order of ෝ's parts matters.** ෙ + ා + ් normalizes to ෝ. But ෙ + ් + ා becomes ේ + ා,
   which is *not* equivalent to ෝ even though it may render the same (VS-005).
3. **The kombuva is written and displayed first but stored after the consonant.** Logical order
   is always consonant (or whole cluster) and then the sign (VS-002, VS-018).
4. **An independent vowel plus a sign is never correct, and most shapers will not warn you.**
   HarfBuzz shows a dotted circle only for the 9 look-alike pairs (අ+ා etc.). Pairs like ඉ+ී
   or ඔ+ා render silently as junk, so validation cannot rely on rendering (VS-006, VS-007).
5. **ra + u and ra + ae look alike.** රු (ra+u) has a hook to the right. රැ (ra+ae) is a
   separate glyph. ක්‍රු (k.ru) must not be stored as ක්‍රැ (k.rae) (VS-012, VS-016).
6. **"ru" has three readings:** රු (ra+u), ෘ (vocalic r, said /ru/), and ්‍රු (rakaransaya+u).
   For example, ගෘහ (gṛha, house) and ග්‍රහ (graha, planet) are different words (VS-020, VS-033).
7. **ai / au are not usually ෛ / ෞ.** Native and English-loan words write අයි / අවු
   (ලයිට්, කවුද). ෛ/ෞ appear only in Sanskrit-derived words (සෛලය, පෞද්ගලික) (VS-022).
8. **ඞ never takes a vowel sign.** It appears only as ඞ් in contemporary writing (VS-023).
   **Sannjakas (ඟ ඬ ඳ ඹ ඦ) never take al-lakuna** (VS-025).
9. **ෟ (U+0DDF) and ෳ (U+0DF3) are effectively unused alone.** ෟ survives only as the second
   half of ෞ (VS-021).

---

## 2. Sign inventory

### VS-001: The dependent-sign repertoire

**Statement.** Sinhala has 17 dependent vowel signs plus al-lakuna. U+0DD5 and U+0DD7 are
unassigned. Data is from S2, the positions from S3 (IndicPositionalCategory), and the
decompositions from S2/UCD, checked locally (S16).

| Code | Sign | Unicode name (S2) | Trad. name (Sinhala) | Vowel (letter id) | Position (S3) | Canonical decomposition | Gen. cat. |
|---|---|---|---|---|---|---|---|
| U+0DCA | ◌් | AL-LAKUNA (= virama) | හල් කිරීම / හල් ලකුණ | hal (kills inherent a) | Top | - (ccc = 9) | Mn |
| U+0DCF | ◌ා | AELA-PILLA | ඇලපිල්ල | aa | Right | - | Mc |
| U+0DD0 | ◌ැ | KETTI AEDA-PILLA | ඇදපිල්ල | ae | Right | - | Mc |
| U+0DD1 | ◌ෑ | DIGA AEDA-PILLA | දිග ඇදපිල්ල | aee | Right | - | Mc |
| U+0DD2 | ◌ි | KETTI IS-PILLA | ඉස්පිල්ල | i | Top | - | Mn |
| U+0DD3 | ◌ී | DIGA IS-PILLA | දිග ඉස්පිල්ල | ii | Top | - | Mn |
| U+0DD4 | ◌ු | KETTI PAA-PILLA | පාපිල්ල | u | Bottom | - | Mn |
| U+0DD6 | ◌ූ | DIGA PAA-PILLA | දිග පාපිල්ල | uu | Bottom | - | Mn |
| U+0DD8 | ◌ෘ | GAETTA-PILLA | ගැටපිල්ල | ru (vocalic r) | Right | - | Mc |
| U+0DF2 | ◌ෲ | DIGA GAETTA-PILLA | දිග ගැටපිල්ල | ruu (vocalic rr) | Right | - | Mc |
| U+0DDF | ◌ෟ | GAYANUKITTA | ගයනුකිත්ත | ilu (vocalic l) | Right | - | Mc |
| U+0DF3 | ◌ෳ | DIGA GAYANUKITTA | දිග ගයනුකිත්ත | iluu (vocalic ll) | Right | - | Mc |
| U+0DD9 | ෙ◌ | KOMBUVA | කොම්බුව | e | Left (pre-base) | - | Mc |
| U+0DDA | ෙ◌් | DIGA KOMBUVA | කොම්බුව සහ හල් කිරීම | ee | Top_And_Left | ≡ 0DD9 0DCA | Mc |
| U+0DDB | ෛ◌ | KOMBU DEKA | කොම්බු දෙක | ai | Left (pre-base) | **none** | Mc |
| U+0DDC | ෙ◌ා | KOMBUVA HAA AELA-PILLA | කොම්බුව සහ ඇලපිල්ල | o | Left_And_Right (split) | ≡ 0DD9 0DCF | Mc |
| U+0DDD | ෙ◌ෝ | KOMBUVA HAA DIGA AELA-PILLA | කොම්බුව, ඇලපිල්ල සහ හල් කිරීම | oo | Top_And_Left_And_Right | ≡ 0DDC 0DCA (full NFD: 0DD9 0DCF 0DCA) | Mc |
| U+0DDE | ෙ◌ෟ | KOMBUVA HAA GAYANUKITTA | කොම්බුව සහ ගයනුකිත්ත | au | Left_And_Right (split) | ≡ 0DD9 0DDF | Mc |

- **Exceptions.** None. Note that "diga" means long and "ketti" means short in the names.
  Short a (inherent) has no sign.
- **Applies to:** every consonant (validity is in §8).
- **Confidence:** high. The Sinhala-script traditional names are medium (not confirmed
  in a school textbook; §10, item 10).
- **Sources:** S2, S3, S5 (Table 1 and Table 4), S16.

### VS-002: Positions, split signs and reordering

**Statement.** The signs fall into five positional classes. ා ැ ෑ ෘ ෲ ෟ ෳ sit to the right.
ි ී ් sit above. ු ූ sit below. ෙ ෛ sit to the left (pre-base). ො ෝ ේ ෞ are split, with a left
kombuva plus a right or top part. In storage, every sign comes **after** the consonant or
cluster it modifies. The shaping engine moves the pre-base part to the front of the whole
cluster. The Microsoft spec says the engine inserts a ෙ glyph for ේ ො ෝ ෞ and reorders it to
the start of the cluster. The second part is then handled by the font's `pstf` feature.

- **Examples:** කො = ක + ො (U+0D9A U+0DDC), shown as ෙ-ක-ා. ක්‍රෙ = ක ් ZWJ ර ෙ, with the
  kombuva shown before ක.
- **Exceptions:** none in encoding. Display order differs from logical order only for the
  kombuva parts.
- **Applies to:** e, ee, ai, o, oo, au.
- **Confidence:** high.
- **Sources:** S2 (two-part signs "follow the consonant in logical order"), S3, S7
  ("Processing split matras" and "Reordering").

---

## 3. Decomposition and normalization

### VS-003: Canonical equivalences and NFC

**Statement.** Four signs have canonical decompositions: ේ ≡ ෙ+්, ො ≡ ෙ+ා, ෝ ≡ ො+් (that
is, ෙ+ා+්), and ෞ ≡ ෙ+ෟ. None of them is a composition exclusion, so NFC composes the
sequences back to the single code point. Local test (UCD 16.0):
`ක ෙ ා → NFC ක ො`, `ක ෙ ් → ක ේ`, `ක ෙ ෟ → ක ෞ`, `ක ො ් → ක ෝ`.

- **Rule for text processing:** always store the precomposed sign (SLS 1134 §5.4 note 2 discourages
  multi-sign spellings). Normalize to NFC before comparing strings.
- **Exceptions:** see VS-004 and VS-005.
- **Applies to:** ee, o, oo, au.
- **Confidence:** high.
- **Sources:** S2, S5 §5.4, S16.

### VS-004: Kombu deka is atomic

**Statement.** ෛ U+0DDB has no decomposition. The sequence ෙ+ෙ is not equivalent to it.
Under HarfBuzz with Nirmala UI, ක+ෙ+ෙ gives two separate kombuva glyphs (gid 3858 twice).
ක+ෛ gives a distinct kombu-deka glyph (gid 3860). Neither case shows a dotted circle, so the
error is silent. SLS 1134 describes ai as written kombuva + kombuva + consonant, but the stored
form must be U+0DDB.

- **Examples:** කෛ = U+0D9A U+0DDB. Wrong: U+0D9A U+0DD9 U+0DD9.
- **Applies to:** ai.
- **Confidence:** high.
- **Sources:** S2, S5 §6.2 ("ai modifier"), S10 (note on kombuva ordering), S16.

### VS-005: Sign order inside ෝ / ේ

**Statement.** ෝ decomposes canonically as ෙ ා ්. Al-lakuna has ccc = 9 and the vowel signs
have ccc = 0, so normalization never reorders them. The sequence ෙ ් ා therefore composes to
ේ + ා, which is a different string from ෝ. Local test:
`ක ෙ ් ා → NFC ක ේ ා` (U+0DDA U+0DCF), not U+0DDD.

- **Applies to:** oo, ee.
- **Confidence:** high.
- **Sources:** S2, S16.

### VS-006: Independent vowels are atomic; never build them from a letter + sign

**Statement.** Nine vowel letters look like a base vowel plus a sign, but they must be encoded
as single code points. Unicode's Table 13-2 and DoNotEmit.txt list them:

| Use | Do not use |
|---|---|
| ආ U+0D86 | අ + ා |
| ඇ U+0D87 | අ + ැ |
| ඈ U+0D88 | අ + ෑ |
| ඌ U+0D8C | උ + ෟ |
| ඎ U+0D8E | ඍ + ෘ |
| ඐ U+0D90 | ඏ + ෟ |
| ඒ U+0D92 | එ + ් |
| ඓ U+0D93 | එ + ෙ |
| ඖ U+0D96 | ඔ + ෟ |

HarfBuzz puts a dotted circle on exactly these sequences.

- **Note.** ඕ (U+0D95) is not in the list. SLS describes ඕ as written ඔ + ්. Local test: ඔ + ්
  shapes *without* a dotted circle, so converters and validators must catch it themselves.
- **Applies to:** a aa ae aee u uu ru ruu ilu iluu e ee ai o oo au.
- **Confidence:** high.
- **Sources:** S1 Table 13-2, S4, S5 §5.1 and §6.2, S8, S16.

---

## 4. Invalid and ill-formed sequences

### VS-007: No vowel sign after an independent vowel

**Statement.** A dependent sign or al-lakuna must follow a consonant (or a sannjaka). The LGR's
whole-label rules say a sign "must be preceded by C or J", and H must be preceded by C. SLS
1134 also says vowel signs follow a consonant. HarfBuzz flags only the VS-006 look-alikes. Local
test: ඉ+ී, ඔ+ා, එ+ැ and අ+ි all render without a dotted circle. These are garbage that is not
detected.

- **Examples:** wrong: ඉී. Right: ඊ.
- **Applies to:** all signs; all independent vowels.
- **Confidence:** high.
- **Sources:** S5 §4, S9 §7 rules 1–2, S8, S16.

### VS-008: A sign with no base

**Statement.** A sign with no base is invalid in text. Shapers show it on a dotted circle
(U+25CC). For deliberately showing a sign in isolation, the sources disagree:

- SLS 1134 draft: ZWNJ + sign.
- SLSI WG 2004: space + sign (with no extra space), and NBSP + pāpilla to show the hook form.
- Microsoft: reportedly ZWJ after a space.

Local test: a lone ා, or ZWNJ + ා, gets a dotted circle in HarfBuzz.

- **Applies to:** all signs.
- **Confidence:** high for "invalid". The display convention is disputed (see §10).
- **Sources:** S5 §5.4, S6 item 1, S7 ("Handling invalid combining marks"), S16.

### VS-009: Nothing after al-lakuna except ZWJ, a consonant or an end

**Statement.** Al-lakuna removes the vowel. A vowel sign after it is contradictory. Local test:
ක + ් + ා → dotted circle before ා. ක + ් + ෙ → dotted circle. ක + ් + ් → dotted circle.
Anusvara/visarga must not follow hal either (the LGR says ං can follow any sign except halanta).

- **Applies to:** hal.
- **Confidence:** high.
- **Sources:** S9 §3.3.4 and §7, S16.

### VS-010: One vowel sign per syllable

**Statement.** A consonant takes at most one vowel sign. SLS 1134 counts exactly 17 vocalic
forms per consonant (bare + hal + 16 vowel signs, excluding ෟ ෳ) and discourages multi-sign
spellings. Shapers are lenient. Local test: කාා, කිි and කුු get no dotted circle in HarfBuzz.
The Microsoft spec notes that implementations differ on this. Well-formed text never
contains two signs on one consonant.

- **Exception:** the anusvara ං or visarga ඃ may follow a vowel sign, and it is always last in
  the cluster (කාං, කෝං).
- **Confidence:** high.
- **Sources:** S5 §3.5 and §5.5, S7, S9 §5.6.4, S16.

---

## 5. Consonant-specific shapes

These are font and shaper matters. They never change the encoding. They matter for text
processing only because writers may try to reproduce what they *see* with look-alike code points.

### VS-011: ra + ae / aee: irregular ligatures

**Statement.** ර + ැ → රැ and ර + ෑ → රෑ are irregular glyphs (Unicode Table 13-5). The
encoding stays ර U+0DBB + U+0DD0/U+0DD1.

- **Examples:** රැය (ræya, "night"), රෑ (ræː).
- **Applies to:** ra; ae, aee.
- **Confidence:** high.
- **Sources:** S1 Table 13-5, S5 §5.4, S7 (`psts` example), S16.

### VS-012: ra + u / uu: irregular ligatures

**Statement.** ර + ු → රු and ර + ූ → රූ have special shapes. In these, the u-sign attaches
at the right like a hook, not below. Wikipedia notes that the sign used for රු/රූ looks like
the one normally used for æ, while රැ/රෑ get different idiosyncratic shapes. SLS 1134 assigns
no separate code: the form is stored as ර + pāpilla.

- **Examples:** රුපියල (rupiyala), රූපය (rūpaya).
- **Applies to:** ra; u, uu.
- **Confidence:** high.
- **Sources:** S1 Table 13-5, S5 §5.4 and §6.2, S14, S16.
- **Note.** S1's HTML shows a stray ZWJ after ◌ු in the රු/ළු rows. It is taken to be a
  rendering artifact, not a required ZWJ; no source states this **[open]** (§10, item 11).

### VS-013: lla + u / uu

**Statement.** ළ + ු → ළු and ළ + ූ → ළූ are irregular glyphs. SLS lists ළු as a distinct form,
but it is still stored as ළ U+0DC5 + ු U+0DD4. ළූ can look like ළු + ෑ, but it must be stored as
ළ + ූ.

- **Examples:** කළු (kaḷu, "black").
- **Applies to:** lla; u, uu.
- **Confidence:** high.
- **Sources:** S1 Table 13-5, S5 §5.4 and §6.1–6.2.

### VS-014: The "koku" (hook) form of u / uu

**Statement.** ු and ූ take an alternative hook form (attached at the right foot) on ක, ග, ඟ,
ත, භ and ශ. SLS calls these "ketti/diga paa-pilla 2" and notes that the stroke shape depends
on the consonant while the code stays the same. Local test with Nirmala UI confirms the hook
form on exactly these six. All other consonants take the plain below-base loop.

- **Examples:** කුකුළා (kukuḷā), ගුරු (guru), තුන (tuna), භූමිය (bhūmiya), ශුද්ධ (śuddha).
- **Applies to:** ka, ga, nnga, ta, bha, sha; u, uu.
- **Confidence:** high.
- **Sources:** S1, S5 Table 1 (7a, 8a), S14, S16.

### VS-015: Descender loss for da-like bases

**Statement.** Bases shaped like ද drop their descending tail when a below-base sign attaches
(දු, දූ, and ද්‍ර). Local test: ඳු also loses its tail in Nirmala UI. Unicode does not list the
whole class, so for ඳ this is a font observation, not a documented rule **[open]** (§10, item 7).

- **Examples:** දුව (duva), අඳුර (an̆dura).
- **Applies to:** da, nda (observed); u, uu, rakaransaya.
- **Confidence:** high for da, medium for nda.
- **Sources:** S1, S16.

### VS-016: Vowel signs on rakaransaya / yansaya clusters

**Statement.** After a cluster such as ක්‍ර or ක්‍ය, the vowel belongs to the ර or ය. Its
sign attaches to the rightmost component. The kombuva goes before the whole cluster.

ු/ූ on a rakaransaya cluster take yet another pair of shapes. These **must not** be encoded
as ැ/ෑ, which look similar but sit higher (Unicode's explicit warning).

SLS 1134 Table 3 lists the valid vowels:

| Cluster | Valid vowels (SLS 1134 Table 3) |
|---|---|
| yansaya | a, aa, u, uu, e, ee, o, oo |
| rakaransaya | a, aa, ae, aee, i, ii, e, ee, ai, o, oo, au |

SLS also says other combinations, though not used, should still be allowed.

- **Examples:** ක්‍රෝධය (krōdhaya), ප්‍රශ්නය, ත්‍රි, ව්‍යාපාරය, ක්‍රූර (krūra).
- **Applies to:** every consonant with rakaransaya/yansaya.
- **Confidence:** high for the encoding. **Conflict** on ru/ruu after rakaransaya (see §10).
- **Sources:** S1, S5 Table 3 and §6.3, S7 (`vatu`, `abvs`).

### VS-017: Al-lakuna has two shapes

**Statement.** Al-lakuna has the usual curl ("kodiya") on most letters and a second shape on
some letters. SLS cites ට්. Unicode cites ච්. Local test (Nirmala UI): ච් ජ් ඦ් ට් and ර්
look distinct, but the exact class is font-dependent. There is one code point (U+0DCA) either
way.

- **Applies to:** hal.
- **Confidence:** high that the code is the same. Low for the exact membership list.
- **Sources:** S1, S5 Table 1 (1a) and §5.4, S16.

### VS-018: Kombuva placement

**Statement.** In display, the kombuva (and the left part of ේ ො ෝ ෞ, and ෛ) goes before
the **entire** orthographic cluster: before the first consonant of a ZWJ conjunct, a
rakaransaya/yansaya cluster or a touching cluster. The rest of the vowel attaches to the
rightmost part. Storage is still cluster first, then sign.

- **Examples:** ක්‍රෝ → displayed as ෙ ක්‍ර ා ්. ද්‍යෙ.
- **Exception:** a repaya is above the following base and is not part of what precedes the
  kombuva. The kombuva goes before that base.
- **Applies to:** e, ee, ai, o, oo, au.
- **Confidence:** high.
- **Sources:** S7 (prebase reorders to the start of the cluster), S10 ("ensure pre-base
  dependent vowels precede consonant clusters"), S14.

---

## 6. Which consonant + vowel combinations occur

### VS-019: ඇ / ඈ and ැ / ෑ are distinctly Sinhala

**Statement.** The æ vowels are unique to Sinhala among Indo-Aryan scripts, and in use since
about the 7th century. They are common in native words and English loans, and absent from
Sanskrit/Pali loans. As a result, aspirated and Sanskrit-only consonants rarely carry ැ/ෑ.

- **Examples:** ඇස (æsa), පැන (pæna), කෑම (kǣma), බැංකුව, ෆෑන් (NLPC 829).
- **Applies to:** ae, aee.
- **Confidence:** high for uniqueness. Medium for "rare on aspirates" (inferred).
- **Sources:** S1, S5 §3 note 1, S9.

### VS-020: ෘ is pronounced /ru/: Sanskrit ṛ, and C + r + u in other words

**Statement.** ෘ (gaetta-pilla) appears in tatsama (Sanskrit) words. It is pronounced as ru
(or ri). The mixed-alphabet ṛ can also be written phonetically as r+u in śuddha Sinhala. SLS
counts it among the 17 standard forms. Because ෘ is read /ru/, writers also use ෘ/ෲ for /ru/
and /ruː/ after a consonant in non-Sanskrit words and English loans (ගෲප්, ඇන්ඩෲ), and it is
the usual spelling of C + r + u/uu (VS-035).

- **Attested consonants (examples, NLPC tokens):** කෘෂිකර්මය 941, ගෘහ 5,906, තෘප්තිය 1,103,
  දෘෂ්ටිය 987, ධෘති (rare: 2), නෘත්‍ය 106, පෘථිවිය 2,451, බෘහස්පති 26, භෘත්‍ය (rare: 2),
  මෘදු 1,616, වෘක්ෂ 350, ශෘංගාර 268, සෘජු 3,302, හෘදය 1,375, ඝෘණා (rare: 0 as a bare word,
  26 with endings; the LGR lists ඝෘ as a sequence).
- **Never:** ර+ෘ (no rṛ in Sanskrit) [inferred], ළ ඞ ඤ ඥ ඦ, the sannjakas, ණ ය ල ෂ
  [inferred]. ෆ is attested in English loans (ෆෘට් "fruit", S17).
- **Applies to:** ru.
- **Confidence:** high for Sanskrit ṛ. High for the wider /ru/ use (S17, VS-035). Medium for the consonant list.
- **Sources:** S5 Table 2, S9 Tables 2 and 3a, S11, S14, S17.

### VS-021: ෲ, ෟ, ෳ, ඎ, ඏ, ඐ are marginal

**Statement.**
- ඏ and ඐ are not in present usage (SLS).
- ඎ is not in present use, but its sign ෲ is used (SLS).
- ෳ (diga gayanukitta) is not used (SLS).
- The LGR excludes ෟ and ෳ as "usage unknown" and also excludes ඎ ඏ ඐ.
- ෟ survives as the second half of ෞ, and SLS treats gayanukitta as the au-forming stroke.

- **Examples:** ෲ appears in Sanskrit stems such as මාතෲ (NLPC 65) and කර්තෲ (rare: NLPC 15).
  The often-cited pitṝ (පිතෲ) does not occur in NLPC as a bare word (4 tokens with endings).
- **Applies to:** ruu, ilu, iluu.
- **Confidence:** high.
- **Sources:** S5 §3.1 notes 2–3 and §3.4 note 4, S9 Table 4.

### VS-022: ෛ / ෞ in loans; native ai/au use ය/ව

**Statement.** The diphthong signs ෛ and ෞ belong to the mixed (Sanskrit-derived) set. In
pure Sinhala spelling, ai is written as a + yi and au as a + wu. Spoken Sinhala has many
diphthongs, all ending in a high vowel. They are written with consonant ය/ව plus a sign.

- **Examples (ෛ):** සෛලය, වෛද්‍ය, දෛනික, ජෛව, මෛත්‍රී, ඓතිහාසික (independent).
- **Examples (ෞ):** පෞද්ගලික, බෞද්ධ, භෞතික, සෞඛ්‍යය, ගෞරවය, යෞවන, ලෞකික, ඖෂධ
  (independent).
- **Examples (native / English loans):** අයිය (ayiya), ලයිට් (light), කවුද (kavuda/kauda), මවුස්.
- **Applies to:** ai, au.
- **Confidence:** high for the principle. Every example above is attested in
  NLPC (from 285 tokens for සෛලය to 46,508 for වෛද්‍ය).
- **Sources:** S11 (diphthong list), S14.

### VS-023: ඞ takes no vowel signs

**Statement.** SLS 1134 says ඞ is never combined with a vowel and appears only as ඞ් (as in
සඞ්ඝ). The LGR excludes ඞ as not in modern usage. In modern writing, anusvara ං usually
replaces ඞ්.

- **Applies to:** nga × every vowel sign (never). nga + hal is valid but rare.
- **Confidence:** high.
- **Sources:** S5 §3.5 note 1, S9 Table 4.

### VS-024: ඦ is archaic

**Statement.** ඦ is not found in contemporary writing (SLS). The LGR says it occurs only in a
dog-calling word. Treat every sign on it as rare. Never use hal with it (VS-025).

- **Applies to:** nyja.
- **Confidence:** high.
- **Sources:** S5 §3.2 note 1, S9 Table 4.

### VS-025: Sannjakas take vowels but not hal

**Statement.** Vowel signs attach to a prenasalized consonant the same way they attach to the
plain stop (S14). The LGR whole-label rules allow sannjaka + vowel sign and sannjaka + ං, but
say sannjakas cannot be followed by halanta.

- **Examples:** කුඹුර (kum̆bura), අඳුර, ගඟ, කඳු, අඹ.
- **Applies to:** nnga, nndda, nda, mba, nyja.
- **Confidence:** high for "no hal". Medium for how often each sign occurs.
- **Sources:** S9 §3.3.6 and §5.6.5, S14.

### VS-026: ඥ and ඤ

**Statement.** ඥ (jña) is an atomic conjunct. Word-initially it sounds the same as ඤ, but
elsewhere it is a cluster. Both take vowel signs. ඥා is by far the most common form.

- **Examples:** ඥාතියා, ඥානය, විඥානය, ප්‍රඥාව, සංඥාව; ඤාණ (Pali-style).
- **Applies to:** jnya, nya.
- **Confidence:** medium for frequency.
- **Sources:** S1, S5 §3.2 note 2.

### VS-027: ෆ is for loans only

**Statement.** ෆ (fa) is used for English and other loans. It takes the ordinary signs (ා ැ ෑ
ි ී ු ූ ෙ ේ ො ෝ ්) but not ෘ ෲ ෛ ෞ.

- **Examples:** ෆයිල් (file), ෆෝන් (phone), ෆිල්ම් (film).
- **Applies to:** fa.
- **Confidence:** medium (inferred from what the letter is for).
- **Sources:** S2, S5 §3.2.

### VS-028: Aspirates and Sanskrit-only consonants

**Statement.** ඛ ඝ ඡ ඣ ඨ ඪ ථ ධ ඵ භ ශ ෂ (and ණ in most positions) belong to the mixed
alphabet. They appear mainly in tatsama/Pali loans, so their sign set is the Sanskrit one: no
or rare ැ/ෑ, but ෘ ෛ ෞ are possible. English loans add ශ/ෂ + ැ (for example ෂැම්පු,
NLPC 218).

- **Confidence:** medium.
- **Sources:** S14 (mixed vs pure alphabet), S5.

---

## 7. Independent vowel vs sign; hiatus and glides; length

### VS-029: Independent vowels are word-initial

**Statement.** SLS 1134 says the 18 vowels, unlike consonants, are used only at the
beginning of words. The LGR adds that independent vowels start words and dependent vowels
follow consonants. Inside a word, a vowel after a consonant is always a sign. A vowel after
another vowel is resolved by a glide (VS-030) or sandhi (VS-031), not by writing a second
independent vowel.

- **Exceptions [open]:** spelled-out acronyms and letter names (ඩී එන් ඒ), some
  compounds and loan-prefix forms written without sandhi, and Pali texts. See §10, item 9.
- **Applies to:** all vowels.
- **Confidence:** high for the rule. Low for the exceptions list.
- **Sources:** S5 §3.1, S9 §3.3.2.

### VS-030: Hiatus is resolved with ය (after front vowels) or ව (after back vowels)

**Statement.** At root–suffix boundaries in nouns, Sinhala always resolves vowel hiatus by
inserting a glide. It is j (ය) after i or æ and w (ව) after u or ā. Verbs prefer deleting
a vowel. Orthography follows the pronunciation, so the glide is written as the consonant
ය/ව carrying the following vowel.

| Underlying | Spoken | Written | Gloss |
|---|---|---|---|
| ræ + a | [ræjə] | රැය | night (def.) |
| toppi + a | [toppijə] | තොප්පිය | hat (def.) |
| ašu + a | [ašuwə] | අටුව (NLPC 85) | attic (def.) |
| maaligaa + a | [maaligaawə] | මාලිගාව | palace (def.) |

Typical spellings: dia → දිය, dua → දුව, kiyanawa → කියනවා, diyunu → දියුණු (iu → ඉයු),
ovun → ඔවුන් (ou → ඔවු), æyi → ඇයි "why" (æi → ඇයි).

- **Applies to:** all vowel sequences; ya, va.
- **Confidence:** high for nouns (linguistic source). Medium for the general orthographic
  claim.
- **Sources:** S12 (citing Smith 2001), S11.

### VS-031: Āgama (insertion) sandhi in compounds

**Statement.** In compounds, ය or ව (or occasionally ර) is inserted between a final and an
initial vowel.

- **Examples:** නො + එක් → නොයෙක් (ය), කටු + අල → කටුවල (ව), නි + අවුල් → නිරවුල් (ර).
- **Other vowel sandhi:** the vowel may be elided or replaced instead (දන්ත + ආලේප → දන්තාලේප).
- **Confidence:** medium (Wikipedia lead only; textbook not reached).
- **Sources:** S13.

### VS-032: Vowel length is phonemic and has separate signs

**Statement.** Short and long vowels are distinct phonemes (14 vowel phonemes in all). Each
long vowel has its own sign:

| Short | Long |
|---|---|
| (inherent) | ා |
| ැ | ෑ |
| ි | ී |
| ු | ූ |
| ෙ | ේ |
| ො | ෝ |
| ෘ | ෲ |

In ේ and ෝ the long mark is the al-lakuna stroke. The independent letters ඒ and ඕ work the
same way.

- **Example pairs (NLPC tokens):** බල 30,873 / බාල 8,405 (bala / bāla), සුදු 30,640 / සූදු 1,106
  (sudu "white" / sūdu "gambling"), මල 12,867 / මාල 1,665.
- **Confidence:** high for the system. Medium for the example pairs.
- **Sources:** S2, S5 Table 2, S11.

### VS-033: Common spelling mistakes involving pili

1. **Vowel length** (hrasva/dirgha) is the most common error class in Sinhala text (S15).
2. **ෘ vs ්‍ර / රු confusion** (ගෘහ vs ග්‍රහ, a real meaning change).
3. **ෛ/ෞ vs ayi/avu.** For example, වෛද්‍ය is correct, and spelling it with අයි is wrong.
4. **Encoding errors:** ෙ+ෙ for ෛ; ෙ+්+ා for ෝ; අ+ා for ආ; ැ/ෑ stored instead of
   rakaransaya-u forms (S1 warning; ක්‍රෑර, ශ්‍රැති, see VS-035); two signs on one consonant.
5. **ඥ/ඤ** swapped word-initially (they sound the same there; S5).

- **Confidence:** high for 1 and 4. Medium for 2, 3 and 5.
- **Sources:** S15, S1, S4, S5, S16.

### VS-035: C + r + u/uu is usually written ෘ/ෲ, with rakaransaya + ු/ූ as the alternative

**Statement.** A consonant followed by /ru/ or /ruː/ has two correct encodings, and both are
read the same way because ෘ is pronounced /ru/ (VS-020, 05:G2P-011):

- C + ෘ / ෲ: කෘ, කෲර, මෘදු, ගෲප්. This is by far the more common spelling.
- C ් ZWJ ර + ු / ූ (rakaransaya + u/uu): ක්‍රු, ක්‍රූර. This is the spelling S1 uses to
  illustrate the rakaransaya + u/uu glyphs (VS-016).

A third spelling copies the look of the rakaransaya + u/uu glyph with ැ/ෑ (ක්‍රෑර, ශ්‍රැති,
භ්‍රෑණ). It is common but wrong: ැ/ෑ write the vowel /æ/, and S1 warns against the substitution
(VS-016, VS-033).

**Evidence (S17).** For every word in the list written with C + ෘ/ෲ, the same word was looked
up with rakaransaya + ු/ූ and with rakaransaya + ැ/ෑ. Where two or more spellings occur, ෘ/ෲ is
the most frequent in 155 words, rakaransaya + ැ/ෑ in 47 and rakaransaya + ු/ූ in 3 (CC-02 in
`reports/corpus-counts.md`). Counts below are the word and its inflected forms, that is every word
that starts with it (CC-03):

| Word | C + ෘ/ෲ | ්‍ර + ු/ූ | ්‍ර + ැ/ෑ |
|---|---:|---:|---:|
| *krūra* "cruel" | කෲර 1,667 | 9 | 186 |
| *saṃskṛtika* "cultural" | සංස්කෘතික 14,680 | 3 | 0 |
| *mṛdukāṃga* "software" | මෘදුකාංග 16,492 | 3 | 0 |
| *ṛju* "direct" | සෘජු 7,013 | 0 | 0 |
| "group" (English) | ගෲප් 937, ගෘප් 685 | 11 | 4 |
| *śruti* | ශෘති 21 | 3 | **124** |
| *bhrūṇa* "embryo" | භෲණ 0 | 2 | **80** |

Sinhala Wikipedia agrees (S18): කෲර in 126 articles, ක්‍රෑර in 24, ක්‍රූර in none (CC-16). The last two
rows show the ැ/ෑ look-alike winning in a few learned words, which is why a lexicon, not a
fixed rule, should choose the spelling of a given word.

ෘ/ෲ are not limited to Sanskrit words. English loans and names use them for /ru/ and /ruː/:
ගෲප් "group", ඇන්ඩෲ "Andrew", බෲනායි "Brunei", ෆෘට් "fruit", ටෲමන් "Truman".

**Rendering (S16).** Fonts disagree on the rakaransaya + u/uu glyph. Noto Sans Sinhala, Noto
Serif Sinhala, Yaldevi and Gemunu Libre draw the special form S1 describes, a stroke after the
cluster that resembles ෑ. Nirmala UI, Iskoola Pota and Abhaya Libre attach an ordinary ු/ූ below
the cluster. With the Windows system fonts a correctly encoded ක්‍රූර therefore looks wrong to
readers, which may be one reason writers avoid it **[inferred]**.

- **Applies to:** every consonant that takes rakaransaya; u, uu, ru, ruu.
- **Confidence:** high for the usage counts. Medium for the font explanation.
- **Sources:** S1, S16, S17, S18.

---

## 8. Validity table: 41 consonants × vowel signs

**Legend.**
- **V** = valid and occurs in ordinary modern words.
- **L** = valid, but in practice only in Sanskrit/Pali loans (tatsama).
- **R** = rare or marginal.
- **N** = never, unattested or excluded by a standard.
- **S** = special glyph shape (the cell also has a V/L/R code). Shape does not change the
  encoding.

Columns: a = inherent vowel; hal = ්; ru ruu ilu iluu = ෘ ෲ ෟ ෳ.

The ෟ and ෳ columns are N for every row (VS-021), so they are omitted below.

**Basis.** The table combines the hard rules (VS-019 to VS-028), the font observations (S16),
and illustrative examples that were not individually counted. Cells beyond the hard rules (N for ඞ signs, sannjaka hal,
ෟ/ෳ; S cells) are **medium/low confidence and need corpus validation** (see §10).

The ru and ruu columns were checked against S17 (counts per consonant: CC-04). A cell was raised when the list
has at least 150 tokens in at least 10 word types, after removing misspellings: ka ga tta dda pa
ba + ෲ and tta dda fa + ෘ became V, and ta + ෲ became L (ශාස්තෲ). The ya and ra rows were left
alone: their ෘ tokens are misspellings (ව්‍යෘපෘති, ද්‍රෘෂ්ටි).

| id | C | a | hal | aa | ae | aee | i | ii | u | uu | ru | ruu | e | ee | ai | o | oo | au |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ka | ක | V | V | V | V | V | V | V | V S | V S | L | V | V | V | L | V | V | L |
| kha | ඛ | L | L | L | R | R | L | L | L | L | N | N | L | L | R | L | L | R |
| ga | ග | V | V | V | V | V | V | V | V S | V S | L | V | V | V | R | V | V | L |
| gha | ඝ | L | L | L | N | N | L | L | L | L | L | N | L | L | N | L | L | N |
| nga | ඞ | N | R | N | N | N | N | N | N | N | N | N | N | N | N | N | N | N |
| nnga | ඟ | V | N | V | R | R | V | V | V S | R S | N | N | V | V | N | V | R | N |
| ca | ච | V | V S | V | V | V | V | V | V | V | N | N | V | V | L | V | V | R |
| cha | ඡ | L | L | L | N | N | L | L | L | L | N | N | L | L | N | L | L | N |
| ja | ජ | V | V S | V | V | V | V | V | V | V | R | N | V | V | L | V | V | R |
| jha | ඣ | R | R | R | N | N | R | R | R | R | N | N | R | R | N | R | R | N |
| nya | ඤ | R | R | R | N | N | R | R | R | N | N | N | R | N | N | R | N | N |
| jnya | ඥ | V | N | V | N | N | R | N | R | N | N | N | R | R | N | R | N | N |
| nyja | ඦ | R | N | R | R | R | R | R | R | R | N | N | R | R | N | R | R | N |
| tta | ට | V | V S | V | V | V | V | V | V | V | V | V | V | V | N | V | V | N |
| ttha | ඨ | L | L | L | N | N | L | L | L | L | N | N | L | L | N | L | L | N |
| dda | ඩ | V | V | V | V | V | V | V | V | V | V | V | V | V | N | V | V | N |
| ddha | ඪ | L | L | L | N | N | L | L | L | L | N | N | L | L | N | L | L | N |
| nna | ණ | V | V | V | R | R | V | V | V | V | N | N | V | V | N | V | V | N |
| nndda | ඬ | V | N | V | R | R | V | V | V | R | N | N | V | V | N | V | R | N |
| ta | ත | V | V | V | V | V | V | V | V S | V S | L | L | V | V | L | V | V | R |
| tha | ථ | L | L | L | N | N | L | L | L | L | N | N | L | L | N | L | L | N |
| da | ද | V | V | V | V | V | V | V | V S | V S | L | R | V | V | L | V | V | L |
| dha | ධ | L | L | L | R | R | L | L | L | L | L | N | L | L | L | L | L | L |
| na | න | V | V | V | V | V | V | V | V | V | L | N | V | V | L | V | V | L |
| nda | ඳ | V | N | V | R | R | V | V | V S | R S | N | N | V | V | N | V | R | N |
| pa | ප | V | V | V | V | V | V | V | V | V | L | V | V | V | L | V | V | L |
| pha | ඵ | L | L | L | N | N | L | L | L | L | N | N | L | L | N | L | L | N |
| ba | බ | V | V | V | V | V | V | V | V | V | L | V | V | V | R | V | V | L |
| bha | භ | L | L | L | R | R | L | L | L S | L S | L | N | L | L | L | L | L | L |
| ma | ම | V | V | V | V | V | V | V | V | V | L | R | V | V | L | V | V | L |
| mba | ඹ | V | N | V | R | R | V | V | V | R | N | N | V | V | N | V | R | N |
| ya | ය | V | V | V | V | V | V | V | V | V | N | N | V | V | R | V | V | L |
| ra | ර | V | V S | V | V S | V S | V | V | V S | V S | N | N | V | V | R | V | V | L |
| la | ල | V | V | V | V | V | V | V | V | V | N | N | V | V | R | V | V | L |
| va | ව | V | V | V | V | V | V | V | V | V | L | N | V | V | L | V | V | R |
| sha | ශ | L | L | L | R | R | L | L | L S | L S | L | N | L | L | L | L | L | L |
| ssa | ෂ | L | L | L | R | R | L | L | L | L | N | N | L | L | N | L | L | N |
| sa | ස | V | V | V | V | V | V | V | V | V | L | N | V | V | L | V | V | L |
| ha | හ | V | V | V | V | V | V | V | V | V | L | N | V | V | R | V | V | R |
| lla | ළ | V | R | V | V | R | V | V | V S | R S | N | N | V | R | N | V | R | N |
| fa | ෆ | V | V | V | V | V | V | V | V | V | V | N | V | V | N | V | V | N |

Notes on the table:
- **S, u/uu:** ka ga nnga ta bha sha take the hook form (VS-014). ra and lla are irregular
  (VS-012, VS-013). da and nda lose their tail (VS-015).
- **S, hal:** the alternative al-lakuna shape (VS-017) seen in Nirmala UI on ca ja tta ra
  (also nyja, though nyja + hal is N).
- **S, ae/aee:** only ra (VS-011).
- ru (ෘ) showed no consonant-specific shape in Nirmala UI on any row.
- jnya/nya/nyja/jha rows: low confidence beyond "a/aa occur".

---

## 9. Implications for romanization and transliteration

These points apply to anyone converting between a Latin-script romanization and Sinhala script,
or validating stored Sinhala text.

1. **Use only canonical, single-code-point signs** (VS-003 to VS-006). Romanized "ee" → ේ,
   "oo" → ෝ, "o" → ො, "au" → ෞ, "ai" → ෛ (U+0DDB) when those signs are intended. ෙෙ, ෙ+්+ා,
   අ+ා and ඔ+් are never correct stored forms. NFC is a useful safety net, but it does not
   produce U+0DDB from ෙෙ.
2. **Logical order is natural for romanization.** A romanized vowel comes after its consonant,
   which matches storage order. The kombuva-first order belongs only to writing and display
   (VS-002, VS-018).
3. **Context decides independent vs sign** (VS-029). After a consonant (or a cluster), a vowel
   corresponds to a sign. At word start, it corresponds to an independent letter. After another
   vowel, the normal spelling uses a **glide** (VS-030) rather than a second independent letter:
   - "dia" → දිය, "dua" → දුව, "aeyi" → ඇයි.
   - Rule of thumb: after i/ii/e/ee/ae/aee use ය. After u/uu/o/oo/a/aa use ව. Before a
     high vowel (ai/au-type sequences), use the ය/ව + sign spelling.
   - A literal independent vowel mid-word is exceptional (acronyms) and a romanization should
     mark it explicitly.
4. **"ai" and "au" are ambiguous** (VS-022). Mapping `ai` → ෛ and `au` → ෞ gives the Sanskrit
   spelling for every word. Native and loan words need අයි/අවු (ලයිට්, කවුද, හවුස්). Options:
   - treat ayi/avu as the default reading and reserve distinct symbols for ෛ/ෞ, or
   - decide per word from a dictionary.
5. **"ru" collides three ways** (VS-012, VS-016, VS-020): ර+ු, ෘ, and rakaransaya + ු.
   - "kru" is usually කෘ (කෘෂි, කෲර) and occasionally ක්‍රු; a lexicon decides per word (VS-035), and
   - "karu" must never become කෘ.
   A reversible romanization should give ෘ a distinct symbol (for example `ṛ`), and let plain
   `ru` mean r+u.
6. **"ae" means ඇ, so a + e hiatus needs another representation.** That is rarely a problem,
   because a + e hiatus is spelled with a glide anyway (නො + එක් → නොයෙක්, VS-031). A
   romanization should state that "ae" always means æ, and use a glide-aware rule (or an
   explicit separator) for a + e.
7. **Impossible pairs** (§8 N cells) are useful validation checks:
   - no sign on ඞ (ං is the usual modern spelling instead);
   - no hal on ඟ ඬ ඳ ඹ ඦ;
   - no ෟ/ෳ outside Sanskrit material;
   - no ෘ/ෛ/ෞ on ෆ, ළ or the sannjakas.
   L/R cells are valid but low-frequency.
8. **No sign + sign, no sign after hal** (VS-009, VS-010). For example, "kaa" + "a" must not
   give කාා. A doubled vowel letter in a romanization means a long vowel (a → aa, i → ii and
   so on), not a second sign.
9. **Lengthening by doubling is consistent.** Every short sign has exactly one long partner
   (VS-032). The consistent scheme is a→aa, ae→aee, i→ii, u→uu, e→ee, o→oo, ru→ruu.
   Informal romanizations often write "ee" for ī. Interpreting "ee" as ී rather than ේ needs
   dictionary support, since ee → ේ is the systematic reading.
10. **Special shapes need no rules** (VS-011 to VS-015). The encoding is uniform (ර+ු, ළ+ු).
    "Visual" equivalents are wrong: ළු is not a separate code point, and ැ is not the
    rakaransaya-u sign.
11. **Spell-checking:** length errors are the most common mistake (VS-033). Both length
    variants are worth checking when a dictionary has only one.

---

## 10. Open questions / conflicting sources

1. **Rakaransaya + u/uu.** SLS 1134 Table 3 leaves kru/kruu out of the valid rakaransaya
   vowels, and says such sequences "are not used". Unicode §13.2 gives ක්‍රු/ක්‍රූ as normal
   forms with dedicated glyph variants. Corpus counts (VS-035) partly support SLS: the sequence
   is valid but rare, because writers use ෘ/ෲ (කෲර) or, wrongly, ැ/ෑ (ක්‍රෑර) instead.
   Treat both ෘ/ෲ and rakaransaya + ු/ූ as valid, with ෘ/ෲ as the usual form.
2. **Displaying a sign in isolation.** Three conventions conflict:
   - SLS 1134 draft: ZWNJ + sign;
   - SLSI WG 2004: space + sign, NBSP + pāpilla for the hook form;
   - Microsoft: reportedly space + ZWJ (per the SLSI note).
   This is only relevant for documentation, charts and teaching material that show a sign on its own.
3. **Gayanukitta ෟ.** SLS Table 1 treats it as the au stroke and does not use it as a standalone
   vowel. The LGR excludes it ("usage unknown"). Unicode names it as the vocalic-l sign.
   Consensus: do not emit it alone in modern Sinhala.
4. **ෲ usage.** SLS says ෲ "is used" (its example is garbled in the PDF; possibly කර්තෲ).
   The LGR includes ෲ but excludes ඎ. In common usage the spelling is කර්තෘ (with ෘ): NLPC has
   කර්තෘ 2,938 tokens against කර්තෲ 15 (rare).
5. **Two-part ai/o/au contextual forms.** An automated summary of Unicode ch. 13 claimed these
   signs have special two-part forms after ga, nya, ttha, nna, tha, dha and sha. That text is
   **not** in the §13.2 extracted here, so it was rejected as an error in a secondary summary.
   Noted so nobody re-imports it.
6. **Al-lakuna shape classes** (VS-017). Unicode cites ච, SLS cites ට. The full set is
   font-dependent and was not found in any normative source.
7. **Tail loss on ඳ** (VS-015). Seen in Nirmala UI only; Unicode says "bases similar to ද"
   without listing them.
8. **The validity table (§8)** is a synthesis, not a corpus measurement. The L/R/N split for
   aspirates, sannjakas + long vowels, ළ + long vowels, and ඤ/ඥ/ඦ needs validation against a
   Sinhala corpus. Suggested: the UCSC 10M-word corpus or a Wikipedia dump, counting C+sign
   bigrams.
9. **Medial independent vowels** (VS-029). SLS says vowels occur only word-initially. Real
   text has acronyms (ඩී එන් ඒ) and some unsandhied compounds. The extent was not found in any
   source.
10. **Native pili names** (VS-001) were not checked against an NIE grammar textbook. Search
    engines returned nothing usable for Sinhala-script queries. Recommend a manual check of the
    Grade 6–9 සිංහල භාෂාව textbooks on educationpublications.gov.lk.
11. **S1 table artifact.** The Unicode HTML shows ◌ු followed by ZWJ in the රු/ළු rows of
    Table 13-5. This is presumed to be an HTML artifact; the SLS encoding (ර U+0DBB + U+0DD4) has
    no ZWJ.
12. **ඔ + ් vs ඕ.** This pair is absent from Unicode Table 13-2 and DoNotEmit, and HarfBuzz does
    not flag it. Well-formed text should still never contain it.
13. **Removed rules:** VS-034 was removed as out of scope.
