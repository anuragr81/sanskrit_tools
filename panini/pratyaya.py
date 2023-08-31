import json

from panini.sutras.common_definitions import sup_pratyayaaH, tiNg_pratyayaaH, taddhita_pratyayaaH, strii_pratyayaaH, kRit_pratyayaaH, next_possible_suffixes

from panini.devanagari.convert import convert_to_devanagari


def get_all_dict_types ():
    return {'noun-endings':sup_pratyayaaH(),'verb-endings':tiNg_pratyayaaH(), 'nominal-suffixes':taddhita_pratyayaaH(), 'verbal-suffixes': kRit_pratyayaaH()}


"""
output in devanagari using mapping from https://everythingfonts.com/unicode/devanagari
"""
def get_all_suffixes():
    dictSuffixes={}
    dictTypes = get_all_dict_types ()

    for ptype, pratyayas in dictTypes.items():
        for pratyaya in pratyayas:
            dictSuffixes[convert_to_devanagari(pratyaya)]  = {'ascii':pratyaya, 'type':ptype}
    return json.dumps(dictSuffixes)


"""
Avoiding sending sup and taddhita suffixes to dhaatus
"""
def get_dhaatu_suffixes():
    dictTypes = {'verb-endings':tiNg_pratyayaaH(), 'verbal-suffixes': kRit_pratyayaaH()}
    dictSuffixes={}
    for ptype, pratyayas in dictTypes.items():
        for pratyaya in pratyayas:
            dictSuffixes[convert_to_devanagari(pratyaya)]  = {'ascii':pratyaya, 'type':ptype}
    return json.dumps(dictSuffixes)


def is_suptingant(pratyaya):
    if pratyaya in sup_pratyayaaH() or pratyaya in tiNg_pratyayaaH():
        return True
    else:
        return False


def get_next_pratyayas(pratyaya):
    dictTypes = get_all_dict_types()
    ptypeDict = {}
    for k,v in dictTypes.items():
        for sufname in v:
            ptypeDict[sufname]=k


    suffixes = next_possible_suffixes(pratyaya)
    dictSuffixes={}

    for suffix in suffixes:
        dictSuffixes[convert_to_devanagari(suffix)]  = {'ascii':suffix, 'type':ptypeDict[suffix]}

    return json.dumps(dictSuffixes)
