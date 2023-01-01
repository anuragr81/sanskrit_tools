

import pandas as pd
import devanagari.convert as cnv
import json
import dhaatus as dh


def print_dhaatus_ascii():
    dhs=[k for k,v in json.loads(dh.get_all_dhaatus()).items()]
    print([''.join(cnv.parse_devanagari_to_ascii(k[0:len(k)])) for k in dhs])

if __name__ == '__main__':
    x = pd.read_csv('dhaatucols.csv')
    x = x [~pd.isnull(x.halantname)]
    x = x [~pd.isnull(x.name)]
    x = x [~pd.isnull(x.english)]
    print(json.dumps(dict(zip(x.halantname,x.english))))


