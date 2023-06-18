import re
from ..common_definitions import pratyaahaara, ach, hal, Node, Suffix

class kharavasaanayorvisarjaniiyaH_8010150:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node):
        # must be used in avasaana
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        pada = node.get_output()
        return pada
        khar = pratyaahaara('kh','r')
        if pada[-1]=="r" and (pada[-2] in khar or pada[-2] in ach()):
            return pada[0:-1] + ['H']
        return pada


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
    

class iXtaiiXti_8020280:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,anga_node ,node):        
        
        #raise ValueError("Unimplemented")
        
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(anga_node,Node):
            raise ValueError("suffix_node must of type Node")
        #if not isinstance(suffix_node._data,Suffix):
        #    raise ValueError("suffix_node._data must be of type Suffix")
    
    
        if not node.get_output():
            return node.get_output()
        #raise ValueError("Check should be node.get_output() =='s'") 
        if isinstance(node._data,Suffix)   and ''.join(node._data._suffix )== 'sNNch':
            print("FOUND")
        
        # if current 's' gave birth to iiXt and iXt then omit/lopa s
        #node._children[1]._data == ['ii', 'Xt']
        #node._children[0]._data == ['i', 'Xt']
        
            
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
        isaadesha = node._parent1 and node._parent2 
        if node.get_output() and node.get_output()[0] == 's' and isaadesha :
            if anga_node.get_output()[-1] in ('i','ii','u','uu','Ri','Rii','lRi','lRii') :
                return ['Xsh'] + node.get_output()[1:]
            
        #vriddhi may also be needed 7020021
            
                
                
        return node.get_output()
        