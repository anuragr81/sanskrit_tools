from generate_path import *
from generate_path import output_string
from panini.sutras.common_definitions import Dhaatu,Node,Suffix, Praatipadika, parse_string,print_expr
from panini.sutras.common_definitions import get_suffix_for_context
from pprint import pprint

# TODO: use https://everythingfonts.com/unicode/devanagari to output devanagari

F=False
T=True


def test_subaadi():
    
    
    if False:
        sup_expr = [Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]
        pprint(generate_subaadi(sup_expr ,linga=1))   ;
        
    else:
        sup_expr = [Node(Dhaatu(parse_string("ramNN")),parent1=None),Node(Suffix("Nnich"),parent1=None),Node(Suffix("ach"),parent1=None)]
        #sup_expr = [Node(Dhaatu(parse_string("vRishNN")),parent1=None),Node(Suffix("ach"),parent1=None),Node(Suffix("Xtaap"),parent1=None) ]
        
        expression = sup_expr  + [Node(Suffix('sup',linga=1),parent1=None) ]
        pe=process_until_finish(expression)
        output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
        print(output_processed_string (pe))
        if F:
            print("===")
            for k in (pe[0]._output):
                pprint(k)
        
        print("DONE")   
        
    
def test_tibaadi():
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
    if True:
        print("Skipping paXthaani")
    else:
        assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mip",lakaara='loXt'),parent1=None)]) == "paXthaani"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("vas",lakaara='loXt'),parent1=None)]) == "paXthaava"
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("mas",lakaara='loXt'),parent1=None)]) == "paXthaama"    
    
    
    ############################# tibaadi for bhuu #################################
    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == "bhavati"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='laXt'),parent1=None)]) == "bhavatas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='laXt'),parent1=None)]) == "bhavanti"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='laXt'),parent1=None)]) == "bhavasi"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='laXt'),parent1=None)]) == "bhavathas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='laXt'),parent1=None)]) == "bhavatha"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='laXt'),parent1=None)]) == "bhavaami"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='laXt'),parent1=None)]) == "bhavaavas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='laXt'),parent1=None)]) == "bhavaamas"
    

    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyati"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyatas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyanti"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyasi"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyathas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyatha"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyaami"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyaavas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='lRiXt'),parent1=None)]) == "bhaviXshyaamas"    
    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='laNg'),parent1=None)]) == "abhavat"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='laNg'),parent1=None)]) == "abhavataam"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='laNg'),parent1=None)]) == "abhavan"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='laNg'),parent1=None)]) == "abhavas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='laNg'),parent1=None)]) == "abhavatam"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='laNg'),parent1=None)]) == "abhavata"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='laNg'),parent1=None)]) == "abhavam"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='laNg'),parent1=None)]) == "abhavaava"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='laNg'),parent1=None)]) == "abhavaama"    

    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='liXt'),parent1=None)]) == "babhuuva"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='liXt'),parent1=None)]) == "babhuuvatus"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='liXt'),parent1=None)]) == "babhuuvus"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='liXt'),parent1=None)]) == "babhuuvitha"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='liXt'),parent1=None)]) == "babhuuvathus"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='liXt'),parent1=None)]) == "babhuuva"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='liXt'),parent1=None)]) == "babhuuva"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='liXt'),parent1=None)]) == "babhuuviva"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='liXt'),parent1=None)]) == "babhuuvima"

    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "bhavitaa"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='luXt'),parent1=None)]) == "bhavitaarau"    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='luXt'),parent1=None)]) == "bhavitaaras"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='luXt'),parent1=None)]) == "bhavitaasi"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='luXt'),parent1=None)]) == "bhavitaasthas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='luXt'),parent1=None)]) == "bhavitaastha"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='luXt'),parent1=None)]) == "bhavitaasmi"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='luXt'),parent1=None)]) == "bhavitaasvas"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='luXt'),parent1=None)]) == "bhavitaasmas"

    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tip",lakaara='loXt'),parent1=None)]) == "bhavatu"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tas",lakaara='loXt'),parent1=None)]) == "bhavataam"    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("jhi",lakaara='loXt'),parent1=None)]) == "bhavantu"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("sip",lakaara='loXt'),parent1=None)]) == "bhava"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("thas",lakaara='loXt'),parent1=None)]) == "bhavatam"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("tha",lakaara='loXt'),parent1=None)]) == "bhavata"
    if True:
        print("Skipping bhavaani")
    else:
        assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='loXt'),parent1=None)]) == "bhavaani"
    
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("vas",lakaara='loXt'),parent1=None)]) == "bhavaava"
    assert output_string ([Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mas",lakaara='loXt'),parent1=None)]) == "bhavaama"    


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
    


def test_siddhis ():
    disabled_tests=True
    
    assert output_string ([Node(Dhaatu(parse_string("NniiNN")),parent1=None),Node(Suffix("Nnvul"),parent1=None)]) == "naayaka"
    assert output_string ([Node(Dhaatu(parse_string("XdukRiNc")),parent1=None),Node(Suffix("Nnvul"),parent1=None)]) == 'kaaraka'
    assert output_string ([Node(Dhaatu(parse_string("bhajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]) == "bhaaga"
    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)] ) == "achaiXshiit"
    assert output_string ([Node(Dhaatu(parse_string("XdukRiNc")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)]) == "akaarXshiit"
    assert output_string ([Node(Dhaatu(parse_string("luuNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)]) == "alaaviit"
    assert output_string ([Node(Praatipadika("shaalaa",1),parent1=None), Node(Suffix("chha"),parent1=None),Node(Suffix("sNN"),parent1=None)] ) == "shaaliiyas"
    
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tRich"),parent1=None),Node(Suffix("sNN"),parent1=None)])=='chetaa'
    #assert output_string ([Node(Dhaatu(parse_string("ji")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)])=='jayati'
    assert output_string ([Node(Dhaatu(parse_string("XdupachaXsh")),parent1=None),Node(Suffix("jhi",lakaara='laXt'),parent1=None)])=='pachanti'
    assert output_string ([Node(Dhaatu(parse_string("XdupachaXsh")),parent1=None),Node(Suffix("iXt",lakaara='laXt'),parent1=None)])=='pache'
    
    assert output_string ([Node(Dhaatu(parse_string("NcimidNN")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)])=='medyati' 
    
    assert output_string ([Node(Dhaatu(parse_string("mRijNN")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == 'maarXshXti'
    
    assert output_string ([Node(Dhaatu(parse_string("mRijNN")),parent1=None),Node(Suffix('yaNg'),parent1=None),Node(Suffix('sNN'),parent1=None)]) == 'mariimRijas'
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("kta"),parent1=None),Node(Suffix('sNN'),parent1=None)]) == 'chitas'
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("ktavatu"),parent1=None),Node(Suffix('sNN'),parent1=None)]) == 'chitavaan'
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tas",lakaara='laXt'),parent1=None)]) == 'chinutas'
    assert output_string([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("jhi",lakaara='laXt'),parent1=None)]) == 'chinvanti'
    assert output_string([Node(Dhaatu(parse_string("diidhiiNN")),parent1=None),Node(Suffix("lyuXt"),parent1=None),Node(Suffix("sNN"),parent1=None)]) == 'diidhyanas'
    assert output_string([Node(Dhaatu(parse_string("diidhiiNN")),parent1=None),Node(Suffix("Nnvul"),parent1=None),Node(Suffix("sNN"),parent1=None)]) == 'diidhyakas'
    assert output_string([Node(Dhaatu(parse_string("paXthaNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    assert output_string([Node(Praatipadika(parse_string("go"),linga=0),parent1=None),Node(Suffix("matNNp"),parent1=None),Node(Suffix("sNN"),parent1=None)]) == 'gomaan'
    assert output_string([Node(Dhaatu(parse_string("XdudaaNc")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)])=='dadaati'
    assert output_string([Node(Dhaatu(parse_string("XdudaaNc")),parent1=None),Node(Suffix("ta",lakaara='laXt',mood='karma'),parent1=None)]) == 'diiyate'
    assert output_string([Node(Dhaatu(parse_string("daaNN")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == 'yachchhati'
    assert output_string([Node(Dhaatu(parse_string("doNN")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]) == 'dyati'
    assert output_string([Node(Dhaatu(parse_string("XdudaaNc")),parent1=None),Node(Suffix("sip",lakaara='loXt'),parent1=None)]) == 'dehi'
    assert output_string([Node(Praatipadika("idam",1),parent1=None), Node(Suffix("bhyaam"),parent1=None)]) == 'aabhyaam'
    
    #test_tibaadi()
    if not disabled_tests:
        assert output_string ([Node(Dhaatu(parse_string("luuNN")),parent1=None),Node(Suffix('yaNg'),parent1=None),Node(Suffix('sNN'),parent1=None)]) == 'loluvas'

    
    print("Tests Done")


def test_expmt():
    pending= True
    
    # pending questions
    # 1. aupagavaH
    # 2. is mRijuuXsh in pachaadi? If not, how nandigrahipachaadibhyolyuNninyachaH apply to it?
    # 3. why is saarvadhaatukaardhaatukayoH not applied in saadhuH or jiXshnu or agnau (why doesn't it become saadhoH, jiXshnoH, agne with sNN)?
    # 4. Are iNno yaNn and oH supi both needed for jayati and bhavati - as exceptions of achishnudhaatubhruvaaMyvoriyaNguvaNgau_6040770 so that ji + tip does not become jiyati (rather than jayati through guNna) or bhuu + tip does not become bhuvati ( instead of bhavati through guNna) ?
    # 5. Why isn't vRiddhi not given to i of Ngi in vipaash+Ngi+aNn.
    # 6. why isn't iko yaNnachi applied to bhu + ati and loluu + as - letting them become bhvati and lolvas
    # 7. are there tip possibilities for karma or bhaava? More generally, is this worth supporting?
    # 8. Since lashakvataddhite doesn't handle Ngiip (which is taddhita), what sutra gets rid of Ng in Ngiip?
    # 9. Why isn't yasyeti cha applied after aa sarvanaamnaH - so that t + aa + vat becomes tvat?
    
    
    
    if not pending:
        expression1=[Node(Praatipadika("upagu",1),parent1=None),
                    Node(Suffix("aNn"),parent1=None),Node(Suffix("sNN"),parent1=None)]
        expression2 = [Node(Dhaatu(parse_string("ji")),parent1=None),Node(Suffix("tip",lakaara='laXt'),parent1=None)]
        expression3 = [Node(Praatipadika(parse_string("vipaash"),linga=0),parent1=None),Node(Suffix("Ngi"),parent1=None),Node(Suffix("aNn"),parent1=None),Node(Suffix("sNN"),parent1=None)]
        expression4 = [Node(Praatipadika("kumaar",1),parent1=None), Node(Suffix("Ngiip"),parent1=None), Node(Suffix("tarap"),parent1=None),Node(Suffix("Xtaap"),parent1=None),Node(Suffix("sNN"),parent1=None)] 
        expression5 = [Node(Praatipadika("tad",1),parent1=None), Node(Suffix("vatNNp"),parent1=None), ] 
        
    else:
        #expression = [Node(Dhaatu(parse_string("diidhiiNN")),parent1=None),Node(Suffix("Nnvul"),parent1=None),Node(Suffix("sNN"),parent1=None)]
        #expression = [Node(Praatipadika(parse_string("agni"),linga=0),parent1=None),Node(Suffix("auXt"),parent1=None)]
        expression = [Node(Praatipadika("kim",1),parent1=None), Node(Suffix("Xdati"),parent1=None), ] 
    # for paXtheta - we need to have for liNg : yaasuXtparasmaipadeXshuudaatto Ngichcha 3.4.103 and then ato yeyaH (because of a-ending paXtha after shap)

    pe=process_until_finish(expression)

    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    print ("=====")
    print(output_processed_string (pe))
    print ("=====")
    print(pe[0]._output)
    print("DONE")
    
if F:
    test_siddhis ()
else:   
    test_expmt()
    #test_subaadi()
