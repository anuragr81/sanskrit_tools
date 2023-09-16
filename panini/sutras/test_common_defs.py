
from unittest import TestCase
from sanskrit_tools.panini.sutras import common_definitions as cd


class TransitionTest(TestCase):
    def test_next_after_taddhita(self):
        x=cd.next_possible_suffixes('aNn')
        self.assertTrue(len(x)>0)
        


