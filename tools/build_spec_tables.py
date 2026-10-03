"""Regenerate the romanization tables inside docs/07-phonetic-romanization.md.

    python tools/build_spec_tables.py

Replaces the text between the <!-- tables:start --> and <!-- tables:end --> markers
with tables built from src/sinhala_orthography/data/*.json.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "sinhala_orthography" / "data"
DOC = ROOT / "docs" / "07-phonetic-romanization.md"
START, END = "<!-- tables:start -->", "<!-- tables:end -->"


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def grouped(rows, letter_index, seq_index=0):
    out = {}
    for r in rows:
        out.setdefault(r[letter_index], []).append(r)
    return out


def main():
    cons = load("consonants.json")
    vows = load("vowels.json")
    specials = load("specials.json")

    lines = ["### Consonants", "",
             "A consonant written without a following vowel takes hal (්): `k` → ක්, `ka` → ක.", "",
             "| Letter | Romanization | Notes |", "|:-:|---|---|"]
    order = [c[1] for c in cons]
    seen = []
    for letter in order:
        if letter in seen:
            continue
        seen.append(letter)
        rows = [c for c in cons if c[1] == letter]
        seqs = " · ".join(f"`{r[0]}`" for r in rows)
        notes = "; ".join(sorted({r[3] for r in rows if r[3]} | ({"archaic option"} if any(r[2] == "archaic" for r in rows) else set())))
        lines.append(f"| **{letter}** | {seqs} | {notes} |")

    lines += ["", "### Vowels", "",
              "The independent letter is used at the start of a word; after a consonant the vowel is written as a sign.", "",
              "| Vowel | Independent | Sign | Romanization | Notes |", "|---|:-:|:-:|---|---|"]
    seen = []
    for r in vows:
        if r[1] in seen:
            continue
        seen.append(r[1])
        rows = [v for v in vows if v[1] == r[1]]
        sign = "*(inherent)*" if r[3] == "" else "◌" + r[3]
        notes = "; ".join(sorted({v[5] for v in rows if v[5]} | ({"archaic option"} if any(v[4] == "archaic" for v in rows) else set())))
        lines.append(f"| {r[1]} | {r[2]} | {sign} | {' · '.join(f'`{v[0]}`' for v in rows)} | {notes} |")

    lines += ["", "### Signs and joins", "", "| Output | Romanization | Notes |", "|:-:|---|---|"]
    for s in specials:
        out = "touching letters (C ZWJ ් C)" if s[1] == "touch" else s[1]
        lines.append(f"| {out} | `{s[0]}` | {s[3]}{'; archaic option' if s[2] == 'archaic' else ''} |")

    doc = DOC.read_text(encoding="utf-8")
    a, b = doc.index(START) + len(START), doc.index(END)
    DOC.write_text(doc[:a] + "\n\n" + "\n".join(lines) + "\n\n" + doc[b:], encoding="utf-8")
    print(f"tables: {len(set(order))} consonants, {len(seen)} vowels, {len(specials)} signs")


if __name__ == "__main__":
    main()
