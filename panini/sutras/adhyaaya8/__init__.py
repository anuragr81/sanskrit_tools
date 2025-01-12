import re
from ..common_definitions import pratyaahaara, ach, hal, Node, Dhaatu
from ..common_definitions import Suffix, Praatipadika, kRit_pratyayaaH
from ..common_definitions import list_past_rules_applied
from ..common_definitions import find_eldest_parent1_of_condition,find_eldest_parent2_of_condition
from ..common_definitions import tiNg_pratyayaaH, sup_pratyayaaH

class kharavasaanayorvisarjaniiyaH_8010150:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node):
        # must be used in avasaana
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        pada = node.get_output()
        return pada
        #khar = pratyaahaara('kh','r')
        #if pada[-1]=="r" and (pada[-2] in khar or pada[-2] in ach()):
        #    return pada[0:-1] + ['H']
        #return pada


class nalopaHpraatipaadikaantasya_8020070:
    def __init__(self):
        self._numconditions = 2 # conditions being two ensures that 
                                # the sutra isn't applied when chetan is formed 
                                # and halNgyaabhyosutisyapraktamhal (6.1.66) is applied
                                # (alternatively, this sutra 
                                # could be explored as a post-processing sutra)
        
    def __call__(self,node,suffix_node):
        #
        
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        
        if not isinstance(node,Node):
            raise ValueError("suffix_node must of type Node")
        
        if node.get_output() and node.get_output()[-1]=='n' and isinstance(suffix_node._data,Suffix) \
            and ''.join(suffix_node._data._suffix) in tiNg_pratyayaaH()+sup_pratyayaaH():
            if isinstance(node._data,Praatipadika) or isinstance(node._data,Suffix):
                return node.get_output()[0:-1]
        return node.get_output()

    
class saMyogaantasyalopaH_8020230:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,anga_node ,node):        
        
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
    
        if not node.get_output():
            return node.get_output()
        
        
        if len(node.get_output())>1:
            # for two consecutive consonants from last in a node, only the 
            #     first consonant remains
            if node.get_output()[-1] in hal() and node.get_output()[-2] in hal():
                return node.get_output()[:-1]
        elif len(node.get_output())==1 and len(anga_node.get_output())>0:
            # for a single-size node with the only char being a consonant and 
            #     an anga_node ending with consonant, the entire node is empty
            if node.get_output()[0] in hal() and anga_node.get_output()[-1] in hal():
                return []
            
        return node.get_output()
    

class vrashchabhrasjasRijamRijayajaraajabhraajachchhashaaMXshaH_8020360:
    def __init__(self):
        self._numconditions = 3
        
    def __call__(self,node,suffix_node):        
                
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        dhaatulist = ('vraschNN','bhrasjNN','sRijNN','mRijNN','yajNN','raajRiNN','XtubhraajRiNN')
        if isinstance(node._data,Dhaatu) and suffix_node.get_output() and \
            (''.join(node._data._data) in dhaatulist or node._data._data[-1] in ('sh','chh',)) :
            if (suffix_node.get_output()[0] in pratyaahaara('jh','l')) or \
                (isinstance(suffix_node._data,Suffix) and \
                 ''.join(suffix_node._data._suffix) in (tiNg_pratyayaaH()+sup_pratyayaaH())): 
                    return node.get_output()[0:-1]+['Xsh']
        
        return node.get_output()



class iXtaiiXti_8020280:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,anga_node ,node):        
        
        
        
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(node._data,Suffix):
            raise ValueError("node._data must be of type Suffix")
    
    
        if not node.get_output():
            return node.get_output()
        
        ## return [] if the node is sNNch, node._children[0]._output is iiXt and node._parent1._children[-1]._suffix is iXt
        ## 0, -1 in indices are important since the rule relies on original names (not later states of output)

        if isinstance(node._data,Suffix)   and ''.join(node._data._suffix )== 'sNNch':
            if node._children and isinstance(node._children[0]._data,Suffix) and node._children[0]._data._suffix==['ii','Xt']:
                if node._parent1 and node._parent1._children and isinstance(node._parent1._children[-1]._data,Suffix) and node._parent1._children[-1]._data._suffix==['i','Xt']:
                    return []
            
        return node.get_output()


class sasajuXshoruH_8020660:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node):
        
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
    
        pada = node.get_output()
        return pada
        if pada[-1]=="s":
            return pada[0:-1] + ["r"]
    
        if pada == "sajuXsh":
            raise ValueError("sajuXsh not supported yet")
        return pada





class aadeshapratyayoH_8030059:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,anga_node ,node):        
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")     
        
        # the 's' to be replaced in the node needs to be aadesha e.g. from sutras 3010460,7020350        
        # the test for aadesha only checks if both parents are there (which happens for all inserted nodes)
        #isaadesha = node._parent1 and node._parent2 
        permittedSuffixes = kRit_pratyayaaH()
        if node.get_output() and node.get_output()[0] == 's' and (node._inserted or ''.join(node._data._suffix) in permittedSuffixes):
            if anga_node.get_output()[-1] in ('i','ii','u','uu','Ri','Rii','lRi','lRii','e','o','ai','au','h','y','v','r','l') :
                return ['Xsh'] + node.get_output()[1:]
            
        #vriddhi may also be needed 7020021
            
                
                
        return node.get_output()


class raXshaabhyaaMnoXnaHsamaanapadeaXtkupvaaNgnumvyavaayeapi_8040010:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,anga_node ,node):        
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if node.get_output() and 8040010 not in list_past_rules_applied(node): 
            if node.get_output()[0] == 'n':
                effective_anga_node = anga_node if anga_node.get_output() else find_eldest_parent1_of_condition(anga_node, lambda x : x.get_output() )
                if effective_anga_node.get_output()[-1] in ( pratyaahaara('a','Xt') + ('aa','r','Xsh') ) :
                    return ['Xn'] + node.get_output()[1:]
            
        return node.get_output()

class XshtunaaXshtuH_8040400:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,anga_node ,node):        
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        mapXshXtunaa = {'s':'Xsh',
                        't':'Xt',
                        'th':'Xth',
                        'd':'Xd',
                        'dh':'Xdh',
                        'n':'Nn'}
        
        if isinstance(node._data,Suffix):    
            if node.get_output() and anga_node.get_output() and 8040400 not in list_past_rules_applied(node):
                if anga_node.get_output()[-1] in ( 'Xsh','Xt'):
                    return [mapXshXtunaa.get(node.get_output()[0],node.get_output()[0])]+ node.get_output()[1:]
        return node.get_output()

        