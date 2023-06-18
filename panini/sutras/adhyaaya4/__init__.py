from ..common_definitions import Suffix

class vRiddhaachchhaH_4021130:
    def __init__(self):
        self._numconditions = 1
    def __call__(self,x):
        if x.has_vRiddhi():
            return [x,Suffix('chha')]
        return [x]
