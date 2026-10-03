# 00 — Sinhala orthography: consolidated rule set

This file merges the topic studies (01–06) into one deduplicated rule list. Each rule
cites the source rules it was built from (e.g. `02:VS-007` = file 02, rule VS-007).
Compiled October 2026.

- **HARD** = encoding or orthographic invariant. A correct text never violates it.
- **SOFT** = spelling tendency. Use it to rank candidate spellings, never as a hard filter.
- **STYLE** = two or more spellings are correct; the choice is a convention.
- Confidence: **H** high · **M** medium · **L** low (same meaning as in the topic files).

Machine-readable companions:

- `data/letters.json`: all 923 letter forms (18 vowels, 3 signs, 41 × 19 consonant forms, 41 × 3 conjuncts).
- `data/validity.json`: the status of each form (`valid` · `loan` · `rare` · `unattested` · `never`)
  and the rules behind it, built by `tools/build_data.py`.

---

## 1. Encoding invariants (HARD)

| ID | Rule | Conf | Sources |
|---|---|---|---|
| G-EN-01 | Store in **logical order**: consonant (or whole cluster) first, then the vowel sign, even for ෙ ේ ෛ ො ෝ ෞ, which display before the consonant | H | 02:VS-002, 03:HC-023 |
| G-EN-02 | Use **precomposed signs**: ේ U+0DDA, ො U+0DDC, ෝ U+0DDD, ෞ U+0DDE. Never their decomposed pieces. NFC-normalize text as a safety net | H | 01:INV-003, 02:VS-003 |
| G-EN-03 | **ෛ U+0DDB has no decomposition.** ෙ+ෙ is a different, silently-wrong string. Always encode U+0DDB | H | 01:INV-003, 02:VS-004 |
| G-EN-04 | Order inside ෝ is ෙ ා ්. The sequence ෙ ් ා normalizes to ේ + ා, which is wrong | H | 02:VS-005 |
| G-EN-05 | **Independent vowels are atomic.** Never encode අ+ා (ආ), අ+ැ, අ+ෑ, එ+් (ඒ), ඔ+් (ඕ), ඔ+ෟ, උ+ෟ, ඍ+ෘ, ඏ+ෟ, එ+ෙ | H | 01:INV-002, 02:VS-006 |
| G-EN-06 | **Consonants are atomic**, including the 5 sanyaka letters, ඥ (U+0DA5, never ජ්‍ඤ) and ෆ | H | 01:INV-001, 03:HC-051 |
| G-EN-07 | **Hal alone never joins.** `C ් C` always shows a visible hal. A joined form needs ZWJ | H | 03:HC-001 |
| G-EN-08 | ZWJ position chooses the style: `C ් ZWJ C` = conjunct / yansaya / rakaransaya / repaya; `C ZWJ ් C` = touching letters (Pali). Unicode and SLS 1134:2011 agree; the 2004 SLS draft differs | H | 03:HC-002/003, 01:INV-005 |
| G-EN-09 | Named sequences: yansaya `0DCA 200D 0DBA` · rakaransaya `0DCA 200D 0DBB` · repaya `0DBB 0DCA 200D` | H | 01:INV-006, 03:HC-004 |
| G-EN-10 | **No ZWNJ** in normal text | H | 03:HC-005 |
| G-EN-11 | Contextual glyph shapes (hook-u, රු රූ රැ රෑ ළු, the tail lost on ද before u, a second hal shape) are font matters. Encoding stays ordinary consonant + sign | H | 01:INV-009/010, 02:VS-011…017 |
| G-EN-12 | Expect ZWJ-less text in real corpora (ශ්රී, අක්ෂර) and fold it for matching. Never strip ZWJ when producing text | H | 03:HC-050, 03:§10.12, 05:SP-011 |

---

## 2. Vowels and vowel signs

| ID | Rule | Kind | Conf | Sources |
|---|---|---|---|---|
| G-VS-01 | 17 dependent signs + al-lakuna. Each consonant has 19 forms: hal, inherent a, and 17 signs | HARD | H | 01:§2d, 02:VS-001 |
| G-VS-02 | An **independent vowel letter** is used word-initially. Inside a word, a vowel after a consonant is always a sign | HARD | H | 02:VS-029, 05:PH-009 |
| G-VS-03 | **No vowel sign after an independent vowel** (ඉී, ඔා). Shapers usually do not warn | HARD | H | 02:VS-007 |
| G-VS-04 | **No vowel sign after hal** (ක්ා), and at most **one** vowel sign per consonant (කාා). Only ං/ඃ may follow a sign | HARD | H | 02:VS-009/010 |
| G-VS-05 | A sign with no base is invalid in text | HARD | H | 02:VS-008 |
| G-VS-06 | **Vowel hiatus is repaired with a glide**: ය after i/ii/e/ee/ae/aee, ව after u/uu/o/oo/aa (රැය, තොප්පිය, මාලිගාව). After short a, the vowel is usually deleted instead (පොතේ) | SOFT | H (glide), L (after a) | 02:VS-030, 05:SN-010, 05:PH-009 |
| G-VS-07 | Spoken diphthongs in native and English words are **V + යි / V + වු** (අයියා, ළමයි, කවුද, ලයිට්) | SOFT | H | 02:VS-022, 05:PH-010 |
| G-VS-08 | **ඏ ඐ ෟ (alone) ෳ** are not used in modern Sinhala. The letter ඎ is obsolete (its sign ෲ survives in a few words). ෟ survives only inside ෞ/ඖ | HARD (normal mode) | H | 01:INV-018, 02:VS-021 |
| G-VS-09 | Vowel length is phonemic, with one long sign per short sign: a→aa, ae→aee, i→ii, u→uu, e→ee, o→oo, ru→ruu | HARD | H | 02:VS-032 |
| G-VS-10 | ර and ළ have irregular glyphs with u/uu (and ර with ae/aee). Never encode a "visual" substitute | HARD | H | 02:VS-011…013 |
| G-VS-11 | **ෘ ෲ ෛ ෞ (and ඍ ඓ ඖ) are Sanskrit-loan only.** ැ/ෑ (ඇ ඈ) are distinctly Sinhala and almost absent from Sanskrit words | SOFT | H | 02:VS-019/020/022, 05:SN-012 |
| G-VS-12 | **"ru" has three readings:** ර+ු, ෘ, and rakaransaya+ු. ගෘහ (house) ≠ ග්‍රහ (planet). ක්‍රු/ක්‍රූ must be encoded with ු/ූ, never ැ/ෑ | HARD (encoding), SOFT (choice) | H | 02:VS-012/016/020, 03:HC-024, 05:G2P-011 |
| G-VS-13 | Per-consonant sign validity (41 × 17): see `data/grammar/validity.json`. Aspirates rarely take ැ/ෑ; ළ rarely takes long signs; sanyaka letters rarely take long signs | SOFT | M | 02:§8 |
| G-VS-14 | On ්‍ය clusters, SLS lists a aa u uu e ee o oo. On ්‍ර clusters, a aa ae aee i ii e ee ai o oo au, plus u uu (SLS omits them, but ක්‍රූර exists). Other combinations are encodable | SOFT | H | 01:INV-018, 02:VS-016, 03:HC-020/021 |

---

## 3. Hal and consonant clusters

| ID | Rule | Kind | Conf | Sources |
|---|---|---|---|---|
| G-HC-01 | A consonant with no following vowel gets hal. This covers word-final position (පොතක්, මල්), before another consonant, and geminates | HARD | H | 03:HC-010/012/013 |
| G-HC-02 | **Pronunciation never decides hal.** Whether inherent a is said as [a] or [ə] is not written | HARD | H | 03:HC-010/011, 05:G2P-001 |
| G-HC-03 | Geminates are `C ් C` with **no ZWJ** (අම්මා, අක්කා, පත්තරය) | HARD | H | 03:HC-042, 05:PH-008 |
| G-HC-04 | These letters **never geminate**: ඟ ඬ ඳ ඹ ඦ ඞ ෆ හ ශ (learned ශ්ශ exists: නිශ්ශබ්ද), and ළ | HARD | H | 03:HC-042, 05:PH-008, 04:NS-075 |
| G-HC-05 | Native syllables are (C)V(C) with no initial clusters. Initial clusters are tatsama or English (ප්‍ර, ස්ව, ස්ටේෂන්) | SOFT | H | 03:HC-040, 05:PH-001 |
| G-HC-06 | **Sanyaka ඟ ඦ ඬ ඳ ඹ never take hal**, so never ්‍ය/්‍ර after them. They are never word-initial | HARD | H | 02:VS-025, 03:HC-014, 04:NS-031, 05:PH-003 |
| G-HC-07 | **ළ never takes hal** (stem-final ළ stays ළ; geminate l is ල්ල) | HARD | M | 03:HC-014, 04:NS-058/075 |
| G-HC-08 | **ඞ appears only as ඞ්** (before a velar, Pali or learned). It never takes a vowel sign. Modern spelling uses ං | HARD | H | 01:INV-018, 02:VS-023, 04:NS-040 |
| G-HC-09 | ණ never ends a stem with hal (a final consonant surfaces as න්). ණ් is fine inside clusters (ණ්ඩ) | SOFT | M | 04:NS-058 |
| G-HC-10 | Each joining point of a long cluster is independent: ZWJ only where a reduced form is wanted (ස්ත්‍රී, රාෂ්ට්‍ර, ශාස්ත්‍ර) | HARD | H | 03:HC-044 |
| G-HC-11 | **Yansaya is mandatory** for C + ය: `C ් ZWJ ය` (වාක්‍ය, විද්‍යාව). වාක්ය without ZWJ is not accepted | HARD | H | 03:HC-020, 05:SP-012 |
| G-HC-12 | **Rakaransaya is mandatory** for C + ර: `C ් ZWJ ර` (ක්‍රම, ශ්‍රී, ප්‍රශ්නය). Valid after **any** consonant that takes hal, including ම (තාම්‍ර), න and ල (rare) | HARD | H (rule), L (m/n/l attestation) | 03:HC-021/052 |
| G-HC-13 | **Repaya is optional style**: ර් + C or ර ් ZWJ + C, both correct (කර්ම / කර්‍ම) | STYLE | H | 01:INV-006, 03:HC-022 |
| G-HC-14 | **No yansaya after ර** (SLS 1134). `ර ් ZWJ ය` means repaya + ය. *kārya* has 3 accepted spellings: කාර්‍ය්‍ය (traditional), කාර්‍ය, කාර්ය. ර්‍ර is unattested | HARD (ra+yansaya), DESIGN (which kārya) | H | 03:HC-033/034/054, 05:PH-012 |
| G-HC-15 | **Other conjuncts (bandi akuru) are optional and mostly classical.** Still seen: ක්‍ෂ, ක්‍ව, න්‍ද, න්‍ධ, න්‍ථ, ත්‍ථ. Not contemporary: ද්‍ධ, ද්‍ව, ට්‍ඨ, ඤ්‍ච. Modern default is plain hal | STYLE | M | 03:HC-030, 03:§9b |
| G-HC-16 | ක්ෂ and ක්‍ෂ are the same spelling of *kṣ*. Both are common | STYLE | H | 03:HC-032, 05:SP-011 |
| G-HC-17 | Touching letters `C ZWJ ් C` are Pali/classical only. They need SLS Level 3 fonts, which barely exist | STYLE | H | 03:HC-031/062 |
| G-HC-18 | Prefer තත්ත්වය / සත්ත්ව (prescriptive), but accept තත්වය / සත්ව. No official ruling exists | SOFT | L | 03:HC-043, 05:SP-008 |

---

## 4. Nasals and ayogavaha signs

| ID | Rule | Kind | Conf | Sources |
|---|---|---|---|---|
| G-NS-01 | **ං follows a vowel, a consonant (+ sign) or a sanyaka.** Never word-initial, never after hal, never takes a sign, always last in its cluster | HARD | H | 01:INV-008, 04:NS-001/002, 05:PH-004 |
| G-NS-02 | ං = [ŋ]. It has replaced ඞ් (and often ඤ්): ලංකාව, මංගල, වංචාව | SOFT | M | 04:NS-003/004 |
| G-NS-03 | **Nasal before a consonant (tatsama):** k/g group, and y r l v ś ṣ s h → **ං**; ට/ඩ group → **ණ්**; ත/ද group → **න්**; ප/බ group → **ම්**; c/j group → ං (modern) or ඤ් (Pali). Native words use න් before ස (පන්සල) | SOFT | H (retroflex, dental), M (others) | 04:NS-005/043/055/056, 05:SP-009 |
| G-NS-04 | *sam-* + vowel → ම + sign (සමාගම). ං never stands before a vowel inside a word | HARD | M | 04:NS-006/010 |
| G-NS-05 | **ඃ** is rare, Sanskrit-only, [h], with the same position rules as ං. Most Sanskrit visarga surfaces as ෝ / ර් / ශ් / ස් / ෂ් through sandhi. It is never predictable from sound alone | SOFT | H | 04:NS-020…023, 05:SN-011 |
| G-NS-06 | **ඁ candrabindu is not modern Sinhala.** It has no place in modern text | HARD | H | 01:INV-011, 04:NS-025 |
| G-NS-07 | Sanyaka = a short nasal fused to a voiced stop (ඞ+ග, ඤ+ජ, ණ+ඩ, න+ද, ම+බ). It contrasts with nasal + hal + stop: **කඳ trunk ≠ කන්ද hill**, අඟල ≠ අංගය | HARD (contrast) | H | 01:INV-021, 04:NS-030/032, 05:SP-010 |
| G-NS-08 | **Sanyaka vs cluster is lexical.** Tatsama words never use sanyaka. Native and tadbhava words often do. English loans use clusters (ලන්ඩන්). Some words accept both (මග/මඟ) | SOFT | M | 04:NS-033/034 |
| G-NS-09 | Nothing nasal precedes a sanyaka (no අංඹ, no න්ඳ) | HARD | M | 04:NS-037 |
| G-NS-10 | Prenasal + consonant in compounds → ං or a hal nasal (ගඟ + වතුර → ගංවතුර) | SOFT | H | 05:SN-007, 04:NS-007 |
| G-NS-11 | **ඦ is practically unused.** Keep it in the inventory, but treat it as obsolete | SOFT | H | 01:§8, 04:NS-036 |
| G-NS-12 | **ඥ** = Sanskrit *jñ* (ඥානය, ප්‍රඥාව, the suffix -ඥ). **`gn` is not always ඥ** (අග්නි, නග්න, ලග්න) | SOFT | H | 04:NS-042/046 |
| G-NS-13 | **`ny` is usually න්‍ය** (අන්‍ය, ශූන්‍ය, ධන්‍ය). ඤ is rare (ඤාණ, පඤ්ච, සඤ්ඤා) | SOFT | H | 04:NS-041/047 |
| G-NS-14 | Word-final ං contrasts with final ම් / න් (දං ≠ දන්). Colloquial final ං stands for formal ම්/න් (මං, එහෙනං) | SOFT | M | 04:NS-008/009 |
| G-NS-15 | A spoken final [ŋ] can be written ං, න් or ම් (මිනිසුන් is said *minisuŋ*). A romanized `-ng` at word end is ambiguous | SOFT | M | 03:HC-012, 05:PH-007 |

---

## 5. Phonotactics and sandhi

| ID | Rule | Kind | Conf | Sources |
|---|---|---|---|---|
| G-PH-01 | **Word-initial bans:** sanyaka letters, ඞ, ං, ඃ, ඎ. ණ only in ණය (plus archaic words). ළ is fine initially (ළමයා) | HARD (except ණ) | H | 04:NS-031/057, 05:PH-003…006 |
| G-PH-02 | Words end in a vowel, a hal consonant or ං. Never in a sanyaka. ළ/ණ end a word only with a vowel | HARD | H | 05:PH-007, 04:NS-058 |
| G-PH-03 | Vowel hiatus inside a word occurs only at compound boundaries and in place names (ගිරිඋල්ල). A romanization needs an explicit separator to express it | SOFT | H | 05:PH-009, 02:VS-029 |
| G-PH-04 | The 10 school sandhi types, plus frozen Sanskrit sandhi (dīrgha, guṇa, vṛddhi, yaṇ, visarga), explain most learned spellings (ඉත්‍යාදි, නිර්මාණ, දුෂ්කර, පෞද්ගලික). They are lexical facts, not productive rules | SOFT | M | 05:SN-001…014 |

---

## 6. Spelling distinctions (sound-alike groups) — lexical, not rule-based

| ID | Rule | Kind | Conf | Sources |
|---|---|---|---|---|
| G-SP-01 | **These groups are pronounced alike:** {ක ඛ} {ග ඝ} {ච ඡ} {ජ ඣ} {ට ඨ} {ඩ ඪ} {ත ථ} {ද ධ} {ප ඵ} {බ භ} {න ණ} {ල ළ} {ස ශ ෂ} {ඤ ඥ}. Sound cannot pick the letter; a corpus-ranked lexicon must (one study reached 82% with ranking alone) | SOFT | H | 01:INV-023, 05:G2P-010, 05:SP-003…006 |
| G-SP-02 | **ණ:** after ර / ෂ / ඍ in nouns, unless a dental, palatal, retroflex, ල, ශ or ස comes between (the *ṇatva* rule); before ට/ඩ; in honorifics (-ආණ, -අණි); in past/passive forms (-ඉණි, -උණු) | SOFT | H | 04:NS-051…060, 05:SP-003 |
| G-SP-03 | **න:** in native verbs even after ර (මරන ≠ මරණ); before dentals and ස; after ස/ශ; in geminates; at compound boundaries | SOFT | H | 04:NS-056/061…063, 05:SP-003 |
| G-SP-04 | **ළ:** in past forms of ර-roots (කර → කළ); the prefix පිළි-; "small / young" words (ළමා); the first l of an l…l noun; before a sanyaka (M); Pali/Sanskrit retroflex reflexes (පොළොව) | SOFT | H | 04:NS-071…079, 05:SP-004 |
| G-SP-05 | **ස / ශ / ෂ:** native words use ස. **ශ** with palatals, before ව, in ශ්‍ර, and first of two sibilants. **ෂ** before retroflexes, in ක්ෂ, after vowels other than a/aa before k/p (ruki), and in -ඉෂ්ඨ. **ස** before dentals | SOFT | H | 04:NS-080…087, 05:SP-005 |
| G-SP-06 | Aspirates have **no rule**; they are learned per word. Some words have accepted variants (කථා/කතා) | SOFT | H | 05:SP-006 |
| G-SP-07 | **Vowel length is the commonest error class.** The verbal noun ending is long -ීම (කිරීම) | SOFT | H | 02:VS-033, 05:SP-007 |
| G-SP-08 | Pairs that differ in meaning must stay distinct: කණ/කන, වණ/වන, කල/කළ, පල/පළ, මරණ/මරන | SOFT | H | 04:§6, 05:SP-003/004 |

---

## 7. Writing Sinhala in Latin script (informal romanization)

Measured from the Dakshina corpus of native-speaker romanizations; see `06-romanization.md`.

| ID | Finding | Conf | Sources |
|---|---|---|---|
| G-TY-01 | `th` = ත and `t` = ට are near-universal (93–99%) | H | 06:RS-001 |
| G-TY-02 | ද is written `d` (99%); ධ is written `dh` | H | 06:RS-002/003 |
| G-TY-03 | ී is written `ee` 40% of the time and ූ is written `oo` 23% | H | 06:RS-006/007 |
| G-TY-04 | Vowel length is rarely marked: ා is written `a` 97% of the time | H | 06:RS-009 |
| G-TY-05 | Informal chat drops vowels (`nthi`, `mta`); only a lexicon or fuzzy matching recovers them | H | 06:RS-010 |
| G-TY-06 | ඳ ඹ ඟ are written `nd` `mb` `ng` (ඳ = `nd` 90%) and ං is written `n` (92%) | H | 06:RS-012/014 |
| G-TY-07 | ඇ is written `e` or `a`, rarely `ae` | H | 06:RS-008 |
| G-TY-08 | Retroflex ණ / ළ are never distinguished in informal writing (always `n`, `l`) | H | 06:RS-025 |
| G-TY-09 | Schwa [ə] is written `a` (sometimes `e`): karanawa / keranawa = කරනවා. Ordered schwa rules (98% accurate) predict it | H | 05:G2P-001…009, 03:HC-011 |
| G-TY-10 | `w` and `v` both stand for ව; `w` is preferred (73%) | H | 06:RS-011 |

---

## 8. Loanword conventions

| ID | Rule | Conf | Sources |
|---|---|---|---|
| G-LW-01 | f → ෆ (older loans ප: කෝපි) | H | 05:LW-001, 01:INV-022 |
| G-LW-02 | v/w → ව; z → ස; ʒ → ජ; θ → ත | M | 05:LW-002/006/008 |
| G-LW-03 | æ → ඇ or ඈ (monosyllables tend to ඈ: ෆෑන්, බෑග්; polysyllables ඇ: බැංකුව). Both occur | M | 05:LW-003 |
| G-LW-04 | ɒ → ඔ; əʊ / ɔː → ඕ; English schwa and -er → අ / -අර් | H | 05:LW-004/005 |
| G-LW-05 | sh → ෂ (popular), sometimes ශ; x → ක්ස් (**never ක්ෂ**); -ng → ං (ඉංග්‍රීසි) | M | 05:LW-007/009/012 |
| G-LW-06 | Loans keep a final hal (බස්, ෆෝන්). Literary forms add -ය/-ව (බෝලය, නෝට්ටුව) | H | 05:LW-011 |

---
## 9. A phonetic romanization built on these rules

`07-phonetic-romanization.md` specifies a phonetic romanization (conventions R-01…R-15)
that encodes every rule above: it can produce all 791 letter forms the rules allow and,
checked exhaustively, never produces a forbidden sequence.

---

## 10. Open gaps and conflicts

| # | Gap | Where it matters |
|---|---|---|
| 1 | NIE textbooks, the final SLS 1134:2004/2011 texts and the Sinhala Lekhana Rīthiya (1989) were **not reachable**. School-grammar rules rest on agreeing secondary sources | G-SP-*, G-HC-07, alphabet counts |
| 2 | The 41 × 17 validity table is a synthesis, **not a corpus count** | G-VS-13 / validity.json |
| 3 | Touching-letter and yansaya-with-repaya encodings changed between SLS drafts | G-EN-08, G-HC-14 |
| 4 | ම්‍ර / න්‍ර / ල්‍ර have no attestation in a Sinhala source | G-HC-12, R-07 |
| 5 | How ං before ය ර ල ව ශ ස හ is actually pronounced | G-NS-02/03 |

**Recommended next step:** count consonant + sign and cluster bigrams in a Sinhala corpus (Wikipedia
dump or UCSC 10M). That turns validity.json from a synthesis into measured data, and it gives the disambiguation layer a better lexicon.

---

