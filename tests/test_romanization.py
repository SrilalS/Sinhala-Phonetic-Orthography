"""Romanization fixtures. Each case cites the rule (G-*) or convention (R-*) it checks.

    python -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from sinhala_orthography import to_sinhala  # noqa: E402

Z = "‍"
CASES = [
    # basics
    ("amma", "අම්ම", "G-HC-03"), ("ammaa", "අම්මා", ""), ("k", "ක්", "G-HC-01"), ("ka", "ක", ""),
    ("sinhala", "සින්හල", "R-11: lexicon decides ං before h"), ("akShara", "අක්ෂර", "R-10"),
    # R-01 d / D / dh
    ("kohomada", "කොහොමද", "R-01"), ("baDa", "බඩ", "R-01"), ("dharmaya", "ධර්මය", "R-01, R-08"),
    ("Dha", "ඪ", "R-01"), ("qa", "ද", "alias"), ("hazda", "හඳ", "R-01 sanyaka"), ("hazDa", "හඬ", "R-01 sanyaka"),
    # R-02 vowel length
    ("kee", "කේ", "R-02"), ("koo", "කෝ", "R-02"), ("kii", "කී", "R-02"), ("kuu", "කූ", "R-02"),
    # R-03 fallback without lexicon: cluster
    ("kanda", "කන්ද", "R-03"), ("amba", "අම්බ", "R-03"), ("anga", "අංග", "R-03 + R-11"),
    # R-04
    ("kae", "කැ", "R-04"), ("kaee", "කෑ", "R-04"), ("kA", "කැ", ""), ("kAa", "කෑ", ""), ("ae", "ඇ", "R-04"),
    # R-05 glides
    ("lait", "ලයිට්", "R-05"), ("kauda", "කවුද", "R-05"), ("ai", "අයි", "R-05"), ("au", "අවු", "R-05"),
    ("Ai", "ඇයි", "G-VS-06"), ("toppia", "ටොප්පිය", "G-VS-06"), ("dua", "දුව", "G-VS-06"), ("kaai", "කායි", "G-VS-06"),
    ("oun", "ඔවුන්", "G-VS-06"),
    # R-05b explicit diphthong signs
    ("kE", "කෛ", "R-05b"), ("AuShadha", "ඖෂධ", "R-05b"), ("pAudgalika", "පෞද්ගලික", "R-05b"),
    # R-06 ru
    ("kru", "කෘ", "R-06, G-VS-15"), ("kruura", "කෲර", "R-06, G-VS-15"), ("mrudu", "මෘදු", "G-VS-15"),
    ("gruup", "ගෲප්", "G-VS-15"), ("kruua", "කෲව", "G-VS-06 glide after ෲ"), ("karu", "කරු", "R-06"),
    ("rru", "ර්රු", "no ෘ after ර"), ("Lru", "ළරු", "C-9"), ("kramaya", "ක්" + Z + "රමය", "R-07"),
    ("kR", "කෘ", "R-06"), ("kRShi", "කෘෂි", "R-06"), ("kRR", "කෲ", "R-06"), ("R", "ඍ", "R-06"),
    # R-07 rakaransaya, but plain hal before ර after ම න ල
    ("dumriya", "දුම්රිය", "R-07"), ("henri", "හෙන්රි", "R-07"), ("mrudu", "මෘදු", "R-06"),
    ("dilrukshi", "දිල්රුක්ශි", "C-13: ලෘ is unattested"), ("samruddhi", "සමෘද්ධි", "C-13: මෘ is attested"),
    ("chru", "ච්" + Z + "රු", "C-13: චෘ is unattested"), ("nruu", "න්රූ", "C-13: නෲ is unattested, R-07"),
    ("lR", "ලෘ", "R-06: explicit R still writes ෘ"), ("kramaya", "ක්" + Z + "රමය", "G-HC-12"), ("shrii", "ශ්" + Z + "රී", ""),
    # R-08 / R-09 repaya plain, kārya
    ("karma", "කර්ම", "R-08"), ("kaarya", "කාර්ය", "R-09"),
    # yansaya
    ("vidyaava", "විද්" + Z + "යාව", "G-HC-11"), ("vaakya", "වාක්" + Z + "ය", "G-HC-11"),
    # R-11 anusvara
    ("lankaava", "ලංකාව", "R-11"), ("bAnkuva", "බැංකුව", "R-11"), ("sing", "සිං", "R-11 final ng"),
    ("kax", "කං", "G-NS-01"), ("kx", "කං", "G-NS-01: hal never before ං"), ("x", "x", "G-NS-01: no base"),
    ("nka", "න්ක", "G-NS-01: ං never word-initial"),
    # R-12
    ("anya", "අන්" + Z + "ය", "R-12"), ("agni", "අග්නි", "R-12"), ("zhaanaya", "ඥානය", "R-12"),
    # hard guards
    ("aXa", "අඟ", "G-HC-08: /ŋ/ + vowel → ඟ"), ("aXga", "අඞ්ග", "G-HC-08"), ("Xa", "Xඅ", "G-PH-01: ඞ never starts a word"), ("kazd", "කඳ", "G-HC-06: no hal on sanyaka"), ("kaL", "කළ", "G-HC-07"),
    ("kaLla", "කළල", "G-HC-07"), ("zdra", "ද්" + Z + "ර", "G-PH-01: no sanyaka word-initially"), ("Ba", "බ", "G-PH-01"), ("axzda", "අඳ", "G-NS-09"), ("RR", "ඍ", "G-VS-08"),
    ("zja", "ජ", "R-14: ඦ is archaic"),
]
SETTINGS = [
    ("karma", {"repaya_zwj": True}, "කර්" + Z + "ම", "R-08 setting"),
    ("kaarya", {"repaya_zwj": True}, "කාර්" + Z + "ය", "R-08 setting"),
    ("akShara", {"classical": True}, "අක්" + Z + "ෂර", "R-10 setting"),
    ("ananda", {"classical": True}, "අනන්" + Z + "ද", "R-10 setting"),
    ("thaamra", {"classical": True}, "තාම්" + Z + "ර", "R-07 setting"),
    ("mrudu", {"rakaransaya_u": True}, "ම්" + Z + "රුදු", "R-06 setting: ෘ written out keeps ZWJ"),
    ("dilrukshi", {"classical": True}, "දිල්රුක්ශි", "R-07: ල්රු stays plain"),
    ("kohomadha", {"retroflex_d": True}, "කොහොමද", "R-01 setting: dh = ද"),
    ("bada", {"retroflex_d": True}, "බඩ", "R-01 setting: d = ඩ"),
    ("Dharmaya", {"retroflex_d": True}, "ධර්මය", "R-01 setting: Dh = ධ"),
    ("Dha", {"retroflex_d": True}, "ධ", "R-01 setting"), ("Da", {"retroflex_d": True}, "ඪ", "R-01 setting: D = ඪ"),
    ("hozdha", {"retroflex_d": True}, "හොඳ", "R-01 setting: zdh = ඳ"), ("kazda", {"retroflex_d": True}, "කඬ", "R-01 setting: zd = ඬ"),
    ("qa", {"retroflex_d": True}, "ද", "alias kept"), ("dhha", {"retroflex_d": True}, "ධ", "alias kept"),
    ("RR", {"archaic": True}, "ඎ", "R-14"),
    ("k~l", {"archaic": True}, "කෟ", "R-14"),
    ("izja", {"archaic": True}, "ඉඦ", "R-14"),
    ("ka~n", {"archaic": True}, "කඁ", "R-14"),
    ("dham+ma", {"archaic": True}, "ධම" + Z + "්" + "ම", "R-14 touching"),
    ("kru", {"rakaransaya_u": True}, "ක්" + Z + "රු", "R-06 setting"),
    ("kruura", {"rakaransaya_u": True}, "ක්" + Z + "රූර", "R-06 setting"),
    ("kR", {"rakaransaya_u": True}, "කෘ", "R-06: explicit R still gives ෘ"),
]



class RomanizationTest(unittest.TestCase):
    def test_default(self):
        for roman, expected, rule in CASES:
            with self.subTest(roman=roman, rule=rule):
                self.assertEqual(to_sinhala(roman), expected)

    def test_options(self):
        for roman, options, expected, rule in SETTINGS:
            with self.subTest(roman=roman, options=options, rule=rule):
                self.assertEqual(to_sinhala(roman, **options), expected)


if __name__ == "__main__":
    unittest.main()
