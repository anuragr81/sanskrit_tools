
import numpy as np

import pandas as pd
import devanagari.convert as cnv
import json
import dhaatus as dh


def print_dhaatus_ascii():
    dhs=[k for k,v in json.loads(dh.get_all_dhaatus()).items()]
    print([''.join(cnv.parse_devanagari_to_ascii(k[0:len(k)])) for k in dhs])


def read_names_json():
    x = pd.read_csv('dhaatucols.csv')
    x = x [~pd.isnull(x.halantname)]
    x = x [~pd.isnull(x.name)]
    x = x [~pd.isnull(x.english)]
    return (json.dumps(dict( (x.iloc[k].halantname,{'meaning':x.iloc[k].english,'ascii': ''.join(cnv.parse_devanagari_to_ascii(x.iloc[k].halantname))  }) for k in range(x.shape[0]))))

def read_aniXt_property():
    x = pd.read_csv('dhaatucols.csv')
    x = x [~pd.isnull(x.halantname)]
    x = x [~pd.isnull(x.name)]
    x = x [~pd.isnull(x.english)]
    x["aniXt"]= (x.iXt !="सेट्")
    x["aniXt"]  = x.aniXt.apply(lambda t : "true" if t else "false")
    dictraw = (dict((''.join(cnv.parse_devanagari_to_ascii( x.iloc[k].halantname )), {'aniXt':x.iloc[k].aniXt} ) for k in range(x.shape[0])))
    return json.dumps(dictraw)


def unique_entries(entries):
    allentries = (list(set(entries)))
    ascii_entries = [cnv.parse_devanagari_to_ascii(e) for e in allentries ]
    return([''.join((ae)) for ae in ascii_entries])


if __name__ == '__main__':
    #print (read_aniXt_property())
    print(read_names_json())

