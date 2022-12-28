import sys
from unittest import TestCase
import sanskrit_tools.panini.devanagari.convert as cnv

class ParsingTest(TestCase):
    def test_always_passes(self):
        self.assertTrue(cnv.convert_to_devanagari('uXshXtraM laabhaM labhyate')=="उष्ट्रंलाभंलभ्यते")
