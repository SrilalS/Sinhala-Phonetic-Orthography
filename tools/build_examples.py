"""Build data/examples.json: a few common words that contain each letter form.

    python tools/build_examples.py WORD_LIST     (or set SINHALA_WORD_LIST)

WORD_LIST is a word-frequency list, one "word<TAB>count" per line, e.g. the University of
Moratuwa NLPC "Word Frequency List for Sinhala"
(https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala). Only the few most frequent
words per form are kept; the list itself is not redistributed.

examples.json: the ids of data/validity.json, in the same order:
  {"id": "ka.u", "words": [["කුමක්", 51234], ...]}

Each word is split into letter forms the way data/letters.json defines them: a consonant
with its vowel sign (or hal, or nothing for the inherent a), a yansaya or rakaransaya
conjunct, a repaya (ර් before a consonant, with or without ZWJ), an independent vowel or a
sign. A word counts for every form it contains; a form keeps its most frequent words,
skipping words that extend (or are extended by) one it already has, so කර and කරන do not
both take a slot. Words with a `never` form, a non-Sinhala character, a spelling that
breaks a positional HARD rule (BAD_SPELLING) or a count below MIN_COUNT are skipped as
likely noise. `never` forms get no examples.
"""
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from sinhala_orthography.lexicon import normalize  # noqa: E402

VALIDITY = ROOT / "data" / "validity.json"
OUT = ROOT / "data" / "examples.json"

PER_FORM = 6
MIN_COUNT = 5

HAL, ZWJ = "්", "‍"
CONS = "ක-ෆ"
SIGNS = "ා-ෟෲෳ"
WORD = re.compile(f"[඀-෿{ZWJ}]+")
# One consonant akshara: C, then a joined ය/ර (yansaya, rakaransaya) or a vowel sign / hal.
LETTER = re.compile("[අ-ඖක-ෆ]")
AKSHARA = re.compile(f"([{CONS}])(?:{HAL}{ZWJ}([යර]))?({HAL}{ZWJ}?|[{SIGNS}])?")


def forms_in(word, by_text, words=()):
    """The ids of the letter forms in `word`, or None when it holds one that is not in the inventory.

    A joined ය/ර right after a prefix that is itself a word in `words` is read as hal + a new
    letter: lists that had their ZWJ restored also join across word boundaries (බවත් + ය).
    """
    ids, i, repaya = set(), 0, False
    while i < len(word):
        m = AKSHARA.match(word, i)
        if not m:
            ch = word[i]
            if ch not in by_text:
                return None
            ids.update(by_text[ch])
            i, repaya = i + 1, False
            continue
        c, conj, sign = m.groups()
        if repaya:
            ids.update(by_text["ර" + HAL + ZWJ + c])
        if conj and m.start() > 0 and word[:m.start()] + c + HAL in words:
            ids.update(by_text[c + HAL])
            i, repaya = m.start(2), False
            continue
        if conj:
            text = c + HAL + ZWJ + conj
        else:
            text = c + (sign or "").replace(ZWJ, "")
        if text not in by_text:
            return None
        ids.update(by_text[text])
        # ර් followed by a consonant is a repaya on that consonant (G-HC-13).
        repaya = c == "ර" and not conj and sign is not None and sign.startswith(HAL)
        i = m.end()
    return ids


# Spellings that break a HARD rule on where a letter may stand; in a word list these are
# typos (මොහොමඞ් for මොහොමඩ්, ඬේවිඞ් for ඩේවිඩ්).
BAD_SPELLING = re.compile(
    "^[ඟඦඬඳඹඞංඃඎ]"                       # G-PH-01: word-initial bans
    "|ඞ්(?![කඛගඝ])"                       # G-HC-08: ඞ් only before a velar
    r"|([ඟඦඬඳඹඞෆහළ])්\1"                  # G-HC-04: letters that never geminate
)


def same_stem(a, b):
    """True when one word extends the other and the shorter has two aksharas or more (a joined letter is not one)."""
    short, long_ = sorted((a, b), key=len)
    return long_.startswith(short) and len(LETTER.findall(short)) - short.count(ZWJ) >= 2


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SINHALA_WORD_LIST")
    if not path:
        sys.exit("usage: build_examples.py WORD_LIST (or set SINHALA_WORD_LIST)")
    validity = json.loads(VALIDITY.read_text(encoding="utf-8"))
    status = {v["id"]: v["status"] for v in validity}
    by_text = {}
    for v in validity:
        by_text.setdefault(v["text"], []).append(v["id"])

    rows = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        word, _, n = line.partition("\t")
        word = unicodedata.normalize("NFC", word.strip())
        if word and n.strip().isdigit() and WORD.fullmatch(word):
            rows.append((word, int(n)))
    # As in Lexicon: only a list with no ZWJ at all is repaired, and only then can a join be a
    # wrong repair across a word boundary.
    repair = not any(ZWJ in w for w, _ in rows)
    count = {}
    for word, n in rows:
        word = normalize(word) if repair else word
        count[word] = count.get(word, 0) + n

    examples = {v["id"]: [] for v in validity}
    for word, n in sorted(count.items(), key=lambda kv: -kv[1]):
        if n < MIN_COUNT:
            break
        ids = forms_in(word, by_text, count if repair else ())
        if not ids or any(status[i] == "never" for i in ids) or BAD_SPELLING.search(word):
            continue
        for i in ids:
            # Skip inflections of a word already chosen (කර, then කරන), for variety.
            if len(examples[i]) < PER_FORM and not any(same_stem(word, w) for w, _ in examples[i]):
                examples[i].append([word, n])

    lines = [json.dumps({"id": v["id"], "words": examples[v["id"]]}, ensure_ascii=False) for v in validity]
    OUT.write_text("[\n  " + ",\n  ".join(lines) + "\n]\n", encoding="utf-8", newline="\n")
    found = sum(1 for e in examples.values() if e)
    allowed = sum(1 for s in status.values() if s != "never")
    print(f"{OUT.relative_to(ROOT)}: {found} / {allowed} allowed forms have examples")
    for s in ("valid", "loan", "rare", "unattested"):
        ids = [i for i in status if status[i] == s]
        print(f"  {s:10} {sum(1 for i in ids if examples[i])} / {len(ids)}")


if __name__ == "__main__":
    main()
