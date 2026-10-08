"""How native speakers romanize each Sinhala letter, measured on the Dakshina dataset (docs/06 §2a).

Called by tools/corpus_counts.py, which downloads the data. Each Sinhala word is split into units (a
consonant, then its vowel sign, inherent a or hal; an independent vowel; ං ඃ), and aligned to its
romanization by dynamic programming over a broad set of candidate spellings per unit. The candidate
probabilities start uniform and are re-estimated from the alignments for a few rounds (hard EM), so
the counts are not decided by the order of a hand-written table. Words that cannot be aligned with
the candidates are left out and reported.
"""
import math
import re
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

ZWJ, HAL = "‍", "්"
INHERENT = "(a)"

CONSONANTS = {
    "ක": "k c ck q kh", "ඛ": "kh k", "ග": "g gh", "ඝ": "gh g", "ඞ": "ng n", "ඟ": "ng g n", "ච": "ch c chh",
    "ඡ": "ch chh c", "ජ": "j z jh", "ඣ": "jh j", "ඤ": "n gn ny kn", "ඥ": "gn kn ny gy", "ට": "t tt th",
    "ඨ": "t th", "ඩ": "d dd dh", "ඪ": "d dh", "ණ": "n", "ඬ": "nd d", "ත": "th t", "ථ": "th t", "ද": "d dh th",
    "ධ": "dh d", "න": "n", "ඳ": "nd d dh ndh", "ප": "p", "ඵ": "p ph f", "බ": "b", "භ": "bh b", "ම": "m",
    "ඹ": "mb b m", "ය": "y", "ර": "r", "ල": "l", "ව": "w v", "ශ": "sh s", "ෂ": "sh s", "ස": "s", "හ": "h",
    "ළ": "l", "ෆ": "f ph",
}
SIGNS = {
    INHERENT: "a e u", HAL: "", "ා": "a aa ah", "ැ": "a e ae aa", "ෑ": "a e ae aa ee", "ි": "i e y",
    "ී": "i ee ii e ie ea", "ු": "u o", "ූ": "u oo uu o", "ෙ": "e a", "ේ": "e ee ay", "ො": "o",
    "ෝ": "o oo", "ෛ": "ai ei e ay", "ෞ": "au ow ou", "ෘ": "ru r ri", "ෲ": "ru ruu",
}
INDEPENDENT = {
    "අ": "a e u", "ආ": "a aa", "ඇ": "a e ae", "ඈ": "a e ae aa", "ඉ": "i e", "ඊ": "i ee ii", "උ": "u o",
    "ඌ": "u oo uu", "එ": "e a", "ඒ": "e ee ay", "ඔ": "o", "ඕ": "o oo", "ඓ": "ai ei", "ඖ": "au ow ou",
    "ඍ": "ru ri r",
}
MARKS = {"ං": "n m ng", "ඃ": "h"}
CAND = {**{k: v.split() for k, v in CONSONANTS.items()}, **{k: v.split() for k, v in INDEPENDENT.items()},
        **{k: v.split() for k, v in MARKS.items()}, **{k: v.split() if v else [""] for k, v in SIGNS.items()}}
# What each table row reports: the sign and the independent vowel share a row in the doc.
LABEL = {k: k for k in CAND}


def units(word):
    """Sinhala word → unit list, or None when it has characters outside the inventory."""
    out, i, word = [], 0, word.replace(ZWJ, "")
    while i < len(word):
        ch = word[i]
        if ch in CONSONANTS:
            nxt = word[i + 1] if i + 1 < len(word) else ""
            if nxt in SIGNS and nxt != INHERENT:
                out += [ch, nxt]
                i += 2
            else:
                out += [ch, INHERENT]
                i += 1
        elif ch in INDEPENDENT or ch in MARKS:
            out.append(ch)
            i += 1
        else:
            return None
    return out


def align(us, roman, logp):
    """Best (highest probability) segmentation of roman over the units, as the chosen spellings."""
    n, m = len(us), len(roman)

    @lru_cache(maxsize=None)
    def best(i, j):
        if i == n:
            return (0.0, ()) if j == m else (-math.inf, ())
        top = (-math.inf, ())
        for spelling in CAND[us[i]]:
            if roman.startswith(spelling, j):
                score, rest = best(i + 1, j + len(spelling))
                score += logp[us[i]][spelling]
                if score > top[0]:
                    top = (score, (spelling,) + rest)
        return top

    score, path = best(0, 0)
    return path if score > -math.inf else None


SINHALA = re.compile("[඀-෿]")
NOT_LETTER = re.compile(r"[^඀-෿a-z‍]")


def clean(native, roman):
    """Drop punctuation and spaces; None for tokens with digits or no Sinhala letter (not words)."""
    if not SINHALA.search(native) or re.search(r"[0-9]", native + roman):
        return None
    return NOT_LETTER.sub("", native), NOT_LETTER.sub("", roman.lower())


def measure(pairs, rounds=4):
    """pairs: (sinhala word, romanization, weight). → (unit → Counter of spellings, aligned, total)."""
    logp = {u: {s: 0.0 for s in c} for u, c in CAND.items()}
    data = [(units(c[0]), c[1], w) for c, w in ((clean(s, r), w) for s, r, w in pairs) if c]
    for _ in range(rounds):
        counts, aligned, total = defaultdict(Counter), 0, 0
        for us, roman, w in data:
            total += w
            if not us:
                continue
            path = align(tuple(us), roman, logp)
            if path is None:
                continue
            aligned += w
            for u, s in zip(us, path):
                counts[u][s] += w
        logp = {u: {s: math.log((counts[u][s] + 0.5) / (sum(counts[u].values()) + 0.5 * len(c))) for s in c}
                for u, c in CAND.items()}
    return counts, aligned, total


def share(counter, top=3):
    total = sum(counter.values())
    if not total:
        return "-"
    parts = [f"{s or '∅'} {100 * n / total:.0f}%" for s, n in counter.most_common(top) if 100 * n / total >= 1]
    return ", ".join(parts) + f" (n={total:,})"


ROWS = ["ක", "ඛ", "ඝ", "ඟ", "ච", "ඡ", "ජ", "ඤ", "ඥ", "ට", "ඨ", "ඩ", "ඪ", "ණ", "ඬ", "ත", "ථ", "ද", "ධ", "ඳ",
        "ඵ", "භ", "ඹ", "ව", "ශ", "ෂ", "ළ", "ෆ", INHERENT, "ා", "ැ", "ඇ", "ෑ", "ී", "ඊ", "ූ", "ඌ", "ේ", "ඒ", "ෝ",
        "ඕ", "ෘ", "ෛ", "ඓ", "ෞ", "ඖ", "ං"]


def claims(root: Path):
    sentences = []
    for line in (root / "romanized" / "si.romanized.rejoined.aligned.tsv").read_text(encoding="utf-8").splitlines():
        if "\t" in line:
            native, roman = line.split("\t")[:2]
            sentences.append((native, roman, 1))
    lexicon = []
    for part in ("train", "dev", "test"):
        for line in (root / "lexicons" / f"si.translit.sampled.{part}.tsv").read_text(encoding="utf-8").splitlines():
            native, roman, n = line.split("\t")
            lexicon.append((native, roman, int(n)))
    s_counts, s_aligned, s_total = measure(sentences)
    l_counts, l_aligned, l_total = measure(lexicon)
    rows = "<br>".join(f"{u}: {share(s_counts[u])} · {share(l_counts[u])}" for u in ROWS)
    return [("CC-17", "Dakshina: Sinhala word tokens aligned (sentences · lexicon variants, weighted by annotators)",
             f"{s_aligned:,} of {s_total:,} · {l_aligned:,} of {l_total:,}", "lowercased, punctuation and spaces removed; tokens with digits or no Sinhala letter are not words and are left out"),
            ("CC-18", "Dakshina: how each letter is romanized (sentences · lexicon variants), docs/06 §2a",
             rows, "share of the aligned occurrences of the letter; ∅ = nothing written")]
