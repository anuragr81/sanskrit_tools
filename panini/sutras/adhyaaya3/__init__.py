from ..common_definitions import Suffix, Node, Dhaatu,tiNg_pratyayaaH, all_pratyayaaH, ach,list_past_rules_applied

    
class kartarishap_3010680:
    def __init__(self):
        self._numconditions=1
        itbeingshpratyayas = [p for p in all_pratyayaaH() if p[0:2]=='sh' or p[-2:]=="sh"]
        self._condition = {'self':{'lakaara':['laXt','loXt','laNg','liNg1'],
                                   'data':{itbeingshpratyayas+list(tiNg_pratyayaaH()) }
                                   }}
    def __call__(self,prefix_node,suffix_node):
        if isinstance(prefix_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) and \
                suffix_node._data.is_saarvadhaatuka() and \
                    suffix_node._data._lakaara in ('laXt','loXt','laNg','liNg1') and \
                    ''.join(suffix_node._data._suffix) != 'shap':
                    # kartari shap is applied only in certain lakaaras
                 return Suffix("shap")
        return []

class chliLuNgi_3010460:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'lakaara':{'domain': ['luNg']}
                           }}
        
    def __call__(self,prefix_node,suffix_node):
        if isinstance(prefix_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) and \
            suffix_node._data._lakaara in ('luNg',) and \
                ''.join(suffix_node._data._suffix) != 'sNNch' and \
                    ''.join(suffix_node._data._suffix) != 'chlNc':
                    # kartari shap is applied only in certain lakaaras
                 return Suffix("sNNch")
        return []

class syataasiilRiluXtoH_3010330:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'lakaara':{'domain':['lRiXt','luXt' ]}}}
    def __call__(self,prefix_node,suffix_node):
        if isinstance(prefix_node._data,Dhaatu) and \
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
        self._numconditions=1
        Xditsuffixes = [ x for x in  all_pratyayaaH() if x[0:2]=='Xd']
        self._condition = {'self': {'data':{'domain':Xditsuffixes}}}
    def __call__(self,node,suffix_node):
        if isinstance(node._data,Suffix) and isinstance(suffix_node._data,Suffix):

            second_suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
            if second_suffix_data[0] == 'Xd':
                ach_indices_in_output = [ i for i,x in enumerate(node.get_output()) if x in ach()]
                if ach_indices_in_output :                
                    # picking the last ach onwards (Xti bhaaga)
                    return node.get_output()[:ach_indices_in_output[-1]]
            
        return node.get_output()

class parasmaipadaanaaMNnalatususthalathusaNnalvamaaH_3040820:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{ 'pada':{'domain':['parasmaipada']}, 'lakaara':{'domain':['liXt']}}}
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
                              'sip':['th','a','l'], 'thas':['a','th','u','s'],'tha':['a'], 
                              'mip':['Nn','a','l'], 'vas':['v','a'], 'mas':['m','a']}
                if suffix_name in tiNg_pratyayaaH() and suffix_name in mapping: 
                    return {'output':mapping[suffix_name],'mutate':True}
        return node.get_output()

class eruH_3040860:
    def __init__(self):
        self._numconditions=1
        self._sutranum =str(type(self).__name__).split("_")[-1]
        self._condition = {'self':{'lakaara':{'domain':['loXt']}}}
        
    def __call__(self,node):

        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        # does not apply to merniH and serhyapichcha
        if isinstance(node._data,Suffix) and node._data._lakaara == 'loXt' and not set(list_past_rules_applied(node)).intersection([3040860,3040870,3040890]):
            i2umap ={'i':'u'}
            return [i2umap.get(x,x) for x in node.get_output()]
        return node.get_output()

class serhyapichcha_3040870:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'data':{'domain':['sip']},'lakaara':{'domain':['loXt']}}}
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self,node):

        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if isinstance(node._data,Suffix) and node._data._lakaara == 'loXt' and ''.join(node._data._suffix) == 'sip' and 3040870 not in list_past_rules_applied(node):
            return {'output':['h','i'], 'mutate':True}
        return node.get_output()

class merniH_3040890:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'data':{'domain':['mip']} ,'lakaara':{'domain':['loXt']}}}
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if isinstance(node._data,Suffix) and node._data._lakaara == 'loXt' and ''.join(node._data._suffix) == 'mip' and 3040890 not in  list_past_rules_applied(node):
            return {'output':['n','i'], 'mutate':True}
        return node.get_output()

class aaXduttamasyapichchha_3040920:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'data':{'domain':['mip','vas','mas','iXt','vahi','mahiNg']} , 
                                   'lakaara':{'domain':['loXt']}} }
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self, prefix_node, suffix_node):
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        if not isinstance(prefix_node,Node):
            raise ValueError("prefix_node must be of Node type")
        
        if 3040920 not in list_past_rules_applied(prefix_node) and 3040920 not in list_past_rules_applied(suffix_node)  and isinstance(suffix_node._data,Suffix) and suffix_node._data._lakaara == 'loXt' and ''.join(suffix_node._data._suffix) in ('mip','vas','mas','iXt','vahi','mahiNg'):
            return Suffix('aaXt')
            
        return []
    
class nityaMNgitaH_3040990:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'lakaara':{'domain':['loXt','laNg','luNg','lRiNg','liNg1','liNg2']}, 
                                   'data':{'domain':['mip','vas','mas',"iXt","vahi","mahiNg"] }}}
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self,node):
        cond_langvat = (node._data._lakaara  and node._data._lakaara.endswith('Ng') or node._data._lakaara == 'loXt' )
        if isinstance(node._data,Suffix) and node._data._lakaara and cond_langvat and ''.join(node._data._suffix) in ('mip','vas','mas',"iXt","vahi","mahiNg"):
            if 3040990 not in list_past_rules_applied(node):
                if node.get_output()[-1]=='s':
                    return node.get_output()[:-1]
                
            
        return node.get_output()



class itashcha_3041000:
    
    def __init__(self):
        self._condition = {'self':{ 'index':{-1:{'domain':['i']}},
                                   'lakaara':{'domain':['loXt','laNg','luNg','lRiNg','liNg1','liNg2']}}}
        self._numconditions=2
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be Node")
            
        if not node.get_output():
            return node.get_output()
        suffix=node._data
        if not isinstance(suffix,Suffix):
            raise ValueError("Must be Suffix")
        if suffix._lakaara and suffix._lakaara in ('laNg','luNg','lRiNg','liNg1','liNg2') and node.get_output()[-1]=='i':
            return node.get_output()[:-1]
        
        return node.get_output()

class tasthasthamipaamtaamtamtaamaH_3041010:
    def __init__(self):
        self._numconditions=1
        self._sutranum =str(type(self).__name__).split("_")[-1]
        self._condition = {'self':{ 'data':{'domain':['tas','thas','tha','mip']},
                                 'lakaara':{'domain':['loXt','laNg','luNg','lRiNg','liNg1','liNg2' ]}}}
    def __call__(self,node):
        # loXtolaNgvat allows loXt 
        if isinstance(node._data,Suffix) and node._data._lakaara and (node._data._lakaara.endswith('Ng') or node._data._lakaara=='loXt' ):
            if 3041010 not in list_past_rules_applied(node):
                suffix_replacement_dict = {'tas':['t','aa','m'] , 'thas':['t','a','m'], 'tha':['t','a'], 'mip':['a','m']}
                if ''.join(node._data._suffix) in suffix_replacement_dict :
                    return suffix_replacement_dict [''.join(node._data._suffix)]
                                
        return node.get_output()



        
class yaasuXtparasmaipadeXshuudaattoNgichchha_3041030:
    def __init__(self):
        self._numconditions=2
        self._condition = {'self':{'pada':{'domain':['parasmaipada']}, 'lakaara':{'domain':['liNg1','liNg2']}}}
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self, prefix_node, suffix_node):
        if not isinstance(prefix_node,Node):
            raise ValueError("prefix_node must be of Node type")                        
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
                 
        # yaasuXt should not be introduced after suXt has been added through suXttithoH
        if isinstance(prefix_node._data,Suffix) and ''.join(prefix_node._data._suffix) != 'yaasuXt' and not set([3041030 ,3041070]).intersection( set(list_past_rules_applied(prefix_node))) :
            if suffix_node._data._lakaara in ('liNg1','ling2',):
                print("yaasuXt created and should be considered Ngitvat")
                return Suffix('yaasNNXt')
                                
        return []


        
class suXttithoH_3041070:
    def __init__(self):
        self._numconditions=2
        itwithtsuffixes = [x for x in all_pratyayaaH() if x[0] == 't' or x[0:2]=='th']
        self._condition = {'self':{'lakaara':{'domain':['liNg1','liNg2']} , 'data':{'domain':[itwithtsuffixes]}}
                           }
        self._sutranum =str(type(self).__name__).split("_")[-1]
    def __call__(self, prefix_node, suffix_node):
        if not isinstance(prefix_node,Node):
            raise ValueError("prefix_node must be of Node type")                        
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")                        
        
        if isinstance(prefix_node._data,Suffix) and ''.join(prefix_node._data._suffix) != 'suXt' and not set([3041070]).intersection( set(list_past_rules_applied(prefix_node))) :
            if suffix_node._data._lakaara in ('liNg1','ling2',) and ('t' in suffix_node._data._suffix or 'th' in suffix_node._data._suffix ):
                return Suffix('sNNXt')
                
                
        return []