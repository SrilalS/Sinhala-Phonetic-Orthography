"""The Sinhala letter inventory: independent vowels, signs, consonants, vowel forms, conjuncts.

IDs follow docs/01-inventory.md. Consonants are in Unicode (alphabet) order, U+0D9A–U+0DC6.
"""

HAL = "්"
ZWJ = "‍"

# (id, independent vowel, dependent sign). "" = inherent a; HAL = no vowel.
VOWELS = [
    ("hal", None, HAL), ("a", "අ", ""), ("aa", "ආ", "ා"), ("ae", "ඇ", "ැ"), ("aee", "ඈ", "ෑ"),
    ("i", "ඉ", "ි"), ("ii", "ඊ", "ී"), ("u", "උ", "ු"), ("uu", "ඌ", "ූ"),
    ("ru", "ඍ", "ෘ"), ("ruu", "ඎ", "ෲ"), ("ilu", "ඏ", "ෟ"), ("iluu", "ඐ", "ෳ"),
    ("e", "එ", "ෙ"), ("ee", "ඒ", "ේ"), ("ai", "ඓ", "ෛ"),
    ("o", "ඔ", "ො"), ("oo", "ඕ", "ෝ"), ("au", "ඖ", "ෞ"),
]

CONSONANTS = [
    ("ka", "ක"), ("kha", "ඛ"), ("ga", "ග"), ("gha", "ඝ"), ("nga", "ඞ"), ("nnga", "ඟ"),
    ("ca", "ච"), ("cha", "ඡ"), ("ja", "ජ"), ("jha", "ඣ"), ("nya", "ඤ"), ("jnya", "ඥ"), ("nyja", "ඦ"),
    ("tta", "ට"), ("ttha", "ඨ"), ("dda", "ඩ"), ("ddha", "ඪ"), ("nna", "ණ"), ("nndda", "ඬ"),
    ("ta", "ත"), ("tha", "ථ"), ("da", "ද"), ("dha", "ධ"), ("na", "න"), ("nda", "ඳ"),
    ("pa", "ප"), ("pha", "ඵ"), ("ba", "බ"), ("bha", "භ"), ("ma", "ම"), ("mba", "ඹ"),
    ("ya", "ය"), ("ra", "ර"), ("la", "ල"), ("va", "ව"),
    ("sha", "ශ"), ("ssa", "ෂ"), ("sa", "ස"), ("ha", "හ"), ("lla", "ළ"), ("fa", "ෆ"),
]

SIGNS = [("anusvara", "ං"), ("visarga", "ඃ"), ("candrabindu", "ඁ")]


def codepoints(text):
    return [f"U+{ord(ch):04X}" for ch in text]


def entries():
    """Every letter form: 18 vowels, 3 signs, 41 × 19 syllables, 41 × 3 conjuncts (923)."""
    rows = []
    for vid, independent, _ in VOWELS:
        if independent:
            rows.append({"id": f"vowel.{vid}", "kind": "vowel", "text": independent, "vowel": vid})
    for sid, text in SIGNS:
        rows.append({"id": f"sign.{sid}", "kind": "sign", "text": text})
    for cid, letter in CONSONANTS:
        for vid, _, sign in VOWELS:
            rows.append({"id": f"{cid}.{vid}", "kind": "syllable", "text": letter + sign,
                         "consonant": cid, "vowel": vid})
    for cid, letter in CONSONANTS:
        rows.append({"id": f"{cid}.yansaya", "kind": "conjunct", "text": letter + HAL + ZWJ + "ය",
                     "consonant": cid, "conjunct": "yansaya"})
        rows.append({"id": f"{cid}.rakaransaya", "kind": "conjunct", "text": letter + HAL + ZWJ + "ර",
                     "consonant": cid, "conjunct": "rakaransaya"})
        rows.append({"id": f"{cid}.repaya", "kind": "conjunct", "text": "ර" + HAL + ZWJ + letter,
                     "consonant": cid, "conjunct": "repaya"})
    for r in rows:
        r["codepoints"] = codepoints(r["text"])
    return rows
