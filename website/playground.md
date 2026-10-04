---
layout: page
title: Playground
description: Convert a phonetic romanization to Sinhala script with the reference implementation, running in your browser.
---

<div class="tool-page">

<h1>Playground</h1>
<p class="lede">
Type Sinhala in Latin letters and get Sinhala script. This page runs the reference converter
<code>to_sinhala()</code> from the Python package, unchanged, in your browser via
<a href="https://pyodide.org">Pyodide</a>, so what you see is exactly what the package does.
The romanization is specified in <a href="./research/phonetic-romanization">07 · Phonetic romanization</a>.
</p>

<ClientOnly>
  <Playground />
</ClientOnly>

</div>
