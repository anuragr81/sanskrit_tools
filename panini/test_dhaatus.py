
from unittest import TestCase
import sanskrit_tools.panini.dhaatus as dh


class DhaatusLoadingTest(TestCase):
    def test_dhaatus_load(self):
        json_dhaatus = dh.get_all_dhaatus()
        self.assertTrue(len(json_dhaatus)>0)
        dmstruct = dh.dhaatus_meaning()
        self.assertTrue(isinstance(dmstruct,dict))
        keys = list(dmstruct.keys())
        self.assertTrue(len(keys)>0)
        self.assertTrue('meaning' in dmstruct[keys[0]] )
        self.assertTrue('ascii' in dmstruct[keys[0]] )

    def test_halanta_upadesha_map(self):
        m=dh.dhaatus_halant_to_upadesha()
        self.assertTrue(m['chiNc'] == "चिँ")




