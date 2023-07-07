import json

from panini.sutras.common_definitions import sup_pratyayaaH, tiNg_pratyayaaH, taddhita_pratyayaaH, strii_pratyayaaH, kRit_pratyayaaH
from panini.devanagari.convert import convert_to_devanagari

def broad_pratyayaclasses ():
    return ('subaadi','tibaadi','taddhita','kRidanta')

"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():
    dictTypes = {'subaadi':sup_pratyayaaH(),'tibaadi':tiNg_pratyayaaH(), 'taddhita':taddhita_pratyayaaH(), 'kRidanta': kRit_pratyayaaH()}
    dictSuffixes={}

    for ptype, pratyayas in dictTypes.items():
        for pratyaya in pratyayas:
            dictSuffixes[convert_to_devanagari(pratyaya)]  = {'ascii':pratyaya, 'type':convert_to_devanagari(ptype)}
    return json.dumps(dictSuffixes)

def is_suptingant(pratyaya):
    if pratyaya in sup_pratyayaaH() or pratyaya in tiNg_pratyayaaH():
        return True
    else:
        return False


