

import pandas as pd
import json


if __name__ == '__main__':
    x = pd.read_csv('dhaatucols.csv')
    x = x [~pd.isnull(x.halantname)]
    x = x [~pd.isnull(x.name)]
    x = x [~pd.isnull(x.english)]
    print(json.dumps(dict(zip(x.halantname,x.english))))


