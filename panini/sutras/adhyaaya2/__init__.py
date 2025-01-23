from ..common_definitions import Suffix, Node, Dhaatu, juhotyaadi_dhaatus, shap_equivalents


class yaNgoachicha_2040740:
    def __init__(self):
        self._numconditions=2 #This is of a lower priority than sanyaNgoH. 
                           
    def __call__(self,node,suffix_node):
        """
        abhyaasa output is stored inside of a dhaatu
        """
        
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if isinstance(node._data,Dhaatu) and node.get_output():
            if node.get_output()[-1] == 'y':
                lastAadesha = [x['output'] for x in suffix_node._output if 'new' in x][-1]
                if ''.join(lastAadesha)=='ach':
                    # lopa of 'y'
                    # ach is already used up now and should prevent the guNna of the 
                    # node preceding the current node
                    return node.get_output()[:-1]

        return node.get_output()

class juhotyaadibhyaHshluH_2040750:
    def __init__(self):
        self._numconditions=0
        
    def __call__(self,prefix_node,suffix_node):
        if isinstance(prefix_node._data,Dhaatu) and \
            ''.join(prefix_node._data._data) in juhotyaadi_dhaatus() and \
            isinstance(suffix_node._data,Suffix) and \
                suffix_node._data.is_saarvadhaatuka() and \
                    suffix_node._data._lakaara in ('laXt','loXt','laNg','liNg1') and \
                    ''.join(suffix_node._data._suffix) not in tuple(shap_equivalents().keys()):
                    # applied only in certain lakaaras/moods
                if suffix_node._data._mood is None or suffix_node._data._mood in ('karttaa',):
                    return Suffix("shlu")
                elif suffix_node._data._mood in ('karma','bhaava'):
                    return Suffix("yak")
        return []


class luXtaHprathamasyaXdaaraurasaH_2040850:
    def __init__(self):
        self._numconditions=1
                           
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