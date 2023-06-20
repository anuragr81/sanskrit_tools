from collections import OrderedDict

import re, sys
from copy import deepcopy
from functools import reduce
from pprint import pprint
import inspect
import pandas as pd



from panini.sutras import adhyaaya1 as a1
from panini.sutras import adhyaaya2 as a2
from panini.sutras import adhyaaya3 as a3
from panini.sutras import adhyaaya4 as a4
from panini.sutras import adhyaaya5 as a5
from panini.sutras import adhyaaya6 as a6
from panini.sutras import adhyaaya7 as a7
from panini.sutras import adhyaaya8 as a8

from panini.sutras.adhyaaya1 import *
from panini.sutras.adhyaaya2 import *
from panini.sutras.adhyaaya3 import *
from panini.sutras.adhyaaya4 import *
from panini.sutras.adhyaaya5 import *
from panini.sutras.adhyaaya6 import *
from panini.sutras.adhyaaya7 import *
from panini.sutras.adhyaaya8 import *


output_processed_string = lambda e: ''.join(reduce(lambda x ,y : x + y.get_output(),  e, []))

"""
Currently the naayaka is broken because aardhadhaatukasyavalaadeH has been enabled due
to default aardhadhaatukaH
"""

def get_sutras_for_module (j):
    res=[]
    for x in dir(j) :        
         if not x.startswith('_')  and re.search('[0-9]+$',x):
             res.append((float(re.search('([0-9]+_*[0-9]*)$',x).group(1)),getattr(j,x)))
    return res

def get_sutras_ordered ():    
    all_sutras = reduce(lambda x , y : x + get_sutras_for_module (y) , [a1,a2,a3,a4,a5,a6,a7,a8],[]) 
    return OrderedDict(sorted(all_sutras))

#6011030

def padaanta_sutras():
    return [8020230]

def transformation_sutras():
    # TODO: add 6010640
    ll = [2040850,3010331,3040820,3040860,3040870,3040890,3040990,3041000,3041010,
          6010080,6010630, 6010750, 6040880, 6010940, 6010980, 
          6010840,6010841,6010850,6010851,
          6010970,6010971,6010990, 6041050, 6041200, 6041480, 7010030,7010010, 7010020, 7010120,7010130,
          
          7020021, 7020790,7020800, 7021150, 7021160, 7030520, 7030840,7031010,7031020,7040500,7040501,
          8010150, 8020280, 8020660, 8030059]
    return sorted(float(x) for x in ll)



def prepend_sutras():
    return [6040710]

def insertion_sutras():
#   to be considered: 601008
    ll=[3010460,3010680,3040920,3010330,3041030,3041070,7020350,7030960,7030961]
    return sorted(float(x) for x in ll)

def apply_transformation_at_end(transformation_rule,new_expr):
    #print(transformation_rule.__name__)
    sig_params = inspect.signature(transformation_rule.__call__).parameters
    i =len(new_expr)-1    
    if isinstance(new_expr[i]._data,Suffix):
        if i>0 :
            if isinstance(new_expr[i-1]._data,Dhaatu):
                dhaatu_index=i-1
                if 'anga_node' in sig_params :
                    new_expr[i].set_output(transformation_rule,anga_node=new_expr[dhaatu_index])           
                if 'suffix_node' in sig_params :
                    new_expr[dhaatu_index].set_output(transformation_rule,suffix_node=new_expr[i])
            else:
                if 'suffix_node' in sig_params :
                    new_expr[i-1].set_output(transformation_rule,suffix_node=new_expr[i])
                if 'anga_node' in sig_params :                                            
                    new_expr[i].set_output(transformation_rule,anga_node=new_expr[i-1])

                
        if 'anga_node' not in sig_params  and 'suffix_node' not in sig_params :
            new_expr[i].set_output(transformation_rule)
            
        
                    
    return new_expr




def is_transformation_applicable(transformation_rule,new_expr):
    sig_params = inspect.signature(transformation_rule.__call__).parameters
    for i in range(0,len(new_expr)):
        old_output = new_expr[i].get_output()
        if isinstance(new_expr[i]._data,Suffix):
            if i>0 :
                #TODO: remove Dhaatu check in anga - since suffixes (that are not Dhaatus) may also act as anga
                
                
                if isinstance(new_expr[i-1]._data,Dhaatu):
                    dhaatu_index=i-1
                    if 'anga_node' in sig_params :        
                        new_output = transformation_rule()(node=new_expr[i],anga_node=new_expr[dhaatu_index])
                        if new_output  != old_output:
                            return True
                    
                    if 'suffix_node' in sig_params :
                        new_output = transformation_rule()(node=new_expr[dhaatu_index],suffix_node=new_expr[i])
                        if new_output  != old_output:
                            return True

                else:
                    if 'suffix_node' in sig_params :
                        new_output = transformation_rule()(node=new_expr[i-1],suffix_node=new_expr[i])
                        if new_output  != old_output:
                            return True
                        
                    if 'anga_node' in sig_params :
                       new_output = transformation_rule()(node=new_expr[i],anga_node=new_expr[i-1])
                       if new_output  != old_output:
                           return True

                    
            if 'anga_node' not in sig_params  and 'suffix_node' not in sig_params :
                new_output = transformation_rule()(node=new_expr[i])
                if new_output  != old_output:
                    return True

            
                    
    return False


def apply_transformation(transformation_rule,new_expr):
    sig_params = inspect.signature(transformation_rule.__call__).parameters
    for i in range(0,len(new_expr)):
        if isinstance(new_expr[i]._data,Suffix):
            if i>0 :
                
                if isinstance(new_expr[i-1]._data,Dhaatu):
                    dhaatu_index=i-1
                    if 'anga_node' in sig_params :
                        new_expr[i].set_output(transformation_rule,anga_node=new_expr[dhaatu_index])           
                    if 'suffix_node' in sig_params :
                        new_expr[dhaatu_index].set_output(transformation_rule,suffix_node=new_expr[i])
                else:
                    if 'suffix_node' in sig_params :
                        #Can check as transformation_rule.__name__=="saarvadhaatukaardhadhaatukayoH_703084" etc.
                        new_expr[i-1].set_output(transformation_rule,suffix_node=new_expr[i])
                    if 'anga_node' in sig_params :
                        new_expr[i].set_output(transformation_rule,anga_node=new_expr[i-1])

                    
            if 'anga_node' not in sig_params  and 'suffix_node' not in sig_params :
                new_expr[i].set_output(transformation_rule)
                
            
                    
    return new_expr
            
            
    
def apply_dhaatu_lopa(dhaatu_node):
    if not isinstance(dhaatu_node,Node):
        raise ValueError("Need Node")

    if not isinstance(dhaatu_node._data,Dhaatu):
        raise ValueError("Need Dhaatu")
        
    MAX_TIMES=10000
    lopa_functions = [halantyam_1030030]
    
    for lopafunc in  lopa_functions :
        not_done=True
        while not_done:
            prev_output=dhaatu_node.get_output()
            dhaatu_node.set_output(lopafunc)
            if dhaatu_node.get_output() == prev_output:
                not_done=False
                
    return dhaatu_node
        
def apply_lopa(suffix_node):
    """
    Only tripaadii sutras need to be re-applied
    others can potentially be applied
    """
    
    if not isinstance(suffix_node,Node):
        raise ValueError("Need Node")

    if not isinstance(suffix_node._data,Suffix):
        raise ValueError("Need Suffix")
    MAX_TIMES=10000
    lopa_functions = [lashakvataddhite_1030080, aadirNciXtuXdavaH_1030050, \
                      halantyam_1030030, chuXtuu_103070,upadesheajanunaasikait_1030020 ]
    
    for lopafunc in  lopa_functions :
        not_done=True
        #print(lopafunc.__name__)
        while not_done:
            prev_output=suffix_node.get_output()
            suffix_node.set_output(lopafunc)
            if suffix_node.get_output() == prev_output:
                not_done=False
                
    return suffix_node
                    

    return new_expr


"""
For any two nodes A and B, insertion can happen in the middle, before A or after B. 
Prepend operation implies the insertion before A
"""
def is_prepend_applicable(prepend_rule,new_expr):
    for i in range(1,len(new_expr)):
        if isinstance(new_expr[i]._data,Suffix):
            sig_params = inspect.signature(prepend_rule.__call__).parameters
            if 'prefix_node' in sig_params :         
                if prepend_rule()(prefix_node=new_expr[i-1],suffix_node=new_expr[i]):
                    return True
                
                
    return False


"""
For any two nodes A and B, insertion can happen in the middle, before A or after B. 
Prepend operation implies the insertion before A
"""
def apply_prepend(prepend_rule,new_expr):
    #TODO: trace history of insertion by modifying the output of both sides of the insertion
    new_inserts=OrderedDict()
    for i in range(1,len(new_expr)):
        if isinstance(new_expr[i]._data,Suffix):
            # reducing expression with combination
            # this involves appending plain-strings (that cannot be reduced further)
            sig_params = inspect.signature(prepend_rule.__call__).parameters
            if 'prefix_node' in sig_params :         
                to_prepend = prepend_rule()(prefix_node=new_expr[i-1],suffix_node=new_expr[i])
                if to_prepend :
                    # prepending happens before the node
                    new_inserts[i-1]={'node_data':to_prepend ,'input_indices':(i-1,i),'rule':prepend_rule}
                
    for pos in reversed(new_inserts):
        dat=new_inserts[pos]
        new_node = Node(dat['node_data'],parent1=new_expr[dat['input_indices'][0]],parent2=new_expr[dat['input_indices'][1]])
        new_node._assign_output_properties(rule=dat['rule'])
        new_expr[pos]._assign_output_properties(rule=dat['rule'])
        
        new_expr.insert(pos,new_node)
    return new_expr



"""
For any two nodes A and B, check whether insertion can happen in the middle, before A or after B. 
"""
def is_insertion_applicable(insertion_rule, new_expr):

    for i in range(1,len(new_expr)):
        if isinstance(new_expr[i]._data,Suffix):
            # reducing expression with combination
            # this involves appending plain-strings (that cannot be reduced further)
            sig_params = inspect.signature(insertion_rule.__call__).parameters
            if 'prefix_node' in sig_params :
                if insertion_rule()(prefix_node=new_expr[i-1],suffix_node=new_expr[i]) :
                    return True

    return False



"""
For any two nodes A and B, insertion can happen in the middle, before A or after B. 
Insert operation implies the insertion between A and B
"""
def apply_insertion(insertion_rule, new_expr):

    new_inserts=OrderedDict()
    for i in range(1,len(new_expr)):
        if isinstance(new_expr[i]._data,Suffix):
            # reducing expression with combination
            # this involves appending plain-strings (that cannot be reduced further)
            sig_params = inspect.signature(insertion_rule.__call__).parameters
            if 'prefix_node' in sig_params :         
                to_insert = insertion_rule()(prefix_node=new_expr[i-1],suffix_node=new_expr[i])
                if to_insert :
                    new_inserts[i]={'node_data':to_insert ,'input_indices':(i-1,i),'rule':insertion_rule}

    for pos in reversed(new_inserts):
        
        dat=new_inserts[pos]
        new_node = Node(dat['node_data'],parent1=new_expr[dat['input_indices'][0]],parent2=new_expr[dat['input_indices'][1]])
        #assigning properties to both sides of the insertion
        new_node._assign_output_properties(rule=dat['rule'])
        #new_expr[pos]._assign_output_properties(rule=dat['rule'])
        
        new_expr.insert(pos,new_node)


    return new_expr

def apply_all_lopas(expression):
        
    suffix_indices= [ index for index,node in enumerate(expression) if isinstance(node._data,Suffix)]
    dhaatu_indices= [ index for index,node in enumerate(expression) if isinstance(node._data,Dhaatu)]
        
    # apply lopa to suffixes
    for suffix_index in suffix_indices:
       suffix_node  = expression[suffix_index]
       expression[suffix_index ] = apply_lopa(suffix_node)
    
    # apply lopa to dhaatus
    for dhaatu_index in dhaatu_indices:
       dhaatu_node  = expression[dhaatu_index ]
       expression[dhaatu_index ] = apply_dhaatu_lopa(dhaatu_node  )
       
    return expression


def apply_all_transformations(expression):
    all_sutras= get_sutras_ordered()
    for transformation_ruleid in transformation_sutras():        
       new_expression= apply_transformation(all_sutras[transformation_ruleid],expression)
    new_expression = apply_all_lopas(new_expression)
    return new_expression

def process_until_finish(expr):
    
    old_string = output_processed_string (expr)
    new_expr = process_list(expr)
    if output_processed_string (new_expr)==old_string:
        # the iterations have finished now apply padaanta rules
        all_sutras= get_sutras_ordered()
        for transformation_ruleid in padaanta_sutras():           
           new_expr = apply_transformation_at_end(all_sutras[transformation_ruleid],new_expr)
        return expr
    else:
        return process_until_finish(new_expr)
        
def process_list(expr):
    all_sutras= get_sutras_ordered()
    
    if any(not isinstance(entry,Node) for entry in expr):
        raise ValueError("Only nodes are to be present")
        
    new_expr = expr.copy()
    
    # the logic for applying it-lopa is that 
    # all suffixes are searched and then lopa-application is applied
    # the lopa changes the suffix's state


    # apply lopa and transformation before insertion
    new_expr = apply_all_lopas(new_expr)        
    
    # apply insertions
    
    itdf= pd.concat([pd.DataFrame({'sutranum':[x for x in transformation_sutras()],'type':'transformation'}), 
                     pd.DataFrame({'sutranum':[x for x in prepend_sutras()],'type':'prepend'}),
              pd.DataFrame({'sutranum':[x for x in insertion_sutras()],'type':'insertion'})
              
              ])
    itdf = itdf.sort_values('sutranum')
    
    # the sutra function do not change the expression itself therefore 
    # a dry-run on the rules filters out only the sutras that apply i.e. would cause a change
    # the application happens only in the order based on num-conditions, sutra-order
    
    listApplicableSutras=[]
    
    for sutra_i in range(0,itdf.shape[0]):
        objSutra = itdf.iloc[sutra_i]
        if objSutra.type == "insertion":
            if is_insertion_applicable (all_sutras[objSutra.sutranum],new_expr):
                listApplicableSutras.append(objSutra.sutranum)

        elif objSutra.type == "prepend":
            if is_prepend_applicable(all_sutras[objSutra.sutranum],new_expr):
                listApplicableSutras.append(objSutra.sutranum)

        elif objSutra.type == "transformation":
            if is_transformation_applicable(all_sutras[objSutra.sutranum],new_expr):
                listApplicableSutras.append(objSutra.sutranum)
        else:
            raise ValueError("Unkonwn type : %s" % objSutra.type)

    ## the sutras to be applied are in list
    
    for sutra_i in range(0,itdf.shape[0]):
        objSutra = itdf.iloc[sutra_i]
        if objSutra.type == "insertion":
            #old_string = output_processed_string(new_expr)
            insertion_sutra_id = objSutra.sutranum
            new_expr = apply_insertion(all_sutras[insertion_sutra_id],new_expr)
            # apply lopa and transformation after insertion       
            new_expr = apply_all_lopas(new_expr)

        elif objSutra.type == "prepend":
            prepend_sutra_id= objSutra.sutranum
            new_expr= apply_prepend(all_sutras[prepend_sutra_id],new_expr)        
            new_expr = apply_all_lopas(new_expr)

        elif objSutra.type == "transformation":
            transformation_ruleid=objSutra.sutranum
            new_expr = apply_transformation(all_sutras[transformation_ruleid],new_expr)
            new_expr = apply_all_lopas(new_expr)
        else:
            raise ValueError("Unkonwn type : %s" % objSutra.type)
    
    return new_expr

def output_string (expr):
    return ''.join(reduce(lambda x ,y : x + y.get_output(),  process_until_finish(expr), []))



def generate_tibaadi(dhaatu_string):
    
    res = {}
    las = ('tip','tas','jhi','sip','thas','tha','mip','vas','mas')
    
    lakaaras = ('liXt','lRiXt','laXt','luXt','luNg')
    for lakaara_string in lakaaras :
        
        res[lakaara_string ] = []
        for la in las:
            dhaatu_node = Node(Dhaatu(parse_string(dhaatu_string)),parent1=None)
            result = output_string ([dhaatu_node, Node(Suffix(la,lakaara=lakaara_string),parent1=None)])
            res[lakaara_string ].append(result)
    return res
    

def generate_subaadi(sup_expression,linga):
    if not isinstance(sup_expression,list):
        raise ValueError("sup_expression must be a list of Nodes")
    if any (not isinstance(x,Node) for x in sup_expression):
        raise ValueError("sup_expression must be a list of Nodes")
    res = []
    sups = ('sNN','au','jas','am','auXt','shas', 'Xtaa','bhyaam','bhis',
            'Nge','bhyaam','bhyas','Ngasi','bhyaam','bhyas',
            'Ngas','os','am','Ngi','os','sup')
    

    for sup_string in sups :
        cur_sup_expression=deepcopy(sup_expression)
        cur_sup_expression.append(Node(Suffix(sup_string,linga=linga),parent1=None))        
        
        result = output_string (cur_sup_expression)
        #print(sup_string + " gives " +result )
        #print(result)
        res.append(result)
    return res

