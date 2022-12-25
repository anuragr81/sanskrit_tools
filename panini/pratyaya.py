from sutras.common_definitions import all_pratyayas
from devanagari.convert import convert_to_devanagari

"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():

    return [convert_to_devanagari(x) for x in all_pratyayas()]


print(get_all_suffixes())
