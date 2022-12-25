import json

from sanskrit_tools.panini.sutras.common_definitions import all_pratyayas
from sanskrit_tools.panini.devanagari.convert import convert_to_devanagari

"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():
    return json.dumps(dict( ( convert_to_devanagari(x) , '') for x in all_pratyayas()))


