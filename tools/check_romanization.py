"""Verify the phonetic romanization against the orthographic rules.

    python tools/check_romanization.py

1. Coverage: every entry of data/letters.json that data/validity.json allows must be
   producible from some romanization (archaic letters and ZWJ repaya with their options).
2. Safety:   every romanization of 1–3 sequences (plus a space) is converted, and the
   output is checked against the forbidden patterns of docs/00-rules.md.

Writes data/romanization-coverage.json and reports/romanization-check.md (and .si.md, in Sinhala).
Exits non-zero on any coverage gap or rule violation.
"""
import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from sinhala_orthography import romanization  # noqa: E402
from sinhala_orthography.romanization import to_sinhala  # noqa: E402

LETTERS = json.loads((ROOT / "data" / "letters.json").read_text(encoding="utf-8"))
VALIDITY = {v["id"]: v for v in json.loads((ROOT / "data" / "validity.json").read_text(encoding="utf-8"))}
PRODUCIBLE = {"valid", "loan", "rare", "unattested"}
ARCHAIC_IDS = {"vowel.ruu", "vowel.ilu", "vowel.iluu", "sign.candrabindu"}
CLASSICAL_IDS = {"ma.rakaransaya", "na.rakaransaya", "la.rakaransaya"}   # R-07: only with `classical`

SIGNS = "ා-ෟෲෳ"
FORBIDDEN = [
    ("G-HC-08 sign on ඞ", rf"ඞ[{SIGNS}]"),
    ("G-HC-06 hal on sanyaka", "[ඟඦඬඳඹ]්"),
    ("G-HC-07 hal on ළ", "ළ්"),
    ("G-VS-04 sign/ං/ඃ after hal", f"්[{SIGNS}ංඃ]"),
    ("G-VS-03 sign after independent vowel", f"[අ-ඖ][්{SIGNS}]"),
    ("G-VS-04 two signs", f"[{SIGNS}][{SIGNS}]"),
    ("G-NS-01 ං/ඃ without a base", "(^|[^඀-෿])[ංඃ]"),
    ("G-NS-01 sign after ං/ඃ", f"[ංඃ][්{SIGNS}]"),
    ("G-NS-09 ං before sanyaka", "ං[ඟඦඬඳඹ]"),
    ("G-PH-01 word-initial sanyaka/ඞ", "(^|[^඀-෿‍])[ඟඦඬඳඹඞ]"),
    ("G-EN-03 ෙෙ", "ෙෙ"),
    ("G-EN-10 ZWNJ", "‌"),
    ("G-VS-02 independent vowel after a consonant", "[ක-ෆ්‍][අ-ඖ]"),
]
ARCHAIC_ONLY = ("G-VS-08/G-NS-06 archaic letter in normal mode", "[ඏඐඎඁඦෟෳ]")
# The pattern names in Sinhala, for reports/romanization-check.si.md.
SI_NAMES = {
    "G-HC-08 sign on ඞ": "G-HC-08 ඞ මත ලකුණක්",
    "G-HC-06 hal on sanyaka": "G-HC-06 සඤ්ඤක අකුරක් මත හල් ලකුණ",
    "G-HC-07 hal on ළ": "G-HC-07 ළ මත හල් ලකුණ",
    "G-VS-04 sign/ං/ඃ after hal": "G-VS-04 හල් ලකුණට පසු පිල්ලක්, ං හෝ ඃ",
    "G-VS-03 sign after independent vowel": "G-VS-03 ස්වතන්ත්‍ර ස්වරයකට පසු ලකුණක්",
    "G-VS-04 two signs": "G-VS-04 පිලි දෙකක් එක ළඟ",
    "G-NS-01 ං/ඃ without a base": "G-NS-01 පාදක අකුරක් නැති ං හෝ ඃ",
    "G-NS-01 sign after ං/ඃ": "G-NS-01 ං හෝ ඃ ට පසු ලකුණක්",
    "G-NS-09 ං before sanyaka": "G-NS-09 සඤ්ඤක අකුරකට පෙර ං",
    "G-PH-01 word-initial sanyaka/ඞ": "G-PH-01 වචනයක මුලට සඤ්ඤක අකුරක් හෝ ඞ",
    "G-EN-03 ෙෙ": "G-EN-03 ෙෙ",
    "G-EN-10 ZWNJ": "G-EN-10 ZWNJ",
    "G-VS-02 independent vowel after a consonant": "G-VS-02 ව්‍යඤ්ජනයකට පසු ස්වතන්ත්‍ර ස්වරයක්",
    "G-VS-08/G-NS-06 archaic letter in normal mode": "G-VS-08/G-NS-06 සාමාන්‍ය ප්‍රකාරයේදී පුරාතන අකුරක්",
}


def sequences(archaic):
    return [k for k, _ in romanization._SEQUENCES[archaic]]


def coverage(settings):
    cons = [(c[0], c[1]) for c in romanization.CONSONANTS if c[2] == "normal" or settings.get("archaic")]
    vows = [(v[0], v[1]) for v in romanization.VOWELS if v[4] == "normal" or settings.get("archaic")]
    letter_seqs = {}
    for k, letter in cons:
        letter_seqs.setdefault(letter, []).append(k)
    vowel_seqs = {}
    for k, vid in vows:
        vowel_seqs.setdefault(vid, []).append(k)
    vowel_seqs["hal"] = [""]
    # C-13: C + r + u/uu also writes C + ෘ/ෲ (candidates are still checked by converting them)
    vowel_seqs["ru"] = vowel_seqs.get("ru", []) + ["ru"]
    vowel_seqs["ruu"] = vowel_seqs.get("ruu", []) + ["ruu"]
    sign_seqs = {"anusvara": "x", "visarga": "H", "candrabindu": "~n"}
    letters_by_id = {r["consonant"]: r["text"] for r in LETTERS if r["kind"] == "syllable" and r["vowel"] == "a"}

    found, missing = {}, []
    for r in LETTERS:
        cands = []
        if r["kind"] == "vowel":
            cands = vowel_seqs.get(r["vowel"], [])
            ok = [c for c in cands if to_sinhala(c, **settings) == r["text"]]
        elif r["kind"] == "sign":
            k = sign_seqs[r["id"].split(".")[1]]
            ok = ["ka" + k] if to_sinhala("ka" + k, **settings) == "ක" + r["text"] else []
        else:
            cks = letter_seqs.get(letters_by_id[r["consonant"]], [])
            if r["kind"] == "syllable":
                cands = [ck + vk for ck in cks for vk in vowel_seqs.get(r["vowel"], [])]
            elif r["conjunct"] == "yansaya":
                cands = [ck + "ya" for ck in cks]
            elif r["conjunct"] == "rakaransaya":
                cands = [ck + "ra" for ck in cks]
            else:
                cands = ["r" + ck + "a" for ck in cks]
            ok = [c for c in cands if to_sinhala(c, **settings) == r["text"]]
            # Letters that cannot start a word (G-PH-01) are checked after a vowel: "a" + input → අ + text
            if not ok:
                ok = ["a" + c for c in cands if to_sinhala("a" + c, **settings) == "අ" + r["text"]]
        found[r["id"]] = sorted(ok, key=lambda s: (len(s), sum(ch.isupper() for ch in s)))[:4]
    return found


def safety(settings):
    archaic = settings.get("archaic", False)
    pool = sequences(archaic) + [" "]
    rules = FORBIDDEN + ([] if archaic else [ARCHAIC_ONLY])
    compiled = [(name, re.compile(p)) for name, p in rules]
    hits = {}
    for n in (1, 2, 3):
        for combo in itertools.product(pool, repeat=n):
            src = "".join(combo)
            out = to_sinhala(src, **settings)
            for name, rx in compiled:
                if rx.search(out):
                    hits.setdefault(name, []).append((src, out))
    return hits, len(pool)


def main():
    configs = [("default", {}), ("repaya_zwj", {"repaya_zwj": True}), ("classical", {"classical": True}),
               ("archaic", {"archaic": True}), ("rakaransaya_u", {"rakaransaya_u": True})]
    cov = {name: coverage(o) for name, o in configs}
    result, gaps = [], []
    for r in LETTERS:
        status = VALIDITY[r["id"]]["status"]
        row = {"id": r["id"], "text": r["text"], "status": status}
        for name, _ in configs:
            row[name] = cov[name][r["id"]]
        result.append(row)
        if status in PRODUCIBLE:
            needs_option = (r.get("conjunct") == "repaya") or r["id"] in ARCHAIC_IDS or r.get("consonant") == "nyja"
            classical_only = r["id"] in CLASSICAL_IDS
            if not row["default"] and not (needs_option and (row["repaya_zwj"] or row["archaic"]))                     and not (classical_only and row["classical"]):
                gaps.append(r["id"])
    out = ROOT / "data" / "romanization-coverage.json"
    lines = ",\n".join("  " + json.dumps(r, ensure_ascii=False) for r in result)
    out.write_text("[\n" + lines + "\n]\n", encoding="utf-8")
    allowed = [r for r in result if r["status"] in PRODUCIBLE]
    print(f"coverage: {len(allowed) - len(gaps)}/{len(allowed)}; gaps: {gaps}")

    produced = f"**{len(allowed) - len(gaps)} / {len(allowed)}**"
    report = ["# Romanization check", "", "Generated by `tools/check_romanization.py`.", "",
              "## Coverage", "",
              f"{produced} letter forms allowed by the rules can be produced "
              "(ZWJ repaya with `repaya_zwj`, archaic letters with `archaic`, ම්‍ර න්‍ර ල්‍ර with `classical`).", ""]
    si = ["# රෝමානුකරණ පරීක්ෂාව", "", "`tools/check_romanization.py` මගින් ජනනය කළ වාර්තාවකි.", "",
          "## ආවරණය", "",
          f"නීති අවසර දෙන අකුරු රූපවලින් {produced} ක් නිපදවිය හැක "
          "(ZWJ රේඵය `repaya_zwj` සමඟ, පුරාතන අකුරු `archaic` සමඟ, ම්‍ර න්‍ර ල්‍ර `classical` සමඟ).", ""]
    if gaps:
        report += ["Gaps: " + ", ".join(gaps), ""]
        si += ["නිපදවිය නොහැකි අකුරු රූප: " + ", ".join(gaps), ""]
    report += ["## Safety", "", "Every romanization of 1–3 sequences plus a space, checked against "
               f"{len(FORBIDDEN) + 1} forbidden patterns.", "", "| Options | Inputs | Violations |", "|---|---:|---:|"]
    si += ["## ආරක්ෂාව", "", "අනුක්‍රම 1 සිට 3 දක්වා (සහ හිස්තැනක්) ඇති සෑම රෝමානු ආදානයක්ම පරිවර්තනය කර, "
           f"ප්‍රතිදානය තහනම් රටා {len(FORBIDDEN) + 1} කට එරෙහිව පරීක්ෂා කර ඇත.", "",
           "| විකල්ප | ආදාන | උල්ලංඝන |", "|---|---:|---:|"]
    total_hits = 0
    for name, o in configs:
        hits, pool = safety(o)
        n = pool + pool ** 2 + pool ** 3
        count = sum(len(v) for v in hits.values())
        total_hits += count
        report.append(f"| {name} | {n:,} | {count} |")
        si.append(f"| {name} | {n:,} | {count} |")
        print(f"safety[{name}]: {n:,} inputs, {count} violations")
        for rule, examples in hits.items():
            shown = ", ".join(f"`{a}`→{b}" for a, b in examples[:3])
            report.append(f"| ↳ {rule} | | e.g. {shown} |")
            si.append(f"| ↳ {SI_NAMES[rule]} | | උදා: {shown} |")
    report += ["", "Forbidden patterns:", ""] + [f"- {name}" for name, _ in FORBIDDEN + [ARCHAIC_ONLY]] + [""]
    si += ["", "තහනම් රටා:", ""] + [f"- {SI_NAMES[name]}" for name, _ in FORBIDDEN + [ARCHAIC_ONLY]] + [""]
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / "romanization-check.md").write_text("\n".join(report), encoding="utf-8")
    (ROOT / "reports" / "romanization-check.si.md").write_text("\n".join(si), encoding="utf-8")
    raise SystemExit(1 if (gaps or total_hits) else 0)


if __name__ == "__main__":
    main()
