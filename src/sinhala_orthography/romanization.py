"""Phonetic romanization → Sinhala script, following the rules in docs/00-rules.md.

The romanization is defined by the tables in data/ (consonants.json, vowels.json,
specials.json) and specified in docs/07-phonetic-romanization.md. The converter is a
longest-match tokenizer followed by one left-to-right pass that decides vowel signs,
hal, ZWJ joins, glides and nasal assimilation. Every output satisfies the hard
orthographic rules (verified exhaustively by tools/check_romanization.py).

Options (all off by default):
  archaic     allow ඏ ඐ ෟ ෳ ඎ ඁ ඦ and touching letters (R-14)
  repaya_zwj  write repaya as ර්‍ + C instead of plain ර් + C (R-08)
  classical   ZWJ conjuncts for the classical bandi akuru pairs (R-10), and rakaransaya after ම න ල (R-07)
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"

HAL, ZWJ = "්", "‍"
ANUSVARA, VISARGA, CANDRABINDU = "ං", "ඃ", "ඁ"
SANYAKA = set("ඟඦඬඳඹ")
NO_HAL = SANYAKA | {"ළ"}                       # G-HC-06, G-HC-07
NGA = "ඞ"                                     # G-HC-08: only as ඞ්
PLAIN = {"ඟ": "ග", "ඦ": "ජ", "ඬ": "ඩ", "ඳ": "ද", "ඹ": "බ"}   # G-PH-01: no sanyaka word-initially
PLAIN_BEFORE_RA = set("මනල")                 # R-07: C ් ර after ම න ල is plain hal (දුම්රිය, හෙන්රි)
VELARS = set("කඛගඝ")                          # R-11: n + velar → ං
GAETTA = {"u": "ෘ", "uu": "ෲ"}                 # R-06: C + r + u/uu is usually written ෘ/ෲ (G-VS-15)
FRONT = {"i", "ii", "e", "ee", "ae", "aee", "ai"}
BACK = {"u", "uu", "o", "oo", "au"}
BANDI = {("ක", "ෂ"), ("ක", "ව"), ("ග", "ධ"), ("ට", "ඨ"), ("ත", "ථ"), ("ත", "ව"), ("ද", "ධ"),
         ("ද", "ව"), ("න", "ථ"), ("න", "ද"), ("න", "ධ"), ("න", "ව"), ("ඤ", "ච")}   # G-HC-15


def _load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


CONSONANTS = _load("consonants.json")
VOWELS = _load("vowels.json")
SPECIALS = _load("specials.json")


def _sequences(archaic):
    """All seqs for this mode, longest first (ties keep table order)."""
    seqs = []
    for seq, letter, mode, _ in CONSONANTS:
        if mode == "normal" or archaic:
            seqs.append((seq, ("C", letter, seq)))
    for seq, vid, ind, sign, mode, _ in VOWELS:
        if mode == "normal" or archaic:
            seqs.append((seq, ("V", vid, ind, sign)))
    for seq, output, mode, _ in SPECIALS:
        if mode == "normal" or archaic:
            kind = {"ං": "ANUS", "ඃ": "VIS", "ඁ": "CANDRA", "touch": "TOUCH"}[output]
            seqs.append((seq, (kind, output, seq)))
    order = {k: n for n, (k, _) in enumerate(seqs)}
    return sorted(seqs, key=lambda kv: (-len(kv[0]), order[kv[0]]))


_SEQUENCES = {False: _sequences(False), True: _sequences(True)}


def tokenize(source, archaic=False):
    toks, i = [], 0
    while i < len(source):
        for seq, tok in _SEQUENCES[archaic]:
            if source.startswith(seq, i):
                toks.append(tok); i += len(seq)
                break
        else:
            ch = source[i]
            if ch != "z":          # an unknown z-combination is dropped
                toks.append(("LIT", ch))
            i += 1
    return toks


def _glide(prev_vowel, vowel):
    """G-VS-06: ය after front vowels, ව after back; after a/aa, decided by the next vowel."""
    if prev_vowel in FRONT:
        return "ය"
    if prev_vowel in BACK:
        return "ව"
    return "ය" if vowel in FRONT else "ව"


def transliterate(source, archaic=False, repaya_zwj=False, classical=False, rakaransaya_u=False):
    toks = tokenize(source, archaic)
    out = []
    # state: None (word start), "V" (ends in a vowel; prev_vowel set), "ANUS", "HAL"
    state, prev_vowel = None, None
    j = 0
    while j < len(toks):
        tok = toks[j]
        kind = tok[0]
        nxt = toks[j + 1] if j + 1 < len(toks) else None
        nk = nxt[0] if nxt else None

        if kind == "C":
            letter, seq = tok[1], tok[2]
            after = toks[j + 2] if j + 2 < len(toks) else None
            if state is None and letter in PLAIN:
                letter = PLAIN[letter]
            if letter == NGA and nk == "V":
                if state is None:                      # G-PH-01: ඞ never starts a word
                    out.append(seq); state = None; j += 1; continue
                letter = "ඟ"                            # G-HC-08: /ŋ/ + vowel is written ඟ
            if letter == NGA and state is None:
                out.append(seq); j += 1; continue
            # R-11: n + velar after a vowel → ං; word-final "ng" → ං
            if letter == "න" and seq == "n" and state == "V" and nk == "C" and nxt[1] in VELARS:
                out.append(ANUSVARA); state = "ANUS"
                if nxt[2] == "g" and (after is None or after[0] == "LIT"):
                    j += 2; continue
                j += 1; continue
            out.append(letter)
            if nk == "V":
                vid, ind, sign = nxt[1], nxt[2], nxt[3]
                out.append(sign); state, prev_vowel = "V", vid
                j += 2; continue
            if nk in ("ANUS", "VIS", "CANDRA"):
                state, prev_vowel = "V", "a"             # ං/ඃ need a vowel base: keep inherent a
                j += 1; continue
            if nk == "C":
                nl = nxt[1]
                if letter in NO_HAL or nl in SANYAKA:   # no hal here: keep inherent a
                    state, prev_vowel = "V", "a"; j += 1; continue
                if letter == NGA:
                    out.append(HAL)
                elif nl == "ය":
                    out.append(HAL + ZWJ if (letter != "ර" or repaya_zwj) else HAL)   # G-HC-11, G-HC-14, R-09
                elif nl == "ර":
                    vowel = after[1] if after and after[0] == "V" else None
                    if vowel in GAETTA and letter != "ර" and not rakaransaya_u:
                        out.append(GAETTA[vowel])                                        # G-VS-15, R-06
                        state, prev_vowel = "V", vowel
                        j += 3; continue
                    plain = letter == "ර" or (letter in PLAIN_BEFORE_RA and not classical
                                              and not (rakaransaya_u and vowel in GAETTA))
                    out.append(HAL if plain else HAL + ZWJ)                              # G-HC-12, R-07
                elif letter == "ර":
                    out.append(HAL + ZWJ if repaya_zwj else HAL)                         # R-08
                elif classical and (letter, nl) in BANDI:
                    out.append(HAL + ZWJ)                                                # R-10
                else:
                    out.append(HAL)
                state = "HAL"; j += 1; continue
            if nk == "TOUCH" and after and after[0] == "C" and letter not in NO_HAL:
                out.append(ZWJ + HAL); state = "HAL"; j += 2; continue
            # end of word
            if letter in NO_HAL:
                state, prev_vowel = "V", "a"
            else:
                out.append(HAL); state = "HAL"
            j += 1; continue

        if kind == "V":
            vid, ind, sign = tok[1], tok[2], tok[3]
            if state == "V":
                glide = _glide(prev_vowel, vid)
                out.append(glide + sign)
                state, prev_vowel = "V", vid
            elif state == "ANUS":
                out[-1] = "ම" + sign                      # G-NS-04: ං never before a vowel
                state, prev_vowel = "V", vid
            else:
                if vid == "ruu" and not archaic:
                    ind = "ඍ"                              # G-VS-08: ඎ is archaic
                out.append(ind); state, prev_vowel = "V", vid
            j += 1; continue

        if kind in ("ANUS", "VIS", "CANDRA"):
            if kind == "ANUS" and nk == "C" and nxt[1] in SANYAKA:
                j += 1; continue                          # G-NS-09: the sanyaka already carries the nasal
            if state == "V":
                out.append(tok[1]); state = "ANUS" if kind == "ANUS" else "V"
            else:
                out.append(tok[2]); state = None          # no base: leave the romanization as written
            j += 1; continue

        if kind == "TOUCH":
            out.append("+"); state = None; j += 1; continue

        out.append(tok[1]); state, prev_vowel = None, None   # LIT
        j += 1
    return "".join(out)


def to_sinhala(source, **options):
    """Convert a romanized word or text to Sinhala script."""
    return transliterate(source, **options)
