"""Reproduce every corpus number quoted in docs/ from pinned public sources.

    python tools/corpus_counts.py            # download (once) and recount everything
    python tools/corpus_counts.py --offline  # use the cache only
    python tools/corpus_counts.py --lookup පිතෲ ෆෑන්   # NLPC tokens of words (exact, and with every ending)

Sources are pinned by commit, release or dump date and checked by hash. They are downloaded into
.cache/corpus/ (not committed; each source keeps its own license). The results go to
reports/corpus-counts.md. Aggregate numbers in docs/ cite a claim id there (CC-xx); a single word's
count is written "NLPC n" and can be checked with --lookup.

Standard library only. The Dakshina release is a 2 GB tar, of which only the Sinhala files are kept.
"""
import bz2
import hashlib
import io
import json
import re
import sys
import tarfile
import urllib.request
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tests"))
from sinhala_orthography import Lexicon, candidates, sound_key, to_sinhala  # noqa: E402

CACHE = ROOT / ".cache" / "corpus"
REPORT = ROOT / "reports" / "corpus-counts.md"
ZWJ, HAL = "‍", "්"
CONS = "ක-ෆ"
VELARS = "කඛගඝ"

NLPC_COMMIT = "1283550a338958136e27bc064a36a14e1ceb7de5"
SOURCES = {
    "nlpc": {
        "name": "NLPC Word Frequency List for Sinhala, word_frequency_list_2M (Fernando & Dias, ICON 2021)",
        "url": f"https://raw.githubusercontent.com/nlpcuom/Word-Frequency-List-for-Sinhala/{NLPC_COMMIT}/word_frequency_list_2M.zip",
        "file": "word_frequency_list_2M.zip",
        "sha256": "efae356f8e7b975a098d9dd006c210b30330057925e5441eea8a24b3ebcdfd6f",
        "pin": f"commit {NLPC_COMMIT[:12]}",
    },
    "siwiki": {
        "name": "Sinhala Wikipedia, pages-articles dump of 2026-10-01",
        "url": "https://dumps.wikimedia.org/siwiki/20261001/siwiki-20261001-pages-articles.xml.bz2",
        "file": "siwiki-20261001-pages-articles.xml.bz2",
        "sha256": "82a7e4e4705c2b984e1a750df5b565c153c9bef86d7cb20e473e46b7f787c859",   # sha1 82788f30… as published
        "pin": "dump 20261001",
    },
    "dakshina": {
        "name": "Dakshina dataset v1.0, Sinhala (Roark et al., LREC 2020)",
        "url": "https://storage.googleapis.com/gresearch/dakshina/dakshina_dataset_v1.0.tar",
        "file": "dakshina_si",   # a directory: only dakshina_dataset_v1.0/si/ is extracted
        "sha256": None,
        "pin": "release v1.0 (2020-05-27)",
        "files": {
            "romanized/si.romanized.rejoined.aligned.tsv": "1d4ef8d368301e43aac6799645b5a944cea158532d69d4f7eaed3a805ba6a655",
            "lexicons/si.translit.sampled.train.tsv": "50744bc60f11a0934d2e97e1655ff1f5b44c3e77ae5fe3db7948549e46d1e84e",
            "lexicons/si.translit.sampled.dev.tsv": "6a13f6436e66cd7e0515f540133164db0ffd6e71d3bc1f6c9b1f6a32c1770cda",
            "lexicons/si.translit.sampled.test.tsv": "116e21eb8ed6249623a2cb3793ef9235b8cf7e3979fed0b45d104b36f755a3b7",
        },
    },
}


# ---------------------------------------------------------------------------- fetching

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fetch(key, offline):
    src = SOURCES[key]
    path = CACHE / src["file"]
    if path.exists():
        if src["sha256"] and path.is_file() and sha256(path) != src["sha256"]:
            raise SystemExit(f"{path}: hash differs from the pinned {src['sha256']}")
        for name, digest in src.get("files", {}).items():
            if sha256(path / name) != digest:
                raise SystemExit(f"{path / name}: hash differs from the pinned {digest}")
        return path
    if offline:
        raise SystemExit(f"{path} is missing; run without --offline to download it")
    CACHE.mkdir(parents=True, exist_ok=True)
    print(f"downloading {src['url']}", file=sys.stderr)
    if key == "dakshina":
        with urllib.request.urlopen(src["url"]) as r, tarfile.open(fileobj=r, mode="r|") as tar:
            for m in tar:
                if m.isfile() and m.name.startswith("dakshina_dataset_v1.0/si/"):
                    out = path / m.name.split("/si/", 1)[1]
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out.write_bytes(tar.extractfile(m).read())
        return path
    tmp = path.with_suffix(".part")
    urllib.request.urlretrieve(src["url"], tmp)
    if src["sha256"] and sha256(tmp) != src["sha256"]:
        raise SystemExit(f"{src['url']}: hash differs from the pinned {src['sha256']}")
    tmp.rename(path)
    return path


# ---------------------------------------------------------------------------- NLPC list

def load_nlpc(path):
    """word → count. The list has "word POS count" lines; a word with several tags is summed."""
    count = Counter()
    with zipfile.ZipFile(path) as z, z.open("word_frequency_list_2M.si") as f:
        for line in io.TextIOWrapper(f, encoding="utf-8"):
            parts = line.split()
            if len(parts) >= 3 and parts[-1].isdigit():
                count[parts[0]] += int(parts[-1])
    return count


def prefix_sum(count, stem):
    return sum(n for w, n in count.items() if w.startswith(stem))


def nlpc_claims(count):
    claims = []
    total = sum(count.values())
    claims.append(("CC-01", "NLPC list size: word types and tokens", f"{len(count):,} types, {total:,} tokens",
                   "README of the list: 2,138,021 unique words, 122,998,105 words"))

    # --- ෘ / ෲ against rakaransaya + ු/ූ and the ැ/ෑ look-alike (02:VS-035)
    gaetta = re.compile(f"([{CONS}])([ෘෲ])")

    def variants(word):
        u = gaetta.sub(lambda m: m.group(1) + HAL + ZWJ + "ර" + ("ු" if m.group(2) == "ෘ" else "ූ"), word)
        ae = gaetta.sub(lambda m: m.group(1) + HAL + ZWJ + "ර" + ("ැ" if m.group(2) == "ෘ" else "ෑ"), word)
        return u, ae

    wins = Counter()
    for w in [w for w in count if gaetta.search(w)]:
        u, ae = variants(w)
        found = {"ෘ/ෲ": count[w], "්‍ර + ු/ූ": count.get(u, 0), "්‍ර + ැ/ෑ": count.get(ae, 0)}
        if sum(1 for n in found.values() if n) >= 2:
            wins[max(found, key=found.get)] += 1
    claims.append(("CC-02", "Words written with C + ෘ/ෲ that also occur in another spelling: which spelling is most frequent "
                   "(02:VS-035)", ", ".join(f"{k} {v}" for k, v in wins.most_common()),
                   "each word type with C + ෘ/ෲ is looked up as rakaransaya + ු/ූ and as rakaransaya + ැ/ෑ; "
                   "only words found in two or more spellings count"))
    rows = []
    for stem in ["කෲර", "සංස්කෘතික", "මෘදුකාංග", "සෘජු", "ගෲප්", "ගෘප්", "ශෘති", "භෲණ"]:
        u, ae = variants(stem)
        rows.append(f"{stem} {prefix_sum(count, stem):,} · {u} {prefix_sum(count, u):,} · {ae} {prefix_sum(count, ae):,}")
    claims.append(("CC-03", "The VS-035 table: tokens of each stem and its inflected forms (all words that start with it)",
                   "<br>".join(rows), "prefix sums; the three spellings of each stem"))

    # --- validity.json ru / ruu cells: tokens and types per consonant
    per = defaultdict(lambda: [0, 0])
    for w, n in count.items():
        for m in gaetta.finditer(w):
            key = m.group(1) + m.group(2)
            per[key][0] += n
            per[key][1] += 1
    top = sorted(per.items(), key=lambda kv: -kv[1][0])
    claims.append(("CC-04", "C + ෘ/ෲ per consonant: tokens / word types (02 §8, validity.json ru and ruu columns)",
                   ", ".join(f"{k} {t:,}/{y:,}" for k, (t, y) in top), "every occurrence in every word type; no misspellings removed"))

    # --- ෛ / ෞ against the glide spellings (07:R-05)
    def pair_ratio(sign, glide):
        rx = re.compile(f"([{CONS}]){sign}")
        sign_n = glide_n = 0
        for w, n in count.items():
            if rx.search(w):
                sign_n += n
                glide_n += count.get(rx.sub(lambda m: m.group(1) + glide, w), 0)
        return sign_n, glide_n
    def tokens(rx):
        r = re.compile(rx)
        return sum(n for w, n in count.items() if r.search(w))
    yi, ai_all, vu, au_all = (tokens(f"[{CONS}]{x}") for x in ("යි", "ෛ", "වු", "ෞ"))
    claims.append(("CC-05", "C + යි against C + ෛ, and C + වු against C + ෞ, over all words (07:R-05)",
                   f"යි {yi:,} vs ෛ {ai_all:,} ({yi / ai_all:.1f}:1); වු {vu:,} vs ෞ {au_all:,} ({vu / au_all:.1f}:1)",
                   "tokens of words containing the sequence: what a typed `ai` / `au` most often stands for"))
    ai, ai_glide = pair_ratio("ෛ", "යි")
    au, au_glide = pair_ratio("ෞ", "වු")
    claims.append(("CC-06", "The same words: C + ෛ / C + ෞ against their glide spelling C + යි / C + වු (07:R-05)",
                   f"ෛ {ai:,} vs යි {ai_glide:,}; ෞ {au:,} vs වු {au_glide:,}; "
                   f"වෛද්‍ය {count.get('වෛද්' + ZWJ + 'ය', 0):,} vs වයිද්‍ය {count.get('වයිද්' + ZWJ + 'ය', 0):,}, "
                   f"බෞද්ධ {count.get('බෞද්ධ', 0):,} vs බවුද්ධ {count.get('බවුද්ධ', 0):,}",
                   "tokens, summed over word types written with the sign; the glide spelling of each is looked up"))

    # --- repaya: plain ර් + C against ර්‍ + C (07:R-08, R-09)
    plain = sum(n for w, n in count.items() if re.search(f"ර{HAL}(?!{ZWJ})[{CONS}]", w))
    joined = sum(n for w, n in count.items() if re.search(f"ර{HAL}{ZWJ}[{CONS}]", w))
    claims.append(("CC-07", "Repaya: tokens of words with plain ර් + C and with ර්‍ + C (07:R-08)",
                   f"plain {plain:,}, joined {joined:,}", ""))
    claims.append(("CC-08", "කාර්ය as a word (07:R-09)", f"{count.get('කාර්ය', 0):,} (කාර්‍ය {count.get('කාර්' + ZWJ + 'ය', 0):,})", ""))

    # --- rakaransaya ZWJ, and ම න ල + ර (03:HC-021, HC-052; 07:R-07)
    rk_zwj = sum(n for w, n in count.items() if re.search(f"[{CONS}]{HAL}{ZWJ}ර", w))
    rk_plain = sum(n for w, n in count.items() if re.search(f"[ක-ෆ]{HAL}ර", w) and not re.search(f"[මනලර]{HAL}ර", w))
    claims.append(("CC-09", "C + ර outside ම න ල ර: tokens of words written with and without ZWJ (03:HC-021)",
                   f"with ZWJ {rk_zwj:,}, without {rk_plain:,}", "ZWJ-less forms are mostly words from texts that lost the joiner"))
    mnl = []
    for c in "මනල":
        p = sum(n for w, n in count.items() if c + HAL + "ර" in w)
        z = sum(n for w, n in count.items() if c + HAL + ZWJ + "ර" in w)
        mnl.append(f"{c}්ර {p:,} vs {c}්‍ර {z:,}")
    claims.append(("CC-10", "ම න ල + ර: tokens with plain hal against rakaransaya (03:HC-052, 07:R-07)", "; ".join(mnl),
                   f"දුම්රිය {count.get('දුම්රිය', 0):,} vs දුම්‍රිය {count.get('දුම්' + ZWJ + 'රිය', 0):,}; "
                   f"තාම්‍ර {count.get('තාම්' + ZWJ + 'ර', 0):,}, තාම්ර {count.get('තාම්ර', 0):,}"))
    claims.append(("CC-11", "Rakaransaya with and without ZWJ in one word (03:HC-021)",
                   f"ක්‍රමය {count.get('ක්' + ZWJ + 'රමය', 0):,} vs ක්රමය {count.get('ක්රමය', 0):,}", ""))

    # --- ද against ඩ (06:RS-030, 07:R-01)
    letters = Counter()
    for w, n in count.items():
        for ch in w:
            if ch in "දධඩඪඳඬතථටඨ":
                letters[ch] += n
    d_total = sum(letters[c] for c in "දධඩඪ")
    claims.append(("CC-12", "Token-weighted letter frequency of ද ධ ඩ ඪ (06:RS-030, 07:R-01)",
                   ", ".join(f"{c} {letters[c]:,} ({100 * letters[c] / d_total:.1f}%)" for c in "දඩධඪ")
                   + f"; ද/ඩ = {letters['ද'] / letters['ඩ']:.1f}", "every occurrence of the letter in every token"))

    # --- ඞ as a typo for ඩ (04:NS-048), in the 40,000 most frequent word types
    top40k = dict(count.most_common(40000))
    nga = [w for w in top40k if "ඞ" in w and not re.search(f"ඞ{HAL}[{VELARS}]", w)]
    fixed = [(w, top40k[w], count.get(w.replace("ඞ", "ඩ"), 0)) for w in nga]
    more = sum(1 for _, n, m in fixed if m > n)
    claims.append(("CC-13", "ඞ outside ඞ් + velar in the 40,000 most frequent words, and how many have a more frequent ඩ spelling (04:NS-048)",
                   f"{len(nga)} words; ඩ spelling more frequent for {more}",
                   ", ".join(f"{w} {n:,}→{m:,}" for w, n, m in sorted(fixed, key=lambda x: -x[1])[:8])))
    return claims


def lexicon_claims(count):
    """07 §4: the evaluation words, with the pinned list as the lexicon."""
    from test_lexicon import EXACT
    tsv = CACHE / "nlpc_2M.tsv"
    if not tsv.exists():
        tsv.write_text("".join(f"{w}\t{n}\n" for w, n in count.items()), encoding="utf-8")
    lex = Lexicon(tsv)
    rules = sum(1 for roman, want, _ in EXACT if to_sinhala(roman) == want)
    lexicon = sum(1 for roman, want, _ in EXACT if candidates(lex, roman)[0] == want)
    missed = [roman for roman, want, _ in EXACT if candidates(lex, roman)[0] != want]
    shared = sum(1 for ws in lex.by_key.values() if len(ws) > 1)
    return [("CC-14", f"07 §4 evaluation, {len(EXACT)} words: correct spelling ranked first",
             f"rules alone {rules}/{len(EXACT)}, rules + lexicon {lexicon}/{len(EXACT)}",
             "missed: " + (", ".join(missed) if missed else "none")),
            ("CC-15", "Sound keys shared by two or more words (07 §4)",
             f"{shared:,} of {len(lex.by_key):,} keys ({100 * shared / len(lex.by_key):.1f}%)", "")]


# ---------------------------------------------------------------------------- Sinhala Wikipedia

def wiki_claims(path):
    pages = Counter()
    rx = {k: re.compile(v) for k, v in {
        "කෲර": "කෲර", "ක්‍රෑර": f"ක්{ZWJ}රෑර", "ක්‍රූර": f"ක්{ZWJ}රූර",
        "ම්ර": f"ම{HAL}ර", "ම්‍ර": f"ම{HAL}{ZWJ}ර", "ප්‍ර": f"ප{HAL}{ZWJ}ර", "ප්ර": f"ප{HAL}ර",
    }.items()}
    n_pages = 0
    text, in_text, ns0 = [], False, False
    with bz2.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if "<ns>" in line:
                ns0 = line.strip() == "<ns>0</ns>"
            if "<text" in line:
                in_text = True
                text = []
            if in_text:
                text.append(line)
            if in_text and "</text>" in line:
                in_text = False
                if ns0:
                    n_pages += 1
                    body = "".join(text)
                    for k, r in rx.items():
                        if r.search(body):
                            pages[k] += 1
    return [("CC-16", "Sinhala Wikipedia articles (namespace 0) containing each spelling (02:VS-035, 03:HC-052)",
             ", ".join(f"{k} {pages[k]:,}" for k in rx) + f" of {n_pages:,} articles", "an article counts once per spelling")]


# ---------------------------------------------------------------------------- report

def lookup(words, offline):
    count = load_nlpc(fetch("nlpc", offline))
    for w in words:
        print(f"{w}	NLPC {count.get(w, 0):,}	(with endings {prefix_sum(count, w):,})")


def main():
    offline = "--offline" in sys.argv
    if "--lookup" in sys.argv:
        return lookup([a for a in sys.argv[sys.argv.index("--lookup") + 1:] if not a.startswith("--")], offline)
    claims = []
    count = load_nlpc(fetch("nlpc", offline))
    claims += nlpc_claims(count)
    claims += lexicon_claims(count)
    wiki = CACHE / SOURCES["siwiki"]["file"]
    if wiki.exists() or not offline:
        claims += wiki_claims(fetch("siwiki", offline))
    if (CACHE / "dakshina_si").exists() or not offline:
        import dakshina_counts
        claims += dakshina_counts.claims(fetch("dakshina", offline))

    lines = ["# Corpus counts", "", "Generated by `tools/corpus_counts.py` from the pinned sources below. Every corpus number "
             "quoted in `docs/` either cites one of these claim ids or, for a single word, is written \"NLPC n\": "
             "the tokens of that word in the NLPC list, which `python tools/corpus_counts.py --lookup WORD` prints.", "", "| Source | Pinned at |", "|---|---|"]
    lines += [f"| [{s['name']}]({s['url']}) | {s['pin']} |" for s in SOURCES.values()]
    lines += ["", "| Id | Claim | Result | Definition and notes |", "|---|---|---|---|"]
    lines += [f"| {cid} | {what} | {res} | {note} |" for cid, what, res, note in claims]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    for cid, what, res, _ in claims:
        print(cid, what[:60], "->", res[:200])


if __name__ == "__main__":
    main()
