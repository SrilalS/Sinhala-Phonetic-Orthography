"""Disambiguating sound-alike spellings with a word-frequency list.

The romanization converter produces one spelling per input. Several Sinhala letter
groups are pronounced alike (G-SP-01), and some choices are lexical (sanyaka vs nasal
cluster, ං vs න්, ෛ vs අයි …), so a romanization alone cannot always pick the
standard spelling. This module:

1. folds words to a *sound key* that erases the distinctions speakers do not hear
   or do not write in Latin script (aspiration, ණ/න, ළ/ල, ශ/ෂ/ස, ද/ඩ, vowel length,
   sanyaka vs cluster, …);
2. returns the words of a frequency list that share the input's sound key, most
   frequent first;
3. keeps the converter's own spelling first when the romanization contains an
   explicit marker for a distinction (a capital, a z- prefix, a doubled vowel …)
   and that spelling is a real word.

Any word-frequency list works (one "word<TAB>count" per line). The evaluation in
docs/07-phonetic-romanization.md used the University of Moratuwa NLPC "Word Frequency
List for Sinhala" (https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala), which
is not redistributed here. Copies of that list without ZWJ are repaired on load
(see normalize()).
"""
import bisect
import re
from pathlib import Path

from .romanization import to_sinhala

HAL, ZWJ = "්", "‍"
CONS = "ක-ෆ"
NO_HAL = "ඟඦඬඳඹළ"

# --- 1. normalisation of lexicon spellings -------------------------------------------

_JOIN = re.compile(f"([{CONS}]){HAL}(?!{ZWJ})(?=[යර])")   # lookahead: ය/ර may start the next join


def normalize(word):
    """Restore the mandatory ZWJ in C ් ය / C ් ර (never after ර: G-HC-14, R-09)."""
    return _JOIN.sub(lambda m: m.group(1) + HAL + (ZWJ if m.group(1) != "ර" else ""), word)


# --- 2. sound key ----------------------------------------------------------------------

_FOLD_SEQ = [
    # composite vowels first
    ("ෛ", "යි"), ("ඓ", "අයි"), ("ෞ", "වු"), ("ඖ", "අවු"),
    ("ෘ", HAL + "රු"), ("ෲ", HAL + "රු"), ("ඍ", "රු"), ("ඎ", "රු"),
    ("ඥ", "ග" + HAL + "න"),                                     # G-NS-12: gn
    # sanyaka → nasal + stop (R-03)
    ("ඟ", "න" + HAL + "ග"), ("ඦ", "න" + HAL + "ජ"), ("ඬ", "න" + HAL + "ද"), ("ඳ", "න" + HAL + "ද"), ("ඹ", "ම" + HAL + "බ"),
    ("ං", "න" + HAL), ("ඞ" + HAL, "න" + HAL),                    # R-11
]
_FOLD_CHAR = str.maketrans({
    # aspirates → plain (G-SP-01, G-SP-06)
    "ඛ": "ක", "ඝ": "ග", "ඡ": "ච", "ඣ": "ජ", "ඨ": "ට", "ඪ": "ද", "ථ": "ත", "ධ": "ද", "ඵ": "ප", "භ": "බ",
    "ඩ": "ද",                                                   # R-01: d is written for both in informal romanization
    "ණ": "න", "ළ": "ල", "ශ": "ස", "ෂ": "ස", "ඤ": "න",            # G-SP-02…05, G-NS-13
    # vowel length and ae/e (G-SP-07, G-TY-04, G-TY-07)
    "ආ": "අ", "ඊ": "ඉ", "ඌ": "උ", "ඒ": "එ", "ඕ": "ඔ", "ඇ": "එ", "ඈ": "එ",
    "ා": "", "ී": "ි", "ූ": "ු", "ේ": "ෙ", "ෝ": "ො", "ැ": "ෙ", "ෑ": "ෙ",
    ZWJ: None,
})


def sound_key(text):
    for a, b in _FOLD_SEQ:
        text = text.replace(a, b)
    return text.translate(_FOLD_CHAR)


# --- 3. lexicon --------------------------------------------------------------------------

class Lexicon:
    """A word-frequency list indexed by sound key. `path`: a "word<TAB>count" file."""

    def __init__(self, path):
        path = Path(path)
        self.count = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            word, _, n = line.partition("\t")
            if word and n.isdigit():
                w = normalize(word)
                self.count[w] = self.count.get(w, 0) + int(n)
        self.by_key = {}
        for w, n in self.count.items():
            self.by_key.setdefault(sound_key(w), []).append(w)
        for ws in self.by_key.values():
            ws.sort(key=lambda w: -self.count[w])
        self.keys = sorted(self.by_key)

    def exact(self, key):
        return self.by_key.get(key, [])

    def prefix(self, key, limit=200):
        i = bisect.bisect_left(self.keys, key)
        out = []
        while i < len(self.keys) and self.keys[i].startswith(key) and len(out) < limit:
            out.extend(self.by_key[self.keys[i]])
            i += 1
        return out


# Romanization markers that pin down a distinction the sound key erases. When one is
# present and the converter's spelling is a word, that spelling outranks frequency.
_EXPLICIT = re.compile(r"[KCGJTDNLPBSWVUIEOAXRMH]|z[a-zA-Z]|aa|ii|uu|ee|oo|ae|thh|dh|kh|gh|chh|jh|ph|bh|x")


def candidates(lex, roman, limit=5, partial=False, **options):
    """Ranked Sinhala spellings for a romanized word (or a word prefix with partial=True)."""
    spelled = to_sinhala(roman, **options)
    key = sound_key(spelled)
    if partial:
        # An incomplete word: its last consonant may still take a vowel, so drop a trailing hal.
        ranked = sorted(set(lex.prefix(key.removesuffix(HAL))), key=lambda w: (-lex.count[w], w))
        return ranked[:limit]
    ranked = sorted(set(lex.exact(key)), key=lambda w: (-lex.count[w], w))
    explicit = bool(_EXPLICIT.search(roman))
    if spelled in lex.count and explicit:
        ranked = [spelled] + [w for w in ranked if w != spelled]   # explicit markers beat frequency
    elif spelled not in ranked:
        ranked.append(spelled)                 # the rule-based spelling is always included
    return ranked[:limit]
