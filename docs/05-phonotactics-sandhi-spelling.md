# 05 — Phonotactics, Spelling Conventions and Sandhi

Scope: **which letter sequences are valid in written Sinhala, and why**. The file covers syllable structure and positional restrictions, sandhi (the spelling changes when morphemes join), letter-to-sound rules (when written inherent *a* is pronounced [ə]), prescriptive spelling rules and their controversies, loanword conventions, and punctuation, spacing and numbers. Unicode encoding details and the full letter inventory are covered elsewhere in this repository. A closing section draws out the consequences for romanization and transliteration.

Compiled October 2026.

## Conventions used in this file

| Item | Convention |
|---|---|
| Rule IDs | `PH-0xx` phonotactics, `SN-0xx` sandhi, `G2P-0xx` letter-to-sound, `SP-0xx` spelling conventions, `LW-0xx` loanwords, `TY-0xx` typography / punctuation / numbers |
| Letter IDs | Letter IDs (used throughout this repository): consonants `ka kha ga gha nga nnga(ඟ) ca cha ja jha nya(ඤ) jnya(ඥ) nyja(ඦ) tta ttha dda ddha nna nndda(ඬ) ta tha da dha na nda(ඳ) pa pha ba bha ma mba(ඹ) ya ra la va sha(ශ) ssa(ෂ) sa ha lla(ළ) fa`; vowels `a aa ae aee i ii u uu ru ruu ilu iluu e ee ai o oo au`; `hal`. Extra IDs used here: `anusvara` (ං), `visarga` (ඃ), `ZWJ` (U+200D). **Note:** `nga` = ඞ (the velar nasal letter), `nnga` = ඟ (prenasalized g). |
| Romanization | Mostly a loose ISO 15919-style form. `ə` = schwa, `æ` = ඇ, `ŋ` = velar nasal, `ṇ` = ණ, `ḷ` = ළ, `ṣ` = ෂ, `ś` = ශ, `ⁿd`/`ᵐb`/`ⁿḍ`/`ᵑg` = prenasalized stops. `/.../` is phonemic. |
| Confidence | **high**: two or more independent sources, or one authoritative source plus general agreement. **medium**: one source, or a source that was hard to read (garbled PDF), or widely known but not verified online. **low**: inference or unverified. |
| `[UNVERIFIED]` | No online source confirmed it in this session. It comes from general knowledge of Sinhala grammar and needs checking against a print grammar (NIE textbook, Disanayaka, Karunatillake). |

### Key sources (short names used below)

| Short name | Source |
|---|---|
| **WWG-G2P 2006** | Wasala, Weerasinghe & Gamage, "Sinhala Grapheme-to-Phoneme Conversion and Rules for Schwa Epenthesis", COLING/ACL 2006 Poster — https://aclanthology.org/P06-2114.pdf |
| **WWG-SYL 2005** | Weerasinghe, Wasala & Gamage, "A Rule Based Syllabification Algorithm for Sinhala", IJCNLP 2005 — https://aclanthology.org/I05-1039.pdf |
| **WASALA-SPELL 2010** | Wasala, Weerasinghe, Pushpananda, Liyanage & Jayalatharachchi, "A Data-Driven Approach to Checking and Correcting Spelling Errors in Sinhala", ICTer 3(1) 2010 — https://distantreader.org/stacks/journals/icter/icter-72.pdf. Appendix A gives prescriptive ණ/න, ළ/ල, ෂ/ශ rules drawn from Disanayaka (2007) and others. **The PDF's Sinhala text extracts with a legacy-font mapping error**, so examples were reconstructed (e.g. extracted `ශ` is really ළ and `඿` is really ස). |
| **SINSPELL 2021** | Liyanapathirana, Gunasinghe & Dias, "SinSpell: A Comprehensive Spelling Checker for Sinhala" — https://arxiv.org/abs/2107.02983 |
| **SI-WP-SANDHI** | Sinhala Wikipedia, සිංහල සන්ධි — https://si.wikipedia.org/wiki/සිංහල_සන්ධි, and සන්ධි — https://si.wikipedia.org/wiki/සන්ධි |
| **PIRIVEN-SANDHI** | Piriven Sinhala Piyasa, "සන්ධි 10 සරලව" — http://piriven.blogspot.com/2021/05/10.html (education blog; matches the school syllabus list of 10 sandhi) |
| **SI-WP-AV** | Sinhala Wikipedia, සිංහල අක්ෂර වින්‍යාසය — https://si.wikipedia.org/wiki/සිංහල_අක්ෂර_වින්‍යාසය |
| **LETSLEARN** | "අපි නිවරදිව සිංහල ලියමු - අක්ෂර වින්‍යාසය" — http://letslearnsinhala.blogspot.com/2012/03/blog-post.html |
| **EN-WP-SIN** | English Wikipedia, Sinhala language (phonology section) — https://en.wikipedia.org/wiki/Sinhala_language and https://en.wikipedia.org/wiki/Sinhala_phonology (lead only) |
| **EN-WP-SCRIPT** | English Wikipedia, Sinhala script — https://en.wikipedia.org/wiki/Sinhala_script |
| **ZYGIS 2010** | Żygis, "Typology of Consonantal Insertions", ZASPiL 52 (cites Smith 2001 for Sinhala) — https://zaspil.leibniz-zas.de/article/download/385/386 |
| **KNAB 1989** | Institute of the Estonian Language, KNAB romanization of Sinhalese — https://arhiiv.eki.ee/knab/lat/kblsi2.pdf |
| **UNICODE-ML 2016** | Unicode mailing list thread on SLS 1134 named sequences — https://unicode.org/mail-arch/unicode-ml/y2016-m10/0218.html |
| **EN-WP-LOAN** | English Wikipedia, List of Sinhala words of English origin — https://en.wikipedia.org/wiki/List_of_Sinhala_words_of_English_origin |

**Things I could not reach:** the e-Thaksalawa Grade 10 PDF "අක්ෂර හා අක්ෂර වින්‍යාසය" (https://e-thaksalawa.moe.gov.lk/moodle/pluginfile.php/10785/mod_resource/content/1/SG10_Sin_Act_Akshara_vinyasaya.pdf) redirects to a login page. No NIE textbook sandhi chapter and no Department of Official Languages spelling standard could be fetched online. Where a rule rests on these kinds of sources, it is marked `[UNVERIFIED]`.

---

## 1. Syllable structure and positional restrictions

### PH-001 — Native syllable template is (C)V(C)
- **Statement:** Native (*nishpanna*) words use only V, CV, VC and CVC syllables. Long vowels are allowed (V̄, CV̄(C)). Native words have no onset clusters.
- **Examples:** අම්මා *am.maː*; ගස් *gas*; පොත *po.tə*; මල්ලී *mal.liː*.
- **Exceptions:** Sanskrit and Pali (*tatsama/tadbhava*) and English loans allow up to (C)(C)(C)V(C)(C)(C): ප්‍රශ්නය *praś.nə.yə*; ස්ත්‍රී *strī*; ශාස්ත්‍රය.
- **Applies to:** all consonants; `hal`.
- **Confidence:** high.
- **Sources:** WWG-SYL 2005 §3.2.2–3.2.3; EN-WP-SIN.

### PH-002 — Medial clusters split as VC.CV; three-consonant clusters are split by rule
- **Statement:** In native words, a VCCV sequence syllabifies as VC.CV. In loans, C+C+r/y splits before the stop+liquid/glide part (*sam.prēk.ṣə.nə*). A C+C+C cluster whose first two members are both stops splits after the first consonant. Any other C+C+C cluster splits after the second consonant.
- **Examples:** මල්ලී *mal.liː*; සම්ප්‍රේෂණ *sam.prē.kṣa.ṇa* / *samp.rē…* (both syllabifications are acceptable); මත්ස්‍ය *mat.syə* ~ *mats.yə*.
- **Exceptions:** Some Sanskrit words with C+r clusters may be pronounced with gemination: ක්‍රමක්‍රමයෙන් *kramak.kra…*; අප්‍රමාණ *ap.pramāṇa* ~ *ap.ramāṇa*.
- **Applies to:** ra, ya (as second member); `hal`; ZWJ conjuncts.
- **Confidence:** high for the algorithm. Its relevance to spelling is indirect.
- **Sources:** WWG-SYL 2005 §3.2.3–3.2.4.

### PH-003 — Prenasalized stops never begin a word and never end a syllable
- **Statement:** ඟ ඬ ඳ ඹ (and the obsolete ඦ) occur only between vowels (intervocalically). They cannot be word-initial, cannot be word-final, cannot take `hal`, and cannot be geminated.
- **Examples:** කඳ *kaⁿdə* "trunk" vs. කන්ද *kandə* "hill" vs. කද *kadə* "shoulder-pole"; අඹ *aᵐbə*; ගඟ *gaᵑgə*; කොළඹ *koḷaᵐbə*.
- **Exceptions:** None in standard vocabulary. Before a consonant in compounds, the prenasal is replaced by ං or a hal nasal: ගඟ + වතුර → ගංවතුර; කොළඹ + තොට → කොළොම්තොට (see SN-007).
- **Applies to:** nnga, nndda, nda, mba, nyja.
- **Confidence:** high.
- **Sources:** EN-WP-SIN (prenasals are intervocalic only); WWG-SYL 2005; SI-WP-SANDHI (ගාත්‍රාක්ෂර ලෝප examples).

### PH-004 — ඞ (`nga`) and ං do not begin a word
- **Statement:** The velar nasal /ŋ/ has no word-initial occurrence. ඞ is almost never written as a free letter. /ŋ/ is written as ං (*anusvara*), which in native words occurs word-finally and before velars.
- **Examples:** ගං *gaŋ* "rivers"; අං *aŋ* "horns"; සිංහල *siŋhələ*; වාඞ්මය (rare Sanskrit spelling).
- **Exceptions:** ඞ appears in a few Sanskrit spellings such as වාඞ්මය and older සඞ්ඝ (now usually සංඝ).
- **Applies to:** nga, anusvara.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 §2.2 (citing Disanayaka 1995); EN-WP-SIN; KNAB 1989 note 1 (ං generally substitutes for ඞ).

### PH-005 — Other consonants: which ones can start a word
- **Statement:** Apart from /ŋ/ and the prenasals, all consonant letters can begin a word. Two letters need comment:
  - **ණ (`nna`)** occurs initially in a handful of words: ණය *ṇayə* "debt", plus some Sanskrit words.
  - **ළ (`lla`)** occurs initially in native words: ළමයා, ළඟ, ළිඳ, ළපටි, ළය, ළද, ළසෝ, ළහිරු. When it starts a word it never carries `hal`.
- **Examples:** see the two bullets above.
- **Exceptions:** WWG-G2P quotes Disanayaka as saying all consonants occur initially "except /ŋ/ and nasals". Since /n/ and /m/ obviously occur initially, this most likely means the *prenasalized* stops (PH-003). Reading "nasals" literally would wrongly exclude ණ-initial words.
- **Applies to:** nna, lla, nya (ඤ is very rare; ඥ-initial words are common: ඥාති, ඥානය).
- **Confidence:** high for ළ; medium for ණ (only a few words).
- **Sources:** SI-WP-AV (ළ initial list); WWG-G2P 2006 §2.2; ණය from general dictionary knowledge `[UNVERIFIED]` against the Sinhala Shabdakoshaya.

### PH-006 — Vowels: only ඎ never begins a word; ඏ ඐ are obsolete
- **Statement:** All independent vowel letters can begin a word except ඎ (*ruu*). ඌ, ඍ, ඓ, ඖ begin words only in Sanskrit loans. ඏ and ඐ (*ilu, iluu*) do not occur in contemporary Sinhala.
- **Examples:** ඍතුව *rituvə* "season"; ඍණ *riṇə* "minus"; ඓතිහාසික *aitihāsika*; ඖෂධ *auṣadha*.
- **Exceptions:** Inside a word, an independent vowel letter appears only at a compound boundary or in a place name (PH-009).
- **Applies to:** ru, ruu, ilu, iluu, ai, au.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 §2.2; EN-WP-SCRIPT; SI-WP (සිංහල හෝඩිය).

### PH-007 — Word-final position: vowel, hal consonant, or ං
- **Statement:** Written native words end in one of three ways:
  - a vowel: inherent *a* pronounced [ə] (පොත), or an explicit vowel sign (පොතේ, ගුරු);
  - a hal consonant, commonly ත් ක් ස් ල් න් ම් (පොත්, මලක්, ගස්, මල්, ගම්, කන්); ට් and ර් occur mostly in loans (කාර්, නෝට්);
  - ං: ගං, අං, ළිං.
  Prenasals never end a word.
- **Spoken note:** In speech, a word-final hal nasal (න්, ම්) is pronounced [ŋ] (EN-WP-SIN: final nasals "collapse to /ŋ/"). People who write Sinhala in Latin script by ear may write `-ng` for a written `-න්` (e.g. *minisuŋ* for මිනිසුන්).
- **Examples:** මිනිසුන් *minisun* [minisuŋ]; ගමන් *gaman* [gamaŋ]; කරනවා.
- **Exceptions:** Loans add final ෆ්, ජ්, ච් and others: ෆෝන් *fōn*, ගරාජ් *garāj*, ස්විච්. A final written *-ම්* in English loans keeps [m].
- **Applies to:** hal, anusvara, na, ma.
- **Confidence:** high (the [ŋ] realisation); medium (the exact set of native final hal consonants).
- **Sources:** EN-WP-SIN; WWG-G2P 2006 Rule #5; KNAB 1989.

### PH-008 — Gemination: intervocalic only; never with prenasals, ŋ, f, h, ś
- **Statement:** Any consonant can be doubled (C්C) between vowels except the prenasals, /ŋ/, /f/, /h/ and /ʃ/. Geminates are frequent and carry meaning: native plural vs. singular-definite forms, past tenses, and loan naturalisation.
- **Examples:** අම්මා, අක්කා, ගත්තා *gattā*, මල්ලී, ගින්න (from ගිනි), නෝට්ටුව, කෝච්චිය.
- **Exceptions:** Learned Sanskrit spellings do write ශ්ශ: නිශ්ශබ්ද, නිශ්ශංක. Here the spelling follows Sanskrit sandhi, not spoken phonotactics.
- **Applies to:** all except nnga nndda nda mba nga fa ha sha.
- **Confidence:** high (spoken rule); medium (the ශ්ශ exceptions).
- **Sources:** EN-WP-SIN; SI-WP-AV (නිශ්ශබ්ද).

### PH-009 — Vowel hiatus is avoided; VV inside a word is very rare
- **Statement:** Native words almost never contain two adjacent vowels. At a root–suffix boundary, hiatus is always repaired:
  - **Nouns** insert a glide (SN-010).
  - **Verbs** usually delete one vowel. Glide insertion is the last resort.
  An independent vowel letter after a consonant, inside one word, appears essentially only at compound or place-name boundaries.
- **Examples:** ගිරිඋල්ල *giri-ulla* (place name); රෑ + අ → රෑය *rǣyə*; තොප්පි + අ → තොප්පිය *toppiyə*.
- **Applies to:** all vowels; ya, va.
- **Confidence:** high.
- **Sources:** WWG-SYL 2005 Rule #3 (only 71 of 78,775 corpus syllables); ZYGIS 2010 (citing Smith 2001).

### PH-010 — Diphthongs are written V + ය / V + ව in native words
- **Statement:** Phonetic diphthongs [ai au ui ei æi oi iu eu æu ou] are written as a vowel followed by යි or වු. ඓ/ෛ and ඖ/ෞ are used only in Sanskrit words.
- **Examples:**
  - Native: අයියා *aiyā* [ajjaː]; ළමයි [ḷamai]; අවුරුදු [auruḍu]; හයි, කැමතියි.
  - Sanskrit: දෛනික, වෛද්‍ය, පෞද්ගලික, ඖෂධ.
- **Exceptions:** Some English loans use either form, e.g. මයික්‍රෆෝනය (EN-WP-LOAN *mayikrafōnaya*).
- **Applies to:** ai, au, ya, va, i, u.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 Table 5 (diphthong mapping /a j i/ → /ai/, /a w u/ → /au/, etc.); EN-WP-LOAN.

### PH-011 — Schwa /ə/ never starts a syllable (except in කර- forms)
- **Statement:** Phonemic /ə/ does not occur syllable-initially. The only exceptions are conjugated forms of the verb stem *kərə* "do". Word-initial /ə, əː/ occurs only in English loans, and is written with අ.
- **Examples:** කරනවා *kərənəwā*. English *urgent* → written with අ (e.g. අර්ජන්ට්) `[UNVERIFIED example]`.
- **Applies to:** a.
- **Confidence:** medium (the source text is a little garbled).
- **Sources:** WWG-G2P 2006 §2.1–2.2 (citing Karunatillake 2004).

### PH-012 — Written ර + yansaya is not allowed; *rya* uses repaya + ය
- **Statement:** SLS 1134 says yansaya is not used after ර. The sequence /rya/ is written ර්‍ය (repaya + ය), not ර්‍ය with yansaya.
- **Examples:** කාර්ය (correct per SLS 1134) — *not* කාර‍්‍ය; සූර්ය; වීර්ය; ආශ්චර්ය.
- **Exceptions:** Older printing wrote *rya* as ය්‍ය (e.g. කාය්‍ය, සූය්‍ය, ආචාය්‍ය). It is still seen in older texts. `[UNVERIFIED: historical convention, from general knowledge]`
- **Applies to:** ra, ya, ZWJ, hal.
- **Confidence:** high (SLS rule); medium (historical variant).
- **Sources:** UNICODE-ML 2016 (quoting SLS 1134:2011).

---

## 2. Sandhi (සන්ධි) — spelling changes when morphemes join

Sinhala school grammar lists **ten** native sandhi types (SI-WP-SANDHI; PIRIVEN-SANDHI). Learned vocabulary also contains Sanskrit sandhi (දීර්ඝ, ගුණ, වෘද්ධි, යණ්, visarga), which is *frozen* into the spelling of many tatsama words.

### SN-001 — ස්වර සන්ධිය (vowel joins a final hal consonant)
- **Statement:** The `hal` of the first word's final consonant is dropped, and the second word's initial vowel becomes a vowel sign on that consonant.
- **Example:** මල් + අසුන → මලසුන *mal + asuna → malasuna*.
- **Applies to:** hal; all vowels.
- **Confidence:** high.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI.

### SN-002 — පූර්වස්වර ලෝප සන්ධිය (first word's final vowel drops)
- **Examples:**
  - නැණ + ඇති → නැණැති
  - දකුණු + ඇස → දකුණැස
  - සුර + ඉඳු → සුරිඳු
  - නර + ඉඳු → නරිඳු
  - යන + එන → යනෙන
  - කර්ණ + ආභරණ → කර්ණාභරණ
  - දන්ත + ආලේප → දන්තාලේප
- **Applies to:** all vowels.
- **Confidence:** high.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI.

### SN-003 — පරස්වර ලෝප සන්ධිය (second word's initial vowel drops)
- **Examples:** ගුරු + උතුමා → ගුරුතුමා; මුනි + උතුමා → මුනිතුමා; යති + උතුමා → යතිතුමා.
- **Applies to:** u, i.
- **Confidence:** high.
- **Sources:** SI-WP-SANDHI.

### SN-004 — ස්වරාදේශ සන්ධිය (vowel substitution; mostly Sanskrit guṇa/vṛddhi)
- **Statement:** Two vowels merge into a third vowel:
  - අ/ආ + ඉ/ඊ → එ/ඒ
  - අ/ආ + උ/ඌ → ඔ/ඕ
  - අ/ආ + එ/ඓ → ඓ
  - අ/ආ + ඔ/ඖ → ඖ
- **Examples:**
  - සහ + උදර → සහෝදර
  - වට + උර → වටොර
  - දේව + ඉන්ද්‍ර → දේවේන්ද්‍ර
  - මහා + උත්සව → මහෝත්සව
  - මහා + ඖෂධ → මහෞෂධ
  - ඒක + ඒක → ඒකෛක
  - ජාතික + අභිමානය → ජාතිකාභිමානය (Wikipedia lists this under ස්වරාදේශ, though it is really a දීර්ඝ-type result)
- **Applies to:** a aa i ii u uu e ee o oo ai au.
- **Confidence:** high for the native examples; medium for the Sanskrit guṇa/vṛddhi examples (standard Sanskrit sandhi, not checked in a Sinhala textbook) `[partly UNVERIFIED]`.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI (lists අ+ඉ→එ, අ+උ→ඔ/ඕ, එ+අ→ඈ). The Sanskrit rules come from general Sanskrit sandhi (dīrgha/guṇa/vṛddhi).

### SN-005 — දීර්ඝ (savarṇa-dīrgha) sandhi in tatsama words
- **Statement:** Two like vowels merge into the long vowel: අ+අ→ආ, ඉ+ඉ→ඊ, උ+උ→ඌ.
- **Examples:** ධර්ම + අශෝක → ධර්මාශෝක; කවි + ඉන්ද්‍ර → කවීන්ද්‍ර; ගුරු + උපදේශ → ගුරූපදේශ; විද්‍යා + ආලය → විද්‍යාලය.
- **Applies to:** aa, ii, uu.
- **Confidence:** medium `[UNVERIFIED in a Sinhala textbook]`.
- **Sources:** general Sanskrit sandhi (search result summary of dīrgha sandhi).

### SN-006 — යණ් sandhi: ඉ/උ before an unlike vowel → ්‍ය / ්ව
- **Statement:** A final ඉ becomes ්‍ය (yansaya), and a final උ becomes ්ව, before a different vowel. **This is the source of most C + ්‍ය and C + ්ව clusters in learned words.**
- **Examples:**
  - ඉති + ආදි → ඉත්‍යාදි
  - අති + අන්ත → අත්‍යන්ත
  - ප්‍රති + උත්තර → ප්‍රත්‍යුත්තර
  - අනු + එෂණ → අන්වේෂණ
  - සු + ආගත → ස්වාගත
- **Applies to:** ya (yansaya), va, hal, ZWJ.
- **Confidence:** medium `[UNVERIFIED in a Sinhala textbook]`.
- **Sources:** general Sanskrit sandhi.

### SN-007 — ගාත්‍රාක්ෂර ලෝප සන්ධිය (prenasal loses its stop before a consonant)
- **Statement:** A prenasalized letter at the end of the first word sheds its stop component and becomes ං or a homorganic hal nasal.
- **Examples:** ගඟ + වතුර → ගංවතුර; කොළඹ + තොට → කොළොම්තොට (note the vowel change too).
- **Applies to:** nnga nndda nda mba nyja → anusvara / ma+hal / na+hal.
- **Confidence:** high.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI.

### SN-008 — ගාත්‍රාදේශ සන්ධිය (consonant substitution)
- **Statement:** One consonant replaces another. Common substitutions are ක → ය/ව, බ් → ප්, ද් → ත්.
- **Example:** ගිනි + කම් → ගිනියම්.
- **Applies to:** ka, ya, va, ba, pa, da, ta.
- **Confidence:** medium (one source lists the substitution set).
- **Sources:** PIRIVEN-SANDHI.

### SN-009 — පූර්වරූප / පරරූප / ද්විත්වරූප (assimilation and doubling)
- **Statement:** At the join, one consonant assimilates to the other and a geminate results.
  - *Pūrvarūpa*: the first consonant copies onto the second.
  - *Pararūpa*: the second consonant copies back onto the first.
  - *Dvitva*: the first word's final vowel drops and its consonant doubles.
- **Examples:**
  - පූර්වරූප: වත් + කම් → වත්තම්; අත් + කම් → අත්තම්; සිත් + කම් → සිත්තම්
  - පරරූප: අත් + සන → අස්සන; අත් + ලස් → අල්ලස්; ලක් + ගල → ලග්ගල
  - ද්විත්වරූප: වැදි + ආ → වැද්දා; වක් + අත්ත → වක්කත්ත
- **Applies to:** any geminable consonant (PH-008); hal.
- **Confidence:** high.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI.

### SN-010 — ආගම සන්ධිය / glide insertion (යකාරාගම, වකාරාගම)
- **Statement:** A new consonant (usually ය or ව, sometimes ර) is inserted between two vowels. In noun inflection this is automatic, and the glide depends on the root-final vowel:
  - **ය [j]** after front vowels: ඉ, ඊ, එ, ඒ, ඇ, ඈ.
  - **ව [w]** after back vowels and after ආ: උ, ඌ, ඔ, ඕ, ආ.
  - After අ, the vowel is usually *deleted* rather than separated by a glide (පොත + ඒ → පොතේ) `[UNVERIFIED generalisation]`.
- **Examples:**
  - Sandhi: පිරි + අත් → පිරියත්; කටු + අල → කටුවල; දැන් + දු → දැනුදු
  - Definite-singular nouns: රෑ + අ → රෑය *rǣyə*; තොප්පි + අ → තොප්පිය *toppiyə*; අසු + අ → අසුව *aśuwə*; මාලිගා + අ → මාලිගාව *māligāwə*
  - Others: පුටුව, හාමු → හාමුවේ, ලෝකය
- **Exceptions:** Verbs usually delete a vowel instead of inserting a glide.
- **Applies to:** ya, va, ra.
- **Confidence:** high for the y/w distribution after i/e/æ vs u/o/aa (four examples in ZYGIS plus the textbook examples); medium for the generalisation about අ.
- **Sources:** SI-WP-SANDHI; PIRIVEN-SANDHI (ආගම inserts ව, ය, ර); ZYGIS 2010 citing Smith 2001.
- **Note:** The terms "යකාරාගම / වකාරාගම" returned no web hits. They seem to be informal labels. School grammar uses "ආගම සන්ධිය".

### SN-011 — Visarga / *s*-final prefix sandhi (නිස්-, දුස්-, මනස්-) fixes ශ/ෂ/ර් spellings
- **Statement:** Sanskrit prefixes ending in *-s/-ḥ* change form according to the next sound:
  - before ක/ප → ෂ්
  - before ච/ජ → ශ්
  - before voiced sounds and vowels → ර් (නිර්-, දුර්-)
  - -අස් before voiced sounds → ඕ
- **Examples:**
  - දුස් + කර → දුෂ්කර; නිස් + පාදන → නිෂ්පාදන
  - නිස් + චල → නිශ්චල; දුස් + චරිත → දුශ්චරිත
  - නිස් + මාණ → නිර්මාණ; දුස් + වල → දුර්වල
  - මනස් + භාව → මනෝභාව; යසස් + ධරා → යශෝධරා
- **Applies to:** sha, ssa, ra+hal (repaya), oo, visarga.
- **Confidence:** medium. The resulting spellings are confirmed by SI-WP-AV (ෂ before ක/ප; ශ before ච). The derivations are `[UNVERIFIED in a Sinhala textbook]`.
- **Sources:** SI-WP-AV; LETSLEARN.

### SN-012 — *-ika* (තද්ධිත) derivation lengthens the first vowel (vṛddhi)
- **Statement:** Adding *-ika* (and similar suffixes) lengthens or strengthens the root's first vowel: අ→ආ, ඉ/එ→ඓ, උ/ඔ→ඖ.
- **Examples:** පරිසර → පාරිසරික; පුද්ගල → පෞද්ගලික; දිනය → දෛනික; ලෝකය → ලෞකික; සමාජ → සාමාජික; ඉතිහාස → ඓතිහාසික.
- **Applies to:** aa, ai, au.
- **Confidence:** high.
- **Sources:** LETSLEARN (පරිසර→පාරිසරික, පුද්ගල→පෞද්ගලික).

### SN-013 — Umlaut in verb past forms (a→æ, o→e, u→i)
- **Statement:** Some suffixes front the root vowel: අ→ඇ, ඔ→එ, උ→ඉ.
- **Examples:** බලනවා → බැලුවා; කපනවා → කැපුවා; අදිනවා → ඇද්දා; කොටනවා → කෙටුවා `[UNVERIFIED example]`.
- **Applies to:** ae, aee, e, i.
- **Confidence:** high (the process); medium (the specific forms).
- **Sources:** EN-WP-SIN (phonology lead).

### SN-014 — Noun singular/plural alternations create geminates and hal endings
- **Statement:**
  - Inanimate nouns: the plural is often the bare hal root, and the singular-definite adds *-ය/-ව/-අ*.
  - Roots ending in ඉ/උ double their last consonant in the singular.
- **Examples:** පොත් (pl) / පොත (sg); ගස් / ගස; ගිනි → ගින්න; ඇඟිලි → ඇඟිල්ල; මහලු → මහල්ලා; ලෙලි → ලෙල්ල; කකුල් / කකුල.
- **Applies to:** hal; geminates (la, na…).
- **Confidence:** high.
- **Sources:** WASALA-SPELL 2010 App. A §2.10, §4.3–4.4.

---

## 3. Letter-to-sound: when written inherent *a* is pronounced [ə]

Informal Latin-script Sinhala follows pronunciation. A word pronounced [kərənəwaː] is romanized informally as *karanawa* or *keranawa*, not *kərənəwā*. WWG-G2P 2006 starts by giving *every* unmarked consonant /ə/ (schwa is the default), then applies ordered rules that change it to /a/. These rules are what a converter from informal romanization back to Sinhala script needs to reverse.

### G2P-001 — Default: an unmarked consonant carries [ə]
- **Statement:** An unmarked consonant (no vowel sign, no `hal`, not the first member of a ZWJ conjunct) carries [ə].
- **Exceptions:** Rules G2P-002 to G2P-009 below.
- **Applies to:** a.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 §5.1.

### G2P-002 — Rule 1: first syllable has [a]
- **Statement:** The first syllable's inherent vowel is [a]. Exceptions:
  - (a) after the onset /sv/: ස්වර *svərə*;
  - (b) words beginning with /kər/, i.e. forms of the verb කර-: කරනවා *kərənəwā*;
  - (c) single-syllable CV words: ද *də*, ය *yə* (particles).
- **Examples:** ගස *gasə*; මල *malə*; පහන *pahanə*.
- **Applies to:** a.
- **Confidence:** high. This rule alone is right for 22,766 of 30,000 test words.
- **Sources:** WWG-G2P 2006 Rule #1, §6.

### G2P-003 — Rule 2: after a C+ර cluster
- **Statement:** Schwa vs [a] after *Cr* depends on what follows. Roughly:
  - before හ, or before a consonant cluster → [a]: ප්‍රහාර *prahārə*, ප්‍රශ්නය *praśnəyə*;
  - otherwise → [ə]: ප්‍රකාශ *prəkāśə*, ක්‍රමය *krəməyə*, ප්‍රති *prəti*.
- **Exceptions:** The extracted text of sub-rules 2(b)/(c) is internally contradictory (garbled). Treat the exact conditions as uncertain.
- **Applies to:** ra (rakaransaya), ha.
- **Confidence:** medium.
- **Sources:** WWG-G2P 2006 Rule #2; WASALA-SPELL (ප්‍රකාශන /prəkāśənə/).

### G2P-004 — Rule 3: [a] next to හ
- **Statement:** A schwa after V+හ becomes [a]. Read as: a vowel in {a, e, æ, o, ə}, then හ, then a schwa that becomes [a].
- **Examples:** මහත *mahatə*; පහන *pahanə*; වහල *wahalə*.
- **Applies to:** ha.
- **Confidence:** medium (the wording in the PDF is ambiguous).
- **Sources:** WWG-G2P 2006 Rule #3.

### G2P-005 — Rule 4: schwa before a consonant cluster becomes [a]
- **Examples:** බලන්න *balannə*; කරන්න *kərannə*; ප්‍රශ්නය *praśnəyə*.
- **Applies to:** hal clusters, geminates.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 Rule #4 (citing Karunatillake 2004).

### G2P-006 — Rule 5: schwa before a word-final consonant becomes [a]
- **Statement:** Schwa before a word-final (hal) consonant becomes [a], except before a final /r/, /b/ and two further consonants that are illegible in the PDF (probably retroflex stops).
- **Examples:** මලක් *malak*; ගමන් *gaman*.
- **Applies to:** hal.
- **Confidence:** medium (the exceptions are unreadable).
- **Sources:** WWG-G2P 2006 Rule #5.

### G2P-007 — Rule 6: schwa before word-final *-yi* becomes [a]
- **Statement:** The result is pronounced as the diphthong [ai].
- **Examples:** ළමයි *ḷamayi* [ḷamai]; කරයි *kərayi*.
- **Applies to:** ya, i.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 Rule #6 and Table 5.

### G2P-008 — Rule 7: /kə/ before *ru/lu* becomes /ka/
- **Examples:** කරුණාව *karuṇāwə*; කළු *kaḷu*.
- **Applies to:** ka, ra, la, lla, u.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 Rule #7.

### G2P-009 — Rule 8: the කල/කළ family reverts to [kə]
- **Statement:** In forms such as /kalaːy/, /kaleː…/ and the word /kalə/, the first [a] reverts to [ə]. This covers the verb forms කළ, කළා, කළේ *kəḷə, kəḷā, kəḷē* ("did").
- **Note:** This creates real homographs: කල *kalə* "time" vs. කළ *kəḷə* "did". In some writing both are spelled කල. The same goes for කර *karə* "shoulder" vs. *kərə* "do", and වන *vanə* vs. *vənə*.
- **Applies to:** ka, la, lla.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 Rule #8, §6.

### G2P-010 — Letters that sound the same in modern speech
- **Statement:** In modern speech these letters are pronounced identically:
  - aspirates sound like the plain consonant: ඛ=ක, ඝ=ග, ඡ=ච, ඣ=ජ, ඨ=ට, ඪ=ඩ, ථ=ත, ධ=ද, ඵ=ප, භ=බ;
  - ණ = න; ළ = ල;
  - ෂ = ශ (both [ʃ], and for many speakers ස [s] as well);
  - ඤ ≈ ඥ (ඥ is often pronounced [gɲ] / "gn").
- **Consequence:** Pronunciation, and therefore any sound-based romanization, cannot tell these letters apart. The spelling has to come from lexical knowledge.
- **Applies to:** kha gha cha jha ttha ddha tha dha pha bha nna lla ssa sha sa nya jnya.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 §2.2 (citing Karunatillake 2004); WASALA-SPELL 2010 §III-A; KNAB 1989 (ඥ [gnʲ]).

### G2P-011 — ෘ (*ru*) is usually [ru], but [ri] word-initially and [ur] in a few words
- **Statement:** The vowel sign ෘ is normally pronounced [ru]. As a word-initial independent vowel (ඍ) it is [ri]. In about 13 words it is [ur].
- **Examples:**
  - [ru]: කෘති *kruti*; පෘෂ්ඨය *pruṣṭhəyə*; උත්කෘෂ්ට *utkruṣṭə*
  - [ri] initial: ඍණ *riṇə*
  - [ur]: ප්‍රවෘත්ති *pravurtti*; සමෘද්ධි *samurddhi*; විවෘත *vivurtə*
- **Confusion risk:** Romanized *kru* can mean either කෘ or ක්‍රු. Both are read [kru], and C + ෘ/ෲ is the usual written form even where the etymology has r + u: *krūra* "cruel" is mostly written කෲර, rarely ක්‍රූර (02:VS-034). Compare කෘෂි *kruṣi*. The paper also says a few words use the ු/ූ signs where one would expect [ru]. Its examples are illegible in the PDF.
- **Applies to:** ru, ruu, ra.
- **Confidence:** high.
- **Sources:** WWG-G2P 2006 §6 (error analysis, citing Disanayaka 2000).

### G2P-012 — Short spellings of kinship words pronounced long
- **Statement:** Some words are written without ා but said with [aː]. These are informal spellings: අම්ම *ammā*, අක්ක *akkā*, ගත්ත *gattā*. The standard written forms are අම්මා, අක්කා, ගත්තා.
- **Applies to:** aa.
- **Confidence:** medium.
- **Sources:** WWG-G2P 2006 §6.

### G2P-013 — Word stress
- **Statement:** Stress falls on the first syllable (except කරනවා-type forms). Long vowels are always stressed, and an unstressed short *a* reduces to [ə]. Word-final long vowels may shorten after a heavy syllable in speech, but spelling keeps them long.
- **Applies to:** a, aa, long vowels.
- **Confidence:** medium.
- **Sources:** EN-WP-SIN.

---

## 4. Official spelling conventions and controversies

### SP-001 — Who sets the standard
- **Statement:** There is no single online statutory spelling code.
  - **De facto authorities:** NIE / Educational Publications Department school textbooks; the *Sinhala Shabdakoshaya* (Sinhala Dictionary Office); Department of Official Languages technical glossaries (පාරිභාෂික ශබ්ද මාලා), which standardise terms rather than spelling rules; SLS 1134 for encoding and rendering.
  - **Hela Havula** (Kumaratunga Munidasa, founded 1941) promotes "pure" Sinhala vocabulary and classical grammar. It prefers the śuddha (Eḷu) alphabet and native forms over Sanskrit tatsama forms. Its specific letter rules are `[UNVERIFIED]`; the English Wikipedia article gives no detail.
- **Confidence:** medium.
- **Sources:** Department of Official Languages performance reports (parliament.lk, e.g. https://www.parliament.lk/uploads/documents/paperspresented/performance-report-official-language-department-2015-si.pdf); https://en.wikipedia.org/wiki/Hela_Havula; EN-WP-SCRIPT (śuddha vs miśra).

### SP-002 — Śuddha vs miśra letters
- **Statement:**
  - **Śuddha** (native, Eḷu) letters are enough for native words: plain stops, ණ, ළ, the prenasals, ස, හ, ය, ර, ල, ව, ං.
  - **Miśra** letters are used for Sanskrit, Pali and English loans: aspirates, ශ, ෂ, ඤ, ඥ, ඞ, ඦ, ෆ, ඃ, ඍ, ඎ, ඏ, ඐ, ඓ, ඖ.
  - ඦ is essentially unused. ඥ and ෆ appear in only a modest number of words.
- **Implication:** A native-looking root rarely contains aspirates, ශ or ෂ. A word with aspirates or ශ/ෂ is a tatsama/loan.
- **Applies to:** all miśra letter IDs.
- **Confidence:** high.
- **Sources:** EN-WP-SCRIPT; SI-WP (සිංහල හෝඩිය).

### SP-003 — ණ vs න (මූර්ධජ / දන්තජ) — the "na-Ṇa-la-Ḷa" problem
- **Background:** The commonest Sinhala spelling error. Clear guidelines reportedly existed until about the 13th century and were then lost.
- **Use ණ:**
  1. after ර, ෂ, ඍ/ෘ in nouns and adjectives, including rakaransaya/repaya: තරුණ, වර්ණ, කාරණය, මරණය, දෙරණ, සරණ, ශ්‍රේණිය, ආමන්ත්‍රණ, විෂ්ණු, තෘෂ්ණා, ගවේෂණ, දක්ෂිණ;
  2. before retroflex ට ඨ ඩ ඪ: කණ්ඩ, ඝණ්ටාර, පණ්ඩිත, දණ්ඩ, චණ්ඩාල;
  3. in the honorific suffix -ආණ/-අණු/-අණි: පියාණන්, තෙරණුවන්;
  4. in intransitive past suffixes -ණ/-ණි/-ණු: සිදුවිණි, ඉදුණු, වැටුණ, මැරුණි;
  5. in inherited Sanskrit/Pali ණ: රුහුණු, උණු.
- **Use න:**
  1. in verbs, even after ර: කරන, මරන, කරනවා, හදාරන, කරනු (imperative -නු), present-participle -න;
  2. as a hal nasal before dentals ත ථ ද ධ: චින්තන, ග්‍රන්ථ, කන්ද, සන්ධි;
  3. in a geminate nasal: ආසන්න, වන්නම්;
  4. as a hal nasal before ස: පන්සල, කාන්සි, වහන්සේ;
  5. after ස/ශ: වාසනා, සේනා, දර්ශන, ප්‍රකාශන;
  6. in hal noun-root endings and plurals: වදන්, කන්, පින්;
  7. before ට in dative and infinitive forms: දරුවන්ට, මිනිසුන්ට, ලබන්ට;
  8. before retroflex consonants in Western loans: කවුන්ටරය, කැන්ටිම;
  9. after ර in compound nouns: පිරිනිවන්.
- **Minimal pairs:** කණ "ear" / කන "eat"; වණ "wound" / වන "forest"; මරණ "death" / මරන "killing"; බණ "sermon" / බන `[UNVERIFIED]`.
- **Applies to:** nna, na.
- **Confidence:** high (both sources agree).
- **Sources:** WASALA-SPELL 2010 App. A §1–2; SI-WP-AV; LETSLEARN.
- **Conflict:** SI-WP-AV says ර is "always" followed by ණ in native words. WASALA lists many exceptions (verbs, compounds, ර-final roots). Treat the "always" as applying to nouns only.

### SP-004 — ළ vs ල
- **Use ළ:**
  1. the prefix පිළි- (from Sanskrit prati-): පිළිතුර, පිළිබඳ, පිළිගන්නවා, පිළිවෙළ, පිළිමය;
  2. past and participle forms of ර-final verb roots: කර → කළ/කළේ; මර → මළ; හදාර → හදාළේය;
  3. reflexes of Sanskrit/Pali ට/ඨ/ඩ/ඪ/ණ/ළ: කූට → කළ; දෘඪ → දළ; ක්‍රීඩා → කෙළි; වෙළඳ;
  4. word-initially in native words: ළමයා, ළඟ, ළිඳ;
  5. often before the prenasals ඟ ඳ ඹ: ළඟ, ළඳ, කොළඹ (exceptions with ල: පොලඹ, සලඹ).
- **Use ල:**
  1. a hal ල at the end of a noun root, which stays ල in inflection: කකුල්/කකුල, ගඩොල්, කරල්;
  2. the geminate in the singular of ඉ/උ roots: ඇඟිලි → ඇඟිල්ල, මහලු → මහල්ලා;
  3. reflexes of Sanskrit/Pali ල/ල්ල: මහල්ලක → මහලු;
  4. most loanwords.
- **Minimal pairs:** කල "time" / කළ "did"; පල "fruit" / පළ "publish(ed)" (පළාත, පළමු); වල "in, of (pl.)" / වළ "pit"; කලා "arts" / කළා "did".
- **Applies to:** lla, la.
- **Confidence:** high.
- **Sources:** WASALA-SPELL 2010 App. A §3–4; SI-WP-AV; LETSLEARN.

### SP-005 — ශ vs ෂ vs ස
- **Use ෂ:**
  1. after a hal ක, i.e. the cluster ක්ෂ: අක්ෂර, දක්ෂ, භික්ෂු, පරීක්ෂණ, තීක්ෂණ;
  2. as hal before ට/ඨ: දෘෂ්ටි, දුෂ්ට, ශිෂ්ට, අධිෂ්ඨාන, ජ්‍යෙෂ්ඨ, ශ්‍රේෂ්ඨ, කනිෂ්ඨ;
  3. before ණ: විෂ්ණු, කෘෂ්ණ, තෘෂ්ණා;
  4. as hal before ක/ප in දුෂ්කර, නිෂ්පාදන (SN-011).
- **Use ශ:**
  1. with palatals ච/ජ: දුශ්චරිත, ආශ්චර්ය, නිශ්චල;
  2. before ව: විශ්වාස, ඊශ්වර, අශ්වයා;
  3. before න: ප්‍රශ්න, දර්ශන, දේශනය;
  4. before ශ: නිශ්ශබ්ද;
  5. ශ්‍රී;
  6. as the first sibilant in ශිෂ්‍ය, විශේෂ, ශාස්ත්‍ර.
- **Use ස:** native words and most tadbhava forms: සිසු (vs tatsama ශිෂ්‍ය), සත (vs ශත).
- **Registers:** Sanskrit and native spellings often coexist with the same meaning: ශිෂ්‍ය/සිසු, දේශය/දෙස `[UNVERIFIED pair]`.
- **Applies to:** sha, ssa, sa.
- **Confidence:** high (rules); medium (completeness — the rules do not cover every word).
- **Sources:** SI-WP-AV; WASALA-SPELL 2010 App. A §5–6; LETSLEARN.

### SP-006 — Aspirate vs plain letters (මහාප්‍රාණ / අල්පප්‍රාණ)
- **Statement:** Aspirates occur only in Sanskrit/Pali words and are pronounced like plain letters (G2P-010). ඣ, ඡ and ඵ are rare. Aspirates can appear at the start, middle or end of a word, so there are **no reliable rules** for them. They must be learned per word.
- **Examples:** ධර්ම, භාෂාව, ඛේදය, ඝෝෂා, ථේර, කථාව/කතාව.
- **Variants:** Some words exist in both aspirated (tatsama) and plain (tadbhava) spellings, both accepted: කථා/කතා, නාථ/නාත `[second pair UNVERIFIED]`.
- **Applies to:** kha gha cha jha ttha ddha tha dha pha bha.
- **Confidence:** high.
- **Sources:** WASALA-SPELL 2010 §III-A-1.

### SP-007 — Short vs long vowels — the most frequent error class
- **Statement:** SinSpell found vowel-length errors and similar-sounding-letter errors to be the most common in a real corpus. Prescriptive points:
  - The verbal noun suffix is long -ීම: කිරීම, බැලීම, ලිවීම. Writing *කිරිම* is an error.
  - Long ඊ/ඌ/ඒ/ඕ in Sanskrit roots: ශ්‍රී, ගීතය, රූපය.
  - Honorific/plural -ූ in some forms `[UNVERIFIED]`.
- **Applies to:** i/ii, u/uu, e/ee, o/oo, ae/aee, a/aa.
- **Confidence:** high (that length is the top error); medium (the specific suffix rules).
- **Sources:** SINSPELL 2021; WASALA-SPELL 2010.

### SP-008 — Gemination controversy: තත්ත්වය vs තත්වය
- **Statement:** Etymologically the word is *tat + tva*, so the strict spelling is තත්ත්වය, with the same pattern in සත්ත්වයා and මහත්ත්වය. Prescriptive teachers and exam guides favour the triple-consonant form. Everyday print and many dictionaries online use තත්වය, සත්වයා.
- **Status:** `[UNVERIFIED: no authoritative online ruling found]`. A Glosbe dictionary entry uses තත්වය (https://glosbe.com/si/en/තත්වය).
- **Applies to:** ta, va, hal.
- **Confidence:** low.
- **Recommendation:** Treat both spellings as acceptable; the conservative (etymological) form is a valid alternative.

### SP-009 — ං vs hal nasal before a consonant
- **Statement:**
  - ං is used before හ, ල, ර, ස, ශ, ෂ, ව, ය (KNAB). It also replaces ඞ before velars: සිංහල, සංස්කෘත, සංවිධානය, හංසයා, අංකය, සංගීතය.
  - Otherwise, learned words use the homorganic hal nasal: ම් before labials (සම්බන්ධ, කම්පනය), න් before dentals (සන්ධි, චින්තන), ණ් before retroflexes (කාණ්ඩ).
  - Native words use න් before ස (පන්සල, වහන්සේ), even though Sanskrit words use ං there (සංසාරය).
- **Conflict:** The choice before ස depends on the word's origin, not its sound.
- **Applies to:** anusvara, na, nna, ma, nga.
- **Confidence:** medium-high.
- **Sources:** KNAB 1989 notes 1 & E; WASALA-SPELL App. A §2.7, §2.9.

### SP-010 — Prenasal letter vs nasal + stop cluster is meaningful
- **Statement:** The two are written differently and mean different things. The prenasal letter is a single short sound; the cluster is a hal nasal plus a full stop.
- **Examples:** කඳ *kaⁿdə* "trunk" ≠ කන්ද *kandə* "hill"; අඹ *aᵐbə* "mango" vs. අම්බ (not a common word).
- **Note:** The ligature forms (ඬ, ඳ) and the ZWJ conjunct forms (න්‍ද) look alike in some fonts.
- **Applies to:** nnga, nndda, nda, mba vs (nga|nna|na|ma)+hal+(ga|dda|da|ba).
- **Confidence:** high.
- **Sources:** EN-WP-SIN (minimal set); KNAB 1989.

### SP-011 — ක්ෂ (with or without ZWJ) is one spelling
- **Statement:** ක්ෂ and ක්‍ෂ (with ZWJ) are the same letters, ka + hal + ssa. The ZWJ only asks for the conjoined glyph. The same holds for other "touching" or bandi conjuncts (න්ද, ද්ධ…).
- **Applies to:** ka, ssa, ZWJ.
- **Confidence:** high.
- **Sources:** KNAB 1989 note 5; EN-WP-SCRIPT.

### SP-012 — Yansaya / rakaransaya / repaya mark real clusters
- **Statement:**
  - Yansaya (C + ් + ZWJ + ය) writes a C+y cluster: විද්‍යාව, ශිෂ්‍ය, ව්‍යාපාරය, ක්‍යා.
  - Rakaransaya (C + ් + ZWJ + ර) writes a C+r cluster: ප්‍රශ්නය, ක්‍රමය, ශ්‍රී, ග්‍රාමය.
  - Repaya (ර + ් + ZWJ) writes r+C: කර්මය, ධර්මය, වර්ණ.
- **Common errors:** writing ප්රශ්නය without ZWJ, so it renders as a visible hal; writing ර + yansaya (PH-012).
- **Applies to:** ya, ra, hal, ZWJ.
- **Confidence:** high.
- **Sources:** UNICODE-ML 2016; EN-WP-SCRIPT.

### SP-013 — ඥ vs ඤ
- **Statement:** ඥ (*jña*) appears in Sanskrit words: ඥාති, ඥානය, විඥාන, ප්‍රඥා, විශේෂඥ. ඤ appears in Pali and native words: ඤාණ, පඤ්ච, කුඤ්ඤම `[examples UNVERIFIED]`. In speech they merge, with ඥ often pronounced "gny-".
- **Applies to:** jnya, nya.
- **Confidence:** medium.
- **Sources:** KNAB 1989; WASALA-SPELL (similar-sound group {ඥ, ඤ}).

### SP-014 — Spoken vs written Sinhala (diglossia)
- **Statement:** Written and spoken Sinhala differ in morphology. Many colloquial words have no "standard" literary spelling, yet colloquial words are written all the same.
- **Examples:** spoken *kiyanawā* / literary *kiyayi*; spoken *eka* (English-loan classifier: බස් එක, කාර් එක) vs. literary බසය.
- **Implication:** Tools that process Sinhala text (transliterators, spelling checkers) must handle both registers.
- **Applies to:** —
- **Confidence:** high.
- **Sources:** WASALA-SPELL 2010 §III (Sinhala is diglossic); Gamage & Dilani 2024, TPLS 14(2) (https://doi.org/10.17507/tpls.1402.02).

---

## 5. Loanword conventions

### LW-001 — English /f/ → ෆ (modern); older loans → ප
- **Statement:** Modern loans use ෆ. Older loans used ප, and some still do.
- **Examples:**
  - ෆ: ෆෝන් *fōn*, ෆයිල්, ෆැෂන්, ෆැක්ස්, ෆේස්බුක්, ෆෑන්
  - ප: ප්‍රංශය "France", කෝපි "coffee" (via Portuguese/Dutch); ග්‍රැමෆෝන් ~ EN-WP-LOAN *gramanfōn*
- **Applies to:** fa, pa.
- **Confidence:** high.
- **Sources:** EN-WP-SCRIPT; EN-WP-SIN (/f/ often replaced by /p/ or /s/ in speech).

### LW-002 — English /v/ and /w/ → ව
- **Statement:** Both sounds are written ව. It is pronounced [ʋ]/[w], or [v] before *i* (KNAB).
- **Examples:** වෑන් *vǣn* "van"; වෝටර් "water"; වීඩියෝ "video".
- **Applies to:** va.
- **Confidence:** high.
- **Sources:** KNAB 1989; EN-WP-LOAN.

### LW-003 — English /æ/ → ඇ / ඈ
- **Statement:** English /æ/ is written ඇ or ඈ. Monosyllables (and stressed open-sounding vowels) tend to take long ඈ; polysyllables tend to take short ඇ.
- **Examples:**
  - ඈ: ෆෑන්, බෑග්, වෑන්, පෑන "pen"
  - ඇ: බැංකුව, කැම්පස්, ටැක්සි, ඇල්බමය, කැබිනට්, ලැප්ටොප්
- **Exceptions:** Many variants exist, e.g. බෑග් / බැග්.
- **Applies to:** ae, aee.
- **Confidence:** medium (a tendency, not a rule).
- **Sources:** EN-WP-LOAN (*pǣna, gæs, kæbinaṭ, læpṭop, blækmēl*); EN-WP-SCRIPT.

### LW-004 — English vowels /ɒ/, /əʊ/, /ɔː/
- **Statement:** /ɒ/ → ඔ; /əʊ/ and /ɔː/ → ඕ.
- **Examples:**
  - ඔ: ලොරිය, කොම්පියුටර්, ලැප්ටොප්
  - ඕ: ෆෝන්, පෝස්ටර්, නෝට්ටුව, හෝටලය, බෝලය, කෝච්චිය
- **Applies to:** o, oo.
- **Confidence:** high.
- **Sources:** EN-WP-LOAN.

### LW-005 — English schwa and /ɜː/ → අ (often with ර්)
- **Statement:** English schwa and /ɜː/ are written with අ; the *-er/-or* ending is written -අර් (hal ර).
- **Examples:** පෝස්ටර්, හෙලිකොප්ටර්, කොම්පියුටර්, බටර් *baṭar*; නර්ස්; ඇම්ප්ලිෆයර්.
- **Applies to:** a, ra+hal.
- **Confidence:** high.
- **Sources:** EN-WP-LOAN; WWG-G2P §2.2 (/ə, əː/ in English loans are written අ).

### LW-006 — English /z/ → ස; /ʒ/ → ජ
- **Statement:** English /z/ is written ස; English /ʒ/ is written ජ.
- **Examples:** සූ "zoo", සීරෝ "zero", සිප් "zip" `[UNVERIFIED]`; ගරාජ් "garage".
- **Note:** There is no dedicated letter for /z/. Writing /z/ with ශ is not standard `[UNVERIFIED]`.
- **Applies to:** sa, ja.
- **Confidence:** medium.
- **Sources:** EN-WP-LOAN (*garāj*).

### LW-007 — English /ʃ/ → ෂ (popular) or ශ; older loans → ස
- **Statement:** Modern popular spelling for English /ʃ/ is mostly ෂ. Learned spelling sometimes uses ශ. Older loans used ස.
- **Examples:**
  - ෂ: ෂර්ට් "shirt", ෆැෂන්, ස්ටේෂන් "station" (-tion → -ෂන්), බ්‍රෂ්
  - ස (old): දීසිය "dish" (*dīsiya*)
- **Applies to:** ssa, sha, sa.
- **Confidence:** medium. Popular usage is clear; no prescriptive rule was found.
- **Sources:** EN-WP-LOAN (*dīsiya*).

### LW-008 — English /θ/ → ත; /ð/ → ද
- **Statement:** English "th" in names is written ත.
- **Examples:** තෝමස් "Thomas", එලිසබෙත් "Elizabeth", තර්ස්ටන් "Thurstan" `[UNVERIFIED examples]`.
- **Applies to:** ta, da (not tha/dha).
- **Confidence:** medium.
- **Sources:** General practice; EN-WP-SIN (speakers substitute stops).

### LW-009 — English *x* → ක්ස් (never ක්ෂ)
- **Statement:** The ක්ෂ cluster is reserved for Sanskrit *kṣ*.
- **Examples:** ටැක්සි, ෆැක්ස්, එක්ස්-රේ, බොක්ස් `[UNVERIFIED last two]`.
- **Applies to:** ka, sa, hal.
- **Confidence:** medium-high.
- **Sources:** General practice.

### LW-010 — English /tʃ/ → ච; /dʒ/ → ජ; /k/ (cheque) → ක
- **Examples:** චොක්ලට්, ජූස්, ජූරිය, ජෙනරාල්; චෙක්/චැක් "cheque" (EN-WP-LOAN gives *cæk*).
- **Applies to:** ca, ja.
- **Confidence:** high.
- **Sources:** EN-WP-LOAN.

### LW-011 — Final consonants and naturalisation suffixes
- **Statement:** Modern loans keep a final hal consonant: බස්, කාර්, ෆෝන්. Fully naturalised literary forms add -ය/-ව/-අ, often with gemination:
  - බෝලය "ball"; බයිබලය "Bible"; කේතලය "kettle"; ලොරිය; ජූරිය; කොම්පැනිය; පාර්ලිමේන්තුව
  - නෝට්ටුව "note"; කෝච්චිය "coach"; බැංකුව
  Colloquial speech uses the bare form plus එක: ෆෝන් එක.
- **Portuguese/Dutch layer:** කමිසය, මේසය, ජනේලය, සපත්තුව, බොත්තම, කාමරය, පාන්, රෝදය `[UNVERIFIED etymologies]`.
- **Applies to:** ya, va, hal, geminates.
- **Confidence:** high.
- **Sources:** EN-WP-LOAN; Gamage & Dilani 2024.

### LW-012 — Clusters in English loans are kept with hal or ZWJ
- **Statement:** Most clusters are kept as written hal sequences. *-ng* is written ං (ඉංග්‍රීසි "English", ෂොපිං).
- **Examples:** ස්ටේෂන්, ස්කූල්, ප්‍රින්ටර්, බ්ලැක්මේල්, ඉංග්‍රීසි.
- **Exceptions:** Older loans broke clusters up with vowels: ඉස්කෝලය "school", ඉස්තෝප්පුව `[UNVERIFIED]`.
- **Applies to:** hal, anusvara, ra (rakaransaya).
- **Confidence:** high.
- **Sources:** EN-WP-LOAN.

### LW-013 — Tamil and Arabic loans/names
- **Statement:** These follow the same sound substitutions:
  - Arabic f → ෆ (ෆාතිමා); z → ස; q/k → ක; kh → ක or ඛ.
  - Tamil retroflexes map to ට/ඩ/ණ/ළ.
  Spelling of Muslim and Tamil names varies widely, e.g. මොහොමඩ් / මුහම්මද්.
- **Applies to:** fa, sa, ka, tta, dda, nna, lla.
- **Confidence:** low `[UNVERIFIED — no source found]`.

---

## 6. Typography: case, punctuation, spacing, numbers

### TY-001 — No letter case
- **Statement:** Sinhala has no upper/lower case. Capitalisation in romanized text carries no Sinhala meaning.
- **Confidence:** high.
- **Sources:** EN-WP-SCRIPT.

### TY-002 — Punctuation
- **Statement:** Modern Sinhala uses Western punctuation: . , ? ! : ; " ' ( ) -. The කුණ්ඩලිය ෴ (U+0DF4) was historically a full stop and is no longer in general use.
- **Confidence:** high.
- **Sources:** EN-WP-SCRIPT.

### TY-003 — Numerals
- **Statement:** Hindu-Arabic digits 0–9 are standard. Sinhala Lith digits (U+0DE6–0DEF) and archaic numerals (Sinhala Archaic Numbers block, U+111E1–111F4) exist only for historical and astrological use.
- **Confidence:** high (usage); medium (code-point ranges, from memory).
- **Sources:** EN-WP-SCRIPT.

### TY-004 — Word spacing
- **Statement:** Words are space-delimited. Case suffixes, postpositional clitics and enclitic particles are written attached: ගෙදරට, ඔහුගේ, පොතෙන්, ඔහුත්, ඔහුද. Free postpositions and auxiliaries are written separately: ගැන, සමඟ, විසින්, කතා කරනවා, බලා සිටියි. Compound nouns are written solid: ගංවතුර, පිළිතුර.
- **Note:** Spacing of compounds and of නම්/වත්/ද is inconsistent in practice.
- **Confidence:** medium `[UNVERIFIED: no prescriptive spacing source found]`.
- **Sources:** WWG-G2P 2006 §2.2 (words are delimited by spaces "in general").

---

## Implications for romanization and transliteration

Guidance for anyone converting between Latin-script romanizations and Sinhala script, building a spelling checker, or validating Sinhala text. These points follow from the rules above; they add no new rules.

1. **⚠️ Sound cannot decide spelling for ~10 letter groups.** These groups each collapse to one sound (G2P-010): {ක ඛ}, {ග ඝ}, {ච ඡ}, {ජ ඣ}, {ට ඨ}, {ඩ ඪ}, {ත ථ}, {ද ධ}, {ප ඵ}, {බ භ}, {න ණ}, {ල ළ}, {ස ශ ෂ}, {ඤ ඥ}. Converting from a sound-based romanization therefore needs either a romanization that marks the distinctions (as the diacritics ṇ, ḷ, ṣ, ś in this file do) **or** a lexicon that ranks the possible spellings. WASALA-SPELL used exactly these groups, ranked by corpus frequency. Their 82% accuracy suggests a lexicon is essential.
2. **Positional rules are hard validity checks.** Well-formed Sinhala never has:
   - a prenasal word-initially, word-finally or with hal (PH-003);
   - ඞ/ං word-initially (PH-004);
   - ඎ word-initially;
   - ර + yansaya (PH-012);
   - a geminate ඟ ඬ ඳ ඹ ං හ ෆ (PH-008).

   In a romanized string, a vowel after a consonant corresponds to a vowel sign, not an independent vowel (PH-009). Compounds like ගිරිඋල්ල are the exception, and a romanization needs an explicit separator to represent them.
3. **Schwa-aware matching.** Informal romanizations write [ə] as *a* or *e* (*karanawa / keranawa*). When converting, treat `a`, and optionally `e`/`u`, in an unstressed non-initial syllable as possibly an inherent vowel. G2P-002 to G2P-009 predict where [ə] occurs; informal romanizations do not use a schwa symbol.
4. **Nasals.**
   - Romanized `nd/mb/ng/nnd` before a vowel is ambiguous: prenasal letter (ඳ ඹ ඟ ඬ) or cluster (න්ද ම්බ ...) (SP-010). The prenasal is the likelier reading in native-looking words and the cluster in Sanskrit-looking ones; both must be considered.
   - Romanized word-final `ng` may correspond to ං **or** to final න්/ම් (PH-007).
   - Before h, s, ś, v, y, r, l, a romanized `n`/`m` may correspond to ං (සිංහල) (SP-009).
5. **Clusters.**
   - Romanized `Cr` → rakaransaya; `rC` → repaya; `Cy` → yansaya with ZWJ. A bare visible hal + ර where a conjunct is meant is an error (SP-012).
   - Romanized `x` → ක්ස්, while `ksh` → ක්ෂ (LW-009).
   - Romanized `kru` is ambiguous between කෘ and ක්‍රු (G2P-011).
6. **Diphthongs.** Romanized `ai/au` corresponds to අයි/අවු (or -යි/-වු after a consonant) in native words, and to ඓ/ඖ (ෛ/ෞ) in learned words (PH-010, SN-012).
7. **Morphology-aware generation.** Sandhi and inflection produce predictable forms (SN-009, SN-010, SN-014). After a root, -ය follows i/e/æ stems and -ව follows u/o/ā stems, and ඉ/උ roots have a geminated singular. These patterns are useful for generating inflected forms for a lexicon or spelling checker.
8. **ළ / ණ heuristics as ranking features:**
   - ණ after ර/ෂ/ෘ in nouns, and before ට/ඩ;
   - න in verb forms, before dentals and ස, and in geminates;
   - ළ in පිළි- and in past forms of ර-verbs;
   - ල for hal-final roots.
   Use these as tie-breakers, not hard rules (SP-003, SP-004).
9. **Loanword correspondences.** Romanized `f` → ෆ (older words may have ප). `w`/`v` → ව; `z` → ස; `sh` → ෂ (ශ also occurs); `th` → ත; `ae` → ඇ/ඈ (both occur); `o` → ඔ/ඕ. Final hal consonants are kept (LW-001 to LW-012).
10. **Accept both standard and variant spellings** where sources conflict: තත්ත්වය/තත්වය, බෑග්/බැග්, කථා/කතා, කල/කළ. A spelling checker or normaliser should not "correct" a deliberate variant.

---

## Open questions / conflicting sources

| # | Issue | Conflict / uncertainty | Status |
|---|---|---|---|
| 1 | Word-initial consonants (PH-005) | WWG-G2P quotes Disanayaka: all except /ŋ/ "and nasals". Read literally, this excludes ණ-initial words like ණය. Probably means prenasals. | Check Disanayaka 1995 in print |
| 2 | ණ after ර (SP-003) | SI-WP-AV says "always" ණ in native words. WASALA-SPELL lists many න exceptions (verbs, compounds). | Treat as nouns-only tendency |
| 3 | තත්ත්වය vs තත්වය (SP-008) | Etymological/prescriptive vs common usage. No authoritative ruling found online. | Low confidence; accept both |
| 4 | G2P Rule 2 and Rule 5 details | The PDF text of Rule 2(b)/(c) is contradictory. Two exception consonants in Rule 5 are illegible. | Needs the clean original paper or the UCSC LTRL implementation |
| 5 | Glide after අ-final stems (SN-010) | Sources show ය/ව insertion after i/æ/u/ā. Behaviour after short අ (deletion vs ය) is my generalisation. | Unverified |
| 6 | "යකාරාගම / වකාරාගම" terminology | No hits. School grammar calls this "ආගම සන්ධිය". | Terminology unverified |
| 7 | Number of sandhi types | si.wikipedia (සන්ධි) lists 10 with slightly different names and examples from සිංහල සන්ධි (9 listed) and Piriven (10, adds ගාත්‍රාදේශ). The ස්වරාදේශ examples differ between pages. | Minor; content is consistent |
| 8 | English /ʃ/: ෂ vs ශ (LW-007) | Popular media mostly ෂ; learned/older forms ශ or ස. No standard found. | Accept both |
| 9 | English /æ/: ඇ vs ඈ (LW-003) | Length assignment varies by word and writer. | Accept both |
| 10 | ං vs න් before ස (SP-009) | Native පන්සල vs Sanskrit සංසාරය: the choice depends on origin. | Lexicon needed |
| 11 | Historical ය්‍ය for *rya* (PH-012) | SLS 1134 forbids ර + yansaya. Older print used ය්‍ය (කාය්‍ය). Whether to treat old forms as valid in modern text is open. | Unverified historical claim |
| 12 | Hela Havula letter rules (SP-001) | No online source detailed which letters or spellings Hela Havula prescribes. | Unverified |
| 13 | Department of Official Languages | No public spelling standard found. The department appears to issue terminology glossaries only. | Unverified |
| 14 | Wikipedia gloss error | EN-WP Sinhala phonology table glosses කන as "ear". The ear word is කණ; කන is "eat". This shows Wikipedia examples need checking. | Noted |
| 15 | Spacing conventions (TY-004) | No prescriptive source found. Practice varies for compounds and particles. | Unverified |
| 16 | Tamil/Arabic loan conventions (LW-013) | No sources found. | Unverified |
