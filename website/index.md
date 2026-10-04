---
layout: home

hero:
  name: Sinhala Phonetic Orthography
  text: How Sinhala words are built in writing
  tagline: A sourced study of the letter inventory, vowel signs, conjuncts, nasals, phonotactics and sandhi, with a phonetic romanization whose output provably obeys the rules.
  image:
    src: /logo.svg
    alt: The Sinhala letter a
  actions:
    - theme: brand
      text: Read the rules
      link: /rules
    - theme: alt
      text: Try the converter
      link: /playground
    - theme: alt
      text: Explore letter forms
      link: /explorer

features:
  - icon: 🔗
    title: ZWJ is spelling, not rendering
    details: Yansaya and rakaransaya need ZWJ, and its position picks conjunct or touching style. Repaya and other conjuncts are optional.
    link: /rules#g-en-08
    linkText: G-EN-07 … 09
  - icon: ⚠️
    title: ෛ has no canonical decomposition
    details: ෙ + ෙ looks the same on screen but is a different, silently wrong string.
    link: /rules#g-en-03
    linkText: G-EN-03
  - icon: 👃
    title: Sanyaka letters never take hal
    details: ඟ ඦ ඬ ඳ ඹ never take hal and never start a word. Whether a word uses one is lexical, so කඳ "trunk" ≠ කන්ද "hill".
    link: /rules#g-hc-06
    linkText: G-HC-06
  - icon: 👂
    title: About 14 letter groups sound alike
    details: Aspirates, ණ/න, ළ/ල, ශ/ෂ/ස and more. No rule can recover their spelling from sound; a frequency lexicon has to.
    link: /rules#g-sp-01
    linkText: G-SP-01
  - icon: 🌊
    title: Two vowels are never written side by side
    details: Hiatus takes a ය or ව glide. "ai" is අයි, not අඉ, and ෛ / ෞ belong to Sanskrit loans.
    link: /rules#g-vs-06
    linkText: G-VS-06
  - icon: ⌨️
    title: Informal romanization isn't formal
    details: In informal writing, d is ද 99% of the time, ee means ී 40% of the time, and vowel length is rarely marked.
    link: /research/romanization-systems
    linkText: Measured usage
---

<div class="home-body vp-doc">

## What's here

| | | |
|---|---|---|
| 🧾 | [Consolidated rule set](/rules) | 88 deduplicated rules, each marked **HARD** (invariant), **SOFT** (tendency) or **STYLE** (accepted variants), each citing its sources |
| 📚 | [Seven topic studies](/research/inventory) | About 250 numbered rules with evidence from Unicode, SLS 1134, the ICANN Sinhala script panel, linguistics and NLP papers, and school grammar material |
| ✍️ | [Playground](/playground) | The reference converter, running in your browser. Type a romanization and see each step |
| 🔤 | [Letter explorer](/explorer) | All 923 letter forms, their validity status, the rules behind it and how to type each one |
| 🐍 | [Python & JS packages](/reference/python) | `to_sinhala` / `toSinhala`, the inventory and a frequency-based disambiguator. No dependencies |
| 📈 | [Verification](/reference/verification) | Every allowed form is producible, and 3.34 million inputs produce no rule violation |

## Quick start

```python
from sinhala_orthography import to_sinhala

to_sinhala("lankaava")   # 'ලංකාව'
to_sinhala("kruura")     # 'කෲර'
to_sinhala("lait")       # 'ලයිට්'
```

Requires Python 3.9 or later and nothing else. See the [Python reference](/reference/python).

</div>

<style>
.home-body { max-width: 1152px; margin: 64px auto 0; padding: 0 24px; }
.home-body h2 { font-size: 24px; font-weight: 700; margin: 40px 0 16px; letter-spacing: -0.01em; }
.home-body table { display: table; width: 100%; }
.home-body td:first-child { width: 36px; font-size: 18px; }
.home-body td:nth-child(2) { white-space: nowrap; font-weight: 600; }
.home-body thead { display: none; }
@media (max-width: 640px) { .home-body { padding: 0 16px; } .home-body td:nth-child(2) { white-space: normal; } }
</style>
