
from ..common_definitions import ach, hal, sup_pratyayaaH, taddhita_pratyayaaH, kRit_pratyayaaH,san_pratyayaaH
from ..common_definitions import pratyaahaara, make_diirgha, yaNn, guna_letters_for_aat, juhotyaadi_dhaatus
from ..common_definitions import vriddhi, guNna, list_past_rules_applied, node_upadhaa
from ..common_definitions import find_eldest_parent1_of_condition, list_achpos, ghu_dhaatus
from ..common_definitions import find_eldest_parent2_of_condition, parasmaidpada_pratyayaaH
from ..common_definitions import Suffix, Aagama, Node, Dhaatu, Praatipadika
from ..common_definitions import nandyaadi_dhaatus, grahaadi_dhaatus, pachaadi_dhaatus, ach_permitted_temp_dhaatus


def hrasvaH(charlist):
    #if charlist[-1] in 
    hrasva_map = {"aa":'a',"ii":'i',"uu":'u',"Rii":'Ri','lRii':'lRi','e':'i','o':'u','ai':'i','au':'u'}
    return charlist[0:-1]+[hrasva_map.get(charlist[-1],charlist[-1])]

def abhyaasecharchcha (charlist):
    charchcha_map = {'bh':'b', 'jh':'j','gh':'g','Xdh':'Xd','dh':'d','kh':'k','ph':'p','chh':'ch','Xth':'Xt','th':'t'}
    return [charchcha_map .get(charlist[0],charlist[0])]+charlist[1:]


def bhavateraH(charlist,node):
    if node._data._data[0:2]==['bh','uu'] and charlist[-1] in ('u','uu'):
        return charlist[0:-1]+['a']
    return charlist

class liXtidhaatoranabhyaasasya_6010080:
    """
    Also implements 
    ekahalmadhya...
    thhali cha seti
    """
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if isinstance   (node._data,Dhaatu):
            
            
            if suffix_node._data._lakaara == None:
            # if lakaara is not found in the suffix but it is found in a nested parent2 then assume the parent2 (subsequent suffix) to be the effective suffix
            # relative to which the abhyaasa-kaarya can take place.
                searched_suffix_node=find_eldest_parent2_of_condition(suffix_node,lambda x: isinstance(x,Node) and isinstance(x._data,Suffix) and x._data._lakaara is not None)
                
                if searched_suffix_node == None:
                    # lakaara not found in any parent2 so return with no change (no abhyaasa)
                    return node.get_output()
                else:
                    # found lakaara so make the searched suffix_node as the effective suffix_node
                    # no need to make a deepcopy
                    effective_suffix_node=searched_suffix_node
            else:
                # suffix_node is the effective node to be searched since it has a lakaara
                # no need to make a deepcopy
                effective_suffix_node=suffix_node 
                
            
            
            if effective_suffix_node._data._lakaara == 'liXt':
                applied_rules= [int(x['rule'].__name__.split('_')[-1]) for x in node._output if 'rule' in x]
                if 6010080 not in applied_rules : # anabhyaasa
                    hals = [i for i,x in enumerate(node.get_output()) if x in hal() and i>0]
                    if hals:
                        if len(hals)==1 and hals[0] >1 and node.get_output()[hals[0]-1] in ('a',): # ekahalmadhye achaH, asaMyoga 
                            if len([x for x in node._output if 'new' in x])==1: # no adesha
                                if ('inputs' in effective_suffix_node._output[-1] and effective_suffix_node._output[-1]['inputs']['state']._data._lakaara  == 'liXt') \
                                     or ('new' in effective_suffix_node._output[-1] and effective_suffix_node._data._lakaara=='liXt') : # check on suffix
                                    last_adesha = [x for x in effective_suffix_node._output if 'new' in x][-1]
                                    if 'output' in last_adesha and last_adesha['output']==['th','a','l']:
                                        return node.get_output()[:hals[0]-1] + ['e'] + node.get_output()[hals[0]:]
                                    if not effective_suffix_node.has_sthaanii_it('p'): # apit check
                                    # apit after asaMyoga would be treated as kit (so that ekahalmadhya... may apply)
                                        last_adesha = [x for x in effective_suffix_node._output if 'new' in x][-1]
                                        if node._output[-1]['output'][-1] in ach() or node._output[-1]['output'][-2] in ach() : # a-saMyoga 
                                            return  node.get_output()[:hals[0]-1] + ['e'] + node.get_output()[hals[0]:]
                                    
                                        
                            
                        # ignore hals after second
                        # use bhavateraH, hrasvaH, abhyaasecharchcha 
                        charchh_reduced = abhyaasecharchcha  ( hrasvaH  ( node.get_output()[:hals[0]] ) )
                        dhaatu_checked = bhavateraH(charchh_reduced,node)
                        return dhaatu_checked +node.get_output()
        return node.get_output()


def urat(x):
    if not isinstance(x,list):
        raise ValueError("input must be a list")
    if x and len(x)>1 :
        if x[-1] == 'Ri':
            return x[0:-1] + ['a','r']
        if x[-1] == 'Rii':
            return x[0:-1]+ ['aa','r']
    
    return x
        
class sanyaNgoH_6010090:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        """
        yaNg or san inputs combine with the dhaatu on which dvitva is applied
        yaNg must therefore disappear - requiring a separate rule (group-sutra) to be made
        part of the san-yaNg group for simultaneous application.
        
        also implements nandigrahipachaadibhyolyuNninyachaH 3.1.134
                        riigRidupadhasyacha 7.4.90
        """
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
            
        if isinstance   (node._data,Dhaatu) and node.get_output() \
            and not set(list_past_rules_applied(node)).intersection(set((6010090,6010091))):
            if isinstance(suffix_node._data,Suffix) and ''.join(suffix_node._data._suffix) in ('san','yaNg',):
                tobeDoubled = node.get_output() + [suffix_node._data._suffix[0]]
                hals=[i for i,x in enumerate(tobeDoubled) if x in hal() and i>0]
                if hals:
                    postUratToBeDoubled = urat(tobeDoubled[:hals[0]])
                    # applying riigRidupadhasyacha
                    nodeUpadhaa = node_upadhaa(node)
                    if nodeUpadhaa  is not None and ''.join(suffix_node._data._suffix)  == 'yaNg' and nodeUpadhaa ['char'] == 'Ri':
                        postRiikUratTobeDouled = postUratToBeDoubled[0:-1] + ['r','ii']
                        # no hrasvaH applied because of Riik aadesha
                        firstPart = bhavateraH(abhyaasecharchcha  (  postRiikUratTobeDouled  ),node)
                        return firstPart+tobeDoubled
                    else:
                        firstPart = bhavateraH(abhyaasecharchcha  ( hrasvaH  ( postUratToBeDoubled ) ),node)
                        if ''.join(suffix_node._data._suffix) :
                            if firstPart[-1] in ach():
                                return firstPart[0:-1] + [guNna(firstPart[-1])] +tobeDoubled
                        return firstPart+tobeDoubled
                
            
        return node.get_output()


class sanyaNgoH_6010091:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,anga_node):
        """
        yaNg or san inputs combine with the dhaatu on which dvitva is applied
        yaNg must therefore disappear - requiring a separate rule (group-sutra) to be made
        part of the san-yaNg group for simultaneous application.
        
        also implements nandigrahipachaadibhyolyuNninyachaH 3.1.134
                        riigRidupadhasyacha 7.4.90
        
        """
        
        if not isinstance(anga_node,Node):
            raise    ValueError ("anga_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
            
        
        if isinstance (node._data,Suffix) and ''.join(node._data._suffix) in ('yaNg','san',) and not set(list_past_rules_applied(node)).intersection(set((6010091,))):
            if isinstance(anga_node._data,Dhaatu) :
                if ''.join(anga_node._data._data) in nandyaadi_dhaatus():
                    return  {'output':['l','y','u'],'mutate':True}
                if ''.join(anga_node._data._data) in grahaadi_dhaatus():
                    return {'output':['Nn','i','n','i'],'mutate':True}
                if ''.join(anga_node._data._data) in pachaadi_dhaatus() + ach_permitted_temp_dhaatus():
                    return {'output':['a','ch'],'mutate':True}
                return []
            
            return []
            
        return node.get_output()

class shlau_6010100:
    """
    shlu is never input by the user and is effectively an intermediate step that causes dvitva. 
    Since the treatment of shlu takes priority over guNna etc. (i.e. it could bar them), the numConditions is set to 0.
    Also implements the exception ghvasoreddhaavabhyaasalopashcha 6.4.119 - which prevents dvitva. Since the rule is 
    dependent on serhyapichcha, the numconditions is also set to 0 in rule serhyapichcha.
    """
    def __init__(self):
        self._numconditions = 0
        
    def __call__(self,node,suffix_node):
        """
        """
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if set(list_past_rules_applied(node)).intersection(set([6010100]) ):
            return node.get_output()
        
        if isinstance(suffix_node._data,Suffix)  and ''.join(suffix_node._data._suffix) == 'shlu' :
            if isinstance(node._data,Dhaatu):
                if ''.join(node._data._data) in ghu_dhaatus() and suffix_node._parent2 \
                    and isinstance(suffix_node._parent2._data,Suffix) \
                        and suffix_node._parent2.get_output() == ['h','i']:
                    return node.get_output()[0:-1]+['e']
                else:
                    tobeDoubled = node.get_output() 
                    hals=[i for i,x in enumerate(tobeDoubled) if x in hal() and i>0]
                    postUratToBeDoubled = urat(tobeDoubled[:hals[0]]) if hals else urat(tobeDoubled)
                    firstPart = bhavateraH(abhyaasecharchcha  ( hrasvaH  ( postUratToBeDoubled ) ),node)
                    
                    return firstPart+tobeDoubled


        return node.get_output()

    
class shlau_6010101:
    """
    6010100 handles the dvitva while the second group-constituent sutra 6010101 removes shlu output
    """
    def __init__(self):
        self._numconditions = 0
        
    def __call__(self,node,anga_node):
        """
        """
        if not isinstance(anga_node,Node):
            raise    ValueError ("anga_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if set(list_past_rules_applied(node)).intersection(set([6010101]) ):
            return node.get_output()
        
        if isinstance(node._data,Suffix)  and ''.join(node._data._suffix) == 'shlu' :
            return []

        return node.get_output()

    
class NnonaH_6010630:
    def __init__(self):
        self._numconditions = 0
        self._condition = {'self':{'index':{0 :{'domain':['Nn']} }
                                   }
                           }
    def __call__(self,node,suffix_node):    
        if not isinstance   (node,Node):
            raise    ValueError ("node must be of type Node")
        if not isinstance   (node._data,Dhaatu):
            return node.get_output()
        dhaatu_string=node.get_output()
        if dhaatu_string and dhaatu_string[0] == "Nn":
            return ['n']+dhaatu_string[1:]
        else:
            return dhaatu_string


class lopovyorvali_6010640:
    def __init__(self):
        self._numconditions = 2

    def __call__(self,node,suffix_node):    
        if not isinstance   (node,Node):
            raise    ValueError ("node must be of type Node")
        if not isinstance   (suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if node.get_output() and node.get_output()[-1] in ('y','v') :
            if suffix_node.get_output() :
                effective_suffix_node= suffix_node
            elif not suffix_node.get_output()  and suffix_node._parent2 and suffix_node._parent2.get_output():
                effective_suffix_node = suffix_node._parent2
            else:
                return node.get_output()
                
            if effective_suffix_node.get_output()[0] in pratyaahaara('v','l'):
                return node.get_output()[0:-1]
            
        return node.get_output()
        

class halNgyaabhyodiirghaatsutisyapraktaMhal_6010660:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,anga_node,node):
        
        """
        invoked when two conditions are met. 
        1. First, the suffix_node is apRikta (single-letter-remaining) with the original 
        suffix being one of sNN,  ti(p), si(p). 
        2. Second, the anga before apRikta has a { hal-ending , aa-ending , Ngi-iending } and the second-last ending is diirgha.
        """
        
        if not isinstance   (node,Node):
            raise    ValueError ("node must be of type Node")
        if not isinstance   (anga_node,Node):
            raise    ValueError ("anga_node must be of type Node")
        
        if isinstance(node._data,Suffix) and ''.join(node._data._suffix) in ('sNN'): #TODO: Revisit ti, si or 'tip','sip' when imeplementing abibharbhavaan, abhinoatra 
            if node.get_output() and len(node.get_output())==1 and len(anga_node.get_output())>1 :
                if anga_node.get_output()[-1] in hal() : # TODO: Revisit aap,Ngiip or ('aa','ii',) when imeplementing kumaarii , khatvaa, ) 
                    return []
                                                      
                
        
        return node.get_output()


class ikoyaNnachi_6010740:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node, suffix_node):
        
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
            
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if not node.get_output():
            return node.get_output()
        
        if not suffix_node.get_output() and suffix_node._children :
            
            effective_suffix_node =  suffix_node._children [-1]
        else:
            effective_suffix_node =  suffix_node
        
        if effective_suffix_node.get_output() and effective_suffix_node.get_output()[0] =='a':
            if node.get_output()[-1] in pratyaahaara('i','k'):
                return node.get_output()[0:-1] + [yaNn(node.get_output()[-1])]
        return node.get_output()

class echoayavaayaavaH_6010750:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node, suffix_node):
        if not node.get_output():
            return node.get_output()
        if not suffix_node.get_output():
            effective_suffix_node =find_eldest_parent2_of_condition(suffix_node,lambda x : isinstance(x ,Node) and isinstance(x._data,Suffix) and x.get_output() )
            if not effective_suffix_node :
                return node.get_output()
        else:
            effective_suffix_node = suffix_node
            
        if effective_suffix_node .get_output()[0] not in ach():
            return node.get_output()
    
        
        node_output=node.get_output()
        if node_output[-1] == "e":
            return node_output[0:-1]+["a" ,"y"]
        if node_output[-1] == "o":
            return node_output[0:-1]+["a","v"]
        if node_output[-1] == "ai":
            return node_output[0:-1]+["aa","y"]
        if node_output[-1] == "au":
            return node_output[0:-1]+["aa","v"]
            
        return node_output


class aadguNnaH_6010840:
    def __init__(self):
        self._numconditions = 1
        pyhik= ['i', 'ii', 'u', 'uu', 'Ri', 'Rii', 'lRi', 'lRii']
        self._condition = {'self':{'index':{0: {'domain': pyhik }}},
                           'prev1':{'index':{ 0 :['a','aa']}}
                           }
    def __call__(self,node, anga_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()                
        if anga_node.get_output():
            suffix_first_letter = node.get_output()[0]
            if anga_node.get_output()[-1] in ('a','aa') and suffix_first_letter  in pratyaahaara('i','k'):
                
                return guna_letters_for_aat(node.get_output()[0])+node.get_output()[1:]
            
            
        return node_output


class aadguNnaH_6010841:
    def __init__(self):
        self._numconditions = 1
        self._condition = {'self':{'index':{0:{'domain':['a','aa']}
                                            }
                                   }
                           }
    def __call__(self,node, suffix_node):
        
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        if isinstance(suffix_node._data,Suffix) and suffix_node.get_output():         
            # no check on suffix_node because that is expected to have changed after the call
            if node_output[-1]  in ('a','aa') and list_past_rules_applied(suffix_node) and list_past_rules_applied(suffix_node)[-1]==6010840:
                return node_output[:-1] #skip because the other instance of the rule uses the diirgha
        return node_output


class vRiddhirechi_6010850:
    def __init__(self):
        self._numconditions = 1
        ech = ('e', 'o', 'ai', 'au')
        self._condition = {'prev1':{'index':{-1:{'domain':['a','aa']}}},
                           'self':{'index':{0:{'domain':ech}}
                                   }
                           }
    def __call__(self,node, anga_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()                
        if anga_node.get_output():
            suffix_first_letter = node.get_output()[0]
            if anga_node.get_output()[-1] in ('a','aa') and suffix_first_letter  in pratyaahaara('e','ch'):
                
                return [vriddhi(node.get_output()[0])]+node.get_output()[1:]
            
            
        return node_output


class vRiddhirechi_6010851:
    def __init__(self):
        self._numconditions = 1
        ech = ['e', 'o', 'ai', 'au']
        self._condition = {
            'self':{'index':{-1:{'domain':['a','aa']}}
                    },
            'next1':{'index':{0:{'domain':ech}} }
            }
    def __call__(self,node, suffix_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        if isinstance(suffix_node._data,Suffix) and suffix_node.get_output():                  
            if node_output[-1]  in ('a','aa') and suffix_node.get_output()[0] in pratyaahaara('e','ch'):
                return node_output[:-1] #skip because the other instance of the rule uses the diirgha
        return node_output


"""
class eNGipararuupam_6010910:
    def __init__(self):
        self._types={'node':['literal'],'suffix_node':['literal']}
    def __call__(self,node, anga_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        
        if isinstance(anga_node._data,Suffix):
            pratyaya =''.join(anga_node._data._suffix)
            if pratyaya in sup_pratyayaaH() :
                # suffix is sup
                    if node.get_output()[-1] in pratyaahaara('e','Ng'):
                        return node_output[1:]
            
        return node_output

"""



def diirgha_mapper ():    
    return {'a':{'match':['a','aa'],'diirgha':'aa'},
     'aa':{'match':['a','aa'],'diirgha':'aa'},
     'i':{'match':['i','ii'],'diirgha':'ii'},
     'ii':{'match':['i','ii'],'diirgha':'ii'},
     'u':{'match':['u','uu'],'diirgha':'uu'},
     'uu':{'match':['u','uu'],'diirgha':'uu'},
     'Ri':{'match':['Ri','Rii','lRi','lRii'],'diirgha':'Rii'},
     'Rii':{'match':['Ri','Rii','lRi','lRii'],'diirgha':'Rii'},
     'lRi':{'match':['lRi','lRii'],'diirgha':'lRii'},
     'lRii':{'match':['lRi','lRii'],'diirgha':'lRii'},
    }

class atoguNne_6010940:
    def __init__(self):
        self._numconditions = 1
        self._condition = {'self':{'index':{-1: {'domain':['a'] }}
                                   },
                           'next1':{'index':{0:{'domain':['a','e','o']}}
                                    }
                           }
    def __call__(self,node, suffix_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
    
        if 6010940 not in list_past_rules_applied(node):
            if node.get_output()[-1]=='a' and suffix_node.get_output() and suffix_node.get_output()[0] in ('a','e','o'):
                return node.get_output()[:-1]
                
        return node_output


"""
A group sutra.
Two classes implement the rule because the output of the rule affects two 
different nodes. The first implementation - which is invoked before the 
latter - changes the node only so no material changes is caused
to the preconditions for the second implementation. 
"""
class akaHsavarNnediirghaH_6010970:

    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node, suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if not node.get_output():
            return node.get_output()
        
        ak_keys = pratyaahaara('a','k')+('aa',) 
        ak_mapper = diirgha_mapper()
        
        if set(ak_keys) - set(ak_mapper.keys()):
            raise ValueError("Missing mapping for diirgha")
            
        if not suffix_node.get_output() and suffix_node._children and suffix_node._children[0]!=node:
            effective_suffix_node = suffix_node._children[0]
        else:
            effective_suffix_node = suffix_node
        
        if node.get_output()  and node.get_output() [-1] in ak_mapper and effective_suffix_node.get_output() and effective_suffix_node.get_output()[0] in ak_mapper[node.get_output() [-1] ]['match']:
            if isinstance(effective_suffix_node._data,Suffix):
                pratyaya  = ''.join(effective_suffix_node._data._suffix)
                # ami puurvaH
                if pratyaya in sup_pratyayaaH() and pratyaya == 'am' :
                    return node.get_output()
            return node.get_output()[0:-1] + [ak_mapper[node.get_output()[-1]]['diirgha']]
            
        return node.get_output()


class akaHsavarNnediirghaH_6010971:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node, anga_node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must be of Node type")
        
        node_output= node.get_output()
        
        if not node.get_output():
            return node.get_output()
        
        
        ak_keys = pratyaahaara('a','k')+('aa',) 
        ak_mapper = diirgha_mapper()
        
        if set(ak_keys) - set(ak_mapper.keys()):
            raise ValueError("Missing mapping for diirgha")
        
        if not anga_node.get_output() and anga_node._parent1 and anga_node._parent1._children and anga_node._parent1._children[-1]!=node:
            effective_anga_node = anga_node._parent1._children[-1]
        else:
            effective_anga_node  = anga_node
            
        if effective_anga_node.get_output() and effective_anga_node.get_output() [-1] in ak_mapper and node.get_output()[0] in ak_mapper[effective_anga_node.get_output() [-1]]['match']:
            if isinstance(node._data,Suffix):
                pratyaya  = ''.join(node._data._suffix)
                # ami puurvaH
                if pratyaya in sup_pratyayaaH() and pratyaya == 'am':
                    return node_output[1:]
            
            return node_output[1:] #skip because the other instance of the rule uses the diirgha
            
        return node.get_output()


class prathamayoHpuurvasavarNnaH_6010980:
    def __init__(self):
        self._numconditions = 1
        self._condition = {
                           'prev1':{'index':{-1:{'domain':ach()}}},
                           'self':{'index':{0:{'domain':ach()}},
                                   'data':{'domain':sup_pratyayaaH()[0:6]}
                                   }
                           }
        
    def __call__(self,node, anga_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        
        if isinstance(node._data,Suffix):
            pratyaya =''.join(node._data._suffix)
            if pratyaya in sup_pratyayaaH()[0:6] : # only prathhama and dvitiiyaa considered
                # suffix is sup
                    if anga_node.get_output() and anga_node.get_output()[-1] in ach() and node.get_output()[0] in ach():
                       if anga_node.get_output()[-1] in ('a','aa',) and node.get_output()[0] in pratyaahaara('i', 'ch'): ## naadichi
                           return node_output
                       else:
                           return node_output[1:]
            
        return node_output

class prathamayoHpuurvasavarNnaH_6010981:
    def __init__(self):
        self._numconditions = 1
        self._condition = {
                           'self':{'index':{-1:{'domain':ach()}}},
                           'next1':{'index':{0:{'domain':ach()}},
                                   'data':{'domain':sup_pratyayaaH()[0:6]}
                                   }
                           }
        
    def __call__(self,node,suffix_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        
        if isinstance(suffix_node._data,Suffix):
            pratyaya =''.join(suffix_node._data._suffix)
            if pratyaya in sup_pratyayaaH()[0:6] : # only prathhama and dvitiiyaa considered
                # suffix is sup
                    if node.get_output() and suffix_node.get_output() and \
                        node.get_output()[-1] in ach() and suffix_node.get_output()[0] in ach():
                            if node.get_output()[-1] in ('a','aa',) and suffix_node.get_output()[0] in pratyaahaara('i', 'ch'): ## naadichi
                                return node.get_output()
                            else:
                                return node.get_output()[0:-1]+[diirgha_mapper()[node.get_output()[-1]]['diirgha']]
            
        return node_output
    
class tasmaatchhasonaHpuMsi_6010990:
    def __init__(self):
        self._numconditions = 2
        self._condition = {
            'self':{'data':{'domain':['shas']},
            'liNga':{'domain':[1]}}
            }
    def __call__(self,node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        
        
        if isinstance(node._data,Suffix):
            pratyaya =''.join(node._data._suffix)
            if pratyaya in sup_pratyayaaH()[0:6] and pratyaya=='shas' : # only shas considered
                #last_rule_applied = list_past_rules_applied(node._prev)[-1]
                # TODO: ensure that this happens only just after 6010980 (prathamayoHpuurvasavarNnaH) is applied
                if node._data._linga == 1 :
                    return node.get_output()[0:-1] + ['n']
        
        
        return node_output

"""
class amipuurvaH_6011030:
    def __init__(self):
        self._types={'node':['literal'],'suffix_node':['literal']}
    def __call__(self,node, anga_node):
        node_output= node.get_output()
        if not node.get_output():
            return node.get_output()
        
        if isinstance(anga_node._data,Suffix):
            pratyaya =''.join(anga_node._data._suffix)
            if pratyaya in sup_pratyayaaH() and pratyaya == 'am':
                # suffix is sup
                    if node.get_output()[-1] in pratyaahaara('a','k'):
                        return node_output[1:]
            
        return node_output

"""


class gharuupakalpachelaXdbruvagotramatahateXshuNgyoanekaachaohrasvaH_6030420:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if node.get_output() and 6030420 not in list_past_rules_applied(node):
            #raise RuntimeError("Work under progress")
            return node.get_output()
        return node.get_output()


class aasarvanaamnaH_6030900:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        sarvanaamaMap = {'tad':['t','aa'],}
        if isinstance(node._data,Praatipadika) and ''.join(node._data._data) in sarvanaamaMap:
            if node.get_output() and 6030900 not in list_past_rules_applied(node):
                if ''.join(suffix_node._data._suffix) in ('vatNNp','dRik','dRish','vatNN'):
                    return sarvanaamaMap[''.join(node._data._data)]
        return node.get_output()
    
    

class naami_6040030:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if node.get_output() and suffix_node.get_output() and suffix_node._parent2 is not None:
            if suffix_node.get_output()==['n'] and isinstance(suffix_node._parent2._data,Suffix) and suffix_node._parent2._data._suffix==['aa','m']:
                if node.get_output()[-1] in ('a','i','u','Ri','lRi',):
                    return node.get_output()[:-1]+[make_diirgha(node.get_output()[-1])]
                
        return node.get_output()


class aptRintRichsvasRinaptRineXshXtRitvaXshXtRikXshatRihotRipotRiprashaastRiiXnaam_6040110:
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        """
        rule applies when the suffix is sarvanaama (i.e. one of 'sNN', 'au','jas','am','auXt')
        
        """
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if node.get_output() and isinstance(suffix_node._data,Suffix) and \
            ''.join(suffix_node._data._suffix) in ('sNN', 'au','jas','am','auXt'):
            if isinstance(node._data,Praatipadika):
                if (''.join(node.get_output()) in ('svasRi','naptRi','neXshXtRi',\
                  'tvaXshXtRi','kXshatRi','hotRi','potRi','prashaastRi',) ):
                    return node.get_output()[0:-1] + ['aa']
            if isinstance(node._data,Suffix): 
                if ''.join(node._data._suffix) in ('ap','tRich','tRin',):
                    # check if there is an ach in upadhaa
                    # which is the last ach when output ends in hal and 
                    # the second-last ach when output ends in ach,
                    achsInNode = [i for i, x in enumerate(node.get_output()) if x in ach()]
                    if len(node.get_output())>2:
                        if node.get_output()[-1] not in ach() :
                            posUpdhaa= achsInNode[-1]
                        elif len(achsInNode)>1:
                            posUpdhaa = achsInNode[-2]
                        else:
                            posUpdhaa = None
                        if posUpdhaa is not None:
                           return node.get_output() [ 0:posUpdhaa ] + \
                               [make_diirgha (node.get_output()[posUpdhaa])] +\
                                   node.get_output() [ posUpdhaa +1:]
                            
            
        return node.get_output()

class atvasantasyachaadhaatoH_6040140:
    
    def __init__(self):
        self._numconditions = 1
        
    def __call__(self,node,suffix_node):
        """
        rule applies when the suffix is sarvanaama (i.e. one of 'sNN', 'au','jas','am','auXt')
        
        """
        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")

        if not isinstance(suffix_node,Node):
            raise ValueError("suffix_node must be of Node type")
        
        if node.get_output() and len(node.get_output()) > 1 and not isinstance(node._data,Dhaatu):
            # adhaatoH
            node_data  = None
            if isinstance(node._data,Praatipadika) :
                node_data = node._data._data 
            elif isinstance(node._data,Suffix):
                node_data = node._data._suffix
            else:
                node_data = None
                
            if node_data  :
                sutra_applicable = False
                if len(node_data ) >= 4:
                    if node_data [-4:] in (['a','t','NN','p'],) :
                        sutra_applicable = True

                if len(node_data ) >= 3:
                    if node_data [-3:] in (['a','t','u'],) :
                        sutra_applicable = True
                elif len(node_data)>=2 and node_data [-2:] == ['a','s']:
                    sutra_applicable = True
                if sutra_applicable :                    
                    nodeUpadhaa = node_upadhaa(node)
                    if nodeUpadhaa is not None :
                        return node.get_output() [0:nodeUpadhaa['pos']] + \
                            [make_diirgha(nodeUpadhaa['char'])] + \
                                node.get_output()[nodeUpadhaa['pos']+1:]
            
            return node.get_output()
        
        return node.get_output()


class luNglaNglRiNgkShvaXdudaattaH_6040710:
    def __init__(self):
        self._numconditions = 1
        self._condition = {'next1':{'lakaara':{'domain':['luNg','laNg','lRiNg']} },
                           }
        
    def __call__(self,prefix_node,suffix_node):
        e1=find_eldest_parent1_of_condition(suffix_node,lambda x : isinstance(x ,Node) and isinstance(x._data,Suffix) and x._data._lakaara in ('luNg','laNg','lRiNg') )
        e2=find_eldest_parent2_of_condition(suffix_node,lambda x : isinstance(x ,Node) and isinstance(x._data,Suffix) and x._data._lakaara in ('luNg','laNg','lRiNg') )

        if e1 is None:
            if e2 is None :
                return []
            else :
                effective_suffix_node = e2
        else:
            effective_suffix_node = e1
            
        if isinstance(prefix_node ._data,Dhaatu) and \
            isinstance(effective_suffix_node._data,Suffix) :
                if effective_suffix_node._data._lakaara in ('luNg','laNg','lRiNg') :
                    past_rules_applied = [int(x['rule'].__name__.split("_")[-1]) for x in prefix_node._output if 'rule' in x]
                    if 6040710 not in past_rules_applied  :
                        #raise ValueError("aXt needs to be checked in dhaatu-nodes modification (while prepending)")
                        return Suffix("aXt")
        return []
  
    
class achishnudhaatubhruvaaMyvoriyaNguvaNgau_6040770:

      def __init__(self):
          self._numconditions = 1
      def __call__(self,node,suffix_node):
          """
          also implements eranekaacho-asaMyogapuurvasya, hushnuvoHsaarvadhaatuke by suppressing iy,uv aadesha
          
          Notice however that only shnu's part of hushnuvoHsaarvadhaatuke has been implemented. The hu
          part may need to be implemented separately.
          """
          if not isinstance(suffix_node,Node):
              raise ValueError("suffix_node must be of Node type")

          if not isinstance(node,Node):
              raise ValueError("node must be of Node type")
          #lastAadeshaInSuffix = [x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
          
          # don't apply twice
          if 6040770 in list_past_rules_applied(node):
              return node.get_output()
          
          if suffix_node.get_output() and suffix_node.get_output()[0] in pratyaahaara('a','ch'): #lastAadeshaInSuffix == ['a','ch']:
              if isinstance(suffix_node._data,Suffix) and suffix_node.get_output():
                  if isinstance(node._data,Suffix):
                      if ''.join(node._data._suffix)== 'shnu':
                          listAchPos = list_achpos(node.get_output())
                          if listAchPos is not None:
                              # anekaach or asaMyoga anga with 'u','uu' ending
                              if len(listAchPos)>1 :
                                  return node.get_output()
                              if len(node.get_output())>2:
                                  # asaMyoga
                                  if node.get_output()[-2] in ach() or node.get_output()[-3] in ach():
                                      return node.get_output()
                              elif len(node.get_output())==2 and not node.get_output()[-2] in ach() :
                                  return node.get_output()
                            
                          return node.get_output()[0:-1] + ['u','v']
                      
                  if isinstance(node._data,Dhaatu) :
                      if node.get_output()[-1] in ('i','ii'):
                          listAchPos = list_achpos(node.get_output())
                          if listAchPos is not None:
                              # anekaach or asaMyoga anga with 'i'/'ii' ending
                              if len(listAchPos)>1 :
                                  return node.get_output()
                              if len(node.get_output())>2:
                                  # asaMyoga
                                  if node.get_output()[-2] in ach() or node.get_output()[-3] in ach():
                                      return node.get_output()
                              elif len(node.get_output())==2 and not node.get_output()[-2] in ach() :
                                  return node.get_output()
                            
                          return node.get_output()[0:-1] + ['i','y']
                      
                      if node.get_output()[-1] in ('u',):# skipping 'uu' because bhuu + tip should not become bhuvati
                          return node.get_output()[0:-1] + ['u','v']
              
              
          return node.get_output()

class bhuvovugluNgliXtoH_6040880:
    def __init__(self):
        self._numconditions = 1
        self._condition = {'next1':{
                            'index':{0:{'domain':ach()}},
                            'lakaara':{'domain':['luNg','liXt'] }
                            },
                           'self':{'data':{'domain':["bhuu"]}}
                           }
        
    def __call__(self,node,suffix_node):   
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
    
        if isinstance(node._data,Dhaatu) and node.get_output()==["bh","uu"] \
            and ( suffix_node._data._lakaara in ('luNg','liXt') or ( not isinstance(suffix_node._data,Aagama) and suffix_node._data._suffix[0] in ach()) ):
            return ['bh','uu','v']
    
            
        return  node.get_output()


class atoheH_6041050:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node,anga_node):
        if not isinstance(anga_node,Node):
            raise ValueError("anga_node must be of Node type")

        if not isinstance(node,Node):
            raise ValueError("node must be of Node type")
        if isinstance(node._data,Suffix) and node._data._lakaara == 'loXt' :
                suffix_data=[x['output'] for x in node._output if 'new' in x and x['new']][-1]
                if anga_node.get_output() and anga_node.get_output()[-1]=='a' and suffix_data==['h','i']:
                    return []
        return node.get_output()




class ataekahalmadhyeanaadeshaaderliXti_6041200:
    def __init__(self):
        self._numconditions = 1
                           
                           
    def __call__(self,node,suffix_node):
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if suffix_node._data._lakaara == 'liXt':
            applied_rules= [int(x['rule'].__name__.split('_')[-1]) for x in node._output if 'rule' in x]
            if 601008 in applied_rules :
                convert_e = lambda x : x if x not in ('a','aa',) else 'e'
                if len([x['output'] for x in node._output if 'new' in x and x['new']]) == 1: # there has been no adesha to anga
                    if node.get_output()[-1] not in ach() and node.get_output()[-2] in ach() : # asaMyoga => kit
                        return node.get_output()[:-2] + [convert_e(node.get_output()[-2])] + node.get_output()[-1:]   
            
        return node.get_output()

class ghumaasthaagaapaajahaatisaaMhali_6040660:
    """
    jahaati has been ignored.
    """
    def __init__(self):
        self._numconditions = 1
                           
                           
    def __call__(self,node,suffix_node):
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if not node.get_output():
            return node.get_output()
        
        
        
        if isinstance(suffix_node._data,Suffix):
            kitOrNgit = True if suffix_node._data._suffix[0] in ('k','Ng') or suffix_node._data._suffix[-1] in ('k','Ng') else False
            if  kitOrNgit :
                sthaaetc=False
                if node.get_output() and not suffix_node._data.is_saarvadhaatuka():
        #            if ''.join(node.get_output()) == "jahaati":
        #                sthaaetc = True
                    if len(node.get_output())>=3 and ''.join(node.get_output()[-3:]) == 'sthaa':
                        sthaaetc = True
                    elif len(node.get_output())>=2 and ''.join(node.get_output()[-2:]) in ('maa','gaa','paa','saa',):
                        sthaaetc = True
                        
                    if (isinstance(node._data,Dhaatu) and ''.join(node._data._data) in (ghu_dhaatus() + ("XshoNN", "haaNN",))) or sthaaetc:
                        return node.get_output()[0:-1] + ['ii']
                
        return node.get_output()

class XteH_6041430:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node,suffix_node):
        if not isinstance(suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if not isinstance(node,Node):
            raise    ValueError ("node must be of type Node")
        if node.get_output() and 6041430 not in list_past_rules_applied(node):
            if isinstance(node._data,Praatipadika) and (suffix_node._data._suffix[0] == 'Xd' or suffix_node._data._suffix[-1] == 'Xd') :
                nodeAchs = [i for i,x in enumerate(node.get_output()) if x in ach()]
                if nodeAchs:
                    return node.get_output()[0:nodeAchs[-1]]
        return node.get_output()



class yasyeticha_6041480:
    def __init__(self):
        self._numconditions = 1

    def __call__(self,node,suffix_node):
    
        suffix = suffix_node._data
        suffix_data = ''.join(suffix._suffix)
        anga_str=node.get_output()
        if not isinstance(suffix ,Suffix):
            raise ValueError("suffix must be of Suffix type")
        
        #pick last value
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        
        if anga_str and anga_str[-1] in ('i', 'ii', 'a', 'aa'): # worry about yasyeticha only when anga ends in i,ii,a,aa
            if suffix.is_taddhita or (suffix_data[0] in ('i','ii') and suffix_data in (sup_pratyayaaH()+kRit_pratyayaaH()+san_pratyayaaH()) ) :
                return anga_str[0:-1]
        return anga_str
