import json

from sanskrit_tools.panini.sutras.common_definitions import all_pratyayas,sup_pratyayaaH, tiNg_pratyayaaH
from sanskrit_tools.panini.devanagari.convert import convert_to_devanagari

"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():
    return json.dumps(dict( ( convert_to_devanagari(x) , {'ascii':x}) for x in all_pratyayas()))

def is_suptingant(pratyaya):
    if pratyaya in sup_pratyayaaH() or pratyaya in tiNg_pratyayaaH():
        return True
    else:
        return False


