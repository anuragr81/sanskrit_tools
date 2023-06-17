
import json

from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string

from generate_path import *

from panini.devanagari.convert import parse_devanagari_to_ascii

from pprint import pprint

def get_expression_tree(expression):
    return json.dumps([ ''.join(parse_devanagari_to_ascii(x)) for x in expression.split(",")])
