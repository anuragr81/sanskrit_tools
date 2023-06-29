from ..common_definitions import Suffix, Node



class luXtaHprathamasyaXdaaraurasaH_2040850:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'data':{'domain':["tip","tas","jhi"]},
                                   'lakaara':{'domain':['luXt']}
                                   }
                           
                           }
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
    
        if isinstance(node._data,Suffix) :
            
            suffix_data=[x['output'] for x in node._output if 'new' in x and x['new']][-1]
            suffix_name =''.join(suffix_data)
            if suffix_name in ("tip","tas","jhi",) and node._data._lakaara == 'luXt':
                mapping= {'tip':['Xd','aa'], 'tas':['r','au'], 'jhi':['r','a','s']}        
                return {'output':mapping[suffix_name],'mutate':True}
        return node.get_output()