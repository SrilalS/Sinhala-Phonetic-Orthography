# Python පැකේජය

`sinhala_orthography` පැකේජයේ අක්ෂර මාලාව, රෝමානුකරණ පරිවර්තකය සහ වචන සංඛ්‍යාතය අනුව නිවැරදි
අක්ෂර වින්‍යාසය තෝරන මෙවලමක් ඇත. එයට Python 3.9 හෝ ඊට පසු සංස්කරණයක් අවශ්‍ය වන අතර වෙනත් පැකේජ අවශ්‍ය නැත.

## ස්ථාපනය

ගබඩාව (repository) clone කර `src/` වෙතින් import කරන්න, නැතහොත් පැකේජය ස්ථාපනය කරන්න:

```sh
git clone https://github.com/SrilalS/Sinhala-Phonetic-Orthography
cd Sinhala-Phonetic-Orthography
pip install .
```

::: tip Windows කොන්සෝල
සිංහල පෙළ print කිරීමට පෙර `PYTHONIOENCODING=utf-8` සකසන්න.
:::

## රෝමානුකරණය පරිවර්තනය කිරීම

```python
from sinhala_orthography import to_sinhala

to_sinhala("lankaava")                  # 'ලංකාව'
to_sinhala("kruura")                    # 'කෲර'
to_sinhala("kruura", rakaransaya_u=True)  # 'ක්‍රූර'
to_sinhala("lait")                      # 'ලයිට්'
to_sinhala("akShara", classical=True)   # 'අක්‍ෂර'
to_sinhala("karma", repaya_zwj=True)    # 'කර්‍ම'
```

### `to_sinhala(source, archaic=False, repaya_zwj=False, classical=False, rakaransaya_u=False)`

රෝම අකුරින් ලියූ වචනයක් හෝ පෙළක් සිංහල අකුරුවලට පරිවර්තනය කරයි. අනුක්‍රම වගුවල නැති අක්ෂර (හිස්තැන්,
ඉලක්කම්, විරාම ලකුණු) වෙනසක් නැතිව ප්‍රතිදානයට යයි. සෑම ප්‍රතිදානයක්ම [නීති මාලාවේ](/si/rules) අනිවාර්ය
නීතිවලට අනුකූලය. අනුක්‍රම තුනක් දක්වා දිග සෑම ආදානයක් සඳහාම මෙය පරීක්ෂා කර ඇත
([සත්‍යාපනය](/si/reference/verification) බලන්න).

| විකල්පය | බලපෑම | සම්මුතිය |
|---|---|---|
| `archaic` | ඏ ඐ ෟ ෳ, තනි ඎ, ඁ, ඦ සහ ස්පර්ශ අකුරු සඳහා ඉඩ දෙයි | R-14 |
| `repaya_zwj` | රේඵය සාමාන්‍ය ර් + C වෙනුවට ර්‍ + C ලෙස ලියයි | R-08 |
| `classical` | සම්භාව්‍ය බැඳි අකුරු යුගල සඳහා ZWJ සංයුක්ත අකුරු යොදයි | R-10 |
| `rakaransaya_u` | C + r + u/uu, සුලබ C + ෘ/ෲ (කෲර) වෙනුවට රකාරාංශය + ු/ූ (ක්‍රූර) ලෙස ලියයි | R-06 |

`transliterate()` යනු එම ශ්‍රිතයම, එහි මුල් නමින්ය. අනුක්‍රම වගු
`src/sinhala_orthography/data/` හි (`consonants.json`, `vowels.json`, `specials.json`) ඇති අතර,
රෝමානුකරණයේ පිරිවිතර [07 · ශබ්දානුසාරී රෝමානුකරණය](/si/research/phonetic-romanization) හි ඇත.
[අත්හදා බැලීමේ පිටුවෙන්](/si/playground) එය උත්සාහ කරන්න.

## වචන ලැයිස්තුවක් භාවිතයෙන් නිවැරදි අක්ෂර වින්‍යාසය තේරීම

අකුරු කාණ්ඩ 14 ක් පමණ එක ලෙස උච්චාරණය වේ (G-SP-01). එබැවින් එක් රෝමානු ආදානයකින් සෑම විටම සම්මත
අක්ෂර වින්‍යාසය තෝරාගත නොහැක. `Lexicon` වචන සංඛ්‍යාත ලැයිස්තුවක් *ශබ්ද යතුර* (sound key) අනුව සුචිගත කරයි.
`candidates()` ආදානයට සමාන ශබ්ද යතුරක් ඇති වචන ශ්‍රේණිගත කරයි.

```python
from sinhala_orthography import Lexicon, candidates

lex = Lexicon("word-frequency-list.tsv")   # one "word<TAB>count" per line
candidates(lex, "honda")                   # ['හොඳ', ...]
candidates(lex, "hon", partial=True)       # completions of a word prefix
```

| ශ්‍රිතය | ප්‍රතිදානය |
|---|---|
| `candidates(lex, roman, limit=5, partial=False, **options)` | ශ්‍රේණිගත අක්ෂර වින්‍යාස. පරිවර්තකයේම අක්ෂර වින්‍යාසය සෑම විටම ඇතුළත්ය. රෝමානු ආදානයේ පැහැදිලි සලකුණක් (ලොකු අකුරක්, `z` උපසර්ගයක්, දෙගුණ කළ ස්වරයක් …) ඇති විට සහ එම අක්ෂර වින්‍යාසය වචනයක් නම්, එය පළමුව එයි |
| `sound_key(text)` | එක ලෙස ඇසෙන අක්ෂර වින්‍යාස ගැළපෙන සේ සරල කළ පෙළ: මහාප්‍රාණ → අල්පප්‍රාණ, ණ → න, ළ → ල, ශ/ෂ → ස, ස්වර දිග ඉවත් කර, සඤ්ඤක → නාසිකය + ස්පර්ශය. `sound_key("හොඳ")` හි අගය `'හොන්ද'` ය |
| `normalize(word)` | ZWJ ඉවත් වූ වචන ලැයිස්තු සඳහා, C ් ය සහ C ් ර හි අනිවාර්ය ZWJ නැවත යොදයි (ර ට පසු කිසි විටෙක නොයොදයි) |
| `Lexicon(path)` | `.count` (වචනය → සංඛ්‍යාතය), `.exact(key)`, `.prefix(key, limit=200)` |

[07](/si/research/phonetic-romanization) හි ඇගයීම සඳහා මොරටුව විශ්වවිද්‍යාලයේ NLPC
[Word Frequency List for Sinhala](https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala) භාවිත කළේය.
එය මෙම ගබඩාව සමඟ නැවත බෙදා හරින්නේ නැත.

## අක්ෂර මාලාව

```python
from sinhala_orthography import VOWELS, CONSONANTS, SIGNS, entries

len(entries())   # 923
entries()[30]    # {'id': 'ka.ru', 'kind': 'syllable', 'text': 'කෘ', 'consonant': 'ka',
                 #  'vowel': 'ru', 'codepoints': ['U+0D9A', 'U+0DD8']}
```

| නම | අන්තර්ගතය |
|---|---|
| `VOWELS` | හල් ලකුණ, ආවේණික අ සහ පිලි 17 සඳහා `(id, ස්වතන්ත්‍ර අකුර, පිල්ල)` |
| `CONSONANTS` | යුනිකේත අනුපිළිවෙළින් ව්‍යඤ්ජන 41 සඳහා `(id, අකුර)` |
| `SIGNS` | ං ඃ ඁ |
| `entries()` | [`data/letters.json`](/si/reference/data) හි මෙන්, සෑම අකුරු රූපයක්ම |

## මෙවලම්

```sh
python tools/build_data.py            # data/letters.json, data/validity.json
python tools/check_romanization.py    # coverage + exhaustive safety (about 20 s)
python tools/build_spec_tables.py     # tables in docs/07
python tools/check_translations.py    # Sinhala translations whose English source changed
python -m unittest discover tests     # set SINHALA_WORD_LIST to also run the lexicon tests
```
