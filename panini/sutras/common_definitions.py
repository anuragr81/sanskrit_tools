import re

def parse_string(input_str):
    """
    build a list of aksharas from the string - unknown letters are ignored
    """
    sorted_achs= ('lRii','Rii', 'lRi', 'Ri','ai', "ii","uu",'au',"aa",'a', 'i', 'u', 'e', 'o',)
    match_re = "("+'|'.join(hal() + sorted_achs)+")" + "(.*)"
    
    
    matches = True
    x_str = input_str
    output=[]
    while matches and x_str:
        res = re.search(match_re, x_str)
        if res:
            output.append(res.group(1))
            x_str = res.group(2)
        else:
            matches =False
    return output



def lakaaras():
    return ('laXt','loXt','lRiXt','laNg','luNg','lRiNg','liNg1','liNg2','liXt','luXt')




def all_pratyayas() : 
    return kRit_pratyayaaH()+tiNg_pratyayaaH()+san_pratyayaaH()+strii_pratyayaaH()+sup_pratyayaaH()+taddhita_pratyayaaH() + unclassified_pratyayaaH()


class Suffix:
    def __init__(self,suffix,lakaara=None,linga=None):
        
        if lakaara is not None:
            if lakaara not in lakaaras():
                raise ValueError("Unknown lakaara")            
        self._lakaara=lakaara

        
        if linga is not None:
            if linga not in (0,1,2):
                raise ValueError("Invalid linga")            
        self._linga=linga


        if isinstance(suffix,str):
            self._suffix = parse_string(suffix)
        elif isinstance(suffix,list) and all(isinstance(j,str) for j in suffix):
            self._suffix= suffix
        else:
            raise ValueError("suffix must be a string")
        
        all_pratyayaaH = all_pratyayas()
        if ''.join(self._suffix) not in all_pratyayaaH:
            raise ValueError("Unknown suffix %s" % ''.join(self._suffix))            
        
        self.is_taddhita = ''.join(self._suffix) in taddhita_pratyayaaH()
        
    def get_data(self):
        return self._suffix
        
    
    def apply_reduction(self,functor, **kwargs):
        self.reduced = functor(**kwargs)
        
    def is_saarvadhaatuka(self):
        if ''.join(self._suffix) in tiNg_pratyayaaH() or self._suffix[0]=='sh':
            return True
        else:
            return False

    def __str__(self):
        return ''.join(self._suffix)

    def __repr__(self):
        return str(self._suffix)


class Dhaatu:
    def __init__(self,data):
        self._data= data
        
    def get_data(self):
        return self._data


def get_dhaatu_properties(dhaatu_string):
    dhaatu_store = {'chiNN':{'aniXt':True}, 
                    'paXthNN':{'aniXt':False},
                    'luuNc':{'aniXt':False}
                    }
    return dhaatu_store [dhaatu_string]


def find_eldest_parent1_of_condition(node,cond):
    
    if node and node.get_parent1():
        if cond(node):
            return node.get_parent1()
        else:
            return find_eldest_parent1_of_condition(node.get_parent1(),cond)
    
    if cond(node):
        return node 
    else:
        return None

def find_eldest_parent2_of_condition(node,cond):
    
    if node and node.get_parent2():
        if cond(node):
            return node.get_parent2()
        else:
            return find_eldest_parent2_of_condition(node.get_parent2(),cond)
    if cond(node):
        return node 
    else:
        return None
    
    
def list_past_rules_applied (nd):
    """
    Returns list of rules applied so far for the node:nd
    """
    return [int(x['rule'].__name__.split("_")[-1]) for x in nd._output if 'rule' in x]
    
class Node:
    def __init__(self,data,parent1,parent2=None):
        if all ( not isinstance(data,x) for x in list(get_supported_types()) + [list] ):
            raise ValueError("Unsupported type %s" % type(data))
        self._children=[]
        
        self._parent1 = parent1
        self._parent2 = parent2
        
        if self._parent1:
            self._parent1._add_child(self)
        
        if self._parent2:
            self._parent2._add_child(self)
        
        
        self._data =data
        self._output = [{'output':self._data.get_data(),'new':True}]
    
    
    def _add_child(self,ptr):
        self._children.append(ptr)
        
    def _assign_output_properties(self,rule,**inputs):                
        # output is not changed
        old_output  = self.get_output()
        # no change in output -just rule and input update
        self._output.append({'rule':rule, 'inputs':{**{'state':self} , **inputs}, 'output':old_output })
            
    def set_output(self,rule,**kwargs):
        old_output = self.get_output()
        # call the function
        #print(rule.__name__ + ":" + str(kwargs))
        new_output = rule()(node=self,**kwargs)
        
        if isinstance(new_output,dict):
            if 'mutate' in new_output :
                if new_output['output'] != old_output :
                    if new_output ['mutate']:
                        self._output.append({'rule':rule,'inputs':{**{'state':self } , **kwargs},'output':new_output['output'] ,'new' :True})
                    else:
                        self._output.append({'rule':rule,'inputs':{**{'state':self } , **kwargs},'output':new_output['output']})
                
        else:
           if new_output != old_output:
              self._output.append({'rule':rule,'inputs':{**{'state':self} , **kwargs},'output':new_output })
        
    def get_output(self):
        return self._output[-1]['output']
    
    def get_parent1 (self):
        return self._parent1
  
    def get_parent2 (self):
        return self._parent2
    
    def has_sthaanii_it(self,itchar):
        """
        Parameters
        ----------
        itchar: character
            The character to be searched all through the output for it presence
    
        Raises
        ------
    
        Returns
        -------
        list
            boolean variable indicating whether it character exists anywhere in the history (sthaani) or not.
        """
        for x in self._output:
            if itchar in x['output']:
                return True
        return False
    


def get_supported_types ():
    return (Suffix,Dhaatu)


def ach():
    return ("aa","ii","uu","Rii",'lRii') + pratyaahaara('a','ch')

def pratyaahaara(start,end):
    """   
    Parameters
    ----------
    start : character
        The starting letter of the  pratyaahaara
    end : character
        The ending letter of the  pratyaahaara

    Raises
    ------
    ValueError
    RuntimeError

    Returns
    -------
    list
        characters in the pratyaahaara.

    """
    
    plist= ({'letters':("a","i",'ii',"u",'uu',),'marker':'Nn'},{'letters':('Ri','Rii','lRi','lRii'),'marker':'k'},
        {'letters':('e','o',),'marker':'Ng'},{'letters':('ai','au'),'marker':'ch'},{'letters':('h','y','v','r',),'marker':'Xt'},{'letters':('l',),'marker':'N'},
        {'letters':('Nc','m','Ng','Nn','n'),'marker':'m'},{'letters':('jh','bh'),'marker':'Nc'},{'letters':('gh','Xdh','dh'),'marker':'Xsh'},
        {'letters':('j','b','g','Xd','d',),'marker':'sh'},{'letters':('kh','ph','chh','Xth','th','ch','Xt','t',),'marker':'v'},
        {'letters':('k','p',),'marker':'y'},{'letters':('sh','Xsh','s',),'marker':'r'},{'letters':('h',),'marker':'l'},)
    markers = [p['marker'] for p in plist]
    if end not in markers:
        raise ValueError("Unkown marker: %s" % end)
    entries = [(i,j) for i,j in enumerate(plist) if end==j['marker']]
    if len(entries)>1:
        raise RuntimeError("Multiple entries not supported")
    else:
        not_found = True
        for i,entry in enumerate(plist):
            if start in entry['letters']:
                not_found = False
                results = plist[i:(entries[0][0]+1)]
                output = list(results[0]['letters'][results[0]['letters'].index(start):])
                for res_entry in results[1:]:
                    output = output+list(res_entry['letters'])
                return tuple(output)
                
        if not_found:
            raise ValueError("Unknown starting letter: %s" % start)
        

def hal():
    return ("kh","k","gh","g","Ng","Nc","NN","Nn","chh","ch","jh","j",
            "Xth","Xt","Xdh","Xd","Xsh","th","t","dh","d","n",
            "ph","p","bh","b","m","y","r","l","v","sh",
            "s","h")
def anunaasika():
    return ("Ng","Nc","Nn","M","m","NN")

def chu():
    return ("ch","chh","j","jh","Nc")

def Xtu():
    return ("Xt","Xth","Xd","Xdh","Nn")



def unclassified_pratyayaaH():
    return ('sNNch','chlNN','shap','taas','sya','aXt','iiXt','aaXt','yaasNNXt','sNNXt')

def san_pratyayaaH():
    return ("san","kyach","kaamyach","kyaNg","kyaXsh",
            "kvip","Nnich","yaNg","yak","aaya",
            "iiyaNg","NniNg")

def tiNg_pratyayaaH():
    return aatmanepada_pratyayaaH()+parasmaidpada_pratyayaaH()

def parasmaidpada_pratyayaaH():
    return ("tip","tas","jhi","sip","thas","tha","mip",
            "vas","mas")

def aatmanepada_pratyayaaH():
    return ("ta","aataam","jha","thaas",
            "aathaam","dhvam","iXt","vahi","mahiNg")
def kRit_pratyayaaH():
    return ("Nnvul","lyuXt","aniiyar","kta","ktavatu",
            "tavyat","tumun","tRich","ktvaa","Nnamul",
            "lyap","yat","Nnyat","kyap","ghaNc","ach",
            "ap","ktin","a","yuch","u","shatRi","shaanach",
            "ka","Nnini","kvip")

def upasargaaH():
    return ("abhi","prati","pari","upa","pra","apa",
            "sam","anu","ava","nis","nir","dus",
            "dur","vi","aaNg","ni","adhi","api",
            "ati","su","ut")

def strii_pratyayaaH():
    return ("Xtaap","Xdaap","chaap","Ngiip","NgiiXsh",
            "Nniin","uuNg","ti","XshyaNg","Xshpha")

def sup_pratyayaaH():
    return ('sNN', 'au','jas','am','auXt','shas','Xtaa','bhyaam','bhis','Nge','bhyaam',
        'bhyas','Ngasi','bhyaam','bhyas','Ngas','os','aam','Ngi','os','sup')


def taddhita_pratyayaaH ():
    return ('chha','iiy','aNn')

def upadhaa(x):    
    if not isinstance(x,list) or not all(isinstance(j,str) for j in x):
        raise ValueError("invalid input: %s" % x)
    if len(x)>=2:
        return len(x)-2
    else:
        raise ValueError("Insufficient length for upadhaa")


def diirgha(x):
    if x =="a":
        return "aa"
    elif x == "i":
        return "ii"
    elif x == "u":
        return "uu"
    else:
        return x


def guNna(x):
    if x =="i" or x=="i":
        return "e"
    elif x == "u" or x=="uu":
        return "o"
    else:
        return x
            
def vriddhi(x):
    if x =="a":
        return "aa"
    elif x == "i":
        return "ai"
    elif x == "e":
        return "ay"
    elif x == 'ii':
        return 'ai'
    elif x=='u':
        return 'o'
    elif x=='uu':
        return 'au'
    else:
        return x
    

def make_diirgha(x):
    
    if x not in ach():
        raise ValueError("must be an ach")
    
    if x in ('a','aa',):
        return "aa"
    if x in ("ii",'i',):
        return 'ii'
    if x in ('u','uu',):
        return 'uu'
    if x in ("Ri","Rii",):
        return 'Rii'
    if x in ('lRii','lRi',):
        return 'lRii'

def guna_letters_for_aat(x):
    
    if x in ( 'i', 'ii',):
        return ['e']
    if x in ('u', 'uu',):
        return ['o']
    if x in ('Ri', 'Rii', ):
        return ['a','r']
    if x in ('lRi', 'lRii',):
        return ['a','l']
    
    raise ValueError("No guNna support")

