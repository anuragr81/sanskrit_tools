from generate_path import *
from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string
from pprint import pprint

# TODO: use https://everythingfonts.com/unicode/devanagari to output devanagari

F=False
T=True

def test_siddhis ():
    
    
    assert output_string ([Node(Dhaatu(parse_string("bhajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]) == "bhaaga"
    assert output_string ([Node(Dhaatu(parse_string("NniiNN")),parent1=None),Node(Suffix("Nnvul"),parent1=None)]) == "naayaka"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == "bhavati"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='laXt'),parent1=None)]) == "bhavatas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='laXt'),parent1=None)]) == "bhavaami"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)] ) == "achaiXshiit"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyati"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='liXt'),parent1=None)]) == "papaaXtha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='liXt'),parent1=None)]) == "peXthatus"
    # liNg is aardhadhaatuk in aashir-liNg
    print("Tests Done")



if F:
    test_siddhis ()
    #print("Test")
    #f=Functor()
    #f(2)
    
else:   
    
    #pprint(generate_tibaadi("paXthNN"))   ;sys.exit(0)
    if F:
        #sup_expr = [Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]
        pprint(generate_subaadi(sup_expr ,linga=1))   ;
        #pprint(generate_tibaadi("paXthNN"))   ;
        sys.exit(0)
    
    else:
        #Xtaa
        #
        #expression=[Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]
        print("na vibhaktau tusmaaH needs to be implemented to prevent chuXtuu on Xthal")
        expression=[Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix('sip',lakaara='liXt'),parent1=None)]
        
        #expression=[Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None),Node(Suffix("am",linga=1),parent1=None)]
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
