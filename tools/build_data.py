"""Build data/letters.json (the letter inventory) and data/validity.json (its grammar status).

    python tools/build_data.py

letters.json: every Sinhala letter form, one object per line (923 entries):
  {"id": "ka.aa", "kind": "syllable", "text": "කා", "consonant": "ka", "vowel": "aa", "codepoints": [...]}

validity.json: the same ids, in the same order:
  {"id": "ka.aa", "text": "කා", "status": "valid", "shape": null, "rules": ["G-VS-13"]}

status:
  valid       occurs in ordinary modern words
  loan        valid, but in practice only in Sanskrit/Pali (tatsama) words
  rare        valid encoding, marginal or archaic in use
  unattested  no known word uses it, but no rule forbids it
  never       forbidden by a hard rule (G-HC-06/07/08/14, G-VS-08)
shape:        "hook-u", "irregular", "tail-loss", "alt-hal" when the glyph is special
              (the encoding is still ordinary; see G-EN-11)

Syllable statuses come from the 41 × 17 table in docs/02-vowel-signs.md §8; the ilu/iluu
columns are "never" (VS-021). Conjunct, vowel and sign statuses follow docs/00-rules.md.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from sinhala_orthography.inventory import CONSONANTS, entries  # noqa: E402

TABLE_SRC = ROOT / "docs" / "02-vowel-signs.md"
LETTERS_OUT = ROOT / "data" / "letters.json"
VALIDITY_OUT = ROOT / "data" / "validity.json"

CODES = {"V": "valid", "L": "loan", "R": "rare", "N": "never"}
TABLE_COLS = ["a", "hal", "aa", "ae", "aee", "i", "ii", "u", "uu", "ru", "ruu",
              "e", "ee", "ai", "o", "oo", "au"]

SANYAKA = {"nnga", "nyja", "nndda", "nda", "mba"}
NO_HAL = SANYAKA | {"lla"}          # G-HC-06, G-HC-07
ASPIRATE_OR_LOAN = {"kha", "gha", "cha", "jha", "ttha", "ddha", "tha", "dha", "pha", "bha",
                    "sha", "ssa", "jnya", "nya"}

INDEPENDENT = {
    "a": "valid", "aa": "valid", "ae": "valid", "aee": "valid", "i": "valid", "ii": "valid",
    "u": "valid", "uu": "valid", "e": "valid", "ee": "valid", "o": "valid", "oo": "valid",
    "ru": "loan", "ai": "loan", "au": "loan",
    "ruu": "never", "ilu": "never", "iluu": "never",
}
SIGNS = {"anusvara": "valid", "visarga": "rare", "candrabindu": "never"}

HOOK_U = {"ka", "ga", "nnga", "ta", "bha", "sha"}
TAIL_LOSS = {"da", "nda"}
ALT_HAL = {"ca", "ja", "tta", "ra"}


def parse_table():
    text = TABLE_SRC.read_text(encoding="utf-8")
    table = {}
    for line in text.splitlines():
        m = re.match(r"\|\s*([a-z]+)\s*\|\s*\S+\s*\|(.*)\|\s*$", line)
        if not m or m.group(1) not in {c for c, _ in CONSONANT_IDS}:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) != len(TABLE_COLS):
            continue
        table[m.group(1)] = dict(zip(TABLE_COLS, cells))
    return table


CONSONANT_IDS = [(cid, None) for cid, _ in CONSONANTS]


def shape_for(cid, vid):
    if vid in ("u", "uu"):
        if cid in HOOK_U:
            return "hook-u"
        if cid in ("ra", "lla"):
            return "irregular"
        if cid in TAIL_LOSS:
            return "tail-loss"
    if vid in ("ae", "aee") and cid == "ra":
        return "irregular"
    if vid == "hal" and cid in ALT_HAL:
        return "alt-hal"
    return None


def syllable(table, cid, vid):
    if vid in ("ilu", "iluu"):
        return "never", ["G-VS-08"]
    if cid == "nga" and vid != "hal":
        return "never", ["G-HC-08"]
    if cid in SANYAKA and vid == "hal":
        return "never", ["G-HC-06"]
    cell = table[cid][vid]
    status = CODES[cell.split()[0]]
    rules = ["G-VS-11"] if vid in ("ru", "ruu", "ai", "au") else ["G-VS-13"]
    if cid == "lla" and vid == "hal":
        return "never", ["G-HC-07"]
    # A table "N" without a hard rule only means no word is known: soft, not forbidden.
    if status == "never":
        status = "unattested"
    return status, rules


def conjunct(cid, kind):
    if cid == "nga" or cid in NO_HAL:
        return "never", ["G-HC-06" if cid in SANYAKA else ("G-HC-07" if cid == "lla" else "G-HC-08")]
    if cid == "ra" and kind in ("rakaransaya", "repaya"):
        return "never", ["G-HC-14"]                 # ර්‍ර: unattested and ambiguous
    if kind == "yansaya":
        if cid == "ra":
            return "never", ["G-HC-14"]
        return ("loan" if cid in ASPIRATE_OR_LOAN else "valid"), ["G-HC-11"]
    if kind == "rakaransaya":
        if cid in ("ma", "na", "la"):
            return "rare", ["G-HC-12"]
        if cid in ("ya", "ra", "lla", "nna", "jnya", "nya"):
            return "rare", ["G-HC-12"]
        return ("loan" if cid in ASPIRATE_OR_LOAN else "valid"), ["G-HC-12"]
    # repaya: optional style (G-HC-13); ර්‍ර unattested
    if cid == "ra":
        return "rare", ["G-HC-13", "G-HC-14"]
    if cid in ("fa", "jha", "ddha", "ttha", "pha", "cha", "nya", "jnya"):
        return "rare", ["G-HC-13"]
    return "valid", ["G-HC-13"]


def dump_rows(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in rows)
    path.write_text("[\n" + lines + "\n]\n", encoding="utf-8")


def main():
    table = parse_table()
    missing = [c for c, _ in CONSONANT_IDS if c not in table]
    assert not missing, f"validity table rows missing for {missing}"
    rows = entries()
    out = []
    for r in rows:
        shape = None
        if r["kind"] == "vowel":
            status, rules = INDEPENDENT[r["vowel"]], ["G-VS-08" if INDEPENDENT[r["vowel"]] == "never" else "G-VS-02"]
        elif r["kind"] == "sign":
            name = r["id"].split(".")[1]
            status, rules = SIGNS[name], [{"anusvara": "G-NS-01", "visarga": "G-NS-05", "candrabindu": "G-NS-06"}[name]]
        elif r["kind"] == "syllable":
            status, rules = syllable(table, r["consonant"], r["vowel"])
            shape = shape_for(r["consonant"], r["vowel"])
        else:
            status, rules = conjunct(r["consonant"], r["conjunct"])
        out.append({"id": r["id"], "text": r["text"], "status": status, "shape": shape, "rules": rules})

    dump_rows(LETTERS_OUT, rows)
    dump_rows(VALIDITY_OUT, out)
    print(f"{len(out)} entries")
    for kind in ("vowel", "sign", "syllable", "conjunct"):
        ids = {r["id"] for r in rows if r["kind"] == kind}
        c = Counter(o["status"] for o in out if o["id"] in ids)
        print(f"  {kind:9} " + "  ".join(f"{k} {c.get(k, 0):3}" for k in ("valid", "loan", "rare", "unattested", "never")))


if __name__ == "__main__":
    main()
