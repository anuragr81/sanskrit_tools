from ..common_definitions import anunaasika, Suffix, ach, hal, chu, Xtu, Node
from ..common_definitions import Dhaatu,tiNg_pratyayaaH,sup_pratyayaaH,all_pratyayas,taddhita_pratyayaaH
from ..common_definitions import list_past_rules_applied

class uraNnraparaH_1010500:
    def __init__(self):
        self._numconditions=1
    def __call__(self,a,b):
        if a[-1] == "Ri" :
            if b[0] == "a":
                return a[0:-1] + ["aa","r"]+ b
            if b[0] == "aa":
                return a[0:-1] + ["aa","r"]+ b
        return a + b
    

    
class halantyam_1030030:
    def __init__(self):
        self._numconditions=1
        # TODO: Include na vibhaktau tusmaaH condition in the condition structure
        self._condition = {'self':{'index':{-1:{'domain':hal()}}}
                           }
    def __call__(self,node):
        #Check isinstance(node._data,Dhaatu) if necessary
        if not node.get_output():
            return node.get_output()
        antyam = node.get_output()[-1]
        #works only once - not after the output has been modified with the call
        if isinstance(node._data,Suffix):
            #navibhaktautusmaaH_1030040
            
            if antyam in ('t','s','m'):
                if ''.join(node._data._suffix) in tiNg_pratyayaaH() or ''.join(node._data._suffix) in sup_pratyayaaH():
                    return node.get_output()
                # output of syataasilRiluXtoH also treated as vibhakti
                if list_past_rules_applied(node) and list_past_rules_applied(node)[0]==3010330:
                    return node.get_output()        
               
        node_data=[x['output'] for x in node._output if 'new' in x and x['new']][-1]
        if antyam in hal() and node_data[-1] == antyam :
                return node.get_output()[:-1]
        else:
            return node.get_output()

    

    
class aadirNciXtuXdavaH_1030050:
    def __init__(self):
        self._numconditions=1
        #TODO : cleanup the weaker (non-equivalent to actual treatment) condition issue
        self._condition = {
            'self':{'ORVEC': [ {'ANDVEC':[{'index':{0:{'domain':['Nc']}}},{'index':{1:{'domain':['i']} }}] },
                              {'ANDVEC':[{'index':{0:{'domain':['Xt']}}},{'index':{1:{'domain':['u']} }}] },
                             { 'ANDVEC':[{'index':{0:{'domain':['Xd']}}},{'index':{1:{'domain':['u']} }}] },
                              ]
                             }
            }
                    
                                        
            
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be Node")
        if not isinstance(node._data,Suffix):
            raise ValueError("Must be Suffix")
        if node.get_output()[0:2] in  (["Nc","i"],["Xt","u"],["Xd","u"]):
            return node.get_output()[2:]
        else:
            return node.get_output()

    
class chuXtuu_103070:
    def __init__(self):
        self._numconditions=1
        self._condition = {'self':{'index':{0:{'domain':chu()+Xtu()}}
                                   }
                           }
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be Node")
        suffix=node._data
        if not isinstance(suffix,Suffix):
            raise ValueError("Must be Suffix")
        # Need not apply chuXtuu on an empty string
        if not node.get_output():
            return node.get_output()
        #antyam = node.get_output()[-1]                

        #navibhaktautusmaaH_1030040
        #if antyam in ('t','s','m'):
        #    if ''.join(node._data._suffix) in tiNg_pratyayaaH() or ''.join(node._data._suffix) in sup_pratyayaaH():
        #        return node.get_output()
            
        # output of syataasilRiluXtoH also treated as vibhakti and thus the skipping is interpreted as
        # navibhaktautusmaaH_1030040
        if list_past_rules_applied(node) and list_past_rules_applied(node)[0]==3010330:
            return node.get_output()

        if not node.get_output():
            return node.get_output()
        
        if node._output[-1]['output'] [0] in  chu() or node._output[-1]['output'][0] in Xtu():
            return node.get_output()[1:]
        
        return node.get_output()



    
class lashakvataddhite_1030080:
    def __init__(self):
        self._numconditions=1
        
        self._condition = {'self':{'index':{0:{'domain':["l","sh","k","kh","g","gh","NN"]}}
                                   },
                           'data':list(set(all_pratyayas())-set(taddhita_pratyayaaH()))
                           }
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be of Node type")
        suffix = node._data
        if not isinstance(suffix,Suffix):
            raise ValueError("Must be of Suffix type")
        if not node.get_output():
            return node.get_output()
        if not suffix.is_taddhita and node.get_output()[0] in ("l","sh","k","kh","g","gh","Ng","NN"):
            return node.get_output()[1:]
    
        return node.get_output()

    
class upadesheajanunaasikait_1030020:
    def __init__(self):
        self._numconditions=1
        self._condition= {'self':{'index':{-1:{'domain':anunaasika}}}}
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("Must be of Node type")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("Must be of Suffix type")
        
        
        if node.get_output() and node.get_output()[-1] in anunaasika()  :
            #navibhaktautusmaaH_1030040
            if node.get_output() [-1] in ('t','s','m'):
                if ''.join(node._data._suffix) in tiNg_pratyayaaH() or ''.join(node._data._suffix) in sup_pratyayaaH():
                    return node.get_output() 
            return node.get_output() [0:-1] 
             
        
        return node.get_output() 

    

    
    
