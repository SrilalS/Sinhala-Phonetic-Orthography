# සිංහල පරිවර්තනය

මෙම ෆෝල්ඩරයේ ඇත්තේ `docs/` හි ලේඛනවල සිංහල පරිවර්තනයයි. **ඉංග්‍රීසි ලේඛන මූලාශ්‍රයයි.**
පරිවර්තනයක් ඉංග්‍රීසි පිටපතට වඩා වෙනස් නම්, ඉංග්‍රීසි පිටපත නිවැරදි යැයි සලකන්න.

This folder holds Sinhala translations of the documents in `docs/`. The English files are
authoritative. Each translation starts with a comment that records the hash of the English file it
was translated from; `python tools/check_translations.py` lists the translations whose English
source has changed since.

---

## පරිවර්තන මාර්ගෝපදේශය (Translation guide)

### ලේඛන විලාසය

- නූතන, පැහැදිලි **ලිඛිත සිංහල** භාවිත කරන්න: ව්‍යාකරණය නිවැරදි විය යුතු නමුත් පැරණි හෝ
  අධික සංස්කෘත වචන වෙනුවට අද භාවිත වන සරල වචන තෝරන්න.
- කෙටි වාක්‍ය ලියන්න. කර්තෘ කාරක වාක්‍ය (“ලියයි”, “භාවිත කරයි”) කර්ම කාරක වාක්‍යවලට (“ලියනු ලැබේ”)
  වඩා කැමති වන්න.
- වාක්‍යයේ අවසාන ක්‍රියාපදය කර්තෘ සමඟ ගැළපිය යුතුය (“නීති … වේ”, “නීතියක් … වෙයි”).
- තාක්ෂණික පදයක් පළමු වරට යෙදෙන තැන ඉංග්‍රීසි පදය වරහන් තුළ දෙන්න: “රකාරාංශය (rakaransaya)”.
- එම් ඉරි (U+2014) භාවිත නොකරන්න. කොමාවක්, කොලනයක්, වරහන් හෝ නව වාක්‍යයක් යොදන්න.

### වෙනස් නොකළ යුතු දේ

- නීති හැඳුනුම් (`G-VS-15`, `VS-035`, `02:VS-007`, `R-06`, `C-13`) සහ ශීර්ෂවල `### VS-035:` ආකෘතිය.
- කේත, `backtick` තුළ ඇති සියල්ල, ගොනු මාර්ග, URL, යුනිකේත කේත ලක්ෂ්‍ය (U+0DD8), සංඛ්‍යා.
- රෝම අකුරු උදාහරණ (`kruura`), සිංහල උදාහරණ වචන, මූලාශ්‍ර නාම, ලේඛක නාම, ලිපි මාතෘකා.
- දත්ත අගයන්: `valid`, `loan`, `rare`, `unattested`, `never`.

### පද මාලාව (Glossary)

| English | සිංහල |
|---|---|
| rule / rule set | නීතිය / නීති මාලාව |
| HARD · SOFT · STYLE | **අනිවාර්ය** · **නැඹුරුව** · **විකල්ප** |
| confidence H · M · L | විශ්වාසය ඉහළ · මධ්‍යම · අඩු |
| finding | සොයාගැනීම |
| source | මූලාශ්‍රය |
| evidence | සාක්ෂි |
| orthography / spelling | අක්ෂර වින්‍යාසය |
| letter / letter form | අකුර / අකුරු රූපය |
| vowel / independent vowel | ස්වරය / ස්වතන්ත්‍ර ස්වරය |
| consonant | ව්‍යඤ්ජනය |
| vowel sign (pilla) | ස්වර ලකුණ (පිල්ල), බහු. පිලි |
| inherent vowel a | ව්‍යඤ්ජනයට ආවේණික “අ” ස්වරය |
| hal (virama, al-lakuna) | හල් ලකුණ (්), “හල් කිරීම” |
| conjunct / cluster | සංයුක්ත අකුර / ව්‍යඤ්ජන පොකුර |
| bandi akuru | බැඳි අකුරු |
| touching letters | ස්පර්ශ අකුරු (touching letters) |
| yansaya · rakaransaya · repaya | යංශය · රකාරාංශය · රේඵය |
| anusvara · visarga · candrabindu | අනුස්වාරය (බින්දුව) · විසර්ගය · චන්ද්‍රබින්දුව |
| ayogavaha | අයෝගවාහ |
| sanyaka (prenasalized) | සඤ්ඤක අකුරු |
| aspirate / unaspirated | මහාප්‍රාණ / අල්පප්‍රාණ |
| retroflex · dental · velar · palatal · labial | මූර්ධජ · දන්තජ · කණ්ඨජ · තාලුජ · ඕෂ්ඨජ |
| nasal | නාසික |
| glide (ය, ව) | අර්ධ ස්වරය |
| hiatus (two vowels side by side) | ස්වර දෙකක් එක ළඟ යෙදීම (hiatus) |
| schwa [ə] | අවධාරණය නොවන [ə] ස්වරය (schwa) |
| vowel length | ස්වර දිග |
| phonotactics | ශබ්ද සංයෝජන නීති (phonotactics) |
| sandhi | සන්ධි |
| loanword / tatsama / tadbhava | ණය වචනය / තත්සම / තද්භව |
| Sanskrit · Pali | සංස්කෘත · පාලි |
| pure / mixed Sinhala | ශුද්ධ සිංහල / මිශ්‍ර සිංහල |
| sound-alike letters | එක ලෙස උච්චාරණය වන අකුරු |
| romanization | රෝමානුකරණය (සිංහල ලතින් අකුරින් ලිවීම) |
| phonetic romanization | ශබ්දානුසාරී රෝමානුකරණය |
| informal romanization ("Singlish") | අවිධිමත් රෝමානුකරණය |
| sequence (Latin letters for one letter) | අනුක්‍රමය |
| converter / reference implementation | පරිවර්තකය / යොමු ක්‍රියාත්මක කිරීම |
| option | විකල්පය |
| Unicode / code point | යුනිකේත / කේත ලක්ෂ්‍යය |
| encoding / encode | කේතනය / කේතනය කරනවා |
| logical order | තාර්කික අනුපිළිවෙළ |
| precomposed / decomposed | පූර්ව සංයුක්ත / වියෝජිත |
| normalization (NFC) | සාමාන්‍යකරණය (NFC) |
| ZWJ / ZWNJ | ZWJ (ශුන්‍ය පළල සම්බන්ධකය) / ZWNJ |
| glyph / font | අක්ෂර රූපය / අකුරු මුහුණත (font) |
| render / rendering | දර්ශනය කිරීම |
| corpus / word list / frequency | පෙළ සංග්‍රහය (corpus) / වචන ලැයිස්තුව / සංඛ්‍යාතය |
| lexicon | ශබ්දකෝෂය (lexicon) |
| attested / unattested | භාවිතයේ හමු වූ / භාවිතයේ හමු නොවූ |
| valid · loan · rare · unattested · never | වලංගු · ණය වචන · දුර්ලභ · හමු නොවූ · තහනම් |
| archaic / obsolete | පුරාතන / භාවිතයෙන් ඉවත් වූ |
| coverage / violation | ආවරණය / උල්ලංඝනය |
| open gap / conflict | විසඳා නැති ප්‍රශ්නය / ගැටුම |
| convention | සම්මුතිය |
| default | පෙරනිමි |
| alias | අමතර ලිවීම (alias) |
| capital / lower-case letter | ලොකු අකුර / කුඩා අකුර |
| ambiguous / ambiguity | අපැහැදිලි / අපැහැදිලිතාව |
| productive (rule or pattern) | නව වචනවලටද අදාළ වන (productive). “ඵලදායී” නොවේ |
| geminate | ද්විත්ව ව්‍යඤ්ජනය |
| reduced form | සංක්ෂිප්ත රූපය |
| shaping (font) | හැඩගැන්වීම |
| local test (checks made for this study) | මෙහි කළ පරීක්ෂණය |
| open (claim not yet confirmed; `[open]`, **Open**) | විසඳා නැත (`[විසඳා නැත]`, **විසඳා නැත**) |
| NLPC n (a word's count in the NLPC list) | NLPC n |

### නීතියක ක්ෂේත්‍ර නාම (Rule field labels)

| English | සිංහල |
|---|---|
| Statement | ප්‍රකාශය |
| Examples | උදාහරණ |
| Exceptions | ව්‍යතිරේක |
| Applies to | අදාළ වන්නේ |
| Confidence | විශ්වාසය |
| Source(s) | මූලාශ්‍රය / මූලාශ්‍ර |
