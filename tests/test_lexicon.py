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
from sinhala_orthography import Lexicon, candidates, normalize, restyle, to_sinhala  # noqa: E402
from sinhala_orthography.romanization import GAETTA_AFTER  # noqa: E402
import json  # noqa: E402

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


class NormalizeTest(unittest.TestCase):
    def test_restores_zwj(self):
        self.assertEqual(normalize("ක්රමය"), "ක්" + Z + "රමය")
        self.assertEqual(normalize("විද්යාව"), "විද්" + Z + "යාව")
        self.assertEqual(normalize("කාර්යය"), "කාර්යය")                        # never after ර (G-HC-14)
        self.assertEqual(normalize("දුම්රිය"), "දුම්රිය")                      # C ් ර after ම න ල stays plain (R-07)
        self.assertEqual(normalize("රම්ය"), "රම්" + Z + "ය")                     # yansaya after ම still joins
        self.assertEqual(normalize("ක්" + Z + "රමය"), "ක්" + Z + "රමය")          # already joined

    def test_overlapping_joins(self):
        w = normalize("ක්ය්ය")
        self.assertEqual(w, "ක්" + Z + "ය්" + Z + "ය")
        self.assertEqual(normalize(w), w)


class GaettaAfterTest(unittest.TestCase):
    def test_matches_validity(self):
        """C-13 writes ෘ / ෲ exactly after the consonants whose form is attested in validity.json."""
        rows = json.loads((Path(__file__).resolve().parents[1] / "data" / "validity.json").read_text(encoding="utf-8"))
        for vid in ("ru", "ruu"):
            attested = {r["text"][0] for r in rows if r["id"].endswith("." + vid) and not r["id"].startswith("vowel.")
                        and r["status"] in ("valid", "loan", "rare")}
            self.assertEqual(GAETTA_AFTER[vid[1:]], attested, vid)   # keyed by the vowel after r


class RestyleTest(unittest.TestCase):
    """Lexicon words follow the converter options, so Space never undoes a chosen style."""

    def test_matches_the_converter(self):
        for roman, options in [("kruura", {"rakaransaya_u": True}), ("mrudu", {"rakaransaya_u": True}),
                               ("karma", {"repaya_zwj": True}), ("kaarya", {"repaya_zwj": True}),
                               ("akShara", {"classical": True}), ("ananda", {"classical": True})]:
            with self.subTest(roman=roman, options=options):
                self.assertEqual(restyle(to_sinhala(roman), **options), to_sinhala(roman, **options))

    def test_no_options_no_change(self):
        for word in ["කෲර", "කර්ම", "අක්ෂර", "ර්රු", "ක්" + Z + "රමය"]:
            self.assertEqual(restyle(word), word)
            self.assertEqual(restyle(word, archaic=True), word)

    def test_leaves_other_spellings_alone(self):
        self.assertEqual(restyle("රෘ", rakaransaya_u=True), "රෘ")                 # never after ර (R-06)
        self.assertEqual(restyle("කර්" + Z + "ම", repaya_zwj=True), "කර්" + Z + "ම")  # already joined
        self.assertEqual(restyle("අක්කා", classical=True), "අක්කා")             # not a bandi pair

    def test_candidates_use_the_options(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8") as f:
            f.write("කෲර\t500\nකර්ම\t900\n")
        lex = Lexicon(f.name)
        os.unlink(f.name)
        self.assertEqual(candidates(lex, "kruura")[0], "කෲර")
        self.assertEqual(candidates(lex, "kruura", rakaransaya_u=True)[0], "ක්" + Z + "රූර")
        self.assertEqual(candidates(lex, "karma", repaya_zwj=True)[0], "කර්" + Z + "ම")

    def test_repairs_only_lists_without_zwj(self):
        import tempfile

        def load(text):
            with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8") as f:
                f.write(text)
            lex = Lexicon(f.name)
            os.unlink(f.name)
            return set(lex.count)

        # No ZWJ anywhere: the list lost it, so joins are restored.
        self.assertEqual(load("ක්රමය\t10\nබවත්ය\t5\n"), {"ක්" + Z + "රමය", "බවත්" + Z + "ය"})
        # Some ZWJ: the list kept it, so a plain hal is a word boundary (බවත් + ය).
        self.assertEqual(load("ක්" + Z + "රමය\t10\nබවත්ය\t5\n"), {"ක්" + Z + "රමය", "බවත්ය"})


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
