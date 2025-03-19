from ..common_definitions import vriddhi,upadhaa, ach, Suffix, Aagama, Node 
from ..common_definitions import hal, Praatipadika
from ..common_definitions import get_dhaatu_properties,pratyaahaara, guNna, Dhaatu
from ..common_definitions import parasmaidpada_pratyayaaH, sup_pratyayaaH,list_past_rules_applied , general_special_pairs
from ..common_definitions import find_eldest_parent1_of_condition,find_eldest_parent2_of_condition,find_recentmost_child_of_condition
from ..common_definitions import parse_string, sarvanaama_praatipadikaaH




class yuvoranaakau_7010010:
    def __init__(self):
        # zero conditions are important
        self._numconditions = 0
        
        
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        suffix_string= node.get_output()

        if len(suffix_string)>=2:
            if suffix_string[-2:] == ["y","u"]:
                return suffix_string[0:-2] + ["a","n","a"]
            if suffix_string[-2:] == ["v","u"]:
                return suffix_string[0:-2] + ["a","k","a"]
    
        return suffix_string

class atobhisaais_7010090:
    def __init__(self):
        self._numconditions = 1
        self._condition = {'self':{'data':{'domain':['bhis']}}}
                           
    def __call__(self,anga_node, node):
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if not node.get_output() : 
            return node.get_output()
        elif node._data._suffix==['bh','i','s']:
            if not anga_node.get_output():
                effective_anga_node = find_eldest_parent1_of_condition(anga_node,lambda x: x.get_output() )
            else:
                effective_anga_node = anga_node
            if 7010090 not in list_past_rules_applied(node) and effective_anga_node.get_output()[-1] in ('a','aa',) :
                return ['ai','s']
            
        return node.get_output()


class XtaaNgasiNgasaaminaatsyaaH_7010120:
    def __init__(self):
        self._numconditions = 1
                   
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
        self._numconditions = 1
        self._condition = {'self':{'data':{'domain':['Nge']}}
                   }
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
        self._numconditions = 0
                   
    def __call__(self,node):
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("node must encapsulate Suffix")
        num_adeshas=len([x for x in node._output if 'new' in x])
        if node._data._suffix[0] == 'jh' and 7010030 not in list_past_rules_applied(node) and num_adeshas<2:
            ## doesn't matter what has happened before (chuXtuu etc.), jh and 
            # ant would be introduced here            
            # the only exception is that there is no adesha after jh
            return ['a','n','t'] +node._data._suffix[1:]
        return node.get_output()


class aayaneyiiniiyiyaHphaXdhakhachchhaghaaMpratyayaadiinaaM_7010020:

    def __init__(self):
        self._numconditions = 1

    def __call__(self,anga_node ,node):        
        if not isinstance(node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
        pratyaya=node.get_output()
        if not pratyaya:
            return pratyaya
        letter = pratyaya[0]
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




class jasaHshii_7010170:

    def __init__(self):
        self._numconditions = 1
                   
    def __call__(self,anga_node,node):
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
           
        if node.get_output() and isinstance(node._data,Suffix) and ''.join(node._data._suffix) == 'jas':
            if 7010170 not in list_past_rules_applied(node) and ''.join(anga_node._data._data) in sarvanaama_praatipadikaaH():
                if anga_node.get_output()[-1] in ('a','aa'):
                    return {'output':['sh','ii'],'mutate':True}

        return node.get_output()


class hrasvanadyaaponuXt_7010540:

    def __init__(self):
        self._numconditions = 1
                   
    def __call__(self,prefix_node,suffix_node):
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
        if not isinstance(prefix_node,Node):
            raise ValueError("prefix_node must of type Node")
           
        if suffix_node.get_output():
            if 7010540 not in list_past_rules_applied(suffix_node) and isinstance(suffix_node._data,Suffix) and suffix_node._data._suffix==['aa','m']:
                # find effective prefix_node if prefix_node is empty
                effective_prefix_node = prefix_node if prefix_node.get_output() else find_eldest_parent1_of_condition(prefix_node,lambda x : x.get_output() is not None)
                if effective_prefix_node.get_output()[-1] in ('a','i','ii','u','uu','Ri',):
                    return Aagama('nNNXt')
                

        return []


class ugidachaaMsarvanaamasthaaneadhaatoH_7010700:
    def __init__(self):
        self._numconditions = 1
                   
    def __call__(self,node,suffix_node):
        """
        insertion rule for num when suffix is sarvanaamasthaana and prefix-node is u-ending 
        since this is an insertion rule, it is not to be applied twice
        """
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
        
        # adhaatoH or aNcchu dhaatu
        if 7010700 in list_past_rules_applied(node):
            return node.get_output()
        
        if (not isinstance(node._data,Dhaatu) or \
            (isinstance(node._data,Dhaatu) and ''.join(node._data._data)=='aNchNN')) \
            and node.get_output() :            
                if isinstance(suffix_node._data,Suffix) \
                    and ''.join(suffix_node._data._suffix) in ('sNN', 'au','jas','am','auXt'):# sarvanaamasthaana
                    ugit = False
                    if node.get_output()[-1] == 'u' or node.get_output()[0] == 'u':
                        # find last hal
                        halPositions = [i for i,x in enumerate(node.get_output()) if x in hal()]
                        if  halPositions :
                            # skipping last 'u'
                            return node.get_output()[0:halPositions [-1]]+['n']+node.get_output()[halPositions [-1]:-1]
                        else :
                            return ['n'] + node.get_output()[0:-1]
                    # suffix where u is not explicit but is an anunaasika/NN (which would be deleted) is 
                    # handled separately where the end is not 'u' and therefore does not need to be skipped 
                    
                    ugitaSuffixes = ('matNNp',)
                    if isinstance(node._data,Suffix) and ''.join(node._data._suffix) in ugitaSuffixes:
                        halPositions = [i for i,x in enumerate(node.get_output()) if x in hal()]
                        if  halPositions :
                            return node.get_output()[0:halPositions [-1]]+['n']+node.get_output()[halPositions [-1]:]
                        else :
                            return ['n'] + node.get_output()
        return node.get_output()
    



    
class RidushanaspurudansoanehasaaNccha_7010940:
    def __init__(self):
        self._numconditions = 1
                   
    def __call__(self,node,suffix_node):
        
        """ 
        invoked when node is either a praatipadika or a suffix and suffix_node 
        is a suNN. Since anaNg aadesha is Ngit, it's applied at the end (due 
        to rule: 1.1.52 Ngichcha)
        """

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
            
        if node.get_output() and isinstance(suffix_node._data,Suffix) and ''.join(suffix_node._data._suffix)=='sNN':
            if isinstance(node._data,Praatipadika) or isinstance(node._data,Suffix): 
                if node.get_output()[-1]=='Ri' or \
                    (''.join(node.get_output()) in \
                     ('purudaMsas','purudansas','purudaMshas',\
                      'purudanshas','ushanas','anehas') ):
                        return node.get_output()[0:-1]+parse_string('an')
        
        return node.get_output()

 
class sichivRiddhiHparasmaipadeXshu_7020021:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,node,suffix_node):
        
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
            
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        # return without doing anything if node is empty
        if not node.get_output(): 
            return node.get_output()
        
        # the sutra acts only on dhaatu itself otherwise we would have aluuNcait (not alaaviit)
        
        # no need for find_eldest_parent1_of_condition(node,lambda x: isinstance(x._data,Dhaatu))
        
        if isinstance(node._data,Dhaatu) :
            achIndices = [i for i,x in enumerate(node.get_output()) if x in ach()]
            if achIndices:
                foundSich = find_recentmost_child_of_condition(node,lambda x : isinstance(x._data,Suffix) and ''.join(x._data._suffix)=='sNNch')
                if foundSich:                    
                    foundParasmaipadaH = find_eldest_parent2_of_condition(suffix_node,lambda x : isinstance(x.get_parent2()._data,Suffix) \
                                                     and ''.join(x.get_parent2()._data._suffix) in parasmaidpada_pratyayaaH() )
                    if foundParasmaipadaH :
                        # find if sNNch has been applied before in any of the dhaatu progeny (children , children of children etc.)
                        past_sich= find_recentmost_child_of_condition(node,lambda x: 7020021 in list_past_rules_applied(x)) is not None
                        if not past_sich :
                            return node.get_output()[0:achIndices[-1]] + [vriddhi(node.get_output()[achIndices[-1]])] +node.get_output()[achIndices[-1]+1:] 
                
        
        return node.get_output() 
    
       
class aardhadhaatukasyeXdvalaadeH_7020350:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,prefix_node,suffix_node):
        """
        insertion rule
        """
        if not isinstance(prefix_node,Node):
            raise ValueError("prefix_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        
        if isinstance(prefix_node._data,Dhaatu) and \
            isinstance(suffix_node._data,Suffix) :
                suffix_node_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]       
                suffix_node_output=suffix_node.get_output()
                if suffix_node._data._lakaara == 'liXt' or not suffix_node._data.is_saarvadhaatuka() :
                    is_like_aardhadhaatuka=True
                else:
                    is_like_aardhadhaatuka=False
                    
                if not iXt_not_allowed(suffix_node_data) and is_like_aardhadhaatuka\
                    and get_dhaatu_properties(''.join(prefix_node._data._data))['aniXt'] == "false"  \
                    and suffix_node_output and suffix_node_output[0] in pratyaahaara('v','l')  and ''.join(suffix_node_data) != 'iXt':
                    return Suffix("iXt")
    
        return []




class liNgaHsalopoanantyasya_7020790:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,node,suffix_node):   
            
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
        
        if not suffix_node.get_output():
            # not applied to antya nodes
            return node.get_output()
        
        nodeliNgRelated= find_eldest_parent2_of_condition(node,lambda x : isinstance(x._data,Suffix) and x._data._lakaara in('liNg1','liNg2') )
        if nodeliNgRelated:
            # omit s
            output_data = [x for x in node.get_output() if x !='s']
            if output_data  != node.get_output() : # only for debugging purposes
                return output_data  
        
        return node.get_output()
    

class atoyeyaH_7020800:
    def __init__(self):
        self._numconditions = 2
       
        
    def __call__(self,anga_node,node):   
            
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must of type Node")
            
        nodeliNgRelated= find_eldest_parent2_of_condition(node,lambda x : isinstance(x._data,Suffix) and x._data._lakaara in('liNg1','liNg2') )
        
        if nodeliNgRelated and anga_node.get_output() and anga_node.get_output()[-1] in ('a','aa'):
            node_output = node.get_output()
            ya_occurrences = [(j['index'],j['index']+1) for j in [ {'index':i-1,'data':(node_output [i-1],node_output [i])} for  i in range(1,len(node_output ))] if j['data'] == ('y','aa')]  
            if ya_occurrences:
                for ya_tuple in ya_occurrences:
                    node_output[ya_tuple[0]] = 'i'
                    node_output[ya_tuple[1]] = 'y'
            return node_output

        return node.get_output()

class tyadaadiinaamaH_7021020:
    
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        tyadaadimap = {'tyad':'tya',
         'idam':['i','d','a'],
         'etad':['e','t','a'],
         'yad':['y','a'],
         'tad':['t','a'],
         'tyat':['t','y','a'],
         'etat':['e','t','a'],
         'yat':['y','a'],
         'tat':['t','a'],
         }
        
        halilopamap ={'idam':['a']}
        if node.get_output() and 7021020 not in list_past_rules_applied(node) :
            if isinstance(node._data,Praatipadika) and ''.join(node._data._data) in tyadaadimap :
                if ''.join(suffix_node._data._suffix) in sup_pratyayaaH():
                    if suffix_node._data._suffix[0] in hal() and ''.join(node._data._data) in halilopamap :
                        return halilopamap [''.join(node._data._data)]
                    else:
                        return tyadaadimap[''.join(node._data._data)]
        return node.get_output()


class mRijervRiddhiH_7021140:
    
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,node,suffix_node):
        
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        # applies to all suffixes
        if isinstance(suffix_node._data,Suffix)  and \
        isinstance(node._data,Dhaatu) and ''.join(node.get_output()) == 'mRij' :
            return ['m','aa','r','j']
        return node.get_output()
            
class acho_NcNniti_7021150:
    def __init__(self):
        
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        """
        also implements diidhiiveviiXtaam
        """
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        # if a more specific rule pertaining to 7021150 has been applied, then do not apply 7021150
        
        if set(y for (x,y) in general_special_pairs() if x == 7021150).intersection(list_past_rules_applied(node)):
            return node.get_output()
        
        # diidhiiveviiXtaam
        if isinstance(node._data,Dhaatu) and ''.join(node._data._data) in ('diidhiiNN','veviiNN',):
            return node.get_output() 
            
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        anga_string= node.get_output()
        if anga_string and suffix_data:
            if anga_string[-1] in ach() and (suffix_data[-1] in ('Nc','Nn') or suffix_data[0] in ('Nc','Nn')):
                return anga_string[0:-1] + parse_string(vriddhi(anga_string[-1]))
        return node.get_output() 


class ataupadhaayaaH_7021160:
    def __init__(self):
        self._numconditions = 1
        
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

class taddhiteXshvachamaadeH_7021170:
    def __init__(self):
        self._numconditions = 1
        
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
            if anga_string[0] in ach() and suffix_node._data.is_taddhita:
                return [vriddhi(anga_string[0])] + anga_string[1:] 
        return node.get_output() 


class chajoHkughiNnNnyatoH_7030520:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
        
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        chakaar_to_ku = lambda y : 'k' if y=='ch' else y
        jakaar_to_ku = lambda y : 'g' if y=='j' else y
        if suffix_data[0] in ('gh',) or suffix_data[-1] in ('gh',) or ''.join(suffix_data) == "Nnyat":
            return [jakaar_to_ku(chakaar_to_ku(j)) for j in node.get_output()]
        
        return node.get_output()

class otaHshyani_7030710:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
        
        if node.get_output() and isinstance(suffix_node._data,Suffix) and ''.join(suffix_node._data._suffix) == 'shyan':
            if node.get_output()[-1] == 'o' and 7030710 not in list_past_rules_applied(node):
                return node.get_output()[0:-1]
           
        return node.get_output()


class paaghraadhmaasthaamnaadaaNndRishyartisarttishadasadaaMpibajighradhamatitXshXthamanayachchhapashyarchchhadhaushiiyasiidaaH_7030780:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")
            
        if isinstance(node._data,Dhaatu) and isinstance(suffix_node._data,Suffix) :
            if node.get_output() and 7030780 not in list_past_rules_applied(node):
                dhaatumap = {'paaNN':['p','i','b','a'],
                 'ghraaNN':['j','i','gh','r','a'],
                 'dhmaaNN':['dh','a','m','a'],
                 'XshXthaaNN':['t','i','Xsh','Xth','a'],
                 'mnaaNN':['m','a','n','a'],
                 'daaNN':['y','a','ch','chh','a'],
                 'dRishNN':['p','a','sh','y','a'],
                 'RiNN':['R','i','ch','chh','a'],
                 'sRiNN':['dh','au'],
                 'shadlRiNN':['sh','ii','y','a'],
                 'XshadlRiNN':['s','ii','d','a'],
                 }
                if ''.join(node._data._data) in dhaatumap :
                    return dhaatumap[''.join(node._data._data)]
            
           
        
        return node.get_output()


class miderguNaH_7030820:
    def __init__(self):
        self._numconditions = 1
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")    
        if isinstance(suffix_node._data,Suffix) and isinstance(node._data,Dhaatu) :
            if ''.join(node.get_output())=='mid':
                return ['m','e','d']
        return node.get_output()


class saarvadhaatukaardhadhaatukayoH_7030840:
    # also implements kNgiticha and n dhaatulopa aardhadhaatuke
    
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")    
        if not isinstance(suffix_node._data,Suffix):
            return node.get_output()
        
        if suffix_node._data._suffix[0] in ('k','Ng','g') or suffix_node._data._suffix[-1] in ('k','Ng','g'):
            return node.get_output()
        
        suffixConsumerSutras = (2040740,)
        
        
        if isinstance(node._data,Suffix) :
    
            if not node.get_output():
                return node.get_output()
            if node._data._suffix[-1] == node.get_output()[-1]:
                if node._data._suffix[-1] in pratyaahaara('i','k'):
                    if not set(list_past_rules_applied(node)).intersection(suffixConsumerSutras):
                        # saarvadhaatuka and apit would not have guNa (1.2.4 saarvadhaatukamapit makes them Ngitvat)
                        if not (suffix_node._data.is_saarvadhaatuka() and (suffix_node._data._suffix[0] != 'p' and suffix_node._data._suffix[-1] != 'p')):
                            return node.get_output()[0:-1]+[guNna(node.get_output()[-1])]
        elif isinstance(node._data,Praatipadika) or isinstance(node._data,Dhaatu):
            if node._data._data and node.get_output() :
                if node.get_output()[-1] in pratyaahaara('i','k'):
                    if not set(list_past_rules_applied(node)).intersection(suffixConsumerSutras):
                        if not (suffix_node._data.is_saarvadhaatuka() and (suffix_node._data._suffix[0] != 'p' and suffix_node._data._suffix[-1] != 'p')):
                            return node.get_output()[0:-1]+[guNna(node.get_output()[-1])]
        
        return node.get_output()
    

class supicha_7031020:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("anga_node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix must of type Node")    
        if not isinstance(suffix_node._data,Suffix):
            raise ValueError("suffix must of type Suffix")
            
        if not node.get_output():
            #print("supicha_7031020: Returned due to sarvaahaari lopa")
            return node.get_output()            
    
        suffix_data = suffix_node.get_output()
        suffix_string = ''.join(suffix_node._data._suffix)
        if suffix_data and node.get_output() and (not list_past_rules_applied (node) or list_past_rules_applied (node)[-1]!=7031020):
            if node.get_output()[-1] =='a' : # a-ending
                #yaNc sup
                # if suffix_data[0]  in pratyaahaara('y','Nc') and suffix_string  in sup_pratyayaaH():
                if suffix_string  in ('bhyaam','bhis','bhyas','Nge',):
                    return node.get_output()[0:-1] + ['aa']
        return node.get_output()

   
def iXt_not_allowed(suffix_node_data):
    # TODO : Remove hack
    return ''.join(suffix_node_data) in ('ghaNc','Nnvul')

    
    
class atodiirghoyaNci_7031010:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
            
        if not node.get_output():
            #print("Returning due to sarvaahaari lopa")
            return node.get_output()
        if node.get_output()[-1] == 'a':
            # instead of checking suffix_node._data._suffix[0] , just check the output
            if suffix_node._data.is_saarvadhaatuka() and suffix_node.get_output() and suffix_node.get_output()[0] in pratyaahaara('y','Nc') :
                return node.get_output()[0:-1]+['aa']
        return node.get_output()
    
class bahuvachanejhalyetosicha_7031030:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
    
        if not isinstance(node,Node):
            raise ValueError("node must of type Node")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must of type Node")
            
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
            
        # if there suffix has become invisible - no changes would be necessary
        
        if not suffix_node.get_output() or not node.get_output():
            return node.get_output()
        
        if suffix_node._data._suffix in (['bh','i','s'],['bh','y','a','s'],['s','u','p'], ['o','s']):
            ## 7010090 i.e. ato bhisa ais is an apavaada sutra hence it needs to be checked whether it has been
            #  applied or not
            if 7031030 not in list_past_rules_applied(node) and 7010090 not in  list_past_rules_applied(suffix_node) and node.get_output()[-1] in ('a','aa',) :
                return node.get_output()[0:-1] + ['e']
        
        return node.get_output()

    
class astisichoapRikte_7030960:
    def __init__(self):
        self._numconditions = 2
    def __call__(self,prefix_node,suffix_node):
        if not isinstance(suffix_node._data, Suffix):
            raise ValueError("Must be suffix")
        suffix_data = suffix_node._data
        numachs = len([x for x in suffix_data._suffix if x in ach()])
        # ekaala saarvadhaatuaka
        if suffix_data.is_saarvadhaatuka() and suffix_data._suffix[0] in hal() and numachs ==1:
            if ''.join(suffix_data ._suffix) != 'iiXt':
                if (isinstance(prefix_node._data,Dhaatu) and ''.join(prefix_node._data._data)=='asNN') :
                    return Suffix("iiXt")
        return []

class astisichoapRikte_7030961:
    def __init__(self):
        self._numconditions = 2
        
    def __call__(self,prefix_node,suffix_node):
        if isinstance(prefix_node._data, Suffix) and isinstance(suffix_node._data, Suffix):            
            suffix_data= suffix_node._data
            
            numachs = len([x for x in suffix_data._suffix if x in ach()])
            # ekaala saarvadhaatuaka
            if suffix_data.is_saarvadhaatuka() and suffix_data._suffix[0] in hal() and numachs ==1:
                if ''.join(suffix_data._suffix) != 'iiXt':
                    if ''.join(prefix_node._data._suffix)=='sNNch' :
                        return Suffix("iiXt")
                    
        return []


class taasastyorlopaH_7040500:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        
        if isinstance(node._data,Suffix) and ''.join(node._data._suffix)=='taas' and node.get_output()[-1]=='s' and 7040500 not in list_past_rules_applied(node):
            if suffix_node.get_output()[0]=='s' or suffix_node.get_output()[0]=='r':
                return node.get_output()[:-1] # omit the last s
        return node.get_output()

class taasastyorlopaH_7040501:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,suffix_node,node):
        if isinstance (node._data,Dhaatu):
            if ''.join(node._data._data[:-1])=='as': # as dhaatu (omitting the last letter i.e. anubandh)
                if node.get_output()[0]=='s'  and 7040501 not in list_past_rules_applied(node):
                    return node.get_output()[:-1] # omit the last s
        return node.get_output()

