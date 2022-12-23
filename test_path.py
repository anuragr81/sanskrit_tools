from generate_path import *
from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string
from pprint import pprint

F=False
T=True

if F:
    test_siddhis ()
    #print("Test")
    #f=Functor()
    #f(2)
    
else:   
    
    #pprint(generate_tibaadi("paXthNN"))   ;sys.exit(0)
    if T:
        sup_expr = [Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]
        pprint(generate_subaadi(sup_expr ,linga=1))   ;
        sys.exit(0)
    
    else:
        #Xtaa
        #
        #expression=[Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]
        expression=[Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None),Node(Suffix("am",linga=1),parent1=None)]
        #expression=[Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='liXt'),parent1=None)]
    
    
    # sorting order is increasing in general but can be superseded by nitya condition (if nitya occurs in a later sutra then that later sutra takes advantage) 
    # which in turn would be superseded by the minimal condition criteria (antaraNga) 
    # The only exception is when there is a an exception that prevents application
    
    print("NEXT: luNglaNglRiNgkXshvaXdudaataH has prepending issue because we don't trace insertion/prepending of vikaraNna histories. This should allow the immediate dhaatu in context.")
    # for paXtheta - we need to have for liNg : yaasuXtparasmaipadeXshuudaatto Ngichcha 3.4.103 and then ato yeyaH (because of a-ending paXtha after shap)
    print("PENDING :rename of anga_node to nonsuffix_node, https://ashtadhyayi.com/sutraani/6/4/120, ,eruH ")
    
    
    
    processed_expr=(process_until_finish(expression))

    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    print(output_processed_string (processed_expr))
    print("DONE")
    if F:
        print("===")
        pprint(processed_expr[0]._output)
        print("===")
        pprint(processed_expr[1]._output)
        
        
        print("===")
        pprint(processed_expr[2]._output)
