"""Write the golden files that keep the JavaScript port (js/) identical to the Python package.

    python tools/build_js_golden.py

js/test/golden/romanization.jsonl.gz: [options, input, to_sinhala, sound_key, normalize(output without ZWJ)]
  for every romanization of 1 or 2 sequences (plus a space) under each option set, a fixed
  random sample of 3-sequence inputs, the unit-test cases and some sentences.
js/test/golden/lexicon.txt and js/test/golden/candidates.jsonl: a synthetic word-frequency list
  and the Python candidates() for a set of queries, exact and partial.
js/test/golden/styled.jsonl: restyle() of the lexicon words and candidates() under each option
  that changes spelling.
js/test/golden/entries.json: inventory.entries().

Rerun after any change to src/sinhala_orthography/; the JS tests must then pass unchanged.
"""
import gzip
import itertools
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tests"))
from sinhala_orthography import Lexicon, candidates, entries, normalize, restyle, sound_key, to_sinhala  # noqa: E402
from sinhala_orthography import romanization  # noqa: E402
from test_romanization import CASES, SETTINGS  # noqa: E402

OUT = ROOT / "js" / "test" / "golden"
ZWJ = "‍"
OPTION_SETS = {
    "default": {},
    "repayaZwj": {"repaya_zwj": True},
    "classical": {"classical": True},
    "archaic": {"archaic": True},
    "rakaransayaU": {"rakaransaya_u": True},
    "retroflexD": {"retroflex_d": True},
}
PY = {"repayaZwj": "repaya_zwj", "rakaransayaU": "rakaransaya_u", "archaic": "archaic", "classical": "classical",
      "retroflexD": "retroflex_d"}
SENTENCES = [
    "shrii lankaava", "aayuboovan oyaata kohomada", "vidyaava saha karma kaarya", "lait kauda",
    "kruura mrudu gruup", "kazda saha kanda", "akShara siMhala", "mama gedhara yanavaa.",
    "2026 okthoobar 4", "ammaa, thaaththaa!", "Xa kaX kax x zzz z", "AuShadha pAudgalika",
    "dham+ma k~l ka~n RR", "naeththam, honda?", "eyaa ena kota mama giyaa", "ශ්‍රී lanka",
]


def js_options(py_opts):
    return {k: True for k, v in PY.items() if py_opts.get(v)}


def inputs(archaic, rng):
    pool = [k for k, _ in romanization._SEQUENCES[archaic]] + [" ", "?"]
    yield from pool
    yield from ("".join(c) for c in itertools.product(pool, repeat=2))
    for _ in range(3000):
        yield "".join(rng.choice(pool) for _ in range(3))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rng = random.Random(20261004)
    rows, seen = [], set()

    def add(name, opts, src):
        if (name, src) in seen:
            return
        seen.add((name, src))
        out = to_sinhala(src, **opts)
        rows.append([name, src, out, sound_key(out), normalize(out.replace(ZWJ, ""))])

    for name, opts in OPTION_SETS.items():
        for src in inputs(opts.get("archaic", False), rng):
            add(name, opts, src)
        for src in SENTENCES:
            add(name, opts, src)
        for roman, _, _ in CASES:
            add(name, opts, roman)
    for roman, opts, _, _ in SETTINGS:
        name = next(n for n, o in OPTION_SETS.items() if o == opts)
        add(name, opts, roman)
    text = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    with open(OUT / "romanization.jsonl.gz", "wb") as f:      # mtime=0: the same rows give the same bytes
        with gzip.GzipFile(fileobj=f, mode="wb", mtime=0, filename="") as gz:
            gz.write(text.encode("utf-8"))

    # A synthetic frequency list: converter outputs plus sound-alike variants, with random counts.
    swaps = [("න", "ණ"), ("ල", "ළ"), ("ස", "ශ"), ("ද", "ධ"), ("ත", "ථ"), ("ි", "ී"), ("ු", "ූ"), ("න්ද", "ඳ")]
    pool = [k for k, _ in romanization._SEQUENCES[False]]
    romans = sorted({"".join(rng.choice(pool) for _ in range(rng.randint(2, 4))) for _ in range(1500)})
    romans += [r for r, _, _ in CASES] + ["honda", "kanda", "kala", "kaLa", "mala", "sinhala", "lankaava"]
    words = {}
    for roman in romans:
        w = to_sinhala(roman)
        if " " in w or not w.strip():
            continue
        words[w] = rng.randint(1, 5000)
        for a, b in swaps:
            if a in w and rng.random() < 0.5:
                words[w.replace(a, b, 1)] = rng.randint(1, 5000)
        if ZWJ in w and rng.random() < 0.3:
            words[w.replace(ZWJ, "")] = rng.randint(1, 50)       # a ZWJ-less variant, kept as written (the list has ZWJ)
    lex_path = OUT / "lexicon.txt"
    lex_path.write_text("".join(f"{w}\t{n}\n" for w, n in words.items()), encoding="utf-8", newline="\n")
    lex = Lexicon(lex_path)
    with open(OUT / "candidates.jsonl", "w", encoding="utf-8", newline="\n") as f:
        queries = sorted(set(romans))[:1200]
        for q in queries:
            f.write(json.dumps([q, False, candidates(lex, q, limit=8)], ensure_ascii=False) + "\n")
            f.write(json.dumps([q[: max(1, len(q) - 2)], True, candidates(lex, q[: max(1, len(q) - 2)], limit=8, partial=True)],
                               ensure_ascii=False) + "\n")
    with open(OUT / "styled.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for name in ("repayaZwj", "classical", "rakaransayaU", "retroflexD"):
            opts = OPTION_SETS[name]
            for w in words:
                f.write(json.dumps(["R", name, w, restyle(w, **opts)], ensure_ascii=False) + "\n")
            for q in queries[:400]:
                for partial in (False, True):
                    f.write(json.dumps(["D", name, q, partial, candidates(lex, q, limit=8, partial=partial, **opts)],
                                       ensure_ascii=False) + "\n")
    (OUT / "entries.json").write_text(json.dumps(entries(), ensure_ascii=False), encoding="utf-8", newline="\n")
    print(f"{len(rows):,} romanizations, {len(words):,} lexicon words, {2 * len(queries):,} candidate queries")


if __name__ == "__main__":
    main()
