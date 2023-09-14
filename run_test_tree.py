from pprint import pprint

import sys
sys.path.append('/home/anuragr/research_persona/sanskrit_tools')
from generate_path import *
from panini.expressiontree import prepare_node_structure,get_vertices_edges
#ep = prepare_node_structure(['bhaj','ghaNc','am']) 
#ep = prepare_node_structure(['chiNc','tip'])
ep = prepare_node_structure(['paXth','tip'])
#print(ep)
pe=process_until_finish(ep)
print("ep is of length=%d " % len(ep))
print("pe is of length=%d " % len(pe))

#1print(''.join(x._output[-1]['output'] for x  in pe))
pprint(get_vertices_edges(pe,devanagari=True))

