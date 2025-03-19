import re,json

from functools import reduce

def print_expr(expr):
    return ''.join(reduce(lambda x ,y : x + y.get_output(),  expr, []))

def hal():
    return ("kh","k","gh","g","Ng","Nc","NN","Nn","chh","ch","jh","j",
            "Xth","Xt","Xdh","Xd","Xsh","th","t","dh","d","n",
            "ph","p","bh","b","m","y","r","l","v","sh",
            "s","h")

def parse_string(input_str):
    """
    build a list of aksharas from the string - unknown letters are ignored
    """
    sorted_achs= ('lRii','Rii', 'lRi', 'Ri','ai', "ii","uu",'au',"aa",'a', 'i', 'u', 'e', 'o',)
    match_re = "("+'|'.join(hal() + sorted_achs)+")" + "(.*)"


    matches = True
    x_str = input_str
    output=[]
    while matches and x_str:
        res = re.search(match_re, x_str)
        if res:
            output.append(res.group(1))
            x_str = res.group(2)
        else:
            matches =False
    return output



def lakaaras():
    return ('laXt','loXt','lRiXt','laNg','luNg','lRiNg','liNg1','liNg2','liXt','luXt')

def valid_moods():
    return ('bhaava','karma','karttaa')

def all_pratyayas() :
    return kRit_pratyayaaH()+tiNg_pratyayaaH()+san_pratyayaaH()+strii_pratyayaaH()+sup_pratyayaaH()+taddhita_pratyayaaH() + unclassified_pratyayaaH()

def get_suffix_for_dhaatu_meaning(meaning,dhaatu):
    suffixDhaatuMeaningMap = { ('ji','tachchhiila') : 'gsnu'}
    return Suffix(suffixDhaatuMeaningMap[(dhaatu,meaning)])

def get_suffix_for_context(contextName,**kwargs):
        if not isinstance(contextName,str):
            raise ValueError("contextName must be str")
        validContexts = "tachchhiila"
        if contextName not in validContexts:
            raise ValueError("Unknown contextName")
        for kwname,kwvalue in kwargs.items():
            if kwname.lower() == "dhaatu":
                return get_suffix_for_dhaatu_meaning(meaning=contextName, dhaatu=kwvalue)
            
        raise ValueError("Unknown meaning/context")
        
def check_mood_compatibility(mood, suffix):
    dictpermittedSuffixesForMood = {'karma':aatmanepada_pratyayaaH(),
                                    'bhaava':aatmanepada_pratyayaaH(),
                                    'karttaa':parasmaidpada_pratyayaaH()+aatmanepada_pratyayaaH()}
    
    if mood is not None:
        if mood not in dictpermittedSuffixesForMood:
            raise ValueError("No valid suffixes known for mood %s" % mood)
        if suffix not in dictpermittedSuffixesForMood[mood]:
            raise ValueError("Suffix %s Invalid for mood %s" % (suffix,mood) )
    
    return True

class Suffix:
    
    def __init__(self, suffix, lakaara=None, linga=None, mood=None):

        if not suffix :
            raise ValueError("suffix cannot be empty")
            
        if lakaara is not None:
            if lakaara not in lakaaras():
                raise ValueError("Unknown lakaara")
                
        self._lakaara=lakaara

        # default mood is karttaa
        if mood is not None:
            if mood not in valid_moods():
                raise ValueError("Unknown mood")
            self._mood = mood
        else:
            # prefer lazy initialisation instead of setting default karttaa mood
            self._mood = None
        
        
        if linga is not None:
            if linga not in (0,1,2):
                # 0 is masc, 1 is fem, 2 is neuter
                raise ValueError("Invalid linga")
        self._linga = linga


        if isinstance(suffix,str):
            self._suffix = parse_string(suffix)
        elif isinstance(suffix,list) and all(isinstance(j,str) for j in suffix):
            self._suffix= suffix
        
        else:
            raise ValueError("suffix must be a string")

        all_pratyayaaH = all_pratyayas()
        
        if ''.join(self._suffix) not in all_pratyayaaH:
            raise ValueError("Unknown suffix %s" % ''.join(self._suffix))
        if ''.join(self._suffix) in tiNg_pratyayaaH():
            check_mood_compatibility(mood=self._mood, suffix=''.join(self._suffix))

        self.is_taddhita = ''.join(self._suffix) in taddhita_pratyayaaH()

    def get_data(self):
        return self._suffix


    def apply_reduction(self,functor, **kwargs):
        self.reduced = functor(**kwargs)

    def is_saarvadhaatuka(self):
        if ''.join(self._suffix) in tiNg_pratyayaaH() or self._suffix[0]=='sh':
            return True
        else:
            return False

    def __str__(self):
        return ''.join(self._suffix)

    def __repr__(self):
        return str(self._suffix)


class Praatipadika:
    def __init__(self,data,linga):
        self._linga = linga
        inp_data = parse_string(data) if isinstance(data,str) else data
        self._data = inp_data
        
    def get_data(self):
        return self._data
    
    def __str__(self):
        return self.get_data()
    
    def __repr__(self):
        return self.get_data()


class Aagama (Suffix):
    pass

class Aadesha (Suffix):
    pass

class Dhaatu:
    def __init__(self,data):
        # this suppresses aNN to NN
        inp_data = parse_string(data) if isinstance(data,str) else data
        if inp_data[-1]=='NN' and inp_data[-2]=='a':
            self._data = inp_data[0:-2]+['NN']
        else:
            self._data= data

    def get_data(self):
        return self._data
    

def get_dhaatu_properties_dict():
    dhaatu_store_str = '{"bhuu": {"aniXt": "false"}, "edhaNN": {"aniXt": "false"}, "spardhaNN": {"aniXt": "false"}, "gaadhRiNN": {"aniXt": "false"}, "baadhRiNN": {"aniXt": "false"}, "naadhRiNN": {"aniXt": "false"}, "naathRiNN": {"aniXt": "false"}, "dadhaNN": {"aniXt": "false"}, "skudiNN": {"aniXt": "false"}, "shvidiNN": {"aniXt": "false"}, "vadiNN": {"aniXt": "false"}, "bhadiNN": {"aniXt": "false"}, "madiNN": {"aniXt": "false"}, "spadiNN": {"aniXt": "false"}, "klidiNN": {"aniXt": "false"}, "mudaNN": {"aniXt": "false"}, "dadaNN": {"aniXt": "false"}, "XshvadaNN": {"aniXt": "false"}, "svardaNN": {"aniXt": "false"}, "urdaNN": {"aniXt": "false"}, "kurdaNN": {"aniXt": "false"}, "khurdaNN": {"aniXt": "false"}, "gurdaNN": {"aniXt": "false"}, "gudaNN": {"aniXt": "false"}, "XshuudaNN": {"aniXt": "false"}, "hraadaNN": {"aniXt": "false"}, "hlaadiiNN": {"aniXt": "false"}, "svaadaNN": {"aniXt": "false"}, "pardaNN": {"aniXt": "false"}, "yatiiNN": {"aniXt": "false"}, "yutRiNN": {"aniXt": "false"}, "jutRiNN": {"aniXt": "false"}, "vithRiNN": {"aniXt": "false"}, "vethRiNN": {"aniXt": "false"}, "shrathiNN": {"aniXt": "false"}, "grathiNN": {"aniXt": "false"}, "katthaNN": {"aniXt": "false"}, "ataNN": {"aniXt": "false"}, "chitiiNN": {"aniXt": "false"}, "chyutiNNr": {"aniXt": "false"}, "shchutiNNr": {"aniXt": "false"}, "shchyutiNNr": {"aniXt": "false"}, "jyutRiNN": {"aniXt": "false"}, "mathiNN": {"aniXt": "false"}, "kuthiNN": {"aniXt": "false"}, "puthiNN": {"aniXt": "false"}, "luthiNN": {"aniXt": "false"}, "manthaNN": {"aniXt": "false"}, "XshidhaNN": {"aniXt": "false"}, "XshidhuuNN": {"aniXt": "true"}, "khaadRiNN": {"aniXt": "false"}, "khadaNN": {"aniXt": "false"}, "badaNN": {"aniXt": "false"}, "gadaNN": {"aniXt": "false"}, "radaNN": {"aniXt": "false"}, "NnadaNN": {"aniXt": "false"}, "ardaNN": {"aniXt": "false"}, "nardaNN": {"aniXt": "false"}, "gardaNN": {"aniXt": "false"}, "tardaNN": {"aniXt": "false"}, "kardaNN": {"aniXt": "false"}, "khardaNN": {"aniXt": "false"}, "atiNN": {"aniXt": "false"}, "adiNN": {"aniXt": "false"}, "idiNN": {"aniXt": "false"}, "bidiNN": {"aniXt": "false"}, "bhidiNN": {"aniXt": "true"}, "gaXdiNN": {"aniXt": "false"}, "NnidiNN": {"aniXt": "false"}, "XtunadNN": {"aniXt": "false"}, "chadiNN": {"aniXt": "false"}, "tradiNN": {"aniXt": "false"}, "kadiNN": {"aniXt": "false"}, "kradiNN": {"aniXt": "false"}, "kladiNN": {"aniXt": "false"}, "shundhaNN": {"aniXt": "false"}, "shiikRiNN": {"aniXt": "false"}, "siikRiNN": {"aniXt": "false"}, "lokRiNN": {"aniXt": "false"}, "shlokRiNN": {"aniXt": "false"}, "srokRiNN": {"aniXt": "false"}, "drekRiNN": {"aniXt": "false"}, "dhrekRiNN": {"aniXt": "false"}, "rekRiNN": {"aniXt": "false"}, "sekRiNN": {"aniXt": "false"}, "srekRiNN": {"aniXt": "false"}, "srakiNN": {"aniXt": "false"}, "shrakiNN": {"aniXt": "false"}, "shlakiNN": {"aniXt": "false"}, "shakiNN": {"aniXt": "false"}, "akiNN": {"aniXt": "false"}, "vakiNN": {"aniXt": "false"}, "makiNN": {"aniXt": "false"}, "kakaNN": {"aniXt": "false"}, "kukaNN": {"aniXt": "false"}, "vRikaNN": {"aniXt": "false"}, "chakaNN": {"aniXt": "false"}, "kakiNN": {"aniXt": "false"}, "shvakiNN": {"aniXt": "false"}, "trakiNN": {"aniXt": "false"}, "XdhaukRiNN": {"aniXt": "false"}, "traukRiNN": {"aniXt": "false"}, "XshvaXshkaNN": {"aniXt": "false"}, "vaskaNN": {"aniXt": "false"}, "maskaNN": {"aniXt": "false"}, "XtikRiNN": {"aniXt": "false"}, "XtiikRiNN": {"aniXt": "false"}, "tikRiNN": {"aniXt": "false"}, "tiikRiNN": {"aniXt": "false"}, "raghiNN": {"aniXt": "false"}, "laghiNN": {"aniXt": "false"}, "XshvakiNN": {"aniXt": "false"}, "aghiNN": {"aniXt": "false"}, "vaghiNN": {"aniXt": "false"}, "maghiNN": {"aniXt": "false"}, "raaghRiNN": {"aniXt": "false"}, "laaghRiNN": {"aniXt": "false"}, "draaghRiNN": {"aniXt": "false"}, "dhraaghRiNN": {"aniXt": "false"}, "shlaaghRiNN": {"aniXt": "false"}, "phakkaNN": {"aniXt": "false"}, "takaNN": {"aniXt": "false"}, "takiNN": {"aniXt": "false"}, "bukkaNN": {"aniXt": "false"}, "shukaNN": {"aniXt": "false"}, "kakhaNN": {"aniXt": "false"}, "okhRiNN": {"aniXt": "false"}, "raakhRiNN": {"aniXt": "false"}, "laakhRiNN": {"aniXt": "false"}, "draakhRiNN": {"aniXt": "false"}, "dhraakhRiNN": {"aniXt": "false"}, "shaakhRiNN": {"aniXt": "false"}, "shlaakhRiNN": {"aniXt": "false"}, "ukhaNN": {"aniXt": "false"}, "ukhiNN": {"aniXt": "false"}, "vakhaNN": {"aniXt": "false"}, "vakhiNN": {"aniXt": "false"}, "makhaNN": {"aniXt": "false"}, "makhiNN": {"aniXt": "false"}, "NnakhaNN": {"aniXt": "false"}, "NnakhiNN": {"aniXt": "false"}, "rakhaNN": {"aniXt": "false"}, "rakhiNN": {"aniXt": "false"}, "lakhaNN": {"aniXt": "false"}, "lakhiNN": {"aniXt": "false"}, "ikhaNN": {"aniXt": "false"}, "ikhiNN": {"aniXt": "false"}, "iikhaNN": {"aniXt": "false"}, "iikhiNN": {"aniXt": "false"}, "valgaNN": {"aniXt": "false"}, "ragiNN": {"aniXt": "false"}, "lagiNN": {"aniXt": "false"}, "agiNN": {"aniXt": "false"}, "vagiNN": {"aniXt": "false"}, "magiNN": {"aniXt": "false"}, "tagiNN": {"aniXt": "false"}, "tvagiNN": {"aniXt": "false"}, "tragiNN": {"aniXt": "false"}, "shragiNN": {"aniXt": "false"}, "shlagiNN": {"aniXt": "false"}, "igiNN": {"aniXt": "false"}, "rigiNN": {"aniXt": "false"}, "ligiNN": {"aniXt": "false"}, "mukhiNN": {"aniXt": "false"}, "thakiNN": {"aniXt": "false"}, "rikhaNN": {"aniXt": "false"}, "rikhiNN": {"aniXt": "false"}, "likhaNN": {"aniXt": "false"}, "likhiNN": {"aniXt": "false"}, "trakhaNN": {"aniXt": "false"}, "trikhiNN": {"aniXt": "false"}, "shikhiNN": {"aniXt": "false"}, "yugiNN": {"aniXt": "false"}, "jugiNN": {"aniXt": "false"}, "bugiNN": {"aniXt": "false"}, "vugiNN": {"aniXt": "false"}, "ghaghaNN": {"aniXt": "false"}, "ghagghaNN": {"aniXt": "false"}, "daghiNN": {"aniXt": "false"}, "shighiNN": {"aniXt": "false"}, "arghaNN": {"aniXt": "false"}, "varchaNN": {"aniXt": "false"}, "XshachaNN": {"aniXt": "false"}, "lochRiNN": {"aniXt": "false"}, "shachaNN": {"aniXt": "false"}, "shvachaNN": {"aniXt": "false"}, "shvachiNN": {"aniXt": "false"}, "kachaNN": {"aniXt": "false"}, "kachiNN": {"aniXt": "false"}, "kaachiNN": {"aniXt": "false"}, "machaNN": {"aniXt": "false"}, "muchiNN": {"aniXt": "false"}, "machiNN": {"aniXt": "false"}, "pachNN": {"aniXt": "false"}, "XshXtuchaNN": {"aniXt": "false"}, "RijaNN": {"aniXt": "false"}, "RijiNN": {"aniXt": "false"}, "bhRijiiNN": {"aniXt": "false"}, "ejRiNN": {"aniXt": "false"}, "bhrejRiNN": {"aniXt": "false"}, "bhraajRiNN": {"aniXt": "false"}, "rejRiNN": {"aniXt": "false"}, "iijaNN": {"aniXt": "false"}, "iijiNN": {"aniXt": "false"}, "viijaNN": {"aniXt": "false"}, "shuchaNN": {"aniXt": "false"}, "kuchaNN": {"aniXt": "false"}, "kunchaNN": {"aniXt": "false"}, "krunchaNN": {"aniXt": "false"}, "lunchaNN": {"aniXt": "false"}, "aNchNN": {"aniXt": "false"}, "vanchuNN": {"aniXt": "false"}, "chanchuNN": {"aniXt": "false"}, "tanchuNN": {"aniXt": "false"}, "tvanchuNN": {"aniXt": "false"}, "mrunchuNN": {"aniXt": "false"}, "mlunchuNN": {"aniXt": "false"}, "mruchuNN": {"aniXt": "false"}, "mluchuNN": {"aniXt": "false"}, "gruchuNN": {"aniXt": "false"}, "gluchuNN": {"aniXt": "false"}, "kujuNN": {"aniXt": "false"}, "khujuNN": {"aniXt": "false"}, "glunchuNN": {"aniXt": "false"}, "XshasjaNN": {"aniXt": "false"}, "gujaNN": {"aniXt": "false"}, "gujiNN": {"aniXt": "false"}, "archaNN": {"aniXt": "false"}, "mlechhaNN": {"aniXt": "false"}, "lachhaNN": {"aniXt": "false"}, "laachhiNN": {"aniXt": "false"}, "vaachhiNN": {"aniXt": "false"}, "aachhiNN": {"aniXt": "false"}, "hriichhaNN": {"aniXt": "false"}, "hurchhaaNN": {"aniXt": "false"}, "murchhaaNN": {"aniXt": "false"}, "sphurchhaaNN": {"aniXt": "false"}, "yuchhaNN": {"aniXt": "false"}, "uchhiNN": {"aniXt": "false"}, "uchhiiNN": {"aniXt": "false"}, "dhrajaNN": {"aniXt": "false"}, "dhrajiNN": {"aniXt": "false"}, "vrajaNN": {"aniXt": "false"}, "vrajiNN": {"aniXt": "false"}, "dhRijaNN": {"aniXt": "false"}, "dhRijiNN": {"aniXt": "false"}, "dhvajaNN": {"aniXt": "false"}, "dhvajiNN": {"aniXt": "false"}, "dhrijaNN": {"aniXt": "false"}, "kuujaNN": {"aniXt": "false"}, "kujiNN": {"aniXt": "false"}, "arjaNN": {"aniXt": "false"}, "XsharjaNN": {"aniXt": "false"}, "garjaNN": {"aniXt": "false"}, "tarjaNN": {"aniXt": "false"}, "karjaNN": {"aniXt": "false"}, "kharjaNN": {"aniXt": "false"}, "ajaNN": {"aniXt": "false"}, "tejaNN": {"aniXt": "false"}, "khajaNN": {"aniXt": "false"}, "kajaNN": {"aniXt": "false"}, "khajiNN": {"aniXt": "false"}, "osphuurjaaNN": {"aniXt": "false"}, "kXshi": {"aniXt": "true"}, "kXshiijaNN": {"aniXt": "false"}, "lajaNN": {"aniXt": "false"}, "lajiNN": {"aniXt": "false"}, "laajaNN": {"aniXt": "false"}, "laajiNN": {"aniXt": "false"}, "jajaNN": {"aniXt": "false"}, "jajiNN": {"aniXt": "false"}, "tujaNN": {"aniXt": "false"}, "tujiNN": {"aniXt": "false"}, "gajaNN": {"aniXt": "false"}, "gajiNN": {"aniXt": "false"}, "gRijaNN": {"aniXt": "false"}, "gRijiNN": {"aniXt": "false"}, "mujaNN": {"aniXt": "false"}, "mujiNN": {"aniXt": "false"}, "vajaNN": {"aniXt": "false"}, "aXtXtaNN": {"aniXt": "false"}, "veXshXtaNN": {"aniXt": "false"}, "cheXshXtaNN": {"aniXt": "false"}, "goXshXtaNN": {"aniXt": "false"}, "loXshXtaNN": {"aniXt": "false"}, "ghaXtXtaNN": {"aniXt": "false"}, "sphuXtaNN": {"aniXt": "false"}, "aXthiNN": {"aniXt": "false"}, "vaXthiNN": {"aniXt": "false"}, "maXthiNN": {"aniXt": "false"}, "kaXthiNN": {"aniXt": "false"}, "muXthiNN": {"aniXt": "false"}, "heXthaNN": {"aniXt": "false"}, "eXthaNN": {"aniXt": "false"}, "hiXdiNN": {"aniXt": "false"}, "huXdiNN": {"aniXt": "false"}, "kuXdiNN": {"aniXt": "false"}, "vaXdiNN": {"aniXt": "false"}, "maXdiNN": {"aniXt": "false"}, "bhaXdiNN": {"aniXt": "false"}, "piXdiNN": {"aniXt": "false"}, "muXdiNN": {"aniXt": "false"}, "tuXdiNN": {"aniXt": "false"}, "sphuXdiNN": {"aniXt": "false"}, "chaXdiNN": {"aniXt": "false"}, "shaXdiNN": {"aniXt": "false"}, "taXdiNN": {"aniXt": "false"}, "paXdiNN": {"aniXt": "false"}, "kaXdiNN": {"aniXt": "false"}, "khaXdiNN": {"aniXt": "false"}, "heXdRiNN": {"aniXt": "false"}, "hoXdRiNN": {"aniXt": "false"}, "baaXdRiNN": {"aniXt": "false"}, "vaaXdRiNN": {"aniXt": "false"}, "draaXdRiNN": {"aniXt": "false"}, "dhraaXdRiNN": {"aniXt": "false"}, "shaaXdRiNN": {"aniXt": "false"}, "shauXtRiNN": {"aniXt": "false"}, "yauXtRiNN": {"aniXt": "false"}, "mreXtRiNN": {"aniXt": "false"}, "mreXdRiNN": {"aniXt": "false"}, "mleXtRiNN": {"aniXt": "false"}, "chaXteNN": {"aniXt": "false"}, "kaXteNN": {"aniXt": "false"}, "aXtaNN": {"aniXt": "false"}, "paXtaNN": {"aniXt": "false"}, "raXtaNN": {"aniXt": "false"}, "laXtaNN": {"aniXt": "false"}, "shaXtaNN": {"aniXt": "false"}, "vaXtaNN": {"aniXt": "false"}, "kiXtaNN": {"aniXt": "false"}, "khiXtaNN": {"aniXt": "false"}, "shiXtaNN": {"aniXt": "false"}, "XshiXtaNN": {"aniXt": "false"}, "jaXtaNN": {"aniXt": "false"}, "jhaXtaNN": {"aniXt": "false"}, "bhaXtaNN": {"aniXt": "false"}, "taXtaNN": {"aniXt": "false"}, "khaXtaNN": {"aniXt": "false"}, "NnaXtaNN": {"aniXt": "false"}, "piXtaNN": {"aniXt": "false"}, "haXtaNN": {"aniXt": "false"}, "XshaXtaNN": {"aniXt": "false"}, "luXtaNN": {"aniXt": "false"}, "luXdaNN": {"aniXt": "false"}, "chiXtaNN": {"aniXt": "false"}, "viXtaNN": {"aniXt": "false"}, "biXtaNN": {"aniXt": "false"}, "hiXtaNN": {"aniXt": "false"}, "iXtaNN": {"aniXt": "false"}, "kaXtiiNN": {"aniXt": "false"}, "kuXtiNN": {"aniXt": "false"}, "muXdaNN": {"aniXt": "false"}, "pruXdaNN": {"aniXt": "false"}, "muXtaNN": {"aniXt": "false"}, "puXtaNN": {"aniXt": "false"}, "chuXdiNN": {"aniXt": "false"}, "puXdiNN": {"aniXt": "false"}, "ruXtiNN": {"aniXt": "false"}, "luXtiNN": {"aniXt": "false"}, "ruXthiNN": {"aniXt": "false"}, "luXthiNN": {"aniXt": "false"}, "ruXdiNN": {"aniXt": "false"}, "luXdiNN": {"aniXt": "false"}, "vaXtiNN": {"aniXt": "false"}, "baXtiNN": {"aniXt": "false"}, "phuXtiNNr": {"aniXt": "false"}, "sphuXtiNN": {"aniXt": "false"}, "paXthaNN": {"aniXt": "false"}, "vaXthaNN": {"aniXt": "false"}, "baXthaNN": {"aniXt": "false"}, "maXthaNN": {"aniXt": "false"}, "kaXthaNN": {"aniXt": "false"}, "raXthaNN": {"aniXt": "false"}, "haXthaNN": {"aniXt": "false"}, "ruXthaNN": {"aniXt": "false"}, "luXthaNN": {"aniXt": "false"}, "uuXthaNN": {"aniXt": "false"}, "uXthaNN": {"aniXt": "false"}, "piXthaNN": {"aniXt": "false"}, "shaXthaNN": {"aniXt": "false"}, "shuXthaNN": {"aniXt": "false"}, "shuuXthaNN": {"aniXt": "false"}, "kuXthiNN": {"aniXt": "false"}, "shuXthiNN": {"aniXt": "false"}, "chuXdXdaNN": {"aniXt": "false"}, "aXdXdaNN": {"aniXt": "false"}, "kaXdXdaNN": {"aniXt": "false"}, "kriiXdRiNN": {"aniXt": "false"}, "tuXdRiNN": {"aniXt": "false"}, "tuuXdRiNN": {"aniXt": "false"}, "huXdRiNN": {"aniXt": "false"}, "huuXdRiNN": {"aniXt": "false"}, "rauXdRiNN": {"aniXt": "false"}, "roXdRiNN": {"aniXt": "false"}, "loXdRiNN": {"aniXt": "false"}, "aXdaNN": {"aniXt": "false"}, "laXdaNN": {"aniXt": "false"}, "lalaNN": {"aniXt": "false"}, "kaXdaNN": {"aniXt": "false"}, "tipRiNN": {"aniXt": "true"}, "tepRiNN": {"aniXt": "false"}, "XshXtipRiNN": {"aniXt": "false"}, "XshXtepRiNN": {"aniXt": "false"}, "glepRiNN": {"aniXt": "false"}, "vepRiNN": {"aniXt": "false"}, "kepRiNN": {"aniXt": "false"}, "gepRiNN": {"aniXt": "false"}, "mepRiNN": {"aniXt": "false"}, "repRiNN": {"aniXt": "false"}, "lepRiNN": {"aniXt": "false"}, "hepRiNN": {"aniXt": "false"}, "dhepRiNN": {"aniXt": "false"}, "rapuuNNXsh": {"aniXt": "true"}, "kapiNN": {"aniXt": "false"}, "rabiNN": {"aniXt": "false"}, "labiNN": {"aniXt": "false"}, "abiNN": {"aniXt": "false"}, "kabRiNN": {"aniXt": "false"}, "kliibRiNN": {"aniXt": "false"}, "kXshiibRiNN": {"aniXt": "false"}, "kXshiivRiNN": {"aniXt": "false"}, "shiibhRiNN": {"aniXt": "false"}, "biibhRiNN": {"aniXt": "false"}, "chiibhRiNN": {"aniXt": "false"}, "rebhRiNN": {"aniXt": "false"}, "abhiNN": {"aniXt": "false"}, "rabhiNN": {"aniXt": "false"}, "labhiNN": {"aniXt": "false"}, "XshXtabhiNN": {"aniXt": "false"}, "skabhiNN": {"aniXt": "false"}, "jabhiiNN": {"aniXt": "false"}, "jRibhiNN": {"aniXt": "false"}, "shalbhaNN": {"aniXt": "false"}, "valbhaNN": {"aniXt": "false"}, "galbhaNN": {"aniXt": "false"}, "shranbhuNN": {"aniXt": "false"}, "sranbhuNN": {"aniXt": "false"}, "XshXtubhuNN": {"aniXt": "false"}, "gupuuNN": {"aniXt": "true"}, "dhuupaNN": {"aniXt": "false"}, "japaNN": {"aniXt": "false"}, "jalpaNN": {"aniXt": "false"}, "chapaNN": {"aniXt": "false"}, "XshapaNN": {"aniXt": "false"}, "rapaNN": {"aniXt": "false"}, "lapaNN": {"aniXt": "false"}, "chupaNN": {"aniXt": "false"}, "tupaNN": {"aniXt": "false"}, "tunpaNN": {"aniXt": "false"}, "trupaNN": {"aniXt": "false"}, "trunpaNN": {"aniXt": "false"}, "tuphaNN": {"aniXt": "false"}, "tunphaNN": {"aniXt": "false"}, "truphaNN": {"aniXt": "false"}, "trunphaNN": {"aniXt": "false"}, "parpaNN": {"aniXt": "false"}, "raphaNN": {"aniXt": "false"}, "raphiNN": {"aniXt": "false"}, "arbaNN": {"aniXt": "false"}, "parbaNN": {"aniXt": "false"}, "larbaNN": {"aniXt": "false"}, "barbaNN": {"aniXt": "false"}, "marbaNN": {"aniXt": "false"}, "karbaNN": {"aniXt": "false"}, "kharbaNN": {"aniXt": "false"}, "garbaNN": {"aniXt": "false"}, "sharbaNN": {"aniXt": "false"}, "XsharbaNN": {"aniXt": "false"}, "charbaNN": {"aniXt": "false"}, "kubiNN": {"aniXt": "false"}, "lubiNN": {"aniXt": "false"}, "tubiNN": {"aniXt": "false"}, "chubiNN": {"aniXt": "false"}, "XshRibhuNN": {"aniXt": "false"}, "XshRinbhuNN": {"aniXt": "false"}, "XshibhuNN": {"aniXt": "false"}, "XshinbhuNN": {"aniXt": "false"}, "shubhaNN": {"aniXt": "false"}, "shunbhaNN": {"aniXt": "false"}, "ghiNniNN": {"aniXt": "false"}, "ghuNniNN": {"aniXt": "false"}, "ghRiNniNN": {"aniXt": "false"}, "ghuNnaNN": {"aniXt": "false"}, "ghurNnaNN": {"aniXt": "false"}, "paNnaNN": {"aniXt": "false"}, "panaNN": {"aniXt": "false"}, "bhaamaNN": {"aniXt": "false"}, "XshamuuNNXsh": {"aniXt": "true"}, "kamuNN": {"aniXt": "false"}, "aNnaNN": {"aniXt": "false"}, "raNnaNN": {"aniXt": "false"}, "vaNnaNN": {"aniXt": "false"}, "bhaNnaNN": {"aniXt": "false"}, "maNnaNN": {"aniXt": "false"}, "kaNnaNN": {"aniXt": "false"}, "kvaNnaNN": {"aniXt": "false"}, "vraNnaNN": {"aniXt": "false"}, "bhraNnaNN": {"aniXt": "false"}, "dhvaNnaNN": {"aniXt": "false"}, "dhaNnaNN": {"aniXt": "false"}, "oNnRiNN": {"aniXt": "false"}, "shoNnRiNN": {"aniXt": "false"}, "shroNnRiNN": {"aniXt": "false"}, "shloNnRiNN": {"aniXt": "false"}, "paiNnRiNN": {"aniXt": "false"}, "praiNnRiNN": {"aniXt": "false"}, "dhraNnaNN": {"aniXt": "false"}, "baNnaNN": {"aniXt": "false"}, "kaniiNN": {"aniXt": "false"}, "XshXtanaNN": {"aniXt": "false"}, "vanaNN": {"aniXt": "false"}, "XshaNnaNN": {"aniXt": "false"}, "amaNN": {"aniXt": "false"}, "dramaNN": {"aniXt": "false"}, "hanmaNN": {"aniXt": "false"}, "miimRiNN": {"aniXt": "false"}, "chamuNN": {"aniXt": "false"}, "chhamuNN": {"aniXt": "false"}, "jamuNN": {"aniXt": "false"}, "jhamuNN": {"aniXt": "false"}, "jimuNN": {"aniXt": "false"}, "kramNN": {"aniXt": "false"}, "ayaNN": {"aniXt": "false"}, "vayaNN": {"aniXt": "false"}, "payaNN": {"aniXt": "false"}, "mayaNN": {"aniXt": "false"}, "chayaNN": {"aniXt": "false"}, "tayaNN": {"aniXt": "false"}, "NnayaNN": {"aniXt": "false"}, "dayaNN": {"aniXt": "false"}, "rayaNN": {"aniXt": "false"}, "layaNN": {"aniXt": "false"}, "uuyiiNN": {"aniXt": "false"}, "puuyiiNN": {"aniXt": "false"}, "knuuyiiNN": {"aniXt": "false"}, "kXshmaayiiNN": {"aniXt": "false"}, "sphaayiiNN": {"aniXt": "false"}, "pyaayiiNN": {"aniXt": "false"}, "taayRiNN": {"aniXt": "false"}, "shalaNN": {"aniXt": "false"}, "valaNN": {"aniXt": "false"}, "vallaNN": {"aniXt": "false"}, "malaNN": {"aniXt": "false"}, "mallaNN": {"aniXt": "false"}, "bhalaNN": {"aniXt": "false"}, "bhallaNN": {"aniXt": "false"}, "kalaNN": {"aniXt": "false"}, "kallaNN": {"aniXt": "false"}, "tevRiNN": {"aniXt": "false"}, "devRiNN": {"aniXt": "false"}, "XshevRiNN": {"aniXt": "false"}, "gevRiNN": {"aniXt": "false"}, "glevRiNN": {"aniXt": "false"}, "pevRiNN": {"aniXt": "false"}, "mevRiNN": {"aniXt": "false"}, "mlevRiNN": {"aniXt": "false"}, "shevRiNN": {"aniXt": "false"}, "khevRiNN": {"aniXt": "false"}, "plevRiNN": {"aniXt": "false"}, "kevRiNN": {"aniXt": "false"}, "revRiNN": {"aniXt": "false"}, "mavyaNN": {"aniXt": "false"}, "XshuurkXshyaNN": {"aniXt": "false"}, "iirkXshyaNN": {"aniXt": "false"}, "iirXshyaNN": {"aniXt": "false"}, "hayaNN": {"aniXt": "false"}, "shuchyaNN": {"aniXt": "false"}, "chuchyaNN": {"aniXt": "false"}, "haryaNN": {"aniXt": "false"}, "alaNN": {"aniXt": "false"}, "phalaaNN": {"aniXt": "false"}, "miilaNN": {"aniXt": "false"}, "shmiilaNN": {"aniXt": "false"}, "smiilaNN": {"aniXt": "false"}, "kXshmiilaNN": {"aniXt": "false"}, "piilaNN": {"aniXt": "false"}, "NniilaNN": {"aniXt": "false"}, "shiilaNN": {"aniXt": "false"}, "kiilaNN": {"aniXt": "false"}, "kuulaNN": {"aniXt": "false"}, "shuulaNN": {"aniXt": "false"}, "tuulaNN": {"aniXt": "false"}, "puulaNN": {"aniXt": "false"}, "muulaNN": {"aniXt": "false"}, "phalaNN": {"aniXt": "false"}, "chullaNN": {"aniXt": "false"}, "phullaNN": {"aniXt": "false"}, "chillaNN": {"aniXt": "false"}, "tilaNN": {"aniXt": "false"}, "tillaNN": {"aniXt": "false"}, "velRiNN": {"aniXt": "false"}, "chelRiNN": {"aniXt": "false"}, "kelRiNN": {"aniXt": "false"}, "khelRiNN": {"aniXt": "false"}, "kXshvelRiNN": {"aniXt": "false"}, "vellaNN": {"aniXt": "false"}, "vehlaNN": {"aniXt": "false"}, "pelRiNN": {"aniXt": "false"}, "phelRiNN": {"aniXt": "false"}, "shelRiNN": {"aniXt": "false"}, "XshelRiNN": {"aniXt": "false"}, "skhalaNN": {"aniXt": "false"}, "khalaNN": {"aniXt": "false"}, "galaNN": {"aniXt": "false"}, "XshalaNN": {"aniXt": "false"}, "dalaNN": {"aniXt": "false"}, "shvalaNN": {"aniXt": "false"}, "shvallaNN": {"aniXt": "false"}, "kholRiNN": {"aniXt": "false"}, "khorRiNN": {"aniXt": "false"}, "dhorRiNN": {"aniXt": "false"}, "tsaraNN": {"aniXt": "false"}, "kmaraNN": {"aniXt": "false"}, "abhraNN": {"aniXt": "false"}, "vabhraNN": {"aniXt": "false"}, "mabhraNN": {"aniXt": "false"}, "charaNN": {"aniXt": "false"}, "XshXthivuNN": {"aniXt": "false"}, "ji": {"aniXt": "true"}, "jiivaNN": {"aniXt": "false"}, "piivaNN": {"aniXt": "false"}, "miivaNN": {"aniXt": "false"}, "tiivaNN": {"aniXt": "false"}, "NniivaNN": {"aniXt": "false"}, "kXshiivuNN": {"aniXt": "false"}, "kXshevuNN": {"aniXt": "false"}, "urviiNN": {"aniXt": "false"}, "turviiNN": {"aniXt": "false"}, "thurviiNN": {"aniXt": "false"}, "durviiNN": {"aniXt": "false"}, "dhurviiNN": {"aniXt": "false"}, "gurviiNN": {"aniXt": "false"}, "murviiNN": {"aniXt": "false"}, "purvaNN": {"aniXt": "false"}, "parvaNN": {"aniXt": "false"}, "marvaNN": {"aniXt": "false"}, "charvaNN": {"aniXt": "false"}, "bharvaNN": {"aniXt": "false"}, "bharbaNN": {"aniXt": "false"}, "bharbhaNN": {"aniXt": "false"}, "karvaNN": {"aniXt": "false"}, "kharvaNN": {"aniXt": "false"}, "garvaNN": {"aniXt": "false"}, "arvaNN": {"aniXt": "false"}, "sharvaNN": {"aniXt": "false"}, "XsharvaNN": {"aniXt": "false"}, "iviNN": {"aniXt": "false"}, "piviNN": {"aniXt": "false"}, "miviNN": {"aniXt": "false"}, "NniviNN": {"aniXt": "false"}, "XshiviNN": {"aniXt": "false"}, "hiviNN": {"aniXt": "false"}, "diviNN": {"aniXt": "false"}, "dhiviNN": {"aniXt": "false"}, "jiviNN": {"aniXt": "false"}, "riviNN": {"aniXt": "false"}, "raviNN": {"aniXt": "false"}, "dhaviNN": {"aniXt": "false"}, "kRiviNN": {"aniXt": "false"}, "mavaNN": {"aniXt": "false"}, "avaNN": {"aniXt": "false"}, "dhaavuNN": {"aniXt": "false"}, "dhukXshaNN": {"aniXt": "false"}, "dhikXshaNN": {"aniXt": "false"}, "vRikXshaNN": {"aniXt": "false"}, "shikXshaNN": {"aniXt": "false"}, "bhikXshaNN": {"aniXt": "false"}, "kleshaNN": {"aniXt": "false"}, "dakXshaNN": {"aniXt": "false"}, "diikXshaNN": {"aniXt": "false"}, "iikXshaNN": {"aniXt": "false"}, "iiXshaNN": {"aniXt": "false"}, "bhaaXshaNN": {"aniXt": "false"}, "varXshaNN": {"aniXt": "false"}, "geXshRiNN": {"aniXt": "false"}, "gleXshRiNN": {"aniXt": "false"}, "peXshRiNN": {"aniXt": "false"}, "eXshRiNN": {"aniXt": "false"}, "yeXshRiNN": {"aniXt": "false"}, "jeXshRiNN": {"aniXt": "false"}, "NneXshRiNN": {"aniXt": "false"}, "preXshRiNN": {"aniXt": "false"}, "reXshRiNN": {"aniXt": "false"}, "heXshRiNN": {"aniXt": "false"}, "hreXshRiNN": {"aniXt": "false"}, "kaasRiNN": {"aniXt": "false"}, "bhaasRiNN": {"aniXt": "false"}, "NnaasRiNN": {"aniXt": "false"}, "raasRiNN": {"aniXt": "false"}, "NnasaNN": {"aniXt": "false"}, "bhyasaNN": {"aniXt": "false"}, "shasiNN": {"aniXt": "false"}, "grasuNN": {"aniXt": "false"}, "glasuNN": {"aniXt": "false"}, "iihaNN": {"aniXt": "false"}, "vahiNN": {"aniXt": "false"}, "mahiNN": {"aniXt": "false"}, "ahiNN": {"aniXt": "false"}, "garhaNN": {"aniXt": "false"}, "galhaNN": {"aniXt": "false"}, "barhaNN": {"aniXt": "false"}, "balhaNN": {"aniXt": "false"}, "varhaNN": {"aniXt": "false"}, "valhaNN": {"aniXt": "false"}, "plihaNN": {"aniXt": "false"}, "vehRiNN": {"aniXt": "false"}, "jehRiNN": {"aniXt": "false"}, "baahRiNN": {"aniXt": "false"}, "draahRiNN": {"aniXt": "false"}, "kaashRiNN": {"aniXt": "false"}, "uuhaNN": {"aniXt": "false"}, "gaahuuNN": {"aniXt": "true"}, "gRihuuNN": {"aniXt": "true"}, "glahaNN": {"aniXt": "false"}, "ghuNga": {"aniXt": "true"}, "ghuXshiNN": {"aniXt": "false"}, "ghuXshiNNraNN": {"aniXt": "false"}, "akXshuuNN": {"aniXt": "true"}, "takXshuuNN": {"aniXt": "true"}, "tvakXshuuNN": {"aniXt": "true"}, "ukXshaNN": {"aniXt": "false"}, "rakXshaNN": {"aniXt": "false"}, "NnikXshaNN": {"aniXt": "false"}, "trakXshaNN": {"aniXt": "false"}, "XshXtrakXshaNN": {"aniXt": "false"}, "tRikXshaNN": {"aniXt": "false"}, "XshXtRikXshaNN": {"aniXt": "false"}, "NnakXshaNN": {"aniXt": "false"}, "vakXshaNN": {"aniXt": "false"}, "mRikXshaNN": {"aniXt": "false"}, "mrakXshaNN": {"aniXt": "false"}, "takXshaNN": {"aniXt": "false"}, "pakXshaNN": {"aniXt": "false"}, "suurkXshaNN": {"aniXt": "false"}, "XsharkXshaNN": {"aniXt": "false"}, "kaakXshiNN": {"aniXt": "false"}, "vaakXshiNN": {"aniXt": "false"}, "maakXshiNN": {"aniXt": "false"}, "draakXshiNN": {"aniXt": "false"}, "dhraakXshiNN": {"aniXt": "false"}, "dhvaakXshiNN": {"aniXt": "false"}, "dhmaakXshiNN": {"aniXt": "false"}, "chuuXshaNN": {"aniXt": "false"}, "tuuXshaNN": {"aniXt": "false"}, "puuXshaNN": {"aniXt": "false"}, "muuXshaNN": {"aniXt": "false"}, "luuXshaNN": {"aniXt": "false"}, "ruuXshaNN": {"aniXt": "false"}, "shuuXshaNN": {"aniXt": "false"}, "suuXshaNN": {"aniXt": "false"}, "yuuXshaNN": {"aniXt": "false"}, "juuXshaNN": {"aniXt": "false"}, "bhuuXshaNN": {"aniXt": "false"}, "tasiNN": {"aniXt": "false"}, "uuXshaNN": {"aniXt": "false"}, "kaXshaNN": {"aniXt": "false"}, "khaXshaNN": {"aniXt": "false"}, "shiXshaNN": {"aniXt": "false"}, "jaXshaNN": {"aniXt": "false"}, "jhaXshaNN": {"aniXt": "false"}, "shaXshaNN": {"aniXt": "false"}, "vaXshaNN": {"aniXt": "false"}, "maXshaNN": {"aniXt": "false"}, "ruXshaNN": {"aniXt": "false"}, "riXshaNN": {"aniXt": "false"}, "bhaXshaNN": {"aniXt": "false"}, "uXshaNN": {"aniXt": "false"}, "jiXshuNN": {"aniXt": "true"}, "viXshuNN": {"aniXt": "true"}, "miXshuNN": {"aniXt": "false"}, "NniXshuNN": {"aniXt": "false"}, "puXshaNN": {"aniXt": "false"}, "shriXshuNN": {"aniXt": "false"}, "shliXshuNN": {"aniXt": "false"}, "pruXshuNN": {"aniXt": "false"}, "pluXshuNN": {"aniXt": "false"}, "pRiXshuNN": {"aniXt": "false"}, "vRiXshuNN": {"aniXt": "false"}, "mRiXshuNN": {"aniXt": "false"}, "ghRiXshuNN": {"aniXt": "false"}, "hRiXshuNN": {"aniXt": "false"}, "tusaNN": {"aniXt": "false"}, "hrasaNN": {"aniXt": "false"}, "hlasaNN": {"aniXt": "false"}, "rasaNN": {"aniXt": "false"}, "lasaNN": {"aniXt": "false"}, "ghaslRiNN": {"aniXt": "true"}, "jarjaNN": {"aniXt": "false"}, "charchaNN": {"aniXt": "false"}, "jharjhaNN": {"aniXt": "false"}, "pisRiNN": {"aniXt": "false"}, "pesRiNN": {"aniXt": "false"}, "visaNN": {"aniXt": "false"}, "vesaNN": {"aniXt": "false"}, "bisaNN": {"aniXt": "false"}, "besaNN": {"aniXt": "false"}, "haseNN": {"aniXt": "false"}, "NnishaNN": {"aniXt": "false"}, "mishaNN": {"aniXt": "false"}, "mashaNN": {"aniXt": "false"}, "shavaNN": {"aniXt": "false"}, "shashaNN": {"aniXt": "false"}, "shasuNN": {"aniXt": "false"}, "nsuNN": {"aniXt": "false"}, "chahaNN": {"aniXt": "false"}, "mahaNN": {"aniXt": "false"}, "rahaNN": {"aniXt": "false"}, "rahiNN": {"aniXt": "false"}, "dRihaNN": {"aniXt": "false"}, "dRihiNN": {"aniXt": "false"}, "bRihaNN": {"aniXt": "false"}, "bRihiNN": {"aniXt": "false"}, "tuhiNNraNN": {"aniXt": "false"}, "hiNNr": {"aniXt": "false"}, "arhaNN": {"aniXt": "false"}, "dyutaNN": {"aniXt": "false"}, "shvitaaNN": {"aniXt": "false"}, "NcimidaNN": {"aniXt": "false"}, "NciXshvidaaNN": {"aniXt": "false"}, "ruchaNN": {"aniXt": "false"}, "ghuXtaNN": {"aniXt": "false"}, "ruXtaNN": {"aniXt": "false"}, "kXshubhaNN": {"aniXt": "false"}, "NnabhaNN": {"aniXt": "false"}, "tubhaNN": {"aniXt": "false"}, "ransuNN": {"aniXt": "false"}, "vansuNN": {"aniXt": "false"}, "ranshuNN": {"aniXt": "false"}, "vRituNN": {"aniXt": "false"}, "vRidhuNN": {"aniXt": "false"}, "shRidhuNN": {"aniXt": "false"}, "syanduuNN": {"aniXt": "true"}, "kRipuuNN": {"aniXt": "true"}, "ghaXtaNN": {"aniXt": "false"}, "vyathaNN": {"aniXt": "false"}, "prathaNN": {"aniXt": "false"}, "prasaNN": {"aniXt": "false"}, "mradaNN": {"aniXt": "false"}, "skhadaNN": {"aniXt": "false"}, "kXshajiNN": {"aniXt": "false"}, "kRipaNN": {"aniXt": "false"}, "krapaNN": {"aniXt": "false"}, "kapaNN": {"aniXt": "false"}, "kadaNN": {"aniXt": "false"}, "kradaNN": {"aniXt": "false"}, "kladaNN": {"aniXt": "false"}, "tvaraaNN": {"aniXt": "false"}, "jvaraNN": {"aniXt": "false"}, "gaXdaNN": {"aniXt": "false"}, "heXdaNN": {"aniXt": "false"}, "XshXtakaNN": {"aniXt": "false"}, "kakheNN": {"aniXt": "false"}, "rageNN": {"aniXt": "false"}, "lageNN": {"aniXt": "false"}, "hrageNN": {"aniXt": "false"}, "hlageNN": {"aniXt": "false"}, "XshageNN": {"aniXt": "false"}, "XshXthageNN": {"aniXt": "false"}, "kageNN": {"aniXt": "false"}, "akaNN": {"aniXt": "false"}, "agaNN": {"aniXt": "false"}, "chaNnaNN": {"aniXt": "false"}, "shaNnaNN": {"aniXt": "false"}, "shraNnaNN": {"aniXt": "false"}, "shrathaNN": {"aniXt": "false"}, "shnathaNN": {"aniXt": "false"}, "shlathaNN": {"aniXt": "false"}, "knathaNN": {"aniXt": "false"}, "krathaNN": {"aniXt": "false"}, "klathaNN": {"aniXt": "false"}, "chanaNN": {"aniXt": "false"}, "jvalaNN": {"aniXt": "false"}, "hvalaNN": {"aniXt": "false"}, "hmalaNN": {"aniXt": "false"}, "smRi": {"aniXt": "true"}, "dRii": {"aniXt": "false"}, "nRii": {"aniXt": "false"}, "shraa": {"aniXt": "true"}, "jNcaa": {"aniXt": "false"}, "chalaNN": {"aniXt": "false"}, "chhadi": {"aniXt": "false"}, "madiiNN": {"aniXt": "false"}, "dhvanaNN": {"aniXt": "false"}, "shamoNN": {"aniXt": "false"}, "yamaNN": {"aniXt": "false"}, "khadiNNr": {"aniXt": "false"}, "svanaNN": {"aniXt": "false"}, "phaNnaNN": {"aniXt": "false"}, "raajRiNN": {"aniXt": "false"}, "XtubhraajRiNN": {"aniXt": "false"}, "XtubhraashRiNN": {"aniXt": "false"}, "XtubhlaashRiNN": {"aniXt": "false"}, "syamuNN": {"aniXt": "false"}, "XshamaNN": {"aniXt": "false"}, "XshXtamaNN": {"aniXt": "false"}, "jalaNN": {"aniXt": "false"}, "XtalaNN": {"aniXt": "false"}, "XtvalaNN": {"aniXt": "false"}, "XshXthalaNN": {"aniXt": "false"}, "halaNN": {"aniXt": "false"}, "NnalaNN": {"aniXt": "false"}, "palaNN": {"aniXt": "false"}, "balaNN": {"aniXt": "false"}, "pulaNN": {"aniXt": "false"}, "kulaNN": {"aniXt": "false"}, "hulaNN": {"aniXt": "false"}, "patlRiNN": {"aniXt": "false"}, "kvatheNN": {"aniXt": "false"}, "patheNN": {"aniXt": "false"}, "matheNN": {"aniXt": "false"}, "vamaNN": {"aniXt": "false"}, "bhramNN": {"aniXt": "false"}, "kXsharaNN": {"aniXt": "false"}, "kXshuraNN": {"aniXt": "false"}, "XshahaNN": {"aniXt": "false"}, "ramNN": {"aniXt": "true"}, "XshadlRiNN": {"aniXt": "true"}, "shadlRiNN": {"aniXt": "true"}, "krushaNN": {"aniXt": "true"}, "budhaNN": {"aniXt": "true"}, "ruhaNN": {"aniXt": "true"}, "kasaNN": {"aniXt": "false"}, "hikkaNN": {"aniXt": "false"}, "achuNN": {"aniXt": "false"}, "achiNN": {"aniXt": "false"}, "XtuyaachRiNN": {"aniXt": "false"}, "reXtRiNN": {"aniXt": "false"}, "chateNN": {"aniXt": "false"}, "chadeNN": {"aniXt": "false"}, "prothRiNN": {"aniXt": "false"}, "midRiNN": {"aniXt": "false"}, "medRiNN": {"aniXt": "false"}, "mithRiNN": {"aniXt": "false"}, "methRiNN": {"aniXt": "false"}, "midhRiNN": {"aniXt": "false"}, "medhRiNN": {"aniXt": "false"}, "NnidRiNN": {"aniXt": "false"}, "NnedRiNN": {"aniXt": "false"}, "mRidhuNN": {"aniXt": "false"}, "dhiNNr": {"aniXt": "false"}, "bundiNNr": {"aniXt": "false"}, "veNnRiNN": {"aniXt": "false"}, "venRiNN": {"aniXt": "false"}, "khanuNN": {"aniXt": "false"}, "chiivRiNN": {"aniXt": "false"}, "chiibRiNN": {"aniXt": "false"}, "chaayRiNN": {"aniXt": "false"}, "vyayaNN": {"aniXt": "false"}, "daashRiNN": {"aniXt": "false"}, "bheXshRiNN": {"aniXt": "false"}, "bhreXshRiNN": {"aniXt": "false"}, "bhleXshRiNN": {"aniXt": "false"}, "asaNN": {"aniXt": "false"}, "aXshaNN": {"aniXt": "false"}, "spashaNN": {"aniXt": "false"}, "laXshaNN": {"aniXt": "false"}, "chaXshaNN": {"aniXt": "false"}, "chhaXshaNN": {"aniXt": "false"}, "bhrakXshaNN": {"aniXt": "false"}, "bhlakXshaNN": {"aniXt": "false"}, "bhakXshaNN": {"aniXt": "false"}, "plakXshaNN": {"aniXt": "false"}, "daasRiNN": {"aniXt": "false"}, "maahRiNN": {"aniXt": "false"}, "guhuuNN": {"aniXt": "true"}, "riNc": {"aniXt": "false"}, "Nc": {"aniXt": "false"}, "Xt": {"aniXt": "true"}, "glai": {"aniXt": "true"}, "mlai": {"aniXt": "true"}, "dyai": {"aniXt": "true"}, "drai": {"aniXt": "true"}, "dhrai": {"aniXt": "true"}, "dhyai": {"aniXt": "true"}, "rai": {"aniXt": "true"}, "styai": {"aniXt": "true"}, "XshXtyai": {"aniXt": "true"}, "khai": {"aniXt": "true"}, "kXshai": {"aniXt": "true"}, "jaiNN": {"aniXt": "true"}, "XshaiNN": {"aniXt": "true"}, "kaiNN": {"aniXt": "true"}, "gaiNN": {"aniXt": "true"}, "shaiNN": {"aniXt": "true"}, "shraiNN": {"aniXt": "true"}, "sraiNN": {"aniXt": "true"}, "paiNN": {"aniXt": "true"}, "ovaiNN": {"aniXt": "true"}, "XshXtaiNN": {"aniXt": "true"}, "XshNnaiNN": {"aniXt": "true"}, "daipaNN": {"aniXt": "true"}, "paaNN": {"aniXt": "true"}, "ghraaNN": {"aniXt": "true"}, "dhmaaNN": {"aniXt": "true"}, "XshXthaaNN": {"aniXt": "true"}, "mnaaNN": {"aniXt": "true"}, "daaNN": {"aniXt": "true"}, "hvRiNN": {"aniXt": "true"}, "svRiNN": {"aniXt": "true"}, "smRiNN": {"aniXt": "true"}, "vRiNN": {"aniXt": "false"}, "sRiNN": {"aniXt": "true"}, "Ri": {"aniXt": "true"}, "gRiNN": {"aniXt": "true"}, "ghRiNN": {"aniXt": "true"}, "dhvRiNN": {"aniXt": "true"}, "sruNN": {"aniXt": "true"}, "Xshu": {"aniXt": "true"}, "shruNN": {"aniXt": "true"}, "dhruNN": {"aniXt": "true"}, "duNN": {"aniXt": "true"}, "druNN": {"aniXt": "true"}, "jiNN": {"aniXt": "true"}, "jriNN": {"aniXt": "true"}, "smiNN": {"aniXt": "true"}, "guNN": {"aniXt": "true"}, "gaaNN": {"aniXt": "true"}, "uNgaNN": {"aniXt": "true"}, "kuNN": {"aniXt": "true"}, "khuNN": {"aniXt": "true"}, "ghuNN": {"aniXt": "true"}, "NguNN": {"aniXt": "true"}, "yuNg": {"aniXt": "true"}, "ruNg": {"aniXt": "true"}, "luNg": {"aniXt": "true"}, "ruNN": {"aniXt": "true"}, "dhRiNN": {"aniXt": "true"}, "meNN": {"aniXt": "true"}, "deNN": {"aniXt": "true"}, "shyaiNN": {"aniXt": "true"}, "pyaiNN": {"aniXt": "true"}, "traiNN": {"aniXt": "true"}, "puuNN": {"aniXt": "false"}, "muuNN": {"aniXt": "false"}, "XdiiNN": {"aniXt": "false"}, "tRiiNN": {"aniXt": "false"}, "gupaNN": {"aniXt": "false"}, "tijaNN": {"aniXt": "false"}, "maanaNN": {"aniXt": "false"}, "badhaNN": {"aniXt": "false"}, "rabhaNN": {"aniXt": "true"}, "labhaNNXsh": {"aniXt": "true"}, "XshvanjaNN": {"aniXt": "true"}, "hadaNN": {"aniXt": "true"}, "XshvidaaNN": {"aniXt": "true"}, "kandiNNr": {"aniXt": "true"}, "yabhaNN": {"aniXt": "true"}, "NnamaNN": {"aniXt": "true"}, "gamlRiNN": {"aniXt": "true"}, "sRiplRiNN": {"aniXt": "true"}, "tapaNN": {"aniXt": "true"}, "tyajaNN": {"aniXt": "true"}, "XshanjaNN": {"aniXt": "true"}, "RiNN": {"aniXt": "true"}, "dRishNN": {"aniXt": "true"}, "danshaNN": {"aniXt": "true"}, "kRiXshaNN": {"aniXt": "true"}, "dahaNN": {"aniXt": "true"}, "mihaNN": {"aniXt": "true"}, "kitaNN": {"aniXt": "true"}, "daanaNN": {"aniXt": "false"}, "shaanaNN": {"aniXt": "false"}, "XdupachNN": {"aniXt": "true"}, "bhajaNN": {"aniXt": "false"}, "ranjaNN": {"aniXt": "true"}, "shapaNN": {"aniXt": "true"}, "tviXshaNN": {"aniXt": "true"}, "yajNN": {"aniXt": "true"}, "XduvapaNN": {"aniXt": "true"}, "vahaNN": {"aniXt": "true"}, "vasaNN": {"aniXt": "false"}, "veNN": {"aniXt": "true"}, "vyeNN": {"aniXt": "true"}, "hveNN": {"aniXt": "true"}, "vadaNN": {"aniXt": "false"}, "shviNN": {"aniXt": "false"}, "RitiNN": {"aniXt": "false"}, "churaNN": {"aniXt": "false"}, "chitiNN": {"aniXt": "false"}, "yatriNN": {"aniXt": "false"}, "lakXshaNN": {"aniXt": "false"}, "kudriNN": {"aniXt": "false"}, "kudRiNN": {"aniXt": "false"}, "midiNN": {"aniXt": "false"}, "midaNN": {"aniXt": "false"}, "olaXdiNN": {"aniXt": "false"}, "piiXdaNN": {"aniXt": "false"}, "naXtaNN": {"aniXt": "false"}, "bandhaNN": {"aniXt": "true"}, "pRii": {"aniXt": "false"}, "urjaNN": {"aniXt": "false"}, "varNnaNN": {"aniXt": "false"}, "churNnaNN": {"aniXt": "false"}, "pRithaNN": {"aniXt": "false"}, "pathaNN": {"aniXt": "false"}, "XshanbaNN": {"aniXt": "false"}, "shanbaNN": {"aniXt": "false"}, "saanbaNN": {"aniXt": "false"}, "kuXtXtaNN": {"aniXt": "false"}, "puXtXtaNN": {"aniXt": "false"}, "chuXtXtaNN": {"aniXt": "false"}, "XshuXtXtaNN": {"aniXt": "false"}, "lunXtaNN": {"aniXt": "false"}, "lunXthaNN": {"aniXt": "false"}, "shvaXthaNN": {"aniXt": "false"}, "shvaXthiNN": {"aniXt": "false"}, "pijaNN": {"aniXt": "false"}, "pijiNN": {"aniXt": "false"}, "lujiNN": {"aniXt": "false"}, "pisaNN": {"aniXt": "false"}, "XshaantvaNN": {"aniXt": "false"}, "shaantvaNN": {"aniXt": "false"}, "shvalkaNN": {"aniXt": "false"}, "valkaNN": {"aniXt": "false"}, "XshNnihaNN": {"aniXt": "true"}, "sphiXtXtaNN": {"aniXt": "false"}, "smiXtaNN": {"aniXt": "false"}, "miNg": {"aniXt": "false"}, "shliXshaNN": {"aniXt": "true"}, "pathiNN": {"aniXt": "false"}, "pichhaNN": {"aniXt": "false"}, "chhadiNN": {"aniXt": "false"}, "taXdaNN": {"aniXt": "false"}, "khaXdaNN": {"aniXt": "false"}, "guXdiNN": {"aniXt": "false"}, "guXthiNN": {"aniXt": "false"}, "khuXdiNN": {"aniXt": "false"}, "chhardaNN": {"aniXt": "false"}, "pustaNN": {"aniXt": "false"}, "bustaNN": {"aniXt": "false"}, "chudaNN": {"aniXt": "false"}, "nakkaNN": {"aniXt": "false"}, "dhakkaNN": {"aniXt": "false"}, "chakkaNN": {"aniXt": "false"}, "chukkaNN": {"aniXt": "false"}, "kXshalaNN": {"aniXt": "false"}, "talaNN": {"aniXt": "false"}, "tulaNN": {"aniXt": "false"}, "dulaNN": {"aniXt": "false"}, "chulaNN": {"aniXt": "false"}, "vilaNN": {"aniXt": "false"}, "bilaNN": {"aniXt": "false"}, "paalaNN": {"aniXt": "false"}, "shulbaNN": {"aniXt": "false"}, "shuurpaNN": {"aniXt": "false"}, "chuXtaNN": {"aniXt": "false"}, "pishaNN": {"aniXt": "false"}, "pasiNN": {"aniXt": "false"}, "pashiNN": {"aniXt": "false"}, "shulkaNN": {"aniXt": "false"}, "chapiNN": {"aniXt": "false"}, "kXshapiNN": {"aniXt": "false"}, "chhajiNN": {"aniXt": "false"}, "shvartaNN": {"aniXt": "false"}, "svartaNN": {"aniXt": "false"}, "shvabhraNN": {"aniXt": "false"}, "jNcapaNN": {"aniXt": "false"}, "chiNca": {"aniXt": "false"}, "mustaNN": {"aniXt": "false"}, "khaXtXtaNN": {"aniXt": "false"}, "XshaXtXtaNN": {"aniXt": "false"}, "puurNnaNN": {"aniXt": "false"}, "puNnaNN": {"aniXt": "false"}, "punsaNN": {"aniXt": "false"}, "XtakiNN": {"aniXt": "false"}, "vyapaNN": {"aniXt": "false"}, "vipaNN": {"aniXt": "false"}, "dhuusaNN": {"aniXt": "false"}, "dhuuXshaNN": {"aniXt": "false"}, "dhuushaNN": {"aniXt": "false"}, "kiiXtaNN": {"aniXt": "false"}, "chuurNnaNN": {"aniXt": "false"}, "puujaNN": {"aniXt": "false"}, "arkaNN": {"aniXt": "false"}, "juXdaNN": {"aniXt": "false"}, "maarjaNN": {"aniXt": "false"}, "marchaNN": {"aniXt": "false"}, "ghRi": {"aniXt": "true"}, "kRiitaNN": {"aniXt": "false"}, "vardhaNN": {"aniXt": "false"}, "kubhiNN": {"aniXt": "false"}, "hlapaNN": {"aniXt": "false"}, "klapaNN": {"aniXt": "false"}, "hrapaNN": {"aniXt": "false"}, "chuXtiNN": {"aniXt": "false"}, "mRiXdiNN": {"aniXt": "false"}, "ilaNN": {"aniXt": "false"}, "mrachhaNN": {"aniXt": "false"}, "bruusaNN": {"aniXt": "false"}, "vruusaNN": {"aniXt": "false"}, "vruuXshaNN": {"aniXt": "false"}, "gardhaNN": {"aniXt": "false"}, "puurvaNN": {"aniXt": "false"}, "jasiNN": {"aniXt": "false"}, "iiXdaNN": {"aniXt": "false"}, "jasuNN": {"aniXt": "false"}, "piXthiNN": {"aniXt": "false"}, "XdipaNN": {"aniXt": "false"}, "XshXtupaNN": {"aniXt": "false"}, "XshXtuupaNN": {"aniXt": "false"}, "chitaNN": {"aniXt": "false"}, "dashiNN": {"aniXt": "false"}, "dasiNN": {"aniXt": "false"}, "dasaNN": {"aniXt": "false"}, "XdapaNN": {"aniXt": "false"}, "tatriNN": {"aniXt": "false"}, "matriNN": {"aniXt": "false"}, "bhartsaNN": {"aniXt": "false"}, "bastaNN": {"aniXt": "false"}, "gandhaNN": {"aniXt": "false"}, "vastaNN": {"aniXt": "false"}, "hastaNN": {"aniXt": "false"}, "viXshkaNN": {"aniXt": "false"}, "hiXshkaNN": {"aniXt": "false"}, "niXshkaNN": {"aniXt": "false"}, "kuuNnaNN": {"aniXt": "false"}, "tuuNnaNN": {"aniXt": "false"}, "bhruuNnaNN": {"aniXt": "false"}, "yakXshaNN": {"aniXt": "false"}, "syamaNN": {"aniXt": "false"}, "guuraNN": {"aniXt": "false"}, "shamaNN": {"aniXt": "false"}, "kutsaNN": {"aniXt": "false"}, "truXtaNN": {"aniXt": "false"}, "kuXtaNN": {"aniXt": "false"}, "kuuXtaNN": {"aniXt": "false"}, "vRiXshaNN": {"aniXt": "false"}, "madaNN": {"aniXt": "false"}, "divuNN": {"aniXt": "false"}, "gRi": {"aniXt": "false"}, "vidaNN": {"aniXt": "true"}, "manaNN": {"aniXt": "true"}, "yu": {"aniXt": "false"}, "kusmaNN": {"aniXt": "false"}, "shabdaNN": {"aniXt": "true"}, "jabhiNN": {"aniXt": "false"}, "pashaNN": {"aniXt": "false"}, "chaXtaNN": {"aniXt": "false"}, "XshiNNr": {"aniXt": "false"}, "krandaNN": {"aniXt": "false"}, "mokXshaNN": {"aniXt": "false"}, "yataNN": {"aniXt": "false"}, "rakaNN": {"aniXt": "false"}, "lagaNN": {"aniXt": "false"}, "raghaNN": {"aniXt": "false"}, "ragaNN": {"aniXt": "false"}, "trasaNN": {"aniXt": "false"}, "dhrasaNN": {"aniXt": "false"}, "ghrasaNN": {"aniXt": "false"}, "muchaNN": {"aniXt": "false"}, "chyu": {"aniXt": "false"}, "vyusaNN": {"aniXt": "false"}, "grasaNN": {"aniXt": "false"}, "mijiNN": {"aniXt": "false"}, "lijiNN": {"aniXt": "false"}, "bhajiNN": {"aniXt": "false"}, "trasiNN": {"aniXt": "false"}, "pisiNN": {"aniXt": "false"}, "kusiNN": {"aniXt": "false"}, "kushiNN": {"aniXt": "false"}, "ghaXtiNN": {"aniXt": "false"}, "vichhaNN": {"aniXt": "false"}, "chiivaNN": {"aniXt": "false"}, "puthaNN": {"aniXt": "false"}, "kupaNN": {"aniXt": "false"}, "tarkaNN": {"aniXt": "false"}, "ajiNN": {"aniXt": "false"}, "bhRishiNN": {"aniXt": "false"}, "rushiNN": {"aniXt": "false"}, "shiikaNN": {"aniXt": "false"}, "rusiNN": {"aniXt": "false"}, "naXtiNN": {"aniXt": "false"}, "puXtiNN": {"aniXt": "false"}, "chi": {"aniXt": "false"}, "radhiNN": {"aniXt": "false"}, "laXdiNN": {"aniXt": "false"}, "nalaNN": {"aniXt": "false"}, "puuriiNN": {"aniXt": "false"}, "rujaNN": {"aniXt": "false"}, "yujaNN": {"aniXt": "true"}, "pRichaNN": {"aniXt": "false"}, "iiraNN": {"aniXt": "false"}, "lii": {"aniXt": "false"}, "vRijiiNN": {"aniXt": "false"}, "jRii": {"aniXt": "false"}, "jri": {"aniXt": "false"}, "richaNN": {"aniXt": "false"}, "tRipaNN": {"aniXt": "false"}, "chhRidiiNN": {"aniXt": "false"}, "chRipaNN": {"aniXt": "false"}, "chhRipaNN": {"aniXt": "false"}, "dRipaNN": {"aniXt": "false"}, "dRibhiiNN": {"aniXt": "false"}, "dRibhaNN": {"aniXt": "false"}, "chhadaNN": {"aniXt": "false"}, "mii": {"aniXt": "false"}, "granthaNN": {"aniXt": "false"}, "chiikaNN": {"aniXt": "false"}, "hisiNN": {"aniXt": "false"}, "XshadaNN": {"aniXt": "false"}, "juXshaNN": {"aniXt": "false"}, "riiNc": {"aniXt": "true"}, "shranthaNN": {"aniXt": "false"}, "aaplRiNN": {"aniXt": "true"}, "tanuNN": {"aniXt": "false"}, "vachaNN": {"aniXt": "true"}, "maargaNN": {"aniXt": "false"}, "mRijNN": {"aniXt": "true"}, "mRiXshaNN": {"aniXt": "false"}, "dhRiXshaNN": {"aniXt": "false"}, "katha": {"aniXt": "false"}, "vara": {"aniXt": "false"}, "gaNna": {"aniXt": "false"}, "shaXtha": {"aniXt": "false"}, "shvaXtha": {"aniXt": "false"}, "paXta": {"aniXt": "false"}, "vaXta": {"aniXt": "false"}, "raha": {"aniXt": "false"}, "rangaNN": {"aniXt": "false"}, "stana": {"aniXt": "false"}, "gada": {"aniXt": "false"}, "pata": {"aniXt": "false"}, "paXsha": {"aniXt": "false"}, "svara": {"aniXt": "false"}, "racha": {"aniXt": "false"}, "kala": {"aniXt": "false"}, "chaha": {"aniXt": "false"}, "maha": {"aniXt": "false"}, "saara": {"aniXt": "false"}, "kRipa": {"aniXt": "false"}, "shratha": {"aniXt": "false"}, "spRiha": {"aniXt": "false"}, "bhaama": {"aniXt": "false"}, "suucha": {"aniXt": "false"}, "kheXta": {"aniXt": "false"}, "kheXdaNN": {"aniXt": "false"}, "khoXta": {"aniXt": "false"}, "kXshoXta": {"aniXt": "false"}, "goma": {"aniXt": "false"}, "kumaara": {"aniXt": "false"}, "shiila": {"aniXt": "false"}, "saama": {"aniXt": "false"}, "vela": {"aniXt": "false"}, "kaala": {"aniXt": "false"}, "palpuula": {"aniXt": "false"}, "vaata": {"aniXt": "false"}, "gaveXsha": {"aniXt": "false"}, "vaasa": {"aniXt": "false"}, "nivaasa": {"aniXt": "false"}, "bhaaja": {"aniXt": "false"}, "sabhaaja": {"aniXt": "false"}, "uuna": {"aniXt": "false"}, "dhvana": {"aniXt": "false"}, "kuuXta": {"aniXt": "false"}, "sanketa": {"aniXt": "false"}, "graama": {"aniXt": "false"}, "kuNna": {"aniXt": "false"}, "guNna": {"aniXt": "false"}, "keta": {"aniXt": "false"}, "stena": {"aniXt": "false"}, "pada": {"aniXt": "false"}, "gRiha": {"aniXt": "false"}, "mRiga": {"aniXt": "false"}, "kuha": {"aniXt": "false"}, "shuura": {"aniXt": "false"}, "viira": {"aniXt": "false"}, "sthuula": {"aniXt": "false"}, "artha": {"aniXt": "false"}, "satra": {"aniXt": "false"}, "garva": {"aniXt": "false"}, "suutra": {"aniXt": "false"}, "muutra": {"aniXt": "false"}, "ruukXsha": {"aniXt": "false"}, "paara": {"aniXt": "false"}, "tiira": {"aniXt": "false"}, "puXta": {"aniXt": "false"}, "katra": {"aniXt": "false"}, "kartaNN": {"aniXt": "false"}, "valka": {"aniXt": "false"}, "chitra": {"aniXt": "false"}, "ansa": {"aniXt": "false"}, "laja": {"aniXt": "false"}, "mishra": {"aniXt": "false"}, "sangraama": {"aniXt": "false"}, "stomaNN": {"aniXt": "false"}, "chhidra": {"aniXt": "false"}, "karNnaNN": {"aniXt": "false"}, "andha": {"aniXt": "false"}, "danXda": {"aniXt": "false"}, "anka": {"aniXt": "false"}, "anga": {"aniXt": "false"}, "sukha": {"aniXt": "false"}, "dukha": {"aniXt": "false"}, "rasa": {"aniXt": "false"}, "vyaya": {"aniXt": "false"}, "ruupa": {"aniXt": "false"}, "chheda": {"aniXt": "false"}, "chhada": {"aniXt": "false"}, "laabha": {"aniXt": "false"}, "vraNna": {"aniXt": "false"}, "varNna": {"aniXt": "false"}, "parNna": {"aniXt": "false"}, "viXshka": {"aniXt": "false"}, "kXshipa": {"aniXt": "false"}, "vasa": {"aniXt": "false"}, "tuttha": {"aniXt": "false"}, "palyuula": {"aniXt": "false"}, "dheka": {"aniXt": "false"}, "adNN": {"aniXt": "true"}, "hanNN": {"aniXt": "true"}, "dviXshNN": {"aniXt": "true"}, "duhaNN": {"aniXt": "true"}, "dihaNN": {"aniXt": "true"}, "lihaNN": {"aniXt": "true"}, "kXshiNg": {"aniXt": "false"}, "iishaNN": {"aniXt": "false"}, "aasaNN": {"aniXt": "false"}, "shaasuNN": {"aniXt": "false"}, "kasiNN": {"aniXt": "false"}, "kashaNN": {"aniXt": "false"}, "NnisiNN": {"aniXt": "false"}, "NnijiNN": {"aniXt": "false"}, "shijiNN": {"aniXt": "false"}, "pRijiNN": {"aniXt": "false"}, "vRijiNN": {"aniXt": "false"}, "pRichiiNN": {"aniXt": "false"}, "Ng": {"aniXt": "true"}, "ru": {"aniXt": "false"}, "tu": {"aniXt": "false"}, "Nnu": {"aniXt": "false"}, "kXshu": {"aniXt": "false"}, "kXshNnu": {"aniXt": "false"}, "XshNnu": {"aniXt": "false"}, "rNnuNc": {"aniXt": "false"}, "dyu": {"aniXt": "true"}, "ku": {"aniXt": "true"}, "XtuNc": {"aniXt": "true"}, "ruuNc": {"aniXt": "false"}, "Nn": {"aniXt": "true"}, "k": {"aniXt": "true"}, "vii": {"aniXt": "true"}, "yaa": {"aniXt": "true"}, "vaa": {"aniXt": "true"}, "bhaa": {"aniXt": "true"}, "XshNnaa": {"aniXt": "true"}, "draa": {"aniXt": "true"}, "psaa": {"aniXt": "true"}, "paa": {"aniXt": "true"}, "raa": {"aniXt": "true"}, "laa": {"aniXt": "true"}, "p": {"aniXt": "true"}, "khyaa": {"aniXt": "true"}, "praa": {"aniXt": "true"}, "maa": {"aniXt": "true"}, "diNNr": {"aniXt": "false"}, "XshvapaNN": {"aniXt": "true"}, "shvasaNN": {"aniXt": "false"}, "anaNN": {"aniXt": "false"}, "jakXshaNN": {"aniXt": "false"}, "jaagRi": {"aniXt": "false"}, "daridraa": {"aniXt": "false"}, "chakaasRiNN": {"aniXt": "false"}, "diidhiiNN": {"aniXt": "false"}, "veviiNN": {"aniXt": "false"}, "XshasaNN": {"aniXt": "false"}, "XshastiNN": {"aniXt": "false"}, "vashaNN": {"aniXt": "false"}, "nuNg": {"aniXt": "true"}, "hu": {"aniXt": "true"}, "bhii": {"aniXt": "true"}, "hrii": {"aniXt": "true"}, "pRi": {"aniXt": "true"}, "bhRiNc": {"aniXt": "true"}, "haaNg": {"aniXt": "true"}, "haaNN": {"aniXt": "true"}, "XdudaaNc": {"aniXt": "true"}, "dhaaNc": {"aniXt": "true"}, "NnijiNNraNN": {"aniXt": "true"}, "vijiNNraNN": {"aniXt": "true"}, "viXshlRiNN": {"aniXt": "true"}, "hRi": {"aniXt": "true"}, "sRi": {"aniXt": "true"}, "bhasaNN": {"aniXt": "false"}, "ki": {"aniXt": "true"}, "turaNN": {"aniXt": "false"}, "dhiXshaNN": {"aniXt": "false"}, "dhanaNN": {"aniXt": "false"}, "janaNN": {"aniXt": "false"}, "gaa": {"aniXt": "true"}, "XshivuNN": {"aniXt": "false"}, "srivuNN": {"aniXt": "false"}, "XshNnusuNN": {"aniXt": "false"}, "XshNnasuNN": {"aniXt": "false"}, "knasuNN": {"aniXt": "false"}, "vyuXshaNN": {"aniXt": "false"}, "pluXshaNN": {"aniXt": "false"}, "nRitiiNN": {"aniXt": "false"}, "trasiiNN": {"aniXt": "false"}, "kuthaNN": {"aniXt": "false"}, "gudhaNN": {"aniXt": "false"}, "kXshipaNN": {"aniXt": "true"}, "puXshpaNN": {"aniXt": "false"}, "timaNN": {"aniXt": "false"}, "tiimaNN": {"aniXt": "false"}, "XshXtimaNN": {"aniXt": "false"}, "XshXtiimaNN": {"aniXt": "false"}, "vriiXdaNN": {"aniXt": "false"}, "iXshaNN": {"aniXt": "false"}, "XshuhaNN": {"aniXt": "false"}, "jRiiXsh": {"aniXt": "false"}, "jhRiiXsh": {"aniXt": "false"}, "XshuuNgaNN": {"aniXt": "true"}, "duuNN": {"aniXt": "false"}, "diiNN": {"aniXt": "true"}, "dhiiNN": {"aniXt": "true"}, "miiNN": {"aniXt": "true"}, "riiNN": {"aniXt": "true"}, "liiNN": {"aniXt": "true"}, "vriiNN": {"aniXt": "true"}, "piiNN": {"aniXt": "true"}, "maaNN": {"aniXt": "true"}, "riiNg": {"aniXt": "true"}, "sho": {"aniXt": "true"}, "chho": {"aniXt": "true"}, "XshoNN": {"aniXt": "true"}, "doNN": {"aniXt": "true"}, "janiiNN": {"aniXt": "false"}, "diipiiNN": {"aniXt": "false"}, "tuuriiNN": {"aniXt": "false"}, "dhuuriiNN": {"aniXt": "false"}, "guuriiNN": {"aniXt": "false"}, "ghuuriiNN": {"aniXt": "false"}, "juuriiNN": {"aniXt": "false"}, "shuuriiNN": {"aniXt": "false"}, "chuuriiNN": {"aniXt": "false"}, "vaavRituNN": {"aniXt": "false"}, "klishaNN": {"aniXt": "false"}, "vaashRiNN": {"aniXt": "false"}, "shuchiNNr": {"aniXt": "false"}, "NnahaNN": {"aniXt": "true"}, "padaNN": {"aniXt": "true"}, "khidaNN": {"aniXt": "true"}, "yudhaNN": {"aniXt": "true"}, "rudhaNN": {"aniXt": "true"}, "sRijNN": {"aniXt": "true"}, "lishaNN": {"aniXt": "true"}, "raadhaNN": {"aniXt": "true"}, "vyadhaNN": {"aniXt": "true"}, "shuXshaNN": {"aniXt": "true"}, "tuXshaNN": {"aniXt": "true"}, "duXshaNN": {"aniXt": "true"}, "shakaNN": {"aniXt": "false"}, "krudhaNN": {"aniXt": "true"}, "kXshudhaNN": {"aniXt": "true"}, "shudhaNN": {"aniXt": "true"}, "XshidhuNN": {"aniXt": "true"}, "radhaNN": {"aniXt": "true"}, "NnashaNN": {"aniXt": "true"}, "druhaNN": {"aniXt": "true"}, "muhaNN": {"aniXt": "true"}, "XshNnuhaNN": {"aniXt": "true"}, "shamuNN": {"aniXt": "false"}, "tamuNN": {"aniXt": "false"}, "damuNN": {"aniXt": "false"}, "shramNN": {"aniXt": "false"}, "kXshamuuNN": {"aniXt": "true"}, "klamuNN": {"aniXt": "false"}, "asuNN": {"aniXt": "false"}, "yasuNN": {"aniXt": "false"}, "tasuNN": {"aniXt": "false"}, "dasuNN": {"aniXt": "false"}, "vasuNN": {"aniXt": "false"}, "basuNN": {"aniXt": "false"}, "bhasuNN": {"aniXt": "false"}, "byusaNN": {"aniXt": "false"}, "busaNN": {"aniXt": "false"}, "vusaNN": {"aniXt": "false"}, "pyuXshaNN": {"aniXt": "false"}, "pyusaNN": {"aniXt": "false"}, "kusaNN": {"aniXt": "false"}, "kushaNN": {"aniXt": "false"}, "kunsaNN": {"aniXt": "false"}, "kunshaNN": {"aniXt": "false"}, "musaNN": {"aniXt": "false"}, "masiiNN": {"aniXt": "false"}, "samiiNN": {"aniXt": "false"}, "uchaNN": {"aniXt": "false"}, "bhRishuNN": {"aniXt": "false"}, "bhranshuNN": {"aniXt": "false"}, "vRishNN": {"aniXt": "false"}, "kRishaNN": {"aniXt": "false"}, "NcitRiXshaaNN": {"aniXt": "false"}, "hRiXshaNN": {"aniXt": "false"}, "yupaNN": {"aniXt": "false"}, "rupaNN": {"aniXt": "false"}, "lupaNN": {"aniXt": "false"}, "lubhaNN": {"aniXt": "false"}, "kliduuNN": {"aniXt": "true"}, "NcimidNN": {"aniXt": "false"}, "NcikXshvidaaNN": {"aniXt": "false"}, "RidhuNN": {"aniXt": "false"}, "gRidhuNN": {"aniXt": "false"}, "suNN": {"aniXt": "true"}, "siNN": {"aniXt": "true"}, "shiNN": {"aniXt": "true"}, "miNc": {"aniXt": "true"}, "chiNN": {"aniXt": "true"}, "tRiNc": {"aniXt": "true"}, "kRiNN": {"aniXt": "true"}, "dhuNN": {"aniXt": "true"}, "dhuuNN": {"aniXt": "false"}, "Xtudu": {"aniXt": "true"}, "hi": {"aniXt": "true"}, "spRi": {"aniXt": "true"}, "shaklRiNN": {"aniXt": "true"}, "saadhaNN": {"aniXt": "true"}, "ashuuNN": {"aniXt": "true"}, "XshXtighaNN": {"aniXt": "false"}, "tikaNN": {"aniXt": "false"}, "tigaNN": {"aniXt": "false"}, "XshaghaNN": {"aniXt": "false"}, "NcidhRiXshaaNN": {"aniXt": "false"}, "danbhuNN": {"aniXt": "false"}, "ahaNN": {"aniXt": "false"}, "daghaNN": {"aniXt": "false"}, "riNN": {"aniXt": "true"}, "chiri": {"aniXt": "false"}, "jiri": {"aniXt": "false"}, "daashaNN": {"aniXt": "false"}, "dRiNN": {"aniXt": "true"}, "tudaNN": {"aniXt": "true"}, "NnudaNN": {"aniXt": "true"}, "dishaNN": {"aniXt": "true"}, "bhrasjNN": {"aniXt": "true"}, "RiXshiiNN": {"aniXt": "false"}, "juXshiiNN": {"aniXt": "false"}, "ovijiiNN": {"aniXt": "false"}, "olajiiNN": {"aniXt": "false"}, "olasjiiNN": {"aniXt": "false"}, "vraschNN": {"aniXt": "true"}, "vyachaNN": {"aniXt": "false"}, "RichhaNN": {"aniXt": "false"}, "michhaNN": {"aniXt": "false"}, "tvachaNN": {"aniXt": "false"}, "RichaNN": {"aniXt": "false"}, "ubjaNN": {"aniXt": "false"}, "ujjhaNN": {"aniXt": "false"}, "riphaNN": {"aniXt": "false"}, "rihaNN": {"aniXt": "false"}, "tRinpaNN": {"aniXt": "false"}, "tRiphaNN": {"aniXt": "false"}, "tRinphaNN": {"aniXt": "false"}, "dRinpaNN": {"aniXt": "false"}, "dRiphaNN": {"aniXt": "false"}, "dRinphaNN": {"aniXt": "false"}, "RiphaNN": {"aniXt": "false"}, "RinphaNN": {"aniXt": "false"}, "guphaNN": {"aniXt": "false"}, "gunphaNN": {"aniXt": "false"}, "ubhaNN": {"aniXt": "false"}, "unbhaNN": {"aniXt": "false"}, "chRitiiNN": {"aniXt": "false"}, "vidhaNN": {"aniXt": "false"}, "junaNN": {"aniXt": "false"}, "mRiXdaNN": {"aniXt": "false"}, "pRiXdaNN": {"aniXt": "false"}, "pRiNnaNN": {"aniXt": "false"}, "vRiNnaNN": {"aniXt": "false"}, "mRiNnaNN": {"aniXt": "false"}, "tuNnaNN": {"aniXt": "false"}, "muNnaNN": {"aniXt": "false"}, "kuNnaNN": {"aniXt": "false"}, "shunaNN": {"aniXt": "false"}, "druNnaNN": {"aniXt": "false"}, "ghuurNnaNN": {"aniXt": "false"}, "XshuraNN": {"aniXt": "false"}, "kuraNN": {"aniXt": "false"}, "khuraNN": {"aniXt": "false"}, "muraNN": {"aniXt": "false"}, "ghuraNN": {"aniXt": "false"}, "puraNN": {"aniXt": "false"}, "vRihuuNN": {"aniXt": "true"}, "bRihuuNN": {"aniXt": "true"}, "tRihuuNN": {"aniXt": "true"}, "stRihuuNN": {"aniXt": "true"}, "tRinhuuNN": {"aniXt": "true"}, "iXshuNN": {"aniXt": "false"}, "miXshaNN": {"aniXt": "false"}, "kilaNN": {"aniXt": "false"}, "chilaNN": {"aniXt": "false"}, "NnilaNN": {"aniXt": "false"}, "hilaNN": {"aniXt": "false"}, "shilaNN": {"aniXt": "false"}, "XshilaNN": {"aniXt": "false"}, "milaNN": {"aniXt": "false"}, "guXdaNN": {"aniXt": "false"}, "chhuraNN": {"aniXt": "false"}, "tuXtaNN": {"aniXt": "false"}, "chhuXtaNN": {"aniXt": "false"}, "juXtaNN": {"aniXt": "false"}, "kRiXdaNN": {"aniXt": "false"}, "kuXdaNN": {"aniXt": "false"}, "puXdaNN": {"aniXt": "false"}, "tuXdaNN": {"aniXt": "false"}, "thuXdaNN": {"aniXt": "false"}, "sthuXdaNN": {"aniXt": "false"}, "khuXdaNN": {"aniXt": "false"}, "chhuXdaNN": {"aniXt": "false"}, "sphuraNN": {"aniXt": "false"}, "sphulaNN": {"aniXt": "false"}, "spharaNN": {"aniXt": "false"}, "sphalaNN": {"aniXt": "false"}, "sphuXdaNN": {"aniXt": "false"}, "chuXdaNN": {"aniXt": "false"}, "vruXdaNN": {"aniXt": "false"}, "kruXdaNN": {"aniXt": "false"}, "bhRiXdaNN": {"aniXt": "false"}, "huXdaNN": {"aniXt": "false"}, "guriiNN": {"aniXt": "false"}, "NnuuNN": {"aniXt": "false"}, "kuuNN": {"aniXt": "false"}, "pRiNN": {"aniXt": "true"}, "mRiNN": {"aniXt": "true"}, "piNN": {"aniXt": "true"}, "dhiNN": {"aniXt": "true"}, "kXshiNN": {"aniXt": "false"}, "XshuuNN": {"aniXt": "false"}, "kRiiNN": {"aniXt": "false"}, "gRiiNN": {"aniXt": "false"}, "prachhaNN": {"aniXt": "true"}, "XtumasjoNN": {"aniXt": "true"}, "rujoNN": {"aniXt": "true"}, "bhujoNN": {"aniXt": "true"}, "chhupaNN": {"aniXt": "true"}, "rushaNN": {"aniXt": "true"}, "rishaNN": {"aniXt": "true"}, "spRishaNN": {"aniXt": "true"}, "vishaNN": {"aniXt": "true"}, "mRishaNN": {"aniXt": "true"}, "muchlRiNN": {"aniXt": "true"}, "luplRiNN": {"aniXt": "true"}, "vidlRiNN": {"aniXt": "false"}, "lipaNN": {"aniXt": "true"}, "XshichaNN": {"aniXt": "true"}, "kRitiiNN": {"aniXt": "false"}, "rudhiNN": {"aniXt": "true"}, "chhidiNN": {"aniXt": "true"}, "richiNN": {"aniXt": "true"}, "vichiNN": {"aniXt": "true"}, "XshudiNNr": {"aniXt": "true"}, "yujiNN": {"aniXt": "true"}, "chhRidiNNr": {"aniXt": "false"}, "tRidiNNr": {"aniXt": "false"}, "NciindhiiNN": {"aniXt": "false"}, "shiXshlRiNN": {"aniXt": "true"}, "piXshlRiNN": {"aniXt": "true"}, "bhanjoNN": {"aniXt": "true"}, "bhujaNN": {"aniXt": "true"}, "tRihaNN": {"aniXt": "false"}, "undiiNN": {"aniXt": "false"}, "anjuuNN": {"aniXt": "true"}, "tanchuuNN": {"aniXt": "true"}, "XshaNnuNN": {"aniXt": "false"}, "kXshaNnuNN": {"aniXt": "false"}, "kXshiNnuNN": {"aniXt": "false"}, "RiNnuNN": {"aniXt": "false"}, "tRiNnuNN": {"aniXt": "false"}, "ghRiNnuNN": {"aniXt": "false"}, "vanuNN": {"aniXt": "false"}, "manuNN": {"aniXt": "false"}, "XdukRiNc": {"aniXt": "true"}, "XdukRiiNc": {"aniXt": "true"}, "skuNN": {"aniXt": "true"}, "stanbhuNN": {"aniXt": "false"}, "stunbhuNN": {"aniXt": "false"}, "skanbhuNN": {"aniXt": "false"}, "skunbhuNN": {"aniXt": "false"}, "yuNN": {"aniXt": "true"}, "knuuNN": {"aniXt": "false"}, "druuNN": {"aniXt": "false"}, "luuNN": {"aniXt": "false"}, "stRiiNc": {"aniXt": "false"}, "kRiiNc": {"aniXt": "false"}, "vRiiNc": {"aniXt": "false"}, "dhuuNc": {"aniXt": "true"}, "shRiiNN": {"aniXt": "false"}, "pRiiNN": {"aniXt": "false"}, "vRiiNN": {"aniXt": "false"}, "bhRiiNN": {"aniXt": "false"}, "mRiiNN": {"aniXt": "false"}, "dRiiNN": {"aniXt": "false"}, "jRiiNN": {"aniXt": "false"}, "jhRiiNN": {"aniXt": "false"}, "nRiiNN": {"aniXt": "false"}, "Rii": {"aniXt": "false"}, "jyaaNN": {"aniXt": "true"}, "vliiNN": {"aniXt": "true"}, "bliiNN": {"aniXt": "true"}, "pliiNN": {"aniXt": "true"}, "bhriiNN": {"aniXt": "true"}, "kXshiiNN": {"aniXt": "true"}, "jNcaaNN": {"aniXt": "true"}, "vRiNg": {"aniXt": "false"}, "kunthaNN": {"aniXt": "false"}, "mRidaNN": {"aniXt": "false"}, "kuXshaNN": {"aniXt": "false"}, "klishuuNN": {"aniXt": "true"}, "ashaNN": {"aniXt": "false"}, "udhrasaNN": {"aniXt": "false"}, "viXshaNN": {"aniXt": "true"}, "pruXshaNN": {"aniXt": "false"}, "muXshaNN": {"aniXt": "false"}, "khachaNN": {"aniXt": "false"}, "khavaNN": {"aniXt": "false"}, "heXdhaNN": {"aniXt": "false"}, "grahNN": {"aniXt": "false"}}'
    dhaatu_store= json.loads(dhaatu_store_str)
    # Dhaatu formation is done to make sure Dhaatu name conditions are met (such as paXthaNN being interpreted as paXthNN)
    dhaatu_store= dict((''.join(Dhaatu(k)._data),v) for k,v in dhaatu_store.items())
    return dhaatu_store

global_dhaatu_store  = get_dhaatu_properties_dict()

def get_dhaatu_properties(string):
    global global_dhaatu_store
    #print ("Returning %s for %s " % (global_dhaatu_store[string],string))

    if string in global_dhaatu_store :
        return global_dhaatu_store[string]
    else:
        raise ValueError("%s not found as in dhaatu-store" % string)

def list_achpos(x):
    if not isinstance(x,list) :
        raise ValueError("input must be a list of strings")
    if any(j for j in x if not isinstance(j,str)):
        raise ValueError("input must be a list of strings")
    if x :
        listAchs = [i for i,k in enumerate(x) if k in ach()]
        return listAchs
    return None

def find_last_ach_pos(x):
    listAchs=list_achpos(x)
    if listAchs:
        return listAchs[-1]
    else:
        return None
    
def find_eldest_parent1_of_condition(node,cond):

    if node and node.get_parent1():
        if cond(node):
            return node.get_parent1()
        else:
            return find_eldest_parent1_of_condition(node.get_parent1(),cond)

    if cond(node):
        return node
    else:
        return None

def find_eldest_parent2_of_condition(node,cond):

    if node and node.get_parent2():
        if cond(node):
            return node.get_parent2()
        else:
            return find_eldest_parent2_of_condition(node.get_parent2(),cond)
    if cond(node):
        return node
    else:
        return None


def find_recentmost_child_of_condition(node,cond):
    
    if node and node._children:
        for child_ in node._children:
            # if cond is met, recursion ends
            if cond(child_):
                return child_
            
        # the function could be written in one pass loop but the second pass is 
        # implements bfs
        
        for child_ in node._children:
            #if cond is not met, recursion follows for child
            if not cond(child_): 
                foundChild_ = find_recentmost_child_of_condition(child_,cond)
                if foundChild_:
                    return foundChild_
    
    return None


def list_past_rules_applied (nd):
    """
    Returns list of rules applied so far for the node:nd
    """
    return [int(x['rule'].__name__.split("_")[-1]) for x in nd._output if 'rule' in x]

class Node:
    def __init__(self,data,parent1,parent2=None,inserted=False):
        if all ( not isinstance(data,x) for x in list(get_supported_types()) + [list] ):
            raise ValueError("Unsupported type %s" % type(data))
        self._children=[]
        self._inserted = inserted
        self._parent1 = parent1
        self._parent2 = parent2

        if self._parent1:
            self._parent1._add_child(self)

        if self._parent2:
            self._parent2._add_child(self)


        self._data =data
        self._output = [{'output':self._data.get_data(),'new':True}]


    def _add_child(self,ptr):
        self._children.append(ptr)

    def _assign_output_properties(self,rule,**inputs):
        # output is not changed
        old_output  = self.get_output()
        # no change in output -just rule and input update
        self._output.append({'rule':rule, 'inputs':{**{'state':self} , **inputs}, 'output':old_output })

    def set_output(self,rule,**kwargs):
        old_output = self.get_output()
        # call the function
        #print(rule.__name__ + ":" + str(kwargs))
        new_output = rule()(node=self,**kwargs)

        if isinstance(new_output,dict):
            if 'mutate' in new_output :
                if new_output['output'] != old_output :
                    if new_output ['mutate']:
                        self._output.append({'rule':rule,'inputs':{**{'state':self } , **kwargs},'output':new_output['output'] ,'new' :True})
                    else:
                        self._output.append({'rule':rule,'inputs':{**{'state':self } , **kwargs},'output':new_output['output']})

        else:
           if new_output != old_output:
              self._output.append({'rule':rule,'inputs':{**{'state':self} , **kwargs},'output':new_output })

    def get_output(self):
        return self._output[-1]['output']

    def get_parent1 (self):
        return self._parent1

    def get_parent2 (self):
        return self._parent2

    def has_sthaanii_it(self,itchar):
        """
        Parameters
        ----------
        itchar: character
            The character to be searched all through the output for it presence

        Raises
        ------

        Returns
        -------
        list
            boolean variable indicating whether it character exists anywhere in the history (sthaani) or not.
        """
        for x in self._output:
            if itchar in x['output']:
                return True
        return False



def get_supported_types ():
    return (Suffix,Dhaatu,Praatipadika)


def ach():
    return ("aa","ii","uu","Rii",'lRii') + pratyaahaara('a','ch')

def pratyaahaara(start,end):
    """
    @param  start : character - starting letter of the  pratyaahaara
    @param  end : character - ending letter of the  pratyaahaara
    @output :     list - characters in the pratyaahaara.
    """

    plist= ({'letters':("a","i",'ii',"u",'uu',),'marker':'Nn'},{'letters':('Ri','Rii','lRi','lRii'),'marker':'k'},
        {'letters':('e','o',),'marker':'Ng'},{'letters':('ai','au'),'marker':'ch'},{'letters':('h','y','v','r',),'marker':'Xt'},{'letters':('l',),'marker':'N'},
        {'letters':('Nc','m','Ng','Nn','n'),'marker':'m'},{'letters':('jh','bh'),'marker':'Nc'},{'letters':('gh','Xdh','dh'),'marker':'Xsh'},
        {'letters':('j','b','g','Xd','d',),'marker':'sh'},{'letters':('kh','ph','chh','Xth','th','ch','Xt','t',),'marker':'v'},
        {'letters':('k','p',),'marker':'y'},{'letters':('sh','Xsh','s',),'marker':'r'},{'letters':('h',),'marker':'l'},)
    markers = [p['marker'] for p in plist]
    if end not in markers:
        raise ValueError("Unkown marker: %s" % end)
    entries = [(i,j) for i,j in enumerate(plist) if end==j['marker']]
    if len(entries)>1:
        raise RuntimeError("Multiple entries not supported")
    else:
        not_found = True
        for i,entry in enumerate(plist):
            if start in entry['letters']:
                not_found = False
                results = plist[i:(entries[0][0]+1)]
                output = list(results[0]['letters'][results[0]['letters'].index(start):])
                for res_entry in results[1:]:
                    output = output+list(res_entry['letters'])
                return tuple(output)

        if not_found:
            raise ValueError("Unknown starting letter: %s" % start)


def anunaasika():
    return ("Ng","Nc","Nn","M","m","NN")

def chu():
    return ("ch","chh","j","jh","Nc")

def Xtu():
    return ("Xt","Xth","Xd","Xdh","Nn")


def intermediate_pratyayaaH():
    return ('shap','shyan','shlu','shnu',)

def unclassified_pratyayaaH():
    return ('sNNch','chlNN','taas','sya','aXt','iiXt','aaXt','yaasNNXt','sNNXt','nNNXt','anaNg','tarap','tamap') + intermediate_pratyayaaH()

def san_pratyayaaH():
    return ("san","kyach","kaamyach","kyaNg","kyaXsh",
            "kvip","Nnich","yaNg","yak","aaya",
            "iiyaNg","NniNg")

def tiNg_pratyayaaH():
    return aatmanepada_pratyayaaH()+parasmaidpada_pratyayaaH()

def parasmaidpada_pratyayaaH():
    return ("tip","tas","jhi","sip","thas","tha","mip",
            "vas","mas")

def aatmanepada_pratyayaaH():
    return ("ta","aataam","jha","thaas",
            "aathaam","dhvam","iXt","vahi","mahiNg")

def tachchhiilakRit_pratyayaaH():
    return {'tachchiila':('tRin','iXshNnuch','gsnu','knu')}

def tadasyaastyasmin_pratyayaaH():
    return {'tadasyaastyasmin':('matNNp',)}

def kRit_pratyayaaH():
    return (("Nnvul","lyuXt","aniiyar",
            "tavyat","tumun","tRich","ktvaa","Nnamul",
            "lyap","yat","Nnyat","kyap","ghaNc",'ach',
            "ap","ktin","a","yuch","shatRi","shaanach",
            "ka","Nnini","kvip") + niXshXthaa_pratyayaaH())  + reduce(lambda x ,y : x + y , tachchhiilakRit_pratyayaaH().values(),())

def niXshXthaa_pratyayaaH():
    return ("kta","ktavatu",)
    
def sarvanaama_praatipadikaaH():
    return ("sarva","tad",)

def upasargaaH():
    return ("abhi","prati","pari","upa","pra","apa",
            "sam","anu","ava","nis","nir","dus",
            "dur","vi","aaNg","ni","adhi","api",
            "ati","su","ut")

def strii_pratyayaaH():
    return ("Xtaap","Xdaap","chaap","Ngiip","NgiiXsh",
            "Nniin","uuNg","ti","XshyaNg","Xshpha")

def sup_pratyayaaH():
    return ('sNN', 'au','jas','am','auXt','shas','Xtaa','bhyaam','bhis','Nge','bhyaam',
        'bhyas','Ngasi','bhyaam','bhyas','Ngas','os','aam','Ngi','os','sup')


def taddhita_pratyayaaH ():
    return ('ghan', 'khaNc', 'aNn', 'a', 'tyak', 'chhas', 'kan', 'Xdya', 'vuk', 'chphaNc', 'ti', \
            'chhaNn', 'snaNc', 'Nca', 'XdhakaNc', 'NgiiXsh', 'airak', 'vun', 'NciXtha', 'Xtaap', \
                'yan', 'phak', 'mayaXt', 'lup', 'chha', 'yat', 'phiNc', 'Xshpha', 'vuNc', 'Xdhak',\
                    'Xdyat', 'ra', 'tyap', 'Ngiip', 'NcyaNg', 'phin', 'Xdmatup', 'ka', 'eNnya',\
                        'Xtyul', 'ila', 'Xthach', 'iNc', 'Xthak', 'sa', 'XshXthan', 'Nna',\
                            'phaNc', 'XdhaNc', 'XthaNc', 'valach', 'ini', 'Xdhrak', 'naNc',\
                                'Nnya', 'aNc', 'Xtyu', 'Ncya', 'XshyaNg', 'bhaktal', 'uuNg',\
                                    'Ngiin', 'ruupya', 'Xthap', 'yaNc', 'vidhal', 'Xdaap', 'chaap', \
                                        'Xdvalach', 'gha', 'matup', 'vyan', 'Xshphak', 'luk', 'tal', 'ma', 'ya', \
                                            'vatNNp','matNNp','Xdati', 'kRitvasNNch', \
                                            'kak', 'kha',) + reduce(lambda x ,y : x + y , tadasyaastyasmin_pratyayaaH().values(),())



def upadhaa(x):
    if not isinstance(x,list) or not all(isinstance(j,str) for j in x):
        raise ValueError("invalid input: %s" % x)
    if len(x)>=2:
        return len(x)-2
    else:
        raise ValueError("Insufficient length for upadhaa")

def node_upadhaa(node):
    if len(node.get_output())>2:
        achsInNode = [i for i, x in enumerate(node.get_output()) if x in ach()]
        if node.get_output()[-1] not in ach() :
            posUpdhaa= achsInNode[-1]
        elif len(achsInNode)>1:
            posUpdhaa = achsInNode[-2]
        else:
            posUpdhaa = None
        if posUpdhaa is not None:
           return {'pos':posUpdhaa, 'char':node.get_output()[posUpdhaa]}
    return None
    
def diirgha(x):
    if x =="a":
        return "aa"
    elif x == "i":
        return "ii"
    elif x == "u":
        return "uu"
    else:
        return x


def yaNn(x):
    if x =="i" or x=="ii":
        return "y"
    elif x == "u" or x=="uu":
        return "v"
    elif x == 'Ri' or x == 'Rii':
        return 'r'
    elif x == 'lRi' or x == 'lRii':
        return 'l'
    else:
        return x


def guNna(x):
    if x =="i" or x=="ii":
        return "e"
    elif x == "u" or x=="uu":
        return "o"
    else:
        return x

def vriddhi(x):
    if x =="a":
        return "aa"
    elif x == "i":
        return "ai"
    elif x == "e":
        return "ay"
    elif x == 'ii':
        return 'ai'
    elif x=='u':
        return 'au'
    elif x=='uu':
        return 'au'
    elif x=='Ri':
        return 'aar'
    elif x=='Rii':
        return 'aar'
    else:
        return x


def make_diirgha(x):

    if x not in ach():
        raise ValueError("must be an ach")

    if x in ('a','aa',):
        return "aa"
    if x in ("ii",'i',):
        return 'ii'
    if x in ('u','uu',):
        return 'uu'
    if x in ("Ri","Rii",):
        return 'Rii'
    if x in ('lRii','lRi',):
        return 'lRii'

def guna_letters_for_aat(x):

    if x in ( 'i', 'ii',):
        return ['e']
    if x in ('u', 'uu',):
        return ['o']
    if x in ('Ri', 'Rii', ):
        return ['a','r']
    if x in ('lRi', 'lRii',):
        return ['a','l']

    raise ValueError("No guNna support")

"""
The function to provide next possible suffixes. This includes non-suffixes such as lakaaras. The only goal is to provide the terminal condition of
a given suffix-string.
"""
def next_possible_suffixes(suffix_str):
    if not isinstance(suffix_str,str):
        raise ValueError("suffix input must be a str")

    subaadi = sup_pratyayaaH()
    taddhita = taddhita_pratyayaaH()
    suptaddhita = subaadi + taddhita
    tibaadi = tiNg_pratyayaaH()
    lakaara = lakaaras()
    kRidanta = kRit_pratyayaaH()

    allowed_next_values = tuple(subaadi + taddhita + tibaadi + lakaara + kRidanta )


    next_values_dict = {"Nnvul": suptaddhita , 'aniiyar':suptaddhita , 'tavyat': suptaddhita , 'tavya': suptaddhita ,
    "lyuXt":suptaddhita, 'kta': subaadi, 'ktavatu': subaadi, 'tumun': None, 'tRich':suptaddhita , 'tRin': kRidanta , 'ktvaa': None, 'Nnamul': subaadi,
    'lyap':subaadi, 'yat':suptaddhita,'Nnyat':suptaddhita, 'kyap':suptaddhita,'ghaNc':suptaddhita, 'ach':suptaddhita, 'ap':suptaddhita,
    'ktin':suptaddhita,'a': subaadi, 'yuch':suptaddhita, 'shatRi':suptaddhita, 'shaanach': suptaddhita, 'ka': suptaddhita,
    'Nnini':suptaddhita,'kvip':suptaddhita,'ghan':suptaddhita,'khaNc':suptaddhita,'aNn':subaadi,'a':subaadi,'tyak':subaadi,
    'chhas':subaadi,'kan':suptaddhita, 'Xthak':suptaddhita,'kan':suptaddhita,'Xdya':suptaddhita,'vuk':subaadi,'chphaNc':subaadi,'ti':subaadi,
    'chhaNn':subaadi, 'snaNc': subaadi, 'Nca': subaadi, 'XdhakaNc': subaadi, 'NgiiXsh': subaadi, 'airak': subaadi, 
    'vun': subaadi, 'NciXtha': subaadi, 'Xtaap': subaadi, 'yan': subaadi, 'phak': subaadi, 'mayaXt': subaadi, 
    'lup': subaadi, 'chha': subaadi,  'phiNc': subaadi, 'Xshpha': subaadi, 'vuNc': subaadi, 'Xdhak': subaadi, 
    'Xdyat': subaadi, 'ra': subaadi, 'tyap': subaadi, 'Ngiip': subaadi, 'NcyaNg': subaadi, 'phin': subaadi, 
    'Xdmatup': subaadi, 'eNnya': subaadi, 'Xtyul': subaadi, 'ila': subaadi, 'Xthach': subaadi, 'iNc': subaadi,
    'sa': subaadi, 'XshXthan': subaadi, 'Nna': subaadi, 'phaNc': subaadi, 'XdhaNc': subaadi, 'XthaNc': subaadi, 
    'valach': subaadi, 'ini': subaadi, 'Xdhrak': subaadi, 'naNc': subaadi, 'Nnya': subaadi, 'aNc': subaadi,
    'Xtyu': subaadi, 'Ncya': subaadi, 'XshyaNg': subaadi, 'bhaktal': subaadi, 'uuNg': subaadi, 'Ngiin': subaadi, 
    'ruupya': subaadi, 'Xthap': subaadi, 'yaNc': subaadi, 'vidhal': subaadi, 'Xdaap': subaadi, 'chaap': subaadi, 
    'Xdvalach': subaadi, 'gha': subaadi, 'vyan': subaadi, 'Xshphak': subaadi, 'luk': subaadi,
    'tal': subaadi, 'ma': subaadi, 'ya': subaadi, 'kak': subaadi, 'kha': subaadi,
    'sNN': None, 'au': None, 'jas': None, 'am': None, 'auXt': None, 'shas': None, 'Xtaa': None, 'bhyaam': None, 'bhis': None, 'Nge': None, 'bhyas': None, 'Ngasi': None, 'Ngas': None, 'os': None, 'aam': None, 'Ngi': None, 'sup': None,
    'tip': lakaara, 'tas': lakaara, 'jhi': lakaara, 'sip': lakaara, 'thas': lakaara, 'tha': lakaara, 'mip': lakaara, 'vas': lakaara, 'mas': lakaara, 'ta': lakaara, 'aataam': lakaara, 'jha': lakaara, 'thaas': lakaara, 'aathaam': lakaara, 'dhvam': lakaara, 'iXt': lakaara, 'vahi': lakaara, 'mahiNg': lakaara,
    'laXt':None, 'loXt':None, 'lRiXt':None ,'laNg':None ,'luNg':None ,'lRiNg':None ,'liNg1':None ,'liNg2':None ,'liXt':None ,'luXt':None,
    'vatNNp':suptaddhita, 'matNNp':suptaddhita
    }


    if suffix_str not in next_values_dict:
        raise ValueError("Unknown Suffix: '"+ suffix_str+"'")
    next_suffixes = next_values_dict[suffix_str]

    if next_suffixes is None:
        return tuple()
    elif any ( next_suffix not in allowed_next_values for next_suffix in next_suffixes):
        raise ValueError("Invalid next suffix")
    else:
        return next_suffixes


def shap_equivalents():
    return {'shyan':divaadigaNna(),'shnu':adaadigaNna(), 'shlu':juhotyaadi_dhaatus()}
    

def divaadigaNna():
    return ('NcimidNN','doNN',)


def adaadigaNna():
    return ('mRijNN','adNN','hanNN','dviXshNN')

def svaadigaNna():
    return ('chiNN',)

def juhotyaadi_dhaatus():
    return ('XdudaaNc',)

def nandyaadi_dhaatus():
    return ('XtunadNN',)

def grahaadi_dhaatus():
    return ('grahNN',)

def pachaadi_dhaatus():
    return ('XdupachNN','luuNN',)


def ghu_dhaatus():
    return ('XdudaaNc','deNN','daaNN','do')

def ach_permitted_temp_dhaatus():
    return ('mRijNN',)

def general_special_pairs ():
    return ( ( 7010030 , 3041080 ) , (7030840, 7020021) , ( 6010971, 6010940) , 
                         (7031030, 7010090) , ( 7021150,  7021170 ) )