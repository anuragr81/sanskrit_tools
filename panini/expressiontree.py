
import json

from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string
from panini.dhaatus import dhaatus_meaning

from generate_path import *

from panini.devanagari.convert import parse_devanagari_to_ascii

from pprint import pprint

"""
Node structure contains additional information such as the lakaara as well. lakaara can be selected after
a tibaadi suffix is selected. subaadi can also be simplified in this manner.
"""
def prepare_node_structure(arr):
    all_dhaatus = [ ''.join(dhaatus_meaning()[k]['ascii']) for k in dhaatus_meaning().keys()]
    tibaadi_suffixes = ('tip','tas','jhi','sip','thas','tha','mip','vas','mas','ta','aataam','jha','thaa','sa','aathaam','dhvam','iXt','vahi','mahiNg',)
    ep=[]
    if len(arr)>1:
       if arr[0] in  all_dhaatus:
           ep.append(Node(Dhaatu(parse_string(arr[0])),parent1=None))
           for x in arr[1:]:
               if x in tibaadi_suffixes:
                   #TODO: consider inputs other than laXt
                   ep.append(Node(Suffix(x,lakaara='laXt'),parent1=None))
           return ep

    return []


"""
  returns the expression in form of a cytoscape graph
"""
def get_expression_tree(expression):
    arrInp=[ ''.join(parse_devanagari_to_ascii(x)) for x in expression.split(",")]

    ep = prepare_node_structure(arrInp)

    return json.dumps(arrInp)
