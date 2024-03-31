from functools import reduce
from ..common_definitions import Suffix, Aagama, Node, Dhaatu, ach, hal, sup_pratyayaaH, taddhita_pratyayaaH
from ..common_definitions import pratyaahaara, make_diirgha, guna_letters_for_aat
from ..common_definitions import vriddhi, list_past_rules_applied
from ..common_definitions import find_eldest_parent1_of_condition 
from ..common_definitions import find_eldest_parent2_of_condition

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
        # conditions are only used for nitya-apavaada comparison
        self._condition= {'self':{'lakaara':{
                                            'domain':['liXt']
                                            }
                                }
                          }
        
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
        pratyaaharaval= ['v', 'r', 'l', 'Nc', 'm', 'Ng', 'Nn', 'n', 'jh', 'bh', 'gh', 'Xdh', 'dh', 'j', 'b', 'g', 'Xd', 'd', 'kh', 'ph', 'chh', 'Xth', 'th', 'ch', 'Xt', 't', 'k', 'p', 'sh', 'Xsh', 's', 'h']
        self._condition = {'self':{'index': { -1 : {'domain:':['y','v']}} 
                                   },
                           'next1':{ 'index': {0 : {'domain': pratyaaharaval}}
                                    }
                           }
    def __call__(self,node,suffix_node):    
        if not isinstance   (node,Node):
            raise    ValueError ("node must be of type Node")
        if not isinstance   (suffix_node,Node):
            raise    ValueError ("suffix_node must be of type Node")
        if node.get_output() and node.get_output()[-1] in ('y','v') :
            if suffix_node.get_output() :
                effective_suffix_node= suffix_node
            elif not suffix_node.get_output()  and suffix_node._parent2.get_output():
                effective_suffix_node = suffix_node._parent2
            else:
                return node.get_output()
                
            if effective_suffix_node.get_output()[0] in pratyaahaara('v','l'):
                return node.get_output()[0:-1]
            
        return node.get_output()
        

class echoayavaayaavaH_6010750:
    def __init__(self):
        self._numconditions = 1
        achs = ['aa', 'ii', 'uu', 'Rii', 'lRii', 'a', 'i', 'ii', 'u', 'uu', 'Ri', 'Rii', 'lRi', 'lRii', 'e', 'o', 'ai', 'au']
        self._condition = {'self':{'index': {'ANDVEC': [{ -1 : { 'domain':['e','o','ai','au'] }} ,
                                              {0 : {'domain':achs}} 
                                              ]
                                             }
                                   
                                   }
                           }
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

Two classes implement this because the output of the rule affects two 
different nodes. The first implementation - which is invoked before the 
latter - changes the node only so no material changes is caused
to the preconditions for the second implementation 
"""
class akaHsavarNnediirghaH_6010970:

    def __init__(self):
        self._numconditions = 1
        # the issue that a condition B might depend on whether condition A has 
        # been satisfied or not has not been handled. We're considering conditions A and B as being independently matched 
        # e.g. by consider a weaker condition in this case
        self._condition = { 'self':{'index': {-1:{'domain': list(diirgha_mapper().keys()) }}
                                    } ,
                            'next1':{'index':{0:{'domain':list(set(reduce(lambda x, y: x + y , [v['match'] for _,v in diirgha_mapper().items()]))) }}
                                    }
                           }
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
        
        if node.get_output()  and node.get_output() [-1] in ak_mapper and suffix_node.get_output() and suffix_node.get_output()[0] in ak_mapper[node.get_output() [-1] ]['match']:
            if isinstance(suffix_node._data,Suffix):
                pratyaya  = ''.join(suffix_node._data._suffix)
                # ami puurvaH
                if pratyaya in sup_pratyayaaH() and pratyaya == 'am' :
                    return node.get_output()
            return node.get_output()[0:-1] + [ak_mapper[node.get_output()[-1]]['diirgha']]
            
        return node.get_output()


class akaHsavarNnediirghaH_6010971:
    def __init__(self):
        self._numconditions = 1
        self._condition = { 'self':{'index': {-1:{'domain': list(diirgha_mapper().keys()) }}
                                    } ,
                            'next1':{'index':{0:{'domain':list(set(reduce(lambda x, y: x + y , [v['match'] for _,v in diirgha_mapper().items()]))) }}
                                    }
                           }

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
        
        if anga_node.get_output() and anga_node.get_output() [-1] in ak_mapper and node.get_output()[0] in ak_mapper[anga_node.get_output() [-1]]['match']:
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
                       if node.get_output()[0] not in pratyaahaara('i', 'ch'): ## naadichi
                           return node_output[1:]
            
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
        self._condition = {'self':{'lakaara':{'domain':['loXt']},'data':{'domain':['hi']}  },
                           'prev1':{'index':{-1:{'domain':['a'] }}}}
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
        self._condition = {'next1':{'lakaara':{'domain':['liXt']}
                                    }, 
                           'self':{'ANDVEC': [{'index':{-2:{'domain': hal()}}},
                                            {'index':{-1:{'domain':hal()}}}
                                            ]
                                            }
                           }
                           
                           
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


class yasyeticha_6041480:
    def __init__(self):
        self._numconditions = 1
        taddhitas = list(taddhita_pratyayaaH ())
        self._condition = {'next1':{'data':{'domain':taddhitas }},
                           'index':{0:{'domain':['i','ii']}}
                           }
    def __call__(self,node,suffix_node):
    
        suffix = suffix_node._data
        anga_str=node.get_output()
        if not isinstance(suffix ,Suffix):
            raise ValueError("suffix must be of Suffix type")
        
        #pick last value
        suffix_data=[x['output'] for x in suffix_node._output if 'new' in x and x['new']][-1]
        if False: # TODO: re-enable
            if suffix.is_taddhita or suffix_data[0] in ('i','ii'):
                 return anga_str[0:-1]
        return anga_str
