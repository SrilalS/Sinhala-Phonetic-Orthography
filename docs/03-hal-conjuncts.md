# 03: Hal (al-lakuna ්) and consonant clusters / conjuncts

Scope: the Sinhala al-lakuna (hal kirīma), the three reduced forms (yansaya, rakāransaya,
rēpaya), ligated conjuncts (bændi akuru), touching letters (sparśa akuru), cluster
phonotactics, geminates, and the stored sequences that SLS 1134 and Unicode specify for them.

Compiled October 2026.

Conventions used in this file:

- **Code points** are given as `U+XXXX` sequences. `U+200D` = ZERO WIDTH JOINER (ZWJ), `U+200C` = ZERO WIDTH NON-JOINER (ZWNJ), `U+0DCA` = SINHALA SIGN AL-LAKUNA (hal).
- Every code point sequence in this file was machine-generated from the Sinhala string shown next to it, so the two always agree.
- **Letter IDs** (used throughout this repository): ka kha ga … lla fa; vowels a aa … au; hal.
- **Confidence**: high = stated directly by Unicode / SLS / font-shaping spec, or by two or more independent sources; medium = one good source, or a reasonable inference from good sources; low = unverified or contested. **[UNVERIFIED]** marks claims I could not confirm in any source I fetched.
- Romanization in examples is informal (`t` = ට, `th` = ත, `d` = ඩ, `dh` = ද, `sh` = ශ, `ss` = ෂ, `ə` = schwa). It is not a proposal.

---

## 0. Sources (cited by ID below)

| ID | Source | Type / authority |
|---|---|---|
| S1 | Unicode Standard 15.0, ch. 13 §13.2 "Sinhala": https://www.unicode.org/versions/Unicode15.0.0/ch13.pdf | Normative-ish (core spec text) |
| S2 | Unicode NamedSequences.txt: https://www.unicode.org/Public/UCD/latest/ucd/NamedSequences.txt | Normative data |
| S3 | SLS 1134:2004 *draft for public comment* (WG2 N2737 / L2/04-131), https://www.unicode.org/wg2/docs/n2737.pdf ; second copy https://sinhala.sourceforge.net/archive/akuru.org/att-0028/sls1134.pdf | National standard (draft). The final 2004 and the 2011 revision were **not** obtainable online. |
| S4 | SLSI working-group decisions 2004-06-09, L2/04-231: https://www.unicode.org/L2/L2004/04231-sinhala-rep.pdf | Standards body minutes |
| S5 | Microsoft, "Creating and Supporting OpenType Fonts for Sinhala Script": https://learn.microsoft.com/en-us/typography/script-development/sinhala | Shaping spec (pre-Win10 engine) |
| S6 | Microsoft, "Universal Shaping Engine" spec: https://learn.microsoft.com/en-us/typography/script-development/use | Shaping spec (current Windows engine for Sinhala) |
| S7 | HarfBuzz source: `src/hb-ot-shaper.hh` (Sinhala → USE) and `src/hb-ot-shaper-use.cc` (`F_MANUAL_ZWJ`), https://github.com/harfbuzz/harfbuzz | Implementation |
| S8 | ICANN Sinhala Generation Panel, "Proposal for a Sinhala Script Root Zone LGR", 22 Apr 2019: https://new.icann.org/en/system/files/files/proposal-sinhala-lgr-22apr19-en.pdf | Expert panel (UCSC, J.B. Disanayaka, et al.) |
| S9 | M. Jansche, unicode list, Oct 2016 (quotes SLS 1134:2011 Table 3 note), https://corp.unicode.org/pipermail/unicode/2016-October/004249.html ; reply (A. Freytag) https://unicode.org/mail-arch/unicode-ml/y2016-m10/0218.html | Secondary quote of the standard |
| S10 | Harshula / R. Wordingham, unicode list, Oct 2018 "Fallback for Sinhala Consonant Clusters": https://www.unicode.org/mail-arch/unicode-ml/y2018-m10/0062.html ; https://www.unicode.org/mail-arch/unicode-ml/y2018-m10/0041.html ; https://corp.unicode.org/pipermail/unicode/2018-October/007087.html | Expert discussion; reports SLS 1134:2011 content |
| S11 | Harshula, unicode list, Sep 2009 "Use of ZWJ to form Sinhala Conjuncts": https://unicode.org/mail-arch/unicode-ml/y2009-m09/0011.html | Expert discussion |
| S12 | Harshula Jayasuriya, "Sinhala Orthography: Ola Leaf to the Computer", UCSC LTRL, 2007, https://ftp3.gwdg.de/pub/gnu/www/savannah-checkouts/non-gnu/sinhala/doc/presentations/sinhala-orthography-hj-20070212.pdf | Expert presentation |
| S13 | Wasala, Weerasinghe, Gamage, "Sinhala Grapheme-to-Phoneme Conversion and Rules for Schwa Epenthesis", COLING/ACL 2006: https://aclanthology.org/P06-2114.pdf | Peer-reviewed linguistics/NLP |
| S14 | Wikipedia, "Sinhala language" (Phonology): https://en.wikipedia.org/wiki/Sinhala_language | Lead only |
| S15 | si.wikipedia "සිංහල හෝඩිය" conjunct table: https://si.wikipedia.org/?curid=2505 | Lead only |
| S16 | Usgoda Dhammagaru, "සිංහල භාෂාවේ අක්ෂර වින්‍යාසය" (teaching notes, 2024): https://ia601404.us.archive.org/21/items/Index_201704/dhgra002.pdf | Teaching material (medium) |
| S17 | Noto Sans Sinhala sources (glyph inventory): https://github.com/notofonts/sinhala | Font implementation |
| S18 | fontconfig `si.orth` patch citing SLS 1134 Part 2:2007 compliance levels, https://bugs.freedesktop.org/attachment.cgi?id=22587 | Secondary quote of the standard |
| S19 | S. Wiles, Indology list, June 2012 "Sinhala ligatures": https://list.indology.info/pipermail/indology/2012-June/036715.html | Scholar's note |
| S20 | M. Kaplan, "The subtle difference between ශ්රී ලංකාව and ශ්‍රීලංකාව", 2007: https://archives.miloush.net/michkap/archive/2007/10/14/5448243.html | Implementer blog |
| S21 | E. Muller (Adobe), comments on Sinhala draft, L2/04-235: https://www.unicode.org/L2/L2004/04235-sinhala-cmt.html | UTC document |
| S22 | si.wikipedia "සිංහල අක්ෂර වින්‍යාසය": https://si.wikipedia.org/wiki/සිංහල_අක්ෂර_වින්‍යාසය | Lead only |
| S23 | A published Sinhala transliteration scheme (nongnu.org Sinhala project documentation): https://www.nongnu.org/sinhala/doc/transliteration/sinhala-transliteration_2.html | Prior-art romanization |
| S24 | RFC 5892 (IDNA2008), Appendix A.2, CONTEXTJ rule for ZWJ: https://www.rfc-editor.org/rfc/rfc5892 | IETF standard (cited from knowledge, not fetched this session) |
| S25 | si.wikipedia articles "දුම්රිය" and "ශ්‍රී ලංකා දුම්රිය සේවය", wikitext fetched 2026-10-05: https://si.wikipedia.org/wiki/දුම්රිය | Usage sample (running text) |

---

## 1. Things that will bite you (read first)

1. **In Sinhala, hal never joins anything by itself.** `C + ් + C` always shows a visible hal. You only get a conjunct, yansaya, rakāransaya or rēpaya when ZWJ is present. Sinhala differs from Devanagari here. (HC-001)
2. **ZWJ order matters.** `් + ZWJ` gives a conjunct or reduced form. `ZWJ + ්` gives a *touching* letter. These are different spellings of the same sounds. (HC-002, HC-003)
3. **Yansaya and rakāransaya are mandatory in correct spelling.** `ක්රම` (no ZWJ) is not an accepted spelling of *krama*. Rēpaya is optional. Other ligated conjuncts (ක්‍ෂ, න්‍ද …) are optional and mostly old-fashioned. (HC-020, HC-030, HC-040)
4. **`ර + ් + ZWJ + ය` is ambiguous** (ra + yansaya, or rēpaya + ya). SLS 1134 says ra + yansaya is not used, so it means rēpaya + ya. Fonts disagree. (HC-033)
5. **ඥ is atomic (U+0DA5).** Never build it as `ජ්‍ඤ`. (HC-051)
6. **A word that ends in a consonant sound is written with hal.** The inherent vowel is pronounced as *a* or *ə*, but spelling never shows which. Schwa never triggers a hal. (HC-010…HC-013)
7. **Rakāransaya + u/ū have special glyph shapes that look like æ/ǣ signs.** They must still be encoded with U+0DD4/U+0DD6. Real corpora contain the wrong encoding, e.g. ක්‍රෑර written for *krūra*. The usual spelling of *krūra* is in fact කෲර, with ෲ (02:VS-035). (HC-024)
8. **Prenasalized letters (ඟ ඦ ඬ ඳ ඹ) never take hal.** ළ does not take hal either. (HC-014)
9. **Many systems strip or mangle ZWJ**: some renderers, search boxes, the root-zone LGR. Expect ZWJ-less spellings in real-world corpora and fold them together when matching. (§10)

---

## 2. Encoding model

### HC-001: Al-lakuna alone never forms a cluster
- **Statement:** Without ZWJ, U+0DCA is always visible. It just "kills" the inherent vowel. It never triggers a conjunct, reduced form or touching form.
- **Examples:** `ද + ් + ධ` → ද්ධ (visible hal on ද, then a full ධ): `U+0DAF U+0DCA U+0DB0`. Same with ධර්ම *dharma* written with explicit hal: `U+0DB0 U+0DBB U+0DCA U+0DB8`.
- **Exceptions:** none. This is the base rule of Sinhala encoding. It differs from Devanagari/Tamil practice.
- **Applies-to:** hal; all consonants.
- **Confidence:** high.
- **Sources:** S1 (§13.2 "Virama (al-lakuna) and Consonant Forms"), S12, S11.

### HC-002: Three representations of a consonant pair
- **Statement:** For a consonant pair C1 C2 (no vowel in between) there are three encodings. Each gives a different visual style:
  | Style | Sequence | Use |
  |---|---|---|
  | Separate letters (modern) | `C1 ් C2` | default modern writing |
  | Conjunct / reduced form | `C1 ් ZWJ C2` | yansaya, rakāransaya, rēpaya, ligatures (bændi akuru) |
  | Touching letters | `C1 ZWJ ් C2` | Pali and classical texts (sparśa akuru) |
- **Examples (d + dh):** separate ද්ධ `U+0DAF U+0DCA U+0DB0`; ligature ද්‍ධ `U+0DAF U+0DCA U+200D U+0DB0`; touching ද‍්ධ `U+0DAF U+200D U+0DCA U+0DB0`.
- **Exceptions:** The ZWJ position does *not* decide which consonant takes the reduced form. That differs from Indic ZWJ use. The order only picks the *style* (S1).
- **Applies-to:** hal + any consonant pair.
- **Confidence:** high.
- **Sources:** S1, S5 (cluster grammar `{C+H+ZWJ}+C` vs `{C+ZWJ+H}+C`), S12, S11, S10.

### HC-003: Touching letters use `ZWJ + al-lakuna` (SLS 1134:2011, Unicode)
- **Statement:** A touching cluster is `C1 + ZWJ + ් + C2`. Unicode says this style is *productive*. A font should handle it generically, not as a case-by-case list.
- **Examples:** Pali *kka* ක‍්ක `U+0D9A U+200D U+0DCA U+0D9A` (S5's example); *mma* ම‍්ම `U+0DB8 U+200D U+0DCA U+0DB8` (S15).
- **Exceptions / history:** The 2004 *draft* SLS 1134 (S3) used `් + ZWJ` for both conjuncts and touching letters. Its note on Pali says the sequence 0DCA 200D "may be" used. The SLSI 2004 minutes (S4) then asked Unicode what joiner to use. The candidates were ZWNJ, or ZWJ+ZWNJ+ZWJ. The final 2004 standard and the 2011 revision settled on `ZWJ + al-lakuna`, per Harshula (S10). Old documents may still use the draft convention.
- **Applies-to:** all consonants; hal.
- **Confidence:** high for current practice; medium for exactly when the change happened.
- **Sources:** S1, S5, S10, S11, S12, S3, S4.

### HC-004: Named sequences for the three reduced forms
- **Statement:** Unicode defines named character sequences:
  - SINHALA CONSONANT SIGN YANSAYA = `U+0DCA U+200D U+0DBA`
  - SINHALA CONSONANT SIGN RAKAARAANSAYA = `U+0DCA U+200D U+0DBB`
  - SINHALA CONSONANT SIGN REPAYA = `U+0DBB U+0DCA U+200D`
- **Applies-to:** ya, ra, hal.
- **Confidence:** high.
- **Sources:** S2, S1 (Table 13-3).

### HC-005: ZWJ/ZWNJ semantics in Sinhala (summary)
- **Statement:**
  - ZWJ after hal: request a conjunct or reduced form.
  - ZWJ before hal: request a touching form.
  - ZWNJ: no role in normal Sinhala text, because hal does not join by default. Its documented uses are marginal:
    - (a) The 2004 draft (S3) put ZWNJ before a vowel sign to show it standalone (`U+200C U+0DCF`). It also used ZWNJ for a standalone yansaya (`U+200C U+0DCA U+200D U+0DBA`) and a standalone rēpaya (`U+0DBB U+0DCA U+200D U+200C`).
    - (b) The SLSI 2004 decisions (S4) replaced these with SPACE-based sequences. Standalone yansaya = `U+0020 U+0DCA U+200D U+0DBA`. Standalone rakāransaya = `U+0020 U+0DCA U+200D U+0DBB`. Standalone rēpaya = `U+0DBB U+0DCA U+200D U+0020`. A standalone vowel sign = space + sign, without ZWJ.
    - (c) Jansche/Freytag (S9) proposed `U+0DBB U+200C U+0DCA U+200D U+0DBA` to force the non-standard "ra + yansaya" reading. This is a proposal only; I found no adoption.
  - Under USE (S6), ZWNJ blocks fusion of two characters. ZWJ joins the preceding cluster to the following character.
- **Applies-to:** hal, ya, ra.
- **Confidence:** high for ZWJ; medium for ZWNJ (the standalone conventions conflict between the draft and the WG decisions).
- **Sources:** S1, S3, S4, S6, S9.

### HC-006: Renderers: Sinhala is shaped by USE in Windows 10+ and HarfBuzz
- **Statement:** Windows 10+ shapes Sinhala with the Universal Shaping Engine, which replaced the dedicated Sinhala engine. HarfBuzz also routes `HB_SCRIPT_SINHALA` to its USE shaper. Its USE basic features are applied with `F_MANUAL_ZWJ`, so ZWJ is not skipped and the font's lookups must match it explicitly. In practice:
  - Whether a conjunct appears depends entirely on the font having a lookup for `C ් ZWJ C`.
  - Fallback differs by platform when the font has no glyph. HarfBuzz shows a visible hal. Windows 10 and iOS also show hal but place vowels differently (S10).
- **Font coverage seen:** Noto Sans Sinhala (S17) has ligature glyphs for exactly the Unicode Table 13-4 set plus ඤ්‍ච (glyph names `ka_ssa, ka_va, ga_dha, tta_ttha, ta_tha, ta_va, da_dha, da_va, na_tha, na_da, na_dha, na_va, nya_ca`). It also has a generic `touch` glyph and special rakāransaya forms for ද ඳ ඤ ඥ and the න්‍ද cluster.
- **Confidence:** high (S6, S7 source code); medium for the platform fallback details (one mailing-list report).
- **Sources:** S5, S6, S7, S10, S17.

---

## 3. Hal usage and pronunciation

### HC-010: Hal marks the absence of a vowel; the inherent vowel is never written
- **Statement:** A consonant letter with no sign carries the inherent vowel. A consonant with hal has no vowel. That is the only distinction spelling makes. Whether the inherent vowel is pronounced [a] or [ə] is **not** shown.
- **Examples:** ගම *gamə* "village": `U+0D9C U+0DB8`. කර "shoulder" /karə/ vs කර "do" /kərə/ is a minimal pair spelled identically (S14).
- **Exceptions:** none in spelling. S23, a transliteration scheme, maps both romanized `a` and `e` to the bare consonant, i.e. it lets ə be written as `e`.
- **Applies-to:** all consonants; vowel a; hal.
- **Confidence:** high.
- **Sources:** S13, S14, S23.

### HC-011: Schwa vs /a/ realisation rules (pronunciation only)
- **Statement:** S13 starts by giving every bare consonant /ə/. It then applies ordered rules (summarised in my own words):
  1. The first syllable's nucleus becomes /a/. Exceptions: the word starts with /sv/; it starts with /kər/ (e.g. කර-, so කරනවා → /kərənəwaː/); or it is a single CV syllable.
  2. After a consonant + /r/, ə→a before a consonant; there are sub-rules for /h/.
  3. ə→a before /h/ when a vowel follows the /h/.
  4. ə→a before a consonant cluster (i.e. before a hal-consonant).
  5. ə→a before a word-final consonant, except final /r/, /b/, /ɖ/, /ʈ/.
  6. Word-final ə before /ji/ → a.
  7. /kə(r|l)u/ → /ka(r|l)u/.
  8. A small lexical rule for *kal-* forms.
  
  The rules reached 98% on 30,000 corpus words. Most remaining errors were compounds and English loans.
- **Examples:** කරනවා: `U+0D9A U+0DBB U+0DB1 U+0DC0 U+0DCF` → /kərənəwaː/ by rule 1(b). Note: S13 gives a schwa in the first syllable too, not "karanəwa".
- **Implication:** Hal placement is never driven by schwa. The romanizations `karanawa`, `karanewa` and `kəranəwa` all correspond to the same letters (ක ර න වා).
- **Exceptions:** S13 found some words written without ා but pronounced with a long final vowel: අම්ම → /ammaː/, අක්ක, ගත්ත. Spelling is conservative here.
- **Applies-to:** vowel a; all consonants.
- **Confidence:** high (peer-reviewed); the rule summary is a paraphrase.
- **Sources:** S13, S14.

### HC-012: Word-final hal
- **Statement:** A word ending in a consonant sound is written with a final hal. This is common in modern Sinhala. Typical sources:
  - inflectional endings: instrumental/ablative *-in* (මගින්, අතින්); indefinite *-ak* (පොතක්); *-t* "also" (මමත්); conditional *-nam* (නම්); plurals (මල්, ගස්, කන්)
  - native nouns (පින්, බත්)
  - loans (බස්, කැම්පස්)
- **Examples:** මගින් `U+0DB8 U+0D9C U+0DD2 U+0DB1 U+0DCA`; පින් `U+0DB4 U+0DD2 U+0DB1 U+0DCA`; පොතක් `U+0DB4 U+0DDC U+0DAD U+0D9A U+0DCA`.
- **Exceptions / gotchas:**
  - Word-final hal occurs only on letters that can take hal at all (see HC-014).
  - S14 says Sinhala words cannot *phonetically* end in a nasal other than /ŋ/. So final න් / ම් may be pronounced [ŋ] in speech, even though the spelling keeps න් / ම්. **Medium confidence; only one lead source.** The anusvara ං also writes /ŋ/ (e.g. සිංහල), so a romanized `ng` at word end is ambiguous between ං, න් and ම්.
- **Applies-to:** hal; ka ta tha na ma la sa pa tta etc.
- **Confidence:** high for the rule; medium for the [ŋ] note.
- **Sources:** S13, S14, S8 (examples of hal use), general corpus observation.

### HC-013: Mid-word hal = cluster or geminate
- **Statement:** A hal inside a word always marks a consonant cluster or geminate with no vowel between (අම්මා, පත්තරය, කරන්න). If ZWJ is also present, the cluster is drawn as a conjunct or reduced form (HC-002).
- **Examples:** අම්මා `U+0D85 U+0DB8 U+0DCA U+0DB8 U+0DCF`; කරන්න `U+0D9A U+0DBB U+0DB1 U+0DCA U+0DB1`.
- **Confidence:** high.
- **Sources:** S1, S3, S13.

### HC-014: Letters that never take hal
- **Statement:**
  - The five prenasalized letters (sannaka) ඟ ඦ ඬ ඳ ඹ cannot be followed by hal (S8, "constraint for Sannjakas"). They also cannot geminate (S14).
  - Retroflex ළ never takes hal (S22).
  - ඞ is the reverse case: it "is never combined with a vowel" and appears only in pure form (S3, Table 3 note 1, text partly garbled in the draft PDF; most likely means ඞ්).
- **Exceptions:** si.wikipedia (S15) lists ඳ්‍ඨ, ඳ්‍ධ, ඳ්‍ව as conjuncts. That contradicts S8. I treat S15 as unreliable here (see Open questions).
- **Applies-to:** nnga, nyja, nndda, nda, mba, lla (no hal); nga (hal only).
- **Confidence:** medium-high (S8 is authoritative, S22 is a lead).
- **Sources:** S8, S14, S22, S3.

---

## 4. Yansaya, rakāransaya, rēpaya

### HC-020: Yansaya (්‍ය): ya after a pure consonant
- **Statement:** When ය follows a pure consonant, it is written as the post-base yansaya. Encoding: `C + ් + ZWJ + ය`.
  - Required in normal text: SLS says yansaya and rakāransaya "are required in normal Sinhala text". S8 says forms like වාක්ය (without ZWJ) are not accepted.
  - Leave the ZWJ out only if, for some reason, the yansaya is deliberately not wanted (S3 note).
- **Examples:** වාක්‍ය *vākya* `U+0DC0 U+0DCF U+0D9A U+0DCA U+200D U+0DBA`; සත්‍ය *satya* `U+0DC3 U+0DAD U+0DCA U+200D U+0DBA`; විද්‍යාව `U+0DC0 U+0DD2 U+0DAF U+0DCA U+200D U+0DBA U+0DCF U+0DC0`; අවශ්‍ය `U+0D85 U+0DC0 U+0DC1 U+0DCA U+200D U+0DBA`; රාජ්‍ය `U+0DBB U+0DCF U+0DA2 U+0DCA U+200D U+0DBA`; මනුෂ්‍ය `U+0DB8 U+0DB1 U+0DD4 U+0DC2 U+0DCA U+200D U+0DBA`; ද්‍රව්‍ය `U+0DAF U+0DCA U+200D U+0DBB U+0DC0 U+0DCA U+200D U+0DBA`; ශය්‍යා (ya+yansaya) `U+0DC1 U+0DBA U+0DCA U+200D U+0DBA U+0DCF`.
- **Vowels allowed on the yansaya (SLS Table 3):** a, aa, u, uu, e, ee, o, oo (8 combinations shown, though the text says "7"), e.g. ක්‍යෝ `U+0D9A U+0DCA U+200D U+0DBA U+0DDD`. The vowel applies to the ය, not the first consonant. Other combinations are described as not used, though SLS does not forbid them (S3 §6.3).
- **Restriction:** never after ර (HC-033).
- **Applies-to:** all consonants except ra (and except the hal-less letters of HC-014) + ya.
- **Confidence:** high.
- **Sources:** S1, S2, S3, S5, S8, S9.

### HC-021: Rakāransaya (්‍ර): ra after a pure consonant
- **Statement:** When ර follows a pure consonant, it is written as the below-base rakāransaya. Encoding: `C + ් + ZWJ + ර`. It is mandatory in normal text: S8 says ක්රම is not accepted for ක්‍රම. Vowel signs follow the ර: `C ් ZWJ ර V`.
- **Examples:**
  - ක්‍රම *krama* `U+0D9A U+0DCA U+200D U+0DBB U+0DB8`
  - ප්‍රශ්නය `U+0DB4 U+0DCA U+200D U+0DBB U+0DC1 U+0DCA U+0DB1 U+0DBA`
  - ප්‍රේමය `U+0DB4 U+0DCA U+200D U+0DBB U+0DDA U+0DB8 U+0DBA`
  - ශ්‍රී `U+0DC1 U+0DCA U+200D U+0DBB U+0DD3`
  - ග්‍රාමය `U+0D9C U+0DCA U+200D U+0DBB U+0DCF U+0DB8 U+0DBA`
  - ද්‍රව `U+0DAF U+0DCA U+200D U+0DBB U+0DC0`
  - බ්‍රාහ්මණ `U+0DB6 U+0DCA U+200D U+0DBB U+0DCF U+0DC4 U+0DCA U+0DB8 U+0DAB`
  - හ්‍රස්ව `U+0DC4 U+0DCA U+200D U+0DBB U+0DC3 U+0DCA U+0DC0`
  - ස්‍රාවය `U+0DC3 U+0DCA U+200D U+0DBB U+0DCF U+0DC0 U+0DBA`
  - ව්‍රත `U+0DC0 U+0DCA U+200D U+0DBB U+0DAD`
- **Vowels allowed on the rakāransaya (SLS Table 3):** a, aa, ae, aee, i, ii, e, ee, ai, o, oo, au (12 combinations). Notice that u/uu are *not* in the table, but see HC-024.
- **Applies-to:** effectively every consonant that can take hal + ra. Common with ka ga gha ta tha da dha pa ba bha va sha sa ha tta; rare with ma (HC-052); loans with fa dda.
- **Confidence:** high.
- **Sources:** S1, S2, S3, S5, S8.

### HC-022: Rēpaya (ර්‍): ra before a consonant
- **Statement:** When ර් comes before a consonant, it can be written as the above-base rēpaya. Encoding: `ර + ් + ZWJ + C`. Shapers reorder the glyph after the base consonant, and after the yansaya if there is one (S5).
  - **The rēpaya is optional.** Both කර්ම and කර්‍ම are valid (S3 §3.5). S8 likewise accepts both තර්ක and තර්‍ක.
- **Examples:**
  - ධර්‍ම / ධර්ම *dharma*: `U+0DB0 U+0DBB U+0DCA U+200D U+0DB8` vs `U+0DB0 U+0DBB U+0DCA U+0DB8`
  - තර්‍කය `U+0DAD U+0DBB U+0DCA U+200D U+0D9A U+0DBA`
  - මාර්‍ගය `U+0DB8 U+0DCF U+0DBB U+0DCA U+200D U+0D9C U+0DBA`
  - වර්‍ෂය `U+0DC0 U+0DBB U+0DCA U+200D U+0DC2 U+0DBA`
  - පූර්‍ව `U+0DB4 U+0DD6 U+0DBB U+0DCA U+200D U+0DC0`
  - අර්‍ථය `U+0D85 U+0DBB U+0DCA U+200D U+0DAE U+0DBA`
  - වර්‍ණ `U+0DC0 U+0DBB U+0DCA U+200D U+0DAB`
- **Applies-to:** ra + hal + almost any consonant (ka ga ca ja nna ta tha da dha na pa ba bha ma ya va sha ssa sa ha).
- **Confidence:** high (encoding); high (optionality).
- **Sources:** S1, S2, S3, S5, S8.

### HC-023: Stacking order and combinations
- **Statement:** Logical order is always left to right in pronunciation order. ZWJ follows every hal that joins:
  - conjunct + rakāransaya: න්‍ද්‍රා `U+0DB1 U+0DCA U+200D U+0DAF U+0DCA U+200D U+0DBB U+0DCF` (SLS 1134 §5.8 example)
  - consonant + yansaya + rakāransaya (si.wikipedia pattern): ක්‍ය්‍ර `U+0D9A U+0DCA U+200D U+0DBA U+0DCA U+200D U+0DBB` (rare; pattern only)
  - rēpaya + consonant + yansaya: ර්‍ක්‍ය `U+0DBB U+0DCA U+200D U+0D9A U+0DCA U+200D U+0DBA` (pattern only)
  - vowel signs come last: ක්‍රෝ `U+0D9A U+0DCA U+200D U+0DBB U+0DDD`, ප්‍රේ `U+0DB4 U+0DCA U+200D U+0DBB U+0DDA`
  - The kombuva (ෙ) is a *pre-base* glyph. It is still encoded after the whole cluster.
- **Confidence:** high.
- **Sources:** S3 §5.6–5.8, S5, S15.

### HC-024: Rakāransaya + u / uu: special shapes, normal encoding
- **Statement:** After a rakāransaya, the u and uu vowel signs take alternative shapes that look like the æ/ǣ signs. Unicode says they must be encoded as U+0DD4/U+0DD6, **not** as U+0DD0/U+0DD1.
- **Examples:** ක්‍රු `U+0D9A U+0DCA U+200D U+0DBB U+0DD4`, ක්‍රූර *krūra* `U+0D9A U+0DCA U+200D U+0DBB U+0DD6 U+0DBB`. Wrong (but attested): ක්‍රෑර `U+0D9A U+0DCA U+200D U+0DBB U+0DD1 U+0DBB`. S13 found corpus words where ැ/ෑ were used for /u, uː/. S13 printed its examples in a legacy font, so they are garbled. They are most likely ශ්‍රැති-type and ක්‍රෑර-type spellings.
- **Also:** Bases shaped like ද lose their tail before a below-base sign. ද්‍ර looks different from ක්‍ර, but the encoding is unaffected (S1).
- **Usage and rendering (02:VS-035):** in practice /Cru/ and /Cruː/ are mostly written C + ෘ/ෲ (කෲර 1,667 vs ක්‍රූර 22 vs ක්‍රෑර 186 in the NLPC 2.1M-word list). Several fonts, including the Windows system fonts Nirmala UI and Iskoola Pota, do not draw the special shape and attach an ordinary ු/ූ below the cluster.
- **Applies-to:** ra (rakāransaya), u, uu, ae, aee.
- **Confidence:** high (S1); medium for the corpus interpretation.
- **Sources:** S1, S13, S3 §6.3 note.

---

## 5. Ligated conjuncts (bændi akuru) and touching letters (sparśa akuru)

### HC-030: Ligated conjuncts are optional and mostly classical
- **Statement:** Apart from yansaya and rakāransaya, Sinhala has no strict obligatory ligatures in modern writing. Harshula describes modern orthography as "separate letters" (S12). Wiles calls bændi akuru "optional", with few in common modern use (S19). Encoding: `C1 ් ZWJ C2`.
- **Classification (S8):**
  - Conjuncts still met today: ක්‍ෂ, ක්‍ව, න්‍ද, න්‍ධ, න්‍ථ, ත්‍ථ (the S8 PDF lost its glyphs; the names are given as kSa, kva, nda, ndha, ntha, ttha).
  - Not used in contemporary writing: ද්‍ධ, ද්‍ව, ට්‍ඨ, ඤ්‍ච.
- **Examples:** අක්‍ෂරය `U+0D85 U+0D9A U+0DCA U+200D U+0DC2 U+0DBB U+0DBA` vs අක්ෂරය `U+0D85 U+0D9A U+0DCA U+0DC2 U+0DBB U+0DBA`; බුද්‍ධ `U+0DB6 U+0DD4 U+0DAF U+0DCA U+200D U+0DB0` vs බුද්ධ `U+0DB6 U+0DD4 U+0DAF U+0DCA U+0DB0`; ආනන්‍ද `U+0D86 U+0DB1 U+0DB1 U+0DCA U+200D U+0DAF`.
- **Confidence:** high that they are optional; medium for the exact "still used" list.
- **Sources:** S1 (Table 13-4), S8, S12, S19, S17.

### HC-031: Touching letters are for Pali/classical text only
- **Statement:** Touching letters show a pure consonant drawn against the next letter instead of with a hal. Encoding: `C1 ZWJ ් C2`. They are used in old Sinhala and are frequent in Pali, but not in contemporary Sinhala (S8, S5, S19).
  - Typical pairs (S8): kka, kkha, gga, ccha, jja, jjha, ṭṭha, ppha, mma, and others.
  - SLS 1134 Part 2 makes touching letters required only at font compliance Level 3. As of 2009 no Level 3 font was known (S11, S18).
- **Examples:** ධම‍්ම *dhamma* `U+0DB0 U+0DB8 U+200D U+0DCA U+0DB8`; බුද‍්ධ `U+0DB6 U+0DD4 U+0DAF U+200D U+0DCA U+0DB0`.
- **Confidence:** high.
- **Sources:** S1, S5, S8, S11, S18, S19.

### HC-032: ක්ෂ vs ක්‍ෂ
- **Statement:** Both are valid encodings of the same cluster *kṣ*:
  - ක්ෂ (hal visible) `U+0D9A U+0DCA U+0DC2` is the modern "separate letters" spelling;
  - ක්‍ෂ `U+0D9A U+0DCA U+200D U+0DC2` is the traditional ligature.
  
  The S16 teaching note mixes the two: රක්ෂණය next to නිරීක්‍ෂණ, අක්‍ෂර. Sinhala text in the wild uses both. A search or spell-check must treat them as equivalent.
- **Spelling rule (not encoding):** *kṣ* is spelled with ෂ (ssa), not ශ or ස, e.g. අක්‍ෂර, ලක්‍ෂ (S22, S16).
- **Confidence:** high.
- **Sources:** S1, S8, S16, S22.

### HC-033: `ර ් ZWJ ය`: rēpaya + ya, never ra + yansaya
- **Statement:** SLS 1134 (Table 3 note, in both the 2004 draft and the 2011 revision as quoted by S9) says yansaya is not used after ර. It gives a ra+yansaya spelling of *kārya* as an example of incorrect spelling. So `ර ් ZWJ ය` means rēpaya over ය.
- **Accepted spellings of *kārya*** (S8):
  - the traditional කාර්‍ය්‍ය: an extra ය is inserted, carrying both the rēpaya and a yansaya. `U+0D9A U+0DCF U+0DBB U+0DCA U+200D U+0DBA U+0DCA U+200D U+0DBA`. This is also the SLSI 2004 decision #3 (S4) and Microsoft's abvs example ර්‍ය්‍ය (S5).
  - the contemporary කාර්‍ය (rēpaya + ya, no yansaya), "also accepted" `U+0D9A U+0DCF U+0DBB U+0DCA U+200D U+0DBA`
  - කාර්ය (no rēpaya, no yansaya) `U+0D9A U+0DCF U+0DBB U+0DCA U+0DBA`, used by "those who do not follow the above writing system"
- **Conflict:** The 2004 draft (S3 §5.7) encoded "yansaya with repaya" as `U+0DBB U+0DCA U+200D U+200C U+0DCA U+200D U+0DBA` (with ZWNJ). The SLSI decisions (S4) replaced this with `U+0DBB U+0DCA U+200D U+0DBA U+0DCA U+200D U+0DBA`. Fonts vary in how they render `ර ් ZWJ ය` (S9).
- **Same family:** සූර්‍ය, ආර්‍ය, ධෛර්‍ය, ආශ්චර්‍ය, ආචාර්‍ය. Their older spellings take the doubled ය්‍ය form **[spellings of individual words UNVERIFIED]**.
- **Applies-to:** ra, ya, hal.
- **Confidence:** high on the rule; medium on which modern variant is preferred.
- **Sources:** S3, S4, S5, S8, S9.

### HC-034: `ර ් ZWJ ර`
- **Statement:** The same ambiguity exists for ra + rakāransaya vs rēpaya + ra (S9). It is very rare in real words **[no attested word found]**. Treat it as rēpaya + ra by analogy with HC-033.
- **Confidence:** low.
- **Sources:** S9.

---

## 6. Clusters: native vs loan, geminates, triples

### HC-040: Native Sinhala syllables are (C)V(C); clusters come from Sanskrit/Pali/English
- **Statement:** Native words are limited to (C)V(C), V̄ and CV̄(C) syllables, with only marginal CC (S14). Native words have:
  - no initial clusters;
  - medial clusters only as coda + onset across a syllable boundary (mostly geminates and nasal + stop).
  
  Initial clusters (ප්‍ර-, ක්‍ර-, ශ්‍ර-, ස්ව-, ද්ව-, ත්‍ර-, ස්ථ-) belong to tatsama (Sanskrit/Pali) words and English loans (e.g. ස්ටේෂන් "station"). Uneducated speech tends to break them up (S14).
- **Examples:** ප්‍රශ්නය, ක්‍රමය, ශ්‍රී, ස්වභාවය `U+0DC3 U+0DCA U+0DC0 U+0DB7 U+0DCF U+0DC0 U+0DBA`, ද්වාරය `U+0DAF U+0DCA U+0DC0 U+0DCF U+0DBB U+0DBA`, ස්ථානය `U+0DC3 U+0DCA U+0DAE U+0DCF U+0DB1 U+0DBA`.
- **Confidence:** high (structure); medium (exact list).
- **Sources:** S14, S1, S8.

### HC-041: Initial clusters and the ZWJ they need
- **Statement:** For word-initial clusters:
  - with ර or ය as second member: always use the reduced form, i.e. ZWJ is required (HC-020/021);
  - with any other second member (ස්ව, ද්ව, ස්ථ, ස්ක, ස්ප, ශ්ව …): explicit hal, no ZWJ;
  - with ව after ක/ත/ද/න: a ligature is *possible* (ක්‍ව, ත්‍ව, ද්‍ව, න්‍ව are in Unicode Table 13-4) but optional.
- **Examples:** ස්ව `U+0DC3 U+0DCA U+0DC0` (no ZWJ); ද්වාරය vs classical ද්‍වාරය `U+0DAF U+0DCA U+200D U+0DC0 U+0DCF U+0DBB U+0DBA`.
- **Confidence:** high.
- **Sources:** S1, S3, S8.

### HC-042: Geminates are written `C ් C` (no ZWJ)
- **Statement:** Doubled consonants are written with an explicit hal on the first copy. They are very common in native words: අම්මා, අක්කා, පත්තරය, බල්ලා, කරන්න. Use touching (`ZWJ ්`) only for Pali.
  - Not all letters geminate. The exceptions are the prenasalized letters, ඞ (/ŋ/), ෆ, හ and ශ (S14).
  - Where morphology would geminate හ, the result is ස්ස (S14).
  - Prenasalized letters revert to nasal + stop: ඳ → න්ද.
- **Examples:** අම්මා `U+0D85 U+0DB8 U+0DCA U+0DB8 U+0DCF`; අක්කා `U+0D85 U+0D9A U+0DCA U+0D9A U+0DCF`; පත්තරය `U+0DB4 U+0DAD U+0DCA U+0DAD U+0DBB U+0DBA`; බල්ලා `U+0DB6 U+0DBD U+0DCA U+0DBD U+0DCF`; කණ්ණාඩිය `U+0D9A U+0DAB U+0DCA U+0DAB U+0DCF U+0DA9 U+0DD2 U+0DBA`.
- **Applies-to:** ka ga ca ja tta dda nna ta da na pa ba ma ya la va sa. Not lla: ළ්ළ is not used (HC-014).
- **Confidence:** high.
- **Sources:** S14, S13, S8.

### HC-043: තත්ත්වය vs තත්වය (and සත්ත්ව vs සත්ව)
- **Statement:** The Sanskrit abstract suffix *-tva* is added to stems ending in *-t* (tat, sat). The prescriptive rule (S16) keeps both t's in tatsama words: තත්ත්වය `U+0DAD U+0DAD U+0DCA U+0DAD U+0DCA U+0DC0 U+0DBA`, සත්ත්වයා `U+0DC3 U+0DAD U+0DCA U+0DAD U+0DCA U+0DC0 U+0DBA U+0DCF`, තත්ත්වඥ. The reduced spellings තත්වය `U+0DAD U+0DAD U+0DCA U+0DC0 U+0DBA` and සත්වයා are common in contemporary writing and journalism.
- **Note:** The ත්ව part may also be drawn as the ligature ත්‍ව `U+0DAD U+0DCA U+200D U+0DC0` (Unicode Table 13-4). That gives a third and fourth spelling (තත්ත්‍වය). Treat all as equivalent for search.
- **Confidence:** medium. S16 is a teaching note, not an official decree. I could not find an Official Languages Department or NIE ruling online.
- **Sources:** S16; Wiktionary lists Sanskrit तत्त्व as තත්ත්ව (lead only).

### HC-044: Triple (and longer) clusters
- **Statement:** These occur only in tatsama words. Each joining point is encoded independently: ZWJ only where a reduced form or ligature is wanted, plain hal elsewhere.
- **Examples:**
  - ස්ත්‍රී *strī* `U+0DC3 U+0DCA U+0DAD U+0DCA U+200D U+0DBB U+0DD3` (s-hal, t + rakāransaya)
  - රාෂ්ට්‍ර *rāṣṭra* `U+0DBB U+0DCF U+0DC2 U+0DCA U+0DA7 U+0DCA U+200D U+0DBB`
  - ක්‍ෂේත්‍ර *kṣetra*: ligature form `U+0D9A U+0DCA U+200D U+0DC2 U+0DDA U+0DAD U+0DCA U+200D U+0DBB`; hal form `U+0D9A U+0DCA U+0DC2 U+0DDA U+0DAD U+0DCA U+200D U+0DBB`
  - ශාස්ත්‍ර `U+0DC1 U+0DCF U+0DC3 U+0DCA U+0DAD U+0DCA U+200D U+0DBB`
  - ඉන්ද්‍රිය `U+0D89 U+0DB1 U+0DCA U+0DAF U+0DCA U+200D U+0DBB U+0DD2 U+0DBA`
  - මන්ත්‍ර `U+0DB8 U+0DB1 U+0DCA U+0DAD U+0DCA U+200D U+0DBB`
  - ලක්‍ෂ්‍ය *lakṣya* `U+0DBD U+0D9A U+0DCA U+200D U+0DC2 U+0DCA U+200D U+0DBA`
  - මත්ස්‍ය *matsya* `U+0DB8 U+0DAD U+0DCA U+0DC3 U+0DCA U+200D U+0DBA`
  - චන්ද්‍ර `U+0DA0 U+0DB1 U+0DCA U+0DAF U+0DCA U+200D U+0DBB`
- **Confidence:** high for the encoding; high for the words (common vocabulary).
- **Sources:** S1, S3 §5.8.

---

## 7. Special cases

### HC-050: ශ්‍රී
- **Statement:** *śrī* is ශ + hal + ZWJ + ර + ී: `U+0DC1 U+0DCA U+200D U+0DBB U+0DD3`. Without ZWJ, ශ්රී `U+0DC1 U+0DCA U+0DBB U+0DD3` shows a visible hal. That is "not conventional", but programmers often accept it (S20). Both are in wide circulation, so search must fold them together.
- **Confidence:** high.
- **Sources:** S20, S1.

### HC-051: ජ්ඤ / ඥ
- **Statement:** The conjunct *j + ñ* is atomically encoded as ඥ U+0DA5 (S1). It should not be built from ජ ් ZWJ ඤ.
  - **Pronunciation:** ඤ and ඥ sound the same only word-initially (ඤාණ / ඥාන). Elsewhere ඥ behaves as two consonant sounds, e.g. ප්‍රඥා (S3 §3.2 note 2).
  - **Script status:** S8 says the ඥ glyph is considered to represent j + ñ, and that it is a regular letter of contemporary Sinhala.
- **Examples:** ඥානය `U+0DA5 U+0DCF U+0DB1 U+0DBA`, ප්‍රඥාව `U+0DB4 U+0DCA U+200D U+0DBB U+0DA5 U+0DCF U+0DC0`, විඥාන `U+0DC0 U+0DD2 U+0DA5 U+0DCF U+0DB1`.
- **Applies-to:** jnya, ja, nya.
- **Confidence:** high.
- **Sources:** S1, S3, S8.

### HC-052: Rakāransaya after ම / න / ල
- **Statement:** Nothing in Unicode, SLS or the shaping specs restricts which consonant may take a rakāransaya. Any `C ් ZWJ ර` is valid encoding, and fonts draw the generic below-base form.
  - ම්‍ර occurs in Sanskrit tatsama words such as තාම්‍ර "copper" and ආම්‍ර "mango" **[UNVERIFIED in a Sinhala source this session]**.
  - න්‍ර and ල්‍ර: I found no attested Sinhala word.
  - **In running text, ම න ල + ර is written with plain hal.** Where ම න ල meets ර there is usually a morpheme or syllable boundary: දුම් + රිය "train", හෙන්රි "Henry", ඉම්රාන්, දිල්රුක්ෂි. In S25 every ම්ර is written without ZWJ, while the same pages write ප්‍ර ත්‍ර ක්‍ර with ZWJ (78 times). A ZWJ would draw a rakāransaya under ම, a form readers do not use for these words.
  - So the general rule of HC-021 (C + ර takes ZWJ) holds within a syllable. After ම න ල the plain form is the norm, and ම්‍ර is kept for a deliberately classical style.
- **Confidence:** medium (encoding high; usage from one source).
- **Sources:** S1, S3, S5, S17, S25.

### HC-053: ඤ්‍ච / ඤ්‍ජ (pañca, vyañjana)
- **Statement:**
  - Noto has a ligature glyph for ඤ්‍ච (`nya_ca`), and S8 lists "njca" among obsolete conjuncts. Modern spelling uses hal: පඤ්ච `U+0DB4 U+0DA4 U+0DCA U+0DA0`, ව්‍යඤ්ජන `U+0DC0 U+0DCA U+200D U+0DBA U+0DA4 U+0DCA U+0DA2 U+0DB1`.
  - ඤ්‍ජ as a dedicated ligature is **[UNVERIFIED]**.
  - Do not confuse either with ඦ (nyja), the archaic prenasalized letter that never takes hal.
- **Confidence:** medium.
- **Sources:** S8, S17, S3.

### HC-054: ර් before ය / ර inside words
- **Statement:** See HC-033 and HC-034. When a romanized `r` + `y` follows a vowel, there are three possible Sinhala spellings:
  - rēpaya + ya (`ර ් ZWJ ය`);
  - explicit hal (`ර ් ය`);
  - the traditional doubled form (`ර ් ZWJ ය ් ZWJ ය`).
  
  ra + yansaya is never a valid choice.
- **Confidence:** high.
- **Sources:** S3, S8, S9.

---

## 8. What SLS 1134 specifies for stored text

### HC-060: Internal representation (stored sequences)
- **Statement:** SLS 1134 (§5) fixes the stored sequences, and conforming text must use them:
  - pure consonant = `C ්`;
  - rakāransaya/yansaya = `C ් ZWJ ර/ය`;
  - rēpaya = `ර ් ZWJ C`;
  - other conjuncts = `C ් ZWJ C`;
  - touching = `C ZWJ ් C` (2011);
  - composite vowel signs: use the single precomposed sign. For example, කෝ is ක + ෝ (U+0DDD), not ක + ෙ + ා + ්. Sequences of separate signs are "discouraged" (S3 §5.4 note 2).
- **Confidence:** high.
- **Sources:** S3, S1, S10.

### HC-062: Font compliance levels (SLS 1134 Part 2:2007)
- **Statement:** There are three font levels.
  - Level 1 = full repertoire minus ඏ ඐ ෟ ෳ ෴.
  - Touching letters are required only at Level 3.
  
  Text containing touching sequences will therefore look broken on most systems.
- **Confidence:** medium (secondary quotes).
- **Sources:** S18, S11.

---

## 9. Complete table of known conjunct / reduced / touching forms

Legend:
- **Status:** M = mandatory in correct modern spelling; O = optional (both forms accepted); C = classical/Pali only (rare today); P = productive pattern (any consonant).
- **Src:** U = Unicode Table 13-3/13-4; N = present in Noto Sans Sinhala; I = ICANN LGR; W = si.wikipedia; S = SLS 1134; MS = Microsoft spec.
- Letter IDs are those used throughout this repository.

### 9a. Reduced forms (productive)

| Form | Letters | Status | Sequence | Example | Src |
|---|---|---|---|---|---|
| ක්‍ය (yansaya) | C + hal + ya | M | `U+0D9A U+0DCA U+200D U+0DBA` | වාක්‍ය | U S MS I |
| ක්‍ර (rakāransaya) | C + hal + ra | M | `U+0D9A U+0DCA U+200D U+0DBB` | ක්‍රමය | U S MS I |
| ර්‍ක (rēpaya) | ra + hal + C | O | `U+0DBB U+0DCA U+200D U+0D9A` | තර්‍කය | U S MS I |
| ර්‍ය්‍ය (rēpaya+ya+yansaya) | ra ya ya | O (traditional) | `U+0DBB U+0DCA U+200D U+0DBA U+0DCA U+200D U+0DBA` | කාර්‍ය්‍ය | S(2004 WG) MS I |
| conjunct + rakāransaya | e.g. na da ra | M for the -r | `U+0DB1 U+0DCA U+200D U+0DAF U+0DCA U+200D U+0DBB` | චන්ද්‍ර (lig.) | S |
| ස්ත්‍ර (hal + rakāransaya) | sa ta ra | M for the -r | `U+0DC3 U+0DCA U+0DAD U+0DCA U+200D U+0DBB` | ස්ත්‍රී | - |

### 9b. Ligated conjuncts (`C1 ් ZWJ C2`): all optional

| Form | IDs | Status | Sequence | Example word | Src |
|---|---|---|---|---|---|
| ක්‍ෂ | ka+ssa | O (still common) | `U+0D9A U+0DCA U+200D U+0DC2` | අක්‍ෂරය, ලක්‍ෂ | U N I W |
| ක්‍ව | ka+va | O | `U+0D9A U+0DCA U+200D U+0DC0` | පක්‍ව | U N I W MS |
| ග්‍ධ | ga+dha | O / C | `U+0D9C U+0DCA U+200D U+0DB0` | දුග්‍ධ, මුග්‍ධ | U N |
| ට්‍ඨ | tta+ttha | C (not contemporary per I) | `U+0DA7 U+0DCA U+200D U+0DA8` | අට්‍ඨකථා (Pali) | U N I |
| ත්‍ථ | ta+tha | O / C | `U+0DAD U+0DCA U+200D U+0DAE` | (Pali) අත්‍ථ | U N I W |
| ත්‍ව | ta+va | O | `U+0DAD U+0DCA U+200D U+0DC0` | සත්‍ව, මහත්‍වය | U N W |
| ද්‍ධ | da+dha | C (not contemporary per I) | `U+0DAF U+0DCA U+200D U+0DB0` | බුද්‍ධ | U N I |
| ද්‍ව | da+va | C (not contemporary per I) | `U+0DAF U+0DCA U+200D U+0DC0` | ද්‍විත්ව | U N I |
| න්‍ථ | na+tha | O | `U+0DB1 U+0DCA U+200D U+0DAE` | ග්‍රන්‍ථ | U N I |
| න්‍ද | na+da | O | `U+0DB1 U+0DCA U+200D U+0DAF` | ආනන්‍ද, චන්‍ද්‍ර | U N I W |
| න්‍ධ | na+dha | O | `U+0DB1 U+0DCA U+200D U+0DB0` | සන්‍ධි, බන්‍ධන | U N I W |
| න්‍ව | na+va | O | `U+0DB1 U+0DCA U+200D U+0DC0` | අන්‍වය | U N |
| ඤ්‍ච | nya+ca | C (not contemporary per I) | `U+0DA4 U+0DCA U+200D U+0DA0` | පඤ්‍ච | N I |
| ඥ | ja+nya | M (atomic letter U+0DA5) | `U+0DA5` | ඥානය | U I |
| ඳ්‍ඨ, ඳ්‍ධ, ඳ්‍ව | nda+… | doubtful | `U+0DB3 U+0DCA U+200D U+0DB0` | - | W only (conflicts with I) |

### 9c. Touching letters (`C1 ZWJ ් C2`): Pali/classical, productive

| Form | IDs | Sequence | Note | Src |
|---|---|---|---|---|
| ක‍්ක | ka+ka | `U+0D9A U+200D U+0DCA U+0D9A` | MS example | MS I |
| ක‍්ඛ | ka+kha | `U+0D9A U+200D U+0DCA U+0D9B` | | I |
| ග‍්ග | ga+ga | `U+0D9C U+200D U+0DCA U+0D9C` | | I |
| ච‍්ඡ | ca+cha | `U+0DA0 U+200D U+0DCA U+0DA1` | | I |
| ජ‍්ජ | ja+ja | `U+0DA2 U+200D U+0DCA U+0DA2` | | I |
| ජ‍්ඣ | ja+jha | `U+0DA2 U+200D U+0DCA U+0DA3` | | I |
| ට‍්ඨ | tta+ttha | `U+0DA7 U+200D U+0DCA U+0DA8` | | I |
| ප‍්ඵ | pa+pha | `U+0DB4 U+200D U+0DCA U+0DB5` | | I |
| ම‍්ම | ma+ma | `U+0DB8 U+200D U+0DCA U+0DB8` | dhamma | W I |
| ද‍්ධ | da+dha | `U+0DAF U+200D U+0DCA U+0DB0` | Unicode example | U |
| any C1 + C2 | - | `C1 U+200D U+0DCA C2` | Unicode: "productive" | U |

---

## 10. Implications for romanization and transliteration

These points apply to anyone converting between a Latin-script romanization and Sinhala script,
or validating and searching stored Sinhala text.

1. **Every vowel-less consonant carries hal.** A romanized consonant followed by another consonant or a word boundary corresponds to `C + ්`. Hal is never inferred from schwa: `a` and `ə`/`e`-for-schwa both mean "no sign" (HC-010, HC-011).
2. **C + r and C + y take ZWJ.** `C + r` / `C + y` correspond to `C ් ZWJ ර/ය` (rakāransaya/yansaya). It is the only accepted modern spelling (HC-020, HC-021). Exception: after ර, `ry` never means ra + yansaya (HC-033).
3. **Rēpaya is a style choice, not grammar.** `rC` can correspond to `ර් C` (hal) or `ර ් ZWJ C` (rēpaya); both are correct. A converter should document which it produces; rēpaya matches the traditional printed form. ර්ය also has a plain-hal option (HC-022, HC-033).
4. **Ligated conjuncts are optional.** Whether *kṣ* is rendered ක්ෂ or ක්‍ෂ is a style decision, because both are common (HC-032). All other bændi akuru (ද්‍ධ, න්‍ද, ත්‍ව …) are classical: plain hal is the modern spelling, with ZWJ only for a deliberately classical style (HC-030).
5. **Touching letters belong to Pali/classical text.** They are encoded `C ZWJ ්`, and most fonts below SLS Level 3 render them poorly (HC-031, HC-062).
6. **ඥ needs its own romanization** (e.g. `GN`/`jny`). It is never composed as `ජ ් ZWJ ඤ` (HC-051).
7. **Geminates:** a doubled consonant (`amma`, `akka`, `paththaraya`) → `C ් C`, no ZWJ (HC-042). For *-tva* words both තත්ත්වය and තත්වය occur; the prescriptive form is තත්ත්වය (HC-043).
8. **Prenasalized letters and ළ cannot take hal.** Romanized `nd` + consonant resolves to න්ද… (dental n + hal), not ඳ් (HC-014).
9. **Word-final nasal ambiguity:** final `ng` could be ං, න් or ම් (HC-012). Resolving it needs a dictionary, not a fixed rule.
10. **Vowel on clusters goes on the last consonant.** `kre` → ක්‍රෙ (ක ් ZWJ ර ෙ). `kyoo` → ක්‍යෝ. Use the precomposed vowel sign (ෝ U+0DDD etc.), never a split sequence (HC-060).
11. **`kru`/`kruu` written with rakāransaya use ු/ූ (U+0DD4/U+0DD6)**, even though the glyph looks like ැ/ෑ (HC-024). The more common spelling is C + ෘ/ෲ (කෘ, කෲ; 02:VS-035).
12. **Normalisation/search:** fold `C ් ZWJ C`, `C ් C` and `C ZWJ ් C` together for matching. Writers and data sources mix them (ශ්‍රී/ශ්රී, අක්‍ෂර/අක්ෂර). Never strip ZWJ from stored or converted text. IDNA permits ZWJ after a virama (S24), but the root-zone LGR excludes it (S8).
13. **ZWNJ does not belong in normal text** (HC-005).
14. **Writing order vs storage order.** A romanization is naturally in logical order. For rēpaya, `r` comes first and the stored form is `ර ් ZWJ` before the base consonant, which is already logical order, even though the rēpaya is drawn above the following consonant (HC-022).

---

## 11. Open questions / conflicting sources

1. **Touching-letter encoding history.** The 2004 *draft* SLS used `් ZWJ` for both conjuncts and touching letters. The SLSI June 2004 minutes left the joiner undecided (ZWNJ or ZWJ+ZWNJ+ZWJ). Unicode, Microsoft and (per Harshula) SLS 1134:2011 use `ZWJ ්`. The final SLS 1134:2004 and 2011 texts were not available to verify first-hand. (S3, S4, S10)
2. **Yansaya-with-rēpaya encoding.** Three candidates:
   - draft SLS: `ර ් ZWJ ZWNJ ් ZWJ ය`
   - SLSI WG 2004: `ර ් ZWJ ය ් ZWJ ය`
   - modern simplified: `ර ් ZWJ ය` (rēpaya on ya)
   
   Fonts render `ර ් ZWJ ය` inconsistently (S9). Which does SLS 1134:2011 mandate? Unverified.
3. **Standalone signs:** ZWNJ-based (2004 draft) vs SPACE-based (SLSI WG 2004 decision). Irrelevant for running text, but matters for documentation that shows a sign on its own.
4. **ඳ + hal conjuncts** (ඳ්‍ධ etc.) appear in si.wikipedia (S15). ICANN (S8) says sannaka letters never take hal. S15 is likely wrong or archaic.
5. **Which ligatures count as "still used".** ICANN puts ක්‍ෂ, ක්‍ව, න්‍ද, න්‍ධ, න්‍ථ, ත්‍ථ in current use, but its text is garbled in the PDF. Harshula says modern writing has *no* strict ligation except r/y forms. I found no corpus frequency data.
6. **ක්ෂ vs ක්‍ෂ preference** in current NIE textbooks: unknown. The S16 notes use both.
7. **තත්ත්වය vs තත්වය:** I found only a teaching note (S16) supporting the double-t form. No official ruling (Official Languages Dept / NIE "Sinhala Lekhana Rithiya", 1989) could be fetched.
8. **Word-final න්/ම් → [ŋ]** (S14) is one lead source. Not checked against Gair/Karunatillake.
9. **ම්‍ර, න්‍ර, ල්‍ර** attestations not verified. Plain ම්ර / න්ර is attested (HC-052); a corpus count of ම්‍ර would show whether any word needs the joined form.
10. **SLS Table 3 count:** it says "7" yansaya combinations but lists 8. It also omits u/uu with rakāransaya, while Unicode shows ක්‍රු/ක්‍රූ shapes. This may be an editorial slip in the draft.
11. **"Sinhala Lekhana Rithiya" (NIE 1989)** is cited by S8 as the alphabet source. It was not accessed and is likely the best source for school-level hal/conjunct rules.
12. **Corpus evidence of wrong encodings** (ැ/ෑ for u/uu after rakāransaya). S13's examples are in a garbled legacy font, so the exact words are inferred.
13. **Removed rules:** HC-025, HC-061, removed: out of scope.
