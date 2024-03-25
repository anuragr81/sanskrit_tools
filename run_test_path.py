from generate_path import *
from generate_path import output_string
from panini.sutras.common_definitions import Dhaatu,Node,Suffix, parse_string,print_expr
from pprint import pprint

# TODO: use https://everythingfonts.com/unicode/devanagari to output devanagari

F=False
T=True

def test_siddhis ():
    
    assert output_string ([Node(Dhaatu(parse_string("NniiNN")),parent1=None),Node(Suffix("Nnvul"),parent1=None)]) == "naayaka"
    
    assert output_string ([Node(Dhaatu(parse_string("bhajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]) == "bhaaga"
    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == "bhavati"
    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='laXt'),parent1=None)]) == "bhavatas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='laXt'),parent1=None)]) == "bhavaami"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)] ) == "achaiXshiit"
    
    ############################# tibaadi for paXthNN #################################
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == "paXthati"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='laXt'),parent1=None)]) == "paXthatas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='laXt'),parent1=None)]) == "paXthanti"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='laXt'),parent1=None)]) == "paXthasi"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='laXt'),parent1=None)]) == "paXthathas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='laXt'),parent1=None)]) == "paXthatha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='laXt'),parent1=None)]) == "paXthaami"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='laXt'),parent1=None)]) == "paXthaavas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='laXt'),parent1=None)]) == "paXthaamas"
    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyati"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyatas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyanti"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyasi"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyathas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyatha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyaami"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyaavas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='lRiXt'),parent1=None)]) == "paXthiXshyaamas"
    
    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='laNg'),parent1=None)]) == "apaXthat"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='laNg'),parent1=None)]) == "apaXthataam"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='laNg'),parent1=None)]) == "apaXthan"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='laNg'),parent1=None)]) == "apaXthas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='laNg'),parent1=None)]) == "apaXthatam"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='laNg'),parent1=None)]) == "apaXthata"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='laNg'),parent1=None)]) == "apaXtham"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='laNg'),parent1=None)]) == "apaXthaava"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='laNg'),parent1=None)]) == "apaXthaama"
    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='liXt'),parent1=None)]) == "papaaXtha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='liXt'),parent1=None)]) == "peXthatus"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='liXt'),parent1=None)]) == "peXthus"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='liXt'),parent1=None)]) == "peXthathus"    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='liXt'),parent1=None)]) == "peXtha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='liXt'),parent1=None)]) == "papaaXtha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='liXt'),parent1=None)]) == "peXthiva"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='liXt'),parent1=None)]) == "peXthima"

    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='luXt'),parent1=None)]) == "paXthitaarau"    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='luXt'),parent1=None)]) == "paXthitaaras"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='luXt'),parent1=None)]) == "paXthitaasi"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='luXt'),parent1=None)]) == "paXthitaasthas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='luXt'),parent1=None)]) == "paXthitaastha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='luXt'),parent1=None)]) == "paXthitaasmi"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='luXt'),parent1=None)]) == "paXthitaasvas"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='luXt'),parent1=None)]) == "paXthitaasmas"

    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='loXt'),parent1=None)]) == "paXthatu"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='loXt'),parent1=None)]) == "paXthataam"    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='loXt'),parent1=None)]) == "paXthantu"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='loXt'),parent1=None)]) == "paXtha"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='loXt'),parent1=None)]) == "paXthatam"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='loXt'),parent1=None)]) == "paXthata"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='loXt'),parent1=None)]) == "paXthaani"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='loXt'),parent1=None)]) == "paXthaava"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='loXt'),parent1=None)]) == "paXthaama"    
    
    
    
    if False:
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='liNg1'),parent1=None)]) == "paXthet"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='liNg1'),parent1=None)]) == "paXthetaam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='liNg1'),parent1=None)]) == "paXtheyus"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='liNg1'),parent1=None)]) == "paXthes"    
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='liNg1'),parent1=None)]) == "paXthetam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='liNg1'),parent1=None)]) == "paXtheta"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='liNg1'),parent1=None)]) == "paXtheyam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='liNg1'),parent1=None)]) == "paXtheva"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='liNg1'),parent1=None)]) == "paXthema"
    
    
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='liNg2'),parent1=None)]) == "paXthyaat"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tas",lakaara='liNg2'),parent1=None)]) == "paXthyaastaam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("jhi",lakaara='liNg2'),parent1=None)]) == "paXthyaasus"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='liNg2'),parent1=None)]) == "paXthyaas"    
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("thas",lakaara='liNg2'),parent1=None)]) == "paXthyaastam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tha",lakaara='liNg2'),parent1=None)]) == "paXthyaasta"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='liNg2'),parent1=None)]) == "paXthyaasam"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='liNg2'),parent1=None)]) == "paXthyaasva"
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='liNg2'),parent1=None)]) == "paXthyaasma"
        
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("sip",lakaara='liXt'),parent1=None)]) == "peXthitha"
     
    #####################################################################################
    
    
    # liNg is aardhadhaatuk in aashir-liNg
    print("Tests Done")

#raise ValueError("Fix alaaviit - The lopa of s needs to be implemented in iXt iiXti")
#raise ValueError("Fix path+jhi(luXt)")

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
        expression=[Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix('jhi',lakaara='laXt'),parent1=None)]
        #expression=[Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix('ghaNc'),parent1=None),Node(Suffix('sNN'),parent1=None)]
        #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix('tip',lakaara="luNg"),parent1=None)]
        #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix('tip'),parent1=None)]
        #raise ValueError("tasthamipaaMtaaMtamTaamaH cannot be applied on mip - it needs to be verified how this is a nitya-apavaada scenario")
        #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)]
        
        #expression=[Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None),Node(Suffix("am",linga=1),parent1=None)]
        
        #expression=[Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]
            
    # sorting order is increasing in general but can be superseded by nitya condition (if nitya occurs in a later sutra then that later sutra takes advantage) 
    # which in turn would be superseded by the minimal condition criteria (antaraNga) 
    # The only exception is when there is a an exception that prevents application
    
    print("NEXT: luNglaNglRiNgkXshvaXdudaataH has prepending issue because we don't trace insertion/prepending of vikaraNna histories. This should allow the immediate dhaatu in context.")
    # for paXtheta - we need to have for liNg : yaasuXtparasmaipadeXshuudaatto Ngichcha 3.4.103 and then ato yeyaH (because of a-ending paXtha after shap)
    
    pe=process_until_finish(expression)

    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    print(output_processed_string (pe))
    
    if F:
        print("===")
        pprint(pe[2]._output)
    
    print("DONE")   