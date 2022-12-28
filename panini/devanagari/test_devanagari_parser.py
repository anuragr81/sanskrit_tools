import sys
from unittest import TestCase
import sanskrit_tools.panini.devanagari.convert as cnv

class ParsingTest(TestCase):
    def test_parsing_from_ascii_to_devanagari(self):
        self.assertTrue(cnv.convert_to_devanagari('uXshXtraM laabhaM labhyate')=="उष्ट्रंलाभंलभ्यते")
        
    def test_parsing_from_devanagari_to_ascii(self):
        self.assertTrue(''.join(cnv.parse_devanagari_to_ascii('अभभूईलृऋलल्लभी')) == 'abhabhuuiilRiRilallabhii')
