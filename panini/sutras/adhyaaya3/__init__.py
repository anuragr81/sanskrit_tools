from ..common_definitions import Suffix, Node, Dhaatu,tiNg_pratyayaaH, ach

class kartarishap_3010680:
    def __init__(self):
        self._types={'dhaatu_node':[Dhaatu],'suffix_node':[Suffix,'literal','lakaara']}
    def __call__(self,dhaatu_node,suffix_node):
        if isinstance(dhaatu_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) and \
                suffix_node._data.is_saarvadhaatuka() and \
                    suffix_node._data._lakaara in ('laXt','loXt','laNg','vidhiliNg') and \
                    ''.join(suffix_node._data._suffix) != 'shap':
                    # kartari shap is applied only in certain lakaaras
                 return Suffix("shap")
        return []

class chliLuNgi_3010460:
    def __init__(self):
        self._types={'dhaatu_node':[Dhaatu],'suffix_node':[Suffix,'literal','lakaara']}
        
    def __call__(self,dhaatu_node,suffix_node):
        if isinstance(dhaatu_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) and \
            suffix_node._data._lakaara in ('luNg',) and \
                ''.join(suffix_node._data._suffix) != 'sNNch' and \
                    ''.join(suffix_node._data._suffix) != 'chlNc':
                    # kartari shap is applied only in certain lakaaras
                 return Suffix("sNNch")
        return []
  

        
class syataasiilRiluXtoH_3010330:
    def __init__(self):
        self._types={'dhaatu_node':[Dhaatu],'suffix_node':[Suffix,'literal','lakaara']}
    def __call__(self,dhaatu_node,suffix_node):
        if isinstance(dhaatu_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) :
                
                if suffix_node._data._lakaara in ('lRiXt',) and \
                    ''.join(suffix_node._data._suffix) != 'sya':
                    return Suffix("sya")
                if suffix_node._data._lakaara in ('luXt',) and \
                    ''.join(suffix_node._data._suffix) != 'taas':                    
                    return Suffix("taas")
        return []
    

class XdityabhasyaapianubandhakaraNnasaamarthyaat_3010331:
    def __init__(self):
        self._types={'node':[Suffix],'suffix_node':[Suffix,'literal','lakaara']}
    def __call__(self,node,suffix_node):
        if isinstance(node._data,Suffix) and isinstance(suffix_node._data,Suffix):
            first_suffix_data=[x['output'] for x in node._output if 'new' in x and x['new']][-1]
            second_suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
            if second_suffix_data[0] == 'Xd':
                ach_indices_in_output = [ i for i,x in enumerate(node.get_output()) if x in ach()]
                if ach_indices_in_output :                
                    # picking the last ach onwards (Xti bhaaga)
                    return node.get_output()[:ach_indices_in_output[-1]]
            
        return node.get_output()
    

class itashcha_3041000:
    
    def __init__(self):
        self._types={'node':[Suffix,'literal']}
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be Node")
        suffix=node._data
        if not isinstance(suffix,Suffix):
            raise ValueError("Must be Suffix")
        if suffix._lakaara and suffix._lakaara in ('laNg','luNg','lRiNg','liNg1','liNg2','liNg') and node.get_output()[-1]=='i':
            return node.get_output()[:-1]
        
        return node.get_output()

class parasmaipadaanaaMNnalatususXthalaXthusaNnalvamaaH_3040820:
    def __init__(self):
        self._types={'node':[Suffix,'literal']}
    def __call__(self,node,anga_node):

        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must be of Node type")
        if isinstance(node._data,Suffix) :
            if node._data._lakaara == "liXt":
                suffix_data=[x['output'] for x in node._output if 'new' in x and x['new']][-1]
                suffix_name =''.join(suffix_data)
                mapping= {'tip':['Nn','a','l'], 'tas':['a','t','u','s'], 'jhi':['u','s'], 
                              'sip':['Xth','a','l'], 'Xthas':['a','Xth','u','s'],'Xtha':['a'], 
                              'mip':['Nn','a','l'], 'vas':['v','a'], 'mas':['m','a']}
                if suffix_name in tiNg_pratyayaaH() and suffix_name in mapping: 
                    return {'output':mapping[suffix_name],'mutate':True}
        return node.get_output()
