from ..common_definitions import vriddhi,upadhaa, ach, Suffix, Node , hal
from ..common_definitions import get_dhaatu_properties,pratyaahaara, guNna, Dhaatu
from ..common_definitions import parasmaidpada_pratyayaaH, sup_pratyayaaH,list_past_rules_applied 
from ..common_definitions import find_eldest_parent2_of_condition

class yuvoranaakau_7010010:
    def __init__(self):
        self._types={'anga_node':[],'node':[Suffix,'literal']}
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        suffix_string= node.get_output()
        if suffix_string is None:
            print("NONE")
        if len(suffix_string)>=2:
            if suffix_string[-2:] == ["y","u"]:
                return suffix_string[0:-2] + ["a","n","a"]
            if suffix_string[-2:] == ["v","u"]:
                return suffix_string[0:-2] + ["a","k","a"]
    
        return suffix_string


class XtaaNgasiNgasaaminaatsyaaH_7010120:
    def __init__(self):
        self._types={'anga_node':[],'node':[Suffix,'literal']}
    def __call__(self,node, anga_node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
            
        sutra_mapping = {6:['i','n','a'],12:['aa','t'],15:['s','y','a']}
        taaNgasiNgas = dict((x,sutra_mapping [i]) for i,x in enumerate(sup_pratyayaaH()) if i in (6,12,15))
        suffix_string= node.get_output()
        suffix_data = ''.join(node._data._suffix)
        if suffix_data in taaNgasiNgas and 7010120 not in list_past_rules_applied(node):
            return taaNgasiNgas[suffix_data]

    
        return suffix_string

class NgeryaH_7010130:
    def __init__(self):
        self._types={'anga_node':[],'node':[Suffix,'literal']}
        
    def __call__(self,node, anga_node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
            

        suffix_string= ''.join(node.get_output())
        #suffix_data = ''.join(node._data._suffix)
        if anga_node.get_output():
            if anga_node.get_output()[-1] in ('a','aa',) and 7010130 not in list_past_rules_applied(node):
                if suffix_string == "Nge" :
                    return ['y','a']
    
        return node.get_output()



class jhoantaH_7010030:
    def __init__(self):
        self._types={'node':[Suffix,'literal']}
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        num_adeshas=len([x for x in node._output if 'new' in x])
        if node._data._suffix[0] == 'jh' and 7010030 not in list_past_rules_applied(node) and num_adeshas<2:
            ## doesn't matter what has happened before (chuXtuu etc.), jh and 
            # ant would be introduced here            
            # the only exception is that there is no adesha after jh
            return ['a','n','t'] +node._data._suffix[1:]
        return node.get_output()


class aayaneyiiniiyiyaH_phaXdhakhachchhaghaaM_pratyayaadiinaaM_7010020:
    def __init__(self):
        self._types={'anga_node':[],'node':[Suffix ,'literal']}
        
    def __call__(self,anga_node ,node):        
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
        pratyaya=node.get_output()
        letter = [0]
        if letter== "ph":
            return ["aa","y","a","n"] + pratyaya[1:]
        elif letter == "Xdh":
            return ["e","y"]+ pratyaya[1:]
        elif letter == "kh":
            return ["ii","n"]+ pratyaya[1:]
        elif letter == "chh":
            return  ["ii","y"]+ pratyaya[1:]
        elif letter == "gh":
            return ["i","y"]+ pratyaya[1:]
        else:
            return pratyaya


class sichivRiddhiHparasmaipadeXshu_7020021:
    def __init__(self):
        self._types={'presuffix_node':['literal'],'suffix_node':[Suffix,'literal']}
        
    def __call__(self,node,suffix_node):
        
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
            
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        anga_string= node.get_output()
        if not anga_string : 
            return anga_string 
        if anga_string[-1] in ach() and ''.join(suffix_node._data._suffix)=='sNNch': 
            found_parasmaipadaH = find_eldest_parent2_of_condition(suffix_node,lambda x : isinstance(x.get_parent2()._data,Suffix) \
                                             and ''.join(x.get_parent2()._data._suffix) in parasmaidpada_pratyayaaH() )
            if found_parasmaipadaH:
                return anga_string[0:-1] + [vriddhi(anga_string[-1])]
        return node.get_output() 
    
       
class aardhadhaatukasyeXdvalaadeH_7020350:
    def __init__(self):
        self._types={'dhaatu_node':[Dhaatu,'literal'],'suffix_node':[Suffix,'literal']}
        self._ruletype = ['insertion']
        
    def __call__(self,dhaatu_node,suffix_node):
        """
        insertion rule
        """
        if not isinstance(dhaatu_node,Node):
            raise ValueError("dhaatu_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        
        if isinstance(dhaatu_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) :
                #dhaatu_node_data=[x['output'] for x in dhaatu_node._output if 'new' in x and x['new']][-1]
                suffix_node_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]       
                suffix_node_output=suffix_node.get_output()
                if suffix_node._data._lakaara == 'liXt' or not suffix_node._data.is_saarvadhaatuka() :
                    is_like_aardhadhaatuka=True
                else:
                    is_like_aardhadhaatuka=False
                    
                if not iXt_not_allowed(suffix_node_data) and is_like_aardhadhaatuka\
                    and not get_dhaatu_properties(''.join(dhaatu_node._data._data))['aniXt'] \
                    and suffix_node_output[0] in pratyaahaara('v','l')  and ''.join(suffix_node_data) != 'iXt':
                    return Suffix("iXt")
    
        return []



class ataupadhaayaaH_7021160:
    def __init__(self):
        self._types={'node':[],'suffix_node':[Suffix,'literal','stateupdate']}
        
    def __call__(self,node,suffix_node):   
            
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
            
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        
        it_chars = (suffix_data[0],suffix_data[-1])
        if 'Nc' in it_chars or 'Nn' in it_chars:
            #Ncit or Nnit
            anga_string = node.get_output()
            #print("ataupadhaayaaH_7021160="+str(anga_string))
            if len(anga_string )>1 :    
                upadhaa_pos = upadhaa(anga_string )
                if anga_string [upadhaa_pos] == 'a':
                    return anga_string [0:upadhaa_pos ]+[vriddhi(anga_string[upadhaa_pos])] + anga_string [upadhaa_pos+1:]
            
        
        return node.get_output()

class acho_NcNniti_7021150:
    def __init__(self):
        self._types={'node':[],'suffix_node':[Suffix,'stateupdate','literal']}
        
    def __call__(self,node,suffix_node):    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        anga_string= node.get_output()
        if anga_string and suffix_data:
            if anga_string[-1] in ach() and (suffix_data[-1] in ('Nc','Nn') or suffix_data[0] in ('Nc','Nn')):
                return anga_string[0:-1] + [vriddhi(anga_string[-1])]
        return node.get_output() 

class chajoHkughiNnNnyatoH_7030520:
    def __init__(self):
        self._types={'node':[],'suffix_node':['stateupdate',Suffix,'literal']}
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        chakaar_to_ku = lambda y : 'k' if y=='ch' else y
        jakaar_to_ku = lambda y : 'g' if y=='j' else y
        if suffix_data[0] in ('gh',) or suffix_data[-1] in ('gh',) or ''.join(suffix_data) == "Nnyat":
            #return ''.join(jakaar_to_ku(chakaar_to_ku(j)) for j in x)
            # print ("chajoHkughiNnNnyatoH_7030520= %s"%[jakaar_to_ku(chakaar_to_ku(j)) for j in node.get_output()])
            return [jakaar_to_ku(chakaar_to_ku(j)) for j in node.get_output()]
        
        return node.get_output()

class saarvadhaatukaardhadhaatukayoH_7030840:
    def __init__(self):
        self._types={'node':[Suffix,'literal'],'suffix_node':[Suffix]}
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")    
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        if isinstance(node._data,Suffix):
    
            if not node.get_output():
                print("saarvadhaatukaardhadhaatukayoH_7030840: Returned due to sarvaahaari lopa")
                return node.get_output()
            if node._data._suffix[-1] == node.get_output()[-1]:
                anga_string= node.get_output()
                if node._data._suffix[-1] in pratyaahaara('i','k'):
                    return anga_string[0:-1]+[guNna(anga_string[-1])]
        else:
            if node._data._data[-1] == node.get_output()[-1]:
                anga_string= node.get_output()
                if node._data._data[-1] in pratyaahaara('i','k'):
                    return anga_string[0:-1]+[guNna(anga_string[-1])]
        
        return node.get_output()
    

class supicha_7031020:
    def __init__(self):
        self._types={'node':[Suffix,'literal'],'suffix_node':[Suffix]}
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")    
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if not node.get_output():
                print("supicha_7031020: Returned due to sarvaahaari lopa")
                return node.get_output()            
        
        suffix_data = suffix_node.get_output()
        suffix_string = ''.join(suffix_node._data._suffix)
        if suffix_data and node.get_output()[-1] =='a' and list_past_rules_applied (node)[-1]!=7031020: # a-ending
            #yaNc sup
            if suffix_data[0]  in pratyaahaara('y','Nc') and suffix_string  in sup_pratyayaaH():
                if suffix_string  == 'am':
                    # amipuurvaH
                    return node.get_output()
                else:
                    return node.get_output()[0:-1] + ['aa']
        return node.get_output()

   
def iXt_not_allowed(suffix_node_data):
    # TODO : Remove hack
    return ''.join(suffix_node_data) in ('ghaNc','Nnvul')


    
    
class atodiirghoyaNci_7031010:
    def __init__(self):
        self._types={'node':['literal'],'suffix_node':[Suffix,'literal']}
        
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
            
        if not node.get_output():
            print("Returning due to sarvaahaari lopa")
            return node.get_output()
        if node.get_output()[-1] == 'a':
            if suffix_node._data.is_saarvadhaatuka() and suffix_node._data._suffix[0] in pratyaahaara('y','Nc') :
                return node.get_output()[0:-1]+['aa']
        return node.get_output()
    
    
    
class astisichoapRikte_7030960:
    def __init__(self):
        self._types={'dhaatu_node':[Dhaatu],'suffix_node':[Suffix,'literal','lakaara']}
    def __call__(self,dhaatu_node,suffix_node):
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
        suffix_data = suffix_node._data
        numachs = len([x for x in suffix_data._suffix if x in ach()])
        # ekaala saarvadhaatuaka
        if suffix_data.is_saarvadhaatuka() and suffix_data._suffix[0] in hal() and numachs ==1:
            if ''.join(suffix_data ._suffix) != 'iiXt':
                if (isinstance(dhaatu_node._data,Dhaatu) and ''.join(dhaatu_node._data._data)=='asNN') :
                    return Suffix("iiXt")
        return []

class astisichoapRikte_7030961:
    def __init__(self):
        self._types={'presuffix_node':[Suffix,'literal','lakaara'],'suffix_node':[Suffix,'literal','lakaara']}
        
    def __call__(self,presuffix_node,suffix_node):
        if not isinstance(presuffix_node._data, Suffix):
            raise ValueError("Must be suffix")
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
        presuffix_data= presuffix_node._data
        suffix_data= suffix_node._data
        
        numachs = len([x for x in suffix_data._suffix if x in ach()])
        # ekaala saarvadhaatuaka
        if suffix_data.is_saarvadhaatuka() and suffix_data._suffix[0] in hal() and numachs ==1:
            if ''.join(suffix_data._suffix) != 'iiXt':
                if ''.join(presuffix_node._data._suffix)=='sNNch' :
                    return Suffix("iiXt")
                
                    
        return []
