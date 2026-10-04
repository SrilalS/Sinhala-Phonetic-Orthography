# දත්ත ගොනු

`data/` හි ඇති JSON ගොනු තුන සිංහල අකුරු රූප 923 ම විස්තර කරයි. එක් එක් රූපයට එක `id` එකක් ඇති අතර
ගොනු තුනම එය බෙදා ගනී. එබැවින් ඒවා `id` මගින් එකට සම්බන්ධ කළ හැක. [අකුරු ගවේෂකයෙන්](/si/explorer) ඒවා බලන්න.

| ගොනුව | ජනනය කරන්නේ | අන්තර්ගතය |
|---|---|---|
| [`letters.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/letters.json) | `tools/build_data.py` | අක්ෂර මාලාව: එක් එක් රූපයේ පෙළ සහ කේත ලක්ෂ්‍ය |
| [`validity.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/validity.json) | `tools/build_data.py` | එක් එක් රූපයේ තත්ත්වය සහ ඊට පදනම් වූ නීති |
| [`romanization-coverage.json`](https://github.com/SrilalS/Sinhala-Phonetic-Orthography/blob/main/data/romanization-coverage.json) | `tools/check_romanization.py` | එක් එක් විකල්ප කට්ටලය යටතේ එක් එක් රූපය නිපදවන රෝමානු ආදාන |

## හැඳුනුම් (IDs)

| වර්ගය | ගණන | ID | උදාහරණ |
|---|---:|---|---|
| ස්වතන්ත්‍ර ස්වරය | 18 | `vowel.<vowel>` | `vowel.aa` ආ |
| ලකුණ | 3 | `sign.<name>` | `sign.anusvara` ං |
| ව්‍යඤ්ජන රූපය | 41 × 19 | `<consonant>.<vowel>` | `ka.hal` ක්, `ka.a` ක, `ka.ru` කෘ |
| සංයුක්ත අකුර | 41 × 3 | `<consonant>.<conjunct>` | `ka.yansaya` ක්‍ය, `ka.rakaransaya` ක්‍ර, `ka.repaya` ර්‍ක |

ස්වර IDs: `hal` `a` `aa` `ae` `aee` `i` `ii` `u` `uu` `ru` `ruu` `ilu` `iluu` `e` `ee` `ai` `o` `oo` `au`.
ව්‍යඤ්ජන IDs [01 · අක්ෂර මාලාව](/si/research/inventory) අනුගමනය කරයි. ඒවා `ka` ක සිට `fa` ෆ දක්වා යුනිකේත අනුපිළිවෙළින් ඇත.

## `letters.json`

```json
{ "id": "ka.ru", "kind": "syllable", "text": "කෘ", "consonant": "ka", "vowel": "ru",
  "codepoints": ["U+0D9A", "U+0DD8"] }
```

`kind` හි අගය `vowel`, `sign`, `syllable` හෝ `conjunct` වේ. සංයුක්ත අකුරුවල `vowel` වෙනුවට `conjunct` ඇත.

## `validity.json`

```json
{ "id": "ka.u", "text": "කු", "status": "valid", "shape": "hook-u", "rules": ["G-VS-13"] }
```

| `status` | ගණන | තේරුම |
|---|---:|---|
| `valid` | 380 | සාමාන්‍ය භාවිතයේ ඇත |
| `loan` | 193 | වලංගුය, නමුත් ප්‍රායෝගිකව සංස්කෘත හෝ පාලි (තත්සම) වචනවල පමණක් යෙදේ |
| `rare` | 101 | වලංගු කේතනයකි, නමුත් භාවිතය ඉතා අඩු හෝ පුරාතනය |
| `unattested` | 117 | එය යෙදෙන වචනයක් හමු වී නැත, නමුත් කිසිදු නීතියක් එය තහනම් නොකරයි |
| `never` | 132 | අනිවාර්ය නීතියකින් තහනම්ය (G-HC-06, G-HC-07, G-HC-08, G-HC-14, G-VS-08) |

`shape` මගින් විශේෂ ආකාරයකට අඳින අක්ෂර රූප සලකුණු කරයි. කේතනය නොවෙනස්ය (G-EN-11):
`hook-u`, `irregular` (u/uu සමඟ ර සහ ළ, ae/aee සමඟ ර), `tail-loss` සහ `alt-hal`. අනෙක් රූප 897 සඳහා
එහි අගය `null` ය.

ව්‍යඤ්ජන × ස්වර තත්ත්වයන් [02 · පිලි §8](/si/research/vowel-signs) හි 41 × 17 වගුවෙන් ගනී. ඒවා
පෙළ සංග්‍රහයක ගණනයක් නොව මූලාශ්‍රවල සංශ්ලේෂණයකි. ව්‍යතිරේකය ෘ / ෲ තීරුය: ඒවා වචන මිලියන 2.1 ක ලැයිස්තුවකට
එරෙහිව පරීක්ෂා කළේය (VS-035).

## `romanization-coverage.json`

```json
{ "id": "ka.repaya", "text": "ර්‍ක", "status": "valid",
  "default": [], "repaya_zwj": ["rka", "rca"], "classical": [], "archaic": [],
  "rakaransaya_u": [] }
```

එක් එක් විකල්ප කට්ටලය, රූපය නිපදවන රෝමානු ආදාන හතරක් දක්වා, කෙටිම ආදානය මුලින් සිටින සේ ලැයිස්තු කරයි.
ලකුණු ක ට පසුව ලියයි (`kax` → කං). වචනයක මුලට යෙදිය නොහැකි අකුරු අ ට පසුව ලියයි (`azda` → අඳ).
හිස් ලැයිස්තුවක් යනු එම විකල්ප කට්ටලයට එම රූපය නිපදවිය නොහැකි බවයි. ZWJ රේඵයට `repaya_zwj` ද, පුරාතන අකුරුවලට
`archaic` ද අවශ්‍යය. `never` නොවන රූප 791 ම කිසියම් විකල්ප කට්ටලයක් යටතේ නිපදවිය හැක.
