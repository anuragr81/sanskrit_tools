
import json
from functools import reduce

from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string,hal
from panini.dhaatus import dhaatus_list 

from generate_path import *

from panini.devanagari.convert import parse_devanagari_to_ascii, convert_to_devanagari

from pprint import pprint
output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))

"""
Node structure contains additional information such as the lakaara as well. lakaara can be selected after
a tibaadi suffix is selected. subaadi can also be simplified in this manner.
"""
def prepare_node_structure(arr):
    all_dhaatus = dhaatus_list ()
    tibaadi_suffixes = ('tip','tas','jhi','sip','thas','tha','mip','vas','mas','ta','aataam','jha','thaa','sa','aathaam','dhvam','iXt','vahi','mahiNg',)
    ep=[]
    if len(arr)>1:
       if arr[0] in  all_dhaatus:
           dhaatu_name = arr[0] + "NN" if arr[0][-1] in hal() else arr[0]
           ep.append(Node(Dhaatu(parse_string(dhaatu_name)),parent1=None))
           for x in arr[1:]:
               if x in tibaadi_suffixes:
                   #TODO: consider inputs other than laXt
                   ep.append(Node(Suffix(x,lakaara='laXt'),parent1=None))
               else:
                   ep.append(Node(Suffix(x),parent1=None))
           return ep

    return []


def get_vertices_edges(nodes):
    edges = []
    edgenames = {}
    for node in nodes:
        for i in range(len(node._output)):
            if i>0:
                rule_name = node._output[i]['rule'].__name__.split("_")[0]
                edge_source = convert_to_devanagari(''.join(node._output[i-1]['output']))

                if rule_name in edgenames : 
                    # change rule_name 
                    rule_name_wcount = convert_to_devanagari(rule_name) + str(edgenames[ rule_name ]['count'])
                    edgenames[rule_name]['count'] = edgenames[rule_name]['count'] + 1
                else:
                    edgenames[rule_name]={}
                    edgenames[rule_name]['count'] = 1
                    rule_name_wcount = convert_to_devanagari(rule_name) + str(edgenames[ rule_name ]['count'])
                    edgenames[rule_name]['count'] = edgenames[rule_name]['count'] + 1


                if not edge_source:
                    edge_source = "empty"+str(edgenames[rule_name]['count'])

                edge_target = convert_to_devanagari(''.join(node._output[i]['output']))
                # reusing the edgename count 
                if not edge_target:
                    edge_target= "empty"+str(edgenames[rule_name]['count'])

                edges.append({'id':rule_name_wcount, 'target':edge_target, 'source':edge_source})

    # add final output and related vertices
    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    finaloutput = convert_to_devanagari(output_processed_string (nodes))
    #TODO: prepare vertices from edge data to make sure that vertex renames are assimilated

    listVertices = reduce(lambda x,y : x + y , [[''.join(x['output']) for x in node._output] for node in nodes])
    vertices = list(convert_to_devanagari(x) for x  in set(listVertices))
    vertices.append(finaloutput)

    for i,node in enumerate(nodes):
        rule_name = str(i+1)
        edge_source = convert_to_devanagari(''.join(node.get_output()))
        edge_target = finaloutput
        edges.append({'id':rule_name, 'target':edge_target, 'source':edge_source})
        


    return {'vertices':vertices,'edges':edges}

"""
  returns the expression in form of a cytoscape graph
"""
def get_expression_tree(expression):
    arrInp=[ ''.join(parse_devanagari_to_ascii(x)) for x in expression.split(",")]

    ep = prepare_node_structure(arrInp)
    pe=process_until_finish(ep)
    return json.dumps(get_vertices_edges(pe))

