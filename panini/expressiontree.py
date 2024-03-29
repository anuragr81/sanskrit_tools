
import json
from functools import reduce

from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string, lakaaras, tiNg_pratyayaaH
from panini.dhaatus import  dhaatus_halant_to_upadesha
from generate_path import process_until_finish

from panini.devanagari.convert import parse_devanagari_to_ascii, convert_to_devanagari

output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))


halant_to_upadesha_map =  dict( (k,''.join(parse_devanagari_to_ascii(v))) for k,v in dhaatus_halant_to_upadesha().items())

"""
Function to return Tree based on ASCII list of node-names where the first Node is assumed to be that of a Dhaatu - also
uses the types passed on by the user. The goal is to translate the user-string into application expression format.
Input: ASCII itemslist, Typelist
Output: Node structure contains additional information such as the lakaara as well. lakaara can be selected after
a tibaadi suffix is selected.
"""
def prepare_node_structure(itemslist,typeslist):
    if len(itemslist)!=len(typeslist):
        raise ValueError("Invalid input: lengths of itemslist and typeslist do not match")

    if len(itemslist)<=1:
        return itemslist

    global halant_to_upadesha_map
    all_dhaatu_names = list(halant_to_upadesha_map.keys())


    ep=[]
    curpos = len(itemslist)-1
    # parsing backwards
    while curpos >= 0 :
        if curpos == 0:
            if itemslist[0] not in all_dhaatu_names :
                raise ValueError("Dhaatu named %s is not in global store" % itemslist[0])
            else:
                dhaatu_name = halant_to_upadesha_map[itemslist[0]]

            ep.insert(0,Node(Dhaatu(parse_string(dhaatu_name)),parent1=None))

        else:
            # if a lakaara is found, then ensure that the item before it is a tiNG
            # and move backwards an extra step
            if itemslist[curpos] in lakaaras():
                if curpos <=1 or itemslist[curpos-1] not in tiNg_pratyayaaH():
                    raise ValueError("Invalid Input: %s must  be a tiNg suffix:" % itemslist[curpos-1])
                else:
                    ep.insert(0,Node(Suffix(itemslist[curpos-1],lakaara=itemslist[curpos]),parent1=None))
                    curpos=curpos-1
            else:
                ep.insert(0,Node(Suffix(itemslist[curpos]),parent1=None))
        # move to next position
        curpos = curpos - 1
    return ep




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
def get_expression_tree(expression,typelist):

    arrInp=[ ''.join(parse_devanagari_to_ascii(x)) for x in expression.split(",")]
    typelist=typelist.split(",")

    ep = prepare_node_structure(arrInp,typelist)
    pe=process_until_finish(ep)
    return json.dumps(get_vertices_edges(pe))

