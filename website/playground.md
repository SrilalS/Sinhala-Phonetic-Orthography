---
layout: page
title: Playground
description: Convert a phonetic romanization to Sinhala script with the reference implementation, running in your browser.
---

<div class="tool-page">

<h1>Playground</h1>
<p class="lede">
Type Sinhala in Latin letters and get Sinhala script. This page runs the converter in your browser
with the <a href="./reference/python#javascript-and-typescript">JavaScript package</a>, which gives exactly
the same output as the Python reference <code>to_sinhala()</code> (a golden test compares them on more than
50,000 inputs).
The romanization is specified in <a href="./research/phonetic-romanization">07 · Phonetic romanization</a>.
</p>

<ClientOnly>
  <Playground />
</ClientOnly>

</div>
