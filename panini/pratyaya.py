import json

from panini.sutras.common_definitions import sup_pratyayaaH, tiNg_pratyayaaH, classified_pratyayaaH
from panini.devanagari.convert import convert_to_devanagari

"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():
    return json.dumps(dict( ( convert_to_devanagari(x) , {'ascii':x}) for x in classified_pratyayaaH()))

def is_suptingant(pratyaya):
    if pratyaya in sup_pratyayaaH() or pratyaya in tiNg_pratyayaaH():
        return True
    else:
        return False


