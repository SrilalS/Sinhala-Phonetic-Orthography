"""Disambiguation fixtures: the expected spelling must rank first.

Needs a word-frequency list ("word<TAB>count" per line). Point SINHALA_WORD_LIST at it,
e.g. the NLPC list from https://github.com/nlpcuom/Word-Frequency-List-for-Sinhala.
The tests are skipped when the variable is not set.
"""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from sinhala_orthography import Lexicon, candidates  # noqa: E402

WORD_LIST = os.environ.get("SINHALA_WORD_LIST")

Z = "‍"
EXACT = [
    # (romanized, expected top-1, rule it exercises)
    ("honda", "හොඳ", "R-03 sanyaka via lexicon"), ("kanda", "කන්ද", "R-03 cluster wins by frequency"),
    ("kazda", "කඳ", "explicit z-key beats frequency"), ("ganga", "ගඟ", "R-03"),
    ("sinhala", "සිංහල", "R-11 ං via lexicon"), ("lankawa", "ලංකාව", "R-11"),
    ("thiyenawa", "තියෙනවා", "G-TY-04 length via lexicon"), ("amma", "අම්මා", "G-TY-04"), ("karanawa", "කරනවා", "G-TY-04"),
    ("kohomada", "කොහොමද", "R-01"), ("gedara", "ගෙදර", "R-01"), ("bada", "බඩ", "R-01 ඩ via lexicon"),
    ("doktar", "ඩොක්ටර්", "R-01 ඩ via lexicon"),
    ("vaidya", "වෛද්" + Z + "ය", "R-05 ෛ via lexicon"), ("aushadha", "ඖෂධ", "R-05 ඖ via lexicon"),
    ("krushi", "කෘෂි", "R-06 ෘ via lexicon"),
    ("prashnaya", "ප්" + Z + "රශ්නය", "ZWJ restored"), ("vidyaava", "විද්" + Z + "යාව", "ZWJ restored"),
    ("sri", "ශ්" + Z + "රී", "ශ/ස + length"), ("vishvaasaya", "විශ්වාසය", "G-SP-05"),
    ("lamaya", "ළමයා", "G-SP-04 ළ via lexicon"), ("pilithura", "පිළිතුර", "G-SP-04"), ("malu", "මාළු", "G-SP-04"),
    ("ayubowan", "ආයුබෝවන්", "length"), ("sthuthiyi", "ස්තූතියි", "length"), ("mama", "මම", ""), ("api", "අපි", ""),
]
PARTIAL = [("kohom", "කොහොම"), ("lank", "ලංකා"), ("sinh", "සිංහල"), ("vidy", "විද්" + Z + "ය")]



@unittest.skipUnless(WORD_LIST, "set SINHALA_WORD_LIST to a word-frequency list")
class DisambiguationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lex = Lexicon(WORD_LIST)

    def test_top1(self):
        for roman, expected, rule in EXACT:
            with self.subTest(roman=roman, rule=rule):
                self.assertEqual(candidates(self.lex, roman)[0], expected)

    def test_partial(self):
        for roman, prefix in PARTIAL:
            with self.subTest(roman=roman):
                self.assertTrue(candidates(self.lex, roman, partial=True)[0].startswith(prefix))


if __name__ == "__main__":
    unittest.main()
