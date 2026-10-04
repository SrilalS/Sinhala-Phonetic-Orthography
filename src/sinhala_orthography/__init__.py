"""Sinhala orthography and phonetic romanization: inventory, rules, conversion, disambiguation."""
from .inventory import CONSONANTS, SIGNS, VOWELS, entries
from .lexicon import Lexicon, candidates, normalize, restyle, sound_key
from .romanization import to_sinhala, transliterate

__all__ = ["CONSONANTS", "SIGNS", "VOWELS", "entries", "Lexicon", "candidates", "normalize", "restyle",
           "sound_key", "to_sinhala", "transliterate"]
__version__ = "0.1.0"
