"""
The module that has all pratyaya-related response-functions i.e. handlers that prepare the response for the client
"""

import json

import panini.dhaatus as dh

from panini.sutras.common_definitions import sup_pratyayaaH, tiNg_pratyayaaH, taddhita_pratyayaaH, kRit_pratyayaaH, next_possible_suffixes, lakaaras

from panini.devanagari.convert import convert_to_devanagari

def update_dict(original_dict, key, value):
    original_dict[key]= value
    return original_dict

def get_all_dhaatus():
    # append type = dhaatu to the values in dhaatu_meaning for response
    return json.dumps(dict( (k,update_dict(v,'type','dhaatu')) for k,v in dh.dhaatus_meaning().items()) )


def get_all_dict_types ():
    return {'noun-endings':sup_pratyayaaH(),'verb-endings':tiNg_pratyayaaH(), 'nominal-suffixes':taddhita_pratyayaaH(), 'verbal-suffixes': kRit_pratyayaaH(),'lakaara':lakaaras() }


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
