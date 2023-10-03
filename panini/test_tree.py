


import sys
from unittest import TestCase

sys.path.append('/home/anuragr/research_persona/sanskrit_tools')


import sanskrit_tools.panini.expressiontree as expt


class ExpressionTreeTest(TestCase):

    def test_tree_wtih_ascii_input(self):
        ep = expt.prepare_node_structure(['paXth','tip'],['dhaatu','tibaadi'])
        pe= expt.process_until_finish(ep)

        output_string = ""
        for x in pe:
            output_string = output_string + ''.join((x._output[-1]['output']))
        self.assertTrue(output_string== "paXthati")




