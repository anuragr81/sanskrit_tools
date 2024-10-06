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
    
    assert output_string ([Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix("tip",lakaara='luXt'),parent1=None)]) == "paXthitaa"
    
    assert output_string ([Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)] ) == "achaiXshiit"
    
    test_tibaadi()
    
    print("Tests Done")


def test_subaadi():
    sup_expr = [Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None)]
    
    if True:
        pprint(generate_subaadi(sup_expr ,linga=1))   ;
        
    else:
        expression = sup_expr  + [Node(Suffix('sup',linga=1),parent1=None) ]
        pe=process_until_finish(expression)
        output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
        print(output_processed_string (pe))
        if F:
            print("===")
            pprint(pe[2]._output)
        
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
    

def test_expmt():
    #pprint(generate_tibaadi("paXthNN"))   ;sys.exit(0)
 
    #expression=[Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix('mip',lakaara='loXt'),parent1=None)]
    #expression=[Node(Dhaatu(parse_string("paXthNN")),parent1=None),Node(Suffix('ghaNc'),parent1=None),Node(Suffix('sNN'),parent1=None)]
    #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix('tip',lakaara="luNg"),parent1=None)]
    #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix('tip'),parent1=None)]
    #raise ValueError("tasthamipaaMtaaMtamTaamaH cannot be applied on mip - it needs to be verified how this is a nitya-apavaada scenario")
    #expression=[Node(Dhaatu(parse_string("chiNN")),parent1=None),Node(Suffix("tip",lakaara='luNg'),parent1=None)]
    
    #expression=[Node(Dhaatu(parse_string("rajNN")),parent1=None),Node(Suffix("ghaNc"),parent1=None),Node(Suffix("am",linga=1),parent1=None)]
    
    expression=[Node(Dhaatu(parse_string("bhuu")),parent1=None),Node(Suffix("mip",lakaara='loXt'),parent1=None)]
        
    # sorting order is increasing in general but can be superseded by nitya condition (if nitya occurs in a later sutra then that later sutra takes advantage) 
    # which in turn would be superseded by the minimal condition criteria (antaraNga) 
    # The only exception is when there is a an exception that prevents application
    

    # for paXtheta - we need to have for liNg : yaasuXtparasmaipadeXshuudaatto Ngichcha 3.4.103 and then ato yeyaH (because of a-ending paXtha after shap)    
    pe=process_until_finish(expression)

    output_processed_string = lambda expr: ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))
    print(output_processed_string (pe))
    
    print("DONE")   
    
if T:
    test_siddhis ()
else:   
    test_expmt()
