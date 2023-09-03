
import json
from functools import reduce

from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string,hal
from panini.dhaatus import  dhaatus_halant_to_upadesha
from generate_path import *

from panini.devanagari.convert import parse_devanagari_to_ascii, convert_to_devanagari

from pprint import pprint
output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))


halant_to_upadesha_map =  dhaatus_halant_to_upadesha()

"""
Node structure contains additional information such as the lakaara as well. lakaara can be selected after
a tibaadi suffix is selected. subaadi can also be simplified in this manner.
"""
def prepare_node_structure(arr):
    global halant_to_upadesha_map
    all_dhaatu_names = list(halant_to_upadesha_map.keys())
    tibaadi_suffixes = ('tip','tas','jhi','sip','thas','tha','mip','vas','mas','ta','aataam','jha','thaa','sa','aathaam','dhvam','iXt','vahi','mahiNg',)
    ep=[]
    if len(arr)>1:
        if arr[0] not in all_dhaatu_names :
            raise ValueError("Dhaatu named %s is not in global store" % arr[0])
        else:
            dhaatu_name = halant_to_upadesha_map[arr[0]]
        ep.append(Node(Dhaatu(parse_string(dhaatu_name)),parent1=None))
        for x in arr[1:]:
            if x in tibaadi_suffixes:
                #TODO: consider inputs other than laXt
                ep.append(Node(Suffix(x,lakaara='laXt'),parent1=None))
            else:
                ep.append(Node(Suffix(x),parent1=None))
        return ep

    return []


def get_vertices_edges(nodes,devanagari=True):
    edges = []
    edgenames = {}
    convert = lambda x : convert_to_devanagari(x) if devanagari else x
    get_second_or_first_parent = lambda node : node._parent2 if node._parent2 else node._parent1
    empty_prefix = "empty" if not devanagari else "रिक्त"

    for k,node in enumerate(nodes):
        for i in range(len(node._output)):
            if i>0:
                rule_name = convert(node._output[i]['rule'].__name__.split("_")[0])
                edge_source = convert(''.join(node._output[i-1]['output']))

                if rule_name in edgenames :
                    # change rule_name
                    rule_name_wcount = (rule_name) + str(edgenames[ rule_name ]['count'])
                    edgenames[rule_name]['count'] = edgenames[rule_name]['count'] + 1
                else:
                    edgenames[rule_name]={}
                    edgenames[rule_name]['count'] = 1
                    rule_name_wcount = (rule_name) + str(edgenames[ rule_name ]['count'])
                    edgenames[rule_name]['count'] = edgenames[rule_name]['count'] + 1


                if not edge_source or edge_source=="":
                    edge_source = empty_prefix+str(k)+"_"+str(i)

                edge_target = convert(''.join(node._output[i]['output']))
                # reusing the edgename count
                if not edge_target or edge_target=="":
                    edge_target= empty_prefix +str(k)+"_"+str(i)
                if edge_source == edge_target and 'new' in node._output[i-1] and ( node._parent1  or node._parent2)  :
                    edge_source = convert( ''.join(get_second_or_first_parent(node)._output[0]['output']))

                edges.append({'id':rule_name_wcount, 'target':edge_target, 'source':edge_source})

    # add final output and related vertices
    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    finaloutput = convert(output_processed_string (nodes))

    for i,node in enumerate(nodes):
        rule_name = str(i+1)
        edge_source = convert(''.join(node.get_output())) if node.get_output() else empty_prefix +str(i)+"_"+str(len(node._output)-1)
        edge_target = finaloutput
        edges.append({'id':rule_name, 'target':edge_target, 'source':edge_source})

    vertices = list(set(e['source'] for e in edges).union(set(e['target'] for e in edges)))
    vertices.append(finaloutput)



    return {'vertices':vertices,'edges':edges}

"""
  returns the expression in form of a cytoscape graph
"""
def get_expression_tree(expression):
    arrInp=[ ''.join(parse_devanagari_to_ascii(x)) for x in expression.split(",")]

    ep = prepare_node_structure(arrInp)
    pe=process_until_finish(ep)
    return json.dumps(get_vertices_edges(pe))

