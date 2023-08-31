import re,json


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




def all_pratyayas() :
    return kRit_pratyayaaH()+tiNg_pratyayaaH()+san_pratyayaaH()+strii_pratyayaaH()+sup_pratyayaaH()+taddhita_pratyayaaH() + unclassified_pratyayaaH()


class Suffix:
    def __init__(self,suffix,lakaara=None,linga=None):

        if lakaara is not None:
            if lakaara not in lakaaras():
                raise ValueError("Unknown lakaara")
        self._lakaara=lakaara


        if linga is not None:
            if linga not in (0,1,2):
                raise ValueError("Invalid linga")
        self._linga=linga


        if isinstance(suffix,str):
            self._suffix = parse_string(suffix)
        elif isinstance(suffix,list) and all(isinstance(j,str) for j in suffix):
            self._suffix= suffix
        else:
            raise ValueError("suffix must be a string")

        all_pratyayaaH = all_pratyayas()
        if ''.join(self._suffix) not in all_pratyayaaH:
            raise ValueError("Unknown suffix %s" % ''.join(self._suffix))

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


class Dhaatu:
    def __init__(self,data):
        self._data= data

    def get_data(self):
        return self._data


def get_dhaatu_properties_dict():
    dhaatu_store_str = '{"bhuu": {"aniXt": "false"}, "edh": {"aniXt": "false"}, "spardh": {"aniXt": "false"}, "gaadh": {"aniXt": "false"}, "baadh": {"aniXt": "false"}, "naadh": {"aniXt": "false"}, "naath": {"aniXt": "false"}, "dadh": {"aniXt": "false"}, "skund": {"aniXt": "false"}, "shvind": {"aniXt": "false"}, "vand": {"aniXt": "false"}, "bhand": {"aniXt": "false"}, "mand": {"aniXt": "false"}, "spand": {"aniXt": "false"}, "klind": {"aniXt": "false"}, "mud": {"aniXt": "false"}, "dad": {"aniXt": "false"}, "svad": {"aniXt": "false"}, "svard": {"aniXt": "false"}, "uurd": {"aniXt": "false"}, "kuurd": {"aniXt": "false"}, "khuurd": {"aniXt": "false"}, "guurd": {"aniXt": "false"}, "gud": {"aniXt": "false"}, "suud": {"aniXt": "false"}, "hraad": {"aniXt": "false"}, "hlaad": {"aniXt": "false"}, "svaad": {"aniXt": "false"}, "pard": {"aniXt": "false"}, "yat": {"aniXt": "false"}, "yut": {"aniXt": "false"}, "jut": {"aniXt": "false"}, "vith": {"aniXt": "false"}, "veth": {"aniXt": "false"}, "shranth": {"aniXt": "false"}, "granth": {"aniXt": "false"}, "katth": {"aniXt": "false"}, "at": {"aniXt": "false"}, "chit": {"aniXt": "false"}, "chyut": {"aniXt": "false"}, "shchut": {"aniXt": "false"}, "shchyut": {"aniXt": "false"}, "jyut": {"aniXt": "false"}, "manth": {"aniXt": "false"}, "kunth": {"aniXt": "false"}, "punth": {"aniXt": "false"}, "lunth": {"aniXt": "false"}, "sidh": {"aniXt": "true"}, "khaad": {"aniXt": "false"}, "khad": {"aniXt": "false"}, "bad": {"aniXt": "false"}, "gad": {"aniXt": "false"}, "rad": {"aniXt": "false"}, "nad": {"aniXt": "false"}, "ard": {"aniXt": "false"}, "nard": {"aniXt": "false"}, "gard": {"aniXt": "false"}, "tard": {"aniXt": "false"}, "kard": {"aniXt": "false"}, "khard": {"aniXt": "false"}, "ant": {"aniXt": "false"}, "and": {"aniXt": "false"}, "ind": {"aniXt": "false"}, "bind": {"aniXt": "false"}, "bhind": {"aniXt": "false"}, "gaNnXd": {"aniXt": "false"}, "nind": {"aniXt": "false"}, "nand": {"aniXt": "false"}, "chand": {"aniXt": "false"}, "trand": {"aniXt": "false"}, "kand": {"aniXt": "false"}, "krand": {"aniXt": "false"}, "kland": {"aniXt": "false"}, "shundh": {"aniXt": "false"}, "shiik": {"aniXt": "false"}, "siik": {"aniXt": "false"}, "lok": {"aniXt": "false"}, "shlok": {"aniXt": "false"}, "srok": {"aniXt": "false"}, "drek": {"aniXt": "false"}, "dhrek": {"aniXt": "false"}, "rek": {"aniXt": "false"}, "sek": {"aniXt": "false"}, "srek": {"aniXt": "false"}, "sraNgk": {"aniXt": "false"}, "shraNgk": {"aniXt": "false"}, "shlaNgk": {"aniXt": "false"}, "shaNgk": {"aniXt": "false"}, "aNgk": {"aniXt": "false"}, "vaNgk": {"aniXt": "false"}, "maNgk": {"aniXt": "false"}, "kak": {"aniXt": "false"}, "kuk": {"aniXt": "false"}, "vRik": {"aniXt": "false"}, "chak": {"aniXt": "false"}, "kaNgk": {"aniXt": "false"}, "shvaNgk": {"aniXt": "false"}, "traNgk": {"aniXt": "false"}, "Xdhauk": {"aniXt": "false"}, "trauk": {"aniXt": "false"}, "XshvaXshk": {"aniXt": "false"}, "vask": {"aniXt": "false"}, "mask": {"aniXt": "false"}, "Xtik": {"aniXt": "false"}, "Xtiik": {"aniXt": "false"}, "tik": {"aniXt": "false"}, "tiik": {"aniXt": "false"}, "raNggh": {"aniXt": "false"}, "laNggh": {"aniXt": "false"}, "svaNgk": {"aniXt": "false"}, "aNggh": {"aniXt": "false"}, "vaNggh": {"aniXt": "false"}, "maNggh": {"aniXt": "false"}, "raagh": {"aniXt": "false"}, "laagh": {"aniXt": "false"}, "draagh": {"aniXt": "false"}, "dhraagh": {"aniXt": "false"}, "shlaagh": {"aniXt": "false"}, "phakk": {"aniXt": "false"}, "tak": {"aniXt": "false"}, "taNgk": {"aniXt": "false"}, "bukk": {"aniXt": "false"}, "shuk": {"aniXt": "false"}, "kakh": {"aniXt": "false"}, "okh": {"aniXt": "false"}, "raakh": {"aniXt": "false"}, "laakh": {"aniXt": "false"}, "draakh": {"aniXt": "false"}, "dhraakh": {"aniXt": "false"}, "shaakh": {"aniXt": "false"}, "shlaakh": {"aniXt": "false"}, "ukh": {"aniXt": "false"}, "uNgkh": {"aniXt": "false"}, "vakh": {"aniXt": "false"}, "vaNgkh": {"aniXt": "false"}, "makh": {"aniXt": "false"}, "maNgkh": {"aniXt": "false"}, "nakh": {"aniXt": "false"}, "naNgkh": {"aniXt": "false"}, "rakh": {"aniXt": "false"}, "raNgkh": {"aniXt": "false"}, "lakh": {"aniXt": "false"}, "laNgkh": {"aniXt": "false"}, "ikh": {"aniXt": "false"}, "iNgkh": {"aniXt": "false"}, "iikh": {"aniXt": "false"}, "iiNgkh": {"aniXt": "false"}, "valg": {"aniXt": "false"}, "raNgg": {"aniXt": "false"}, "laNgg": {"aniXt": "false"}, "aNgg": {"aniXt": "false"}, "vaNgg": {"aniXt": "false"}, "maNgg": {"aniXt": "false"}, "taNgg": {"aniXt": "false"}, "tvaNgg": {"aniXt": "false"}, "traNgg": {"aniXt": "false"}, "shraNgg": {"aniXt": "false"}, "shlaNgg": {"aniXt": "false"}, "iNgg": {"aniXt": "false"}, "riNgg": {"aniXt": "false"}, "liNgg": {"aniXt": "false"}, "muNgkh": {"aniXt": "false"}, "thaNgk": {"aniXt": "false"}, "rikh": {"aniXt": "false"}, "riNgkh": {"aniXt": "false"}, "likh": {"aniXt": "false"}, "liNgkh": {"aniXt": "false"}, "trakh": {"aniXt": "false"}, "triNgkh": {"aniXt": "false"}, "shiNgkh": {"aniXt": "false"}, "yuNgg": {"aniXt": "false"}, "juNgg": {"aniXt": "false"}, "buNgg": {"aniXt": "false"}, "vuNgg": {"aniXt": "false"}, "ghagh": {"aniXt": "false"}, "ghaggh": {"aniXt": "false"}, "daNggh": {"aniXt": "false"}, "shiNggh": {"aniXt": "false"}, "argh": {"aniXt": "false"}, "varch": {"aniXt": "false"}, "sach": {"aniXt": "false"}, "loch": {"aniXt": "false"}, "shach": {"aniXt": "false"}, "shvach": {"aniXt": "false"}, "shvaNcch": {"aniXt": "false"}, "kach": {"aniXt": "false"}, "kaNcch": {"aniXt": "false"}, "kaaNcch": {"aniXt": "false"}, "mach": {"aniXt": "false"}, "muNcch": {"aniXt": "false"}, "maNcch": {"aniXt": "false"}, "paNcch": {"aniXt": "false"}, "stuch": {"aniXt": "false"}, "Rij": {"aniXt": "false"}, "RiNcj": {"aniXt": "false"}, "bhRij": {"aniXt": "false"}, "ej": {"aniXt": "false"}, "bhrej": {"aniXt": "false"}, "bhraaj": {"aniXt": "false"}, "rej": {"aniXt": "false"}, "iij": {"aniXt": "false"}, "iiNcj": {"aniXt": "false"}, "viij": {"aniXt": "false"}, "shuch": {"aniXt": "false"}, "kuch": {"aniXt": "false"}, "kuNcch": {"aniXt": "false"}, "kruNcch": {"aniXt": "false"}, "luNcch": {"aniXt": "false"}, "aNcch": {"aniXt": "false"}, "vaNcch": {"aniXt": "false"}, "chaNcch": {"aniXt": "false"}, "taNcch": {"aniXt": "true"}, "tvaNcch": {"aniXt": "false"}, "mruNcch": {"aniXt": "false"}, "mluNcch": {"aniXt": "false"}, "mruch": {"aniXt": "false"}, "mluch": {"aniXt": "false"}, "gruch": {"aniXt": "false"}, "gluch": {"aniXt": "false"}, "kuj": {"aniXt": "false"}, "khuj": {"aniXt": "false"}, "gluNcch": {"aniXt": "false"}, "sajj": {"aniXt": "false"}, "guj": {"aniXt": "false"}, "guNcj": {"aniXt": "false"}, "arch": {"aniXt": "false"}, "mlechchh": {"aniXt": "false"}, "lachchh": {"aniXt": "false"}, "laaNcchh": {"aniXt": "false"}, "vaaNcchh": {"aniXt": "false"}, "aaNcchh": {"aniXt": "false"}, "hriichchh": {"aniXt": "false"}, "huurchh": {"aniXt": "false"}, "muurchh": {"aniXt": "false"}, "sphuurchh": {"aniXt": "false"}, "yuchchh": {"aniXt": "false"}, "uNcchh": {"aniXt": "false"}, "uchchh": {"aniXt": "false"}, "dhraj": {"aniXt": "false"}, "dhraNcj": {"aniXt": "false"}, "vraj": {"aniXt": "false"}, "vraNcj": {"aniXt": "false"}, "dhRij": {"aniXt": "false"}, "dhRiNcj": {"aniXt": "false"}, "dhvaj": {"aniXt": "false"}, "dhvaNcj": {"aniXt": "false"}, "dhrij": {"aniXt": "false"}, "kuuj": {"aniXt": "false"}, "kuNcj": {"aniXt": "false"}, "arj": {"aniXt": "false"}, "sarj": {"aniXt": "false"}, "garj": {"aniXt": "false"}, "tarj": {"aniXt": "false"}, "karj": {"aniXt": "false"}, "kharj": {"aniXt": "false"}, "aj": {"aniXt": "false"}, "tej": {"aniXt": "false"}, "khaj": {"aniXt": "false"}, "kaj": {"aniXt": "false"}, "khaNcj": {"aniXt": "false"}, "sphuurjXtu": {"aniXt": "false"}, "kXshi": {"aniXt": "false"}, "kXshiij": {"aniXt": "false"}, "laj": {"aniXt": "false"}, "laNcj": {"aniXt": "false"}, "laaj": {"aniXt": "false"}, "laaNcj": {"aniXt": "false"}, "jaj": {"aniXt": "false"}, "jaNcj": {"aniXt": "false"}, "tuj": {"aniXt": "false"}, "tuNcj": {"aniXt": "false"}, "gaj": {"aniXt": "false"}, "gaNcj": {"aniXt": "false"}, "gRij": {"aniXt": "false"}, "gRiNcj": {"aniXt": "false"}, "muj": {"aniXt": "false"}, "muNcj": {"aniXt": "false"}, "vaj": {"aniXt": "false"}, "aXtXt": {"aniXt": "false"}, "veXshXt": {"aniXt": "false"}, "cheXshXt": {"aniXt": "false"}, "goXshXt": {"aniXt": "false"}, "loXshXt": {"aniXt": "false"}, "ghaXtXt": {"aniXt": "false"}, "sphuXt": {"aniXt": "false"}, "aNnXth": {"aniXt": "false"}, "vaNnXth": {"aniXt": "false"}, "maNnXth": {"aniXt": "false"}, "kaNnXth": {"aniXt": "false"}, "muNnXth": {"aniXt": "false"}, "heXth": {"aniXt": "false"}, "eXth": {"aniXt": "false"}, "hiNnXd": {"aniXt": "false"}, "huNnXd": {"aniXt": "false"}, "kuNnXd": {"aniXt": "false"}, "vaNnXd": {"aniXt": "false"}, "maNnXd": {"aniXt": "false"}, "bhaNnXd": {"aniXt": "false"}, "piNnXd": {"aniXt": "false"}, "muNnXd": {"aniXt": "false"}, "tuNnXd": {"aniXt": "false"}, "sphuNnXd": {"aniXt": "false"}, "chaNnXd": {"aniXt": "false"}, "shaNnXd": {"aniXt": "false"}, "taNnXd": {"aniXt": "false"}, "paNnXd": {"aniXt": "false"}, "kaNnXd": {"aniXt": "false"}, "khaNnXd": {"aniXt": "false"}, "heXd": {"aniXt": "false"}, "hoXd": {"aniXt": "false"}, "baaXd": {"aniXt": "false"}, "vaaXd": {"aniXt": "false"}, "draaXd": {"aniXt": "false"}, "dhraaXd": {"aniXt": "false"}, "shaaXd": {"aniXt": "false"}, "shauXt": {"aniXt": "false"}, "yauXt": {"aniXt": "false"}, "mreXt": {"aniXt": "false"}, "mreXd": {"aniXt": "false"}, "mleXt": {"aniXt": "false"}, "chaXt": {"aniXt": "false"}, "kaXt": {"aniXt": "false"}, "aXt": {"aniXt": "false"}, "paXt": {"aniXt": "false"}, "raXt": {"aniXt": "false"}, "laXt": {"aniXt": "false"}, "shaXt": {"aniXt": "false"}, "vaXt": {"aniXt": "false"}, "kiXt": {"aniXt": "false"}, "khiXt": {"aniXt": "false"}, "shiXt": {"aniXt": "false"}, "siXt": {"aniXt": "false"}, "jaXt": {"aniXt": "false"}, "jhaXt": {"aniXt": "false"}, "bhaXt": {"aniXt": "false"}, "taXt": {"aniXt": "false"}, "khaXt": {"aniXt": "false"}, "naXt": {"aniXt": "false"}, "piXt": {"aniXt": "false"}, "haXt": {"aniXt": "false"}, "saXt": {"aniXt": "false"}, "luXt": {"aniXt": "false"}, "luXd": {"aniXt": "false"}, "chiXt": {"aniXt": "false"}, "viXt": {"aniXt": "false"}, "biXt": {"aniXt": "false"}, "hiXt": {"aniXt": "false"}, "iXt": {"aniXt": "false"}, "kuNnXt": {"aniXt": "false"}, "muXd": {"aniXt": "false"}, "pruXd": {"aniXt": "false"}, "muXt": {"aniXt": "false"}, "puXt": {"aniXt": "false"}, "chuNnXd": {"aniXt": "false"}, "puNnXd": {"aniXt": "false"}, "ruNnXt": {"aniXt": "false"}, "luNnXt": {"aniXt": "false"}, "ruNnXth": {"aniXt": "false"}, "luNnXth": {"aniXt": "false"}, "ruNnXd": {"aniXt": "false"}, "luNnXd": {"aniXt": "false"}, "vaNnXt": {"aniXt": "false"}, "baNnXt": {"aniXt": "false"}, "sphuXts": {"aniXt": "false"}, "sphuNnXt": {"aniXt": "false"}, "paXth": {"aniXt": "false"}, "vaXth": {"aniXt": "false"}, "baXth": {"aniXt": "false"}, "maXth": {"aniXt": "false"}, "kaXth": {"aniXt": "false"}, "raXth": {"aniXt": "false"}, "haXth": {"aniXt": "false"}, "ruXth": {"aniXt": "false"}, "luXth": {"aniXt": "false"}, "uuXth": {"aniXt": "false"}, "uXth": {"aniXt": "false"}, "piXth": {"aniXt": "false"}, "shaXth": {"aniXt": "false"}, "shuXth": {"aniXt": "false"}, "shuuXth": {"aniXt": "false"}, "kuNnXth": {"aniXt": "false"}, "shuNnXth": {"aniXt": "false"}, "chuXdXd": {"aniXt": "false"}, "aXdXd": {"aniXt": "false"}, "kaXdXd": {"aniXt": "false"}, "kriiXd": {"aniXt": "false"}, "tuXd": {"aniXt": "false"}, "tuuXd": {"aniXt": "false"}, "huXd": {"aniXt": "false"}, "huuXd": {"aniXt": "false"}, "rauXd": {"aniXt": "false"}, "roXd": {"aniXt": "false"}, "loXd": {"aniXt": "false"}, "aXd": {"aniXt": "false"}, "laXd": {"aniXt": "false"}, "lal": {"aniXt": "false"}, "kaXd": {"aniXt": "false"}, "tip": {"aniXt": "true"}, "tep": {"aniXt": "false"}, "stip": {"aniXt": "false"}, "step": {"aniXt": "false"}, "glep": {"aniXt": "false"}, "vepXta": {"aniXt": "false"}, "kep": {"aniXt": "false"}, "gep": {"aniXt": "false"}, "mep": {"aniXt": "false"}, "rep": {"aniXt": "false"}, "lep": {"aniXt": "false"}, "hep": {"aniXt": "false"}, "dhep": {"aniXt": "false"}, "trapt": {"aniXt": "true"}, "kamp": {"aniXt": "false"}, "ramb": {"aniXt": "false"}, "lamb": {"aniXt": "false"}, "amb": {"aniXt": "false"}, "kab": {"aniXt": "false"}, "kliib": {"aniXt": "false"}, "kXshiib": {"aniXt": "false"}, "kXshiiv": {"aniXt": "false"}, "shiibh": {"aniXt": "false"}, "biibh": {"aniXt": "false"}, "chiibh": {"aniXt": "false"}, "rebh": {"aniXt": "false"}, "ambh": {"aniXt": "false"}, "rambh": {"aniXt": "false"}, "lambh": {"aniXt": "false"}, "stambh": {"aniXt": "false"}, "skambh": {"aniXt": "false"}, "jabh": {"aniXt": "false"}, "jRimbh": {"aniXt": "false"}, "shalbh": {"aniXt": "false"}, "valbh": {"aniXt": "false"}, "galbh": {"aniXt": "false"}, "shrambh": {"aniXt": "false"}, "srambh": {"aniXt": "false"}, "stubh": {"aniXt": "false"}, "gup": {"aniXt": "false"}, "dhuup": {"aniXt": "false"}, "jap": {"aniXt": "false"}, "jalp": {"aniXt": "false"}, "chap": {"aniXt": "false"}, "sap": {"aniXt": "false"}, "rap": {"aniXt": "false"}, "lap": {"aniXt": "false"}, "chup": {"aniXt": "false"}, "tup": {"aniXt": "false"}, "tump": {"aniXt": "false"}, "trup": {"aniXt": "false"}, "trump": {"aniXt": "false"}, "tuph": {"aniXt": "false"}, "tumph": {"aniXt": "false"}, "truph": {"aniXt": "false"}, "trumph": {"aniXt": "false"}, "parp": {"aniXt": "false"}, "raph": {"aniXt": "false"}, "ramph": {"aniXt": "false"}, "arb": {"aniXt": "false"}, "parb": {"aniXt": "false"}, "larb": {"aniXt": "false"}, "barb": {"aniXt": "false"}, "marb": {"aniXt": "false"}, "karb": {"aniXt": "false"}, "kharb": {"aniXt": "false"}, "garb": {"aniXt": "false"}, "sharb": {"aniXt": "false"}, "sarb": {"aniXt": "false"}, "charb": {"aniXt": "false"}, "kumb": {"aniXt": "false"}, "lumb": {"aniXt": "false"}, "tumb": {"aniXt": "false"}, "chumb": {"aniXt": "false"}, "sRibh": {"aniXt": "false"}, "sRimbh": {"aniXt": "false"}, "sibh": {"aniXt": "false"}, "simbh": {"aniXt": "false"}, "shubh": {"aniXt": "false"}, "shumbh": {"aniXt": "false"}, "ghiNnNn": {"aniXt": "false"}, "ghuNnNn": {"aniXt": "false"}, "ghRiNnNn": {"aniXt": "false"}, "ghuNn": {"aniXt": "false"}, "ghuurNn": {"aniXt": "false"}, "paNn": {"aniXt": "false"}, "pan": {"aniXt": "false"}, "bhaam": {"aniXt": "false"}, "kXshamk": {"aniXt": "true"}, "kam": {"aniXt": "false"}, "aNn": {"aniXt": "false"}, "raNn": {"aniXt": "false"}, "vaNn": {"aniXt": "false"}, "bhaNn": {"aniXt": "false"}, "maNn": {"aniXt": "false"}, "kaNn": {"aniXt": "false"}, "kvaNn": {"aniXt": "false"}, "vraNn": {"aniXt": "false"}, "bhraNn": {"aniXt": "false"}, "dhvaNn": {"aniXt": "false"}, "dhaNn": {"aniXt": "false"}, "oNn": {"aniXt": "false"}, "shoNn": {"aniXt": "false"}, "shroNn": {"aniXt": "false"}, "shloNn": {"aniXt": "false"}, "paiNn": {"aniXt": "false"}, "praiNn": {"aniXt": "false"}, "dhraNn": {"aniXt": "false"}, "baNn": {"aniXt": "false"}, "kan": {"aniXt": "false"}, "stan": {"aniXt": "false"}, "van": {"aniXt": "false"}, "san": {"aniXt": "false"}, "am": {"aniXt": "false"}, "dram": {"aniXt": "false"}, "hamm": {"aniXt": "false"}, "miim": {"aniXt": "false"}, "cham": {"aniXt": "false"}, "chham": {"aniXt": "false"}, "jam": {"aniXt": "false"}, "jham": {"aniXt": "false"}, "jim": {"aniXt": "false"}, "kram": {"aniXt": "false"}, "ay": {"aniXt": "false"}, "vay": {"aniXt": "false"}, "pay": {"aniXt": "false"}, "may": {"aniXt": "false"}, "chay": {"aniXt": "false"}, "tay": {"aniXt": "false"}, "nay": {"aniXt": "false"}, "day": {"aniXt": "false"}, "ray": {"aniXt": "false"}, "lay": {"aniXt": "false"}, "uuy": {"aniXt": "false"}, "puuy": {"aniXt": "false"}, "knuuy": {"aniXt": "false"}, "kXshmaay": {"aniXt": "false"}, "sphaay": {"aniXt": "false"}, "pyaayo": {"aniXt": "false"}, "taay": {"aniXt": "false"}, "shal": {"aniXt": "false"}, "val": {"aniXt": "false"}, "vall": {"aniXt": "false"}, "mal": {"aniXt": "false"}, "mall": {"aniXt": "false"}, "bhal": {"aniXt": "false"}, "bhall": {"aniXt": "false"}, "kal": {"aniXt": "false"}, "kall": {"aniXt": "false"}, "tev": {"aniXt": "false"}, "dev": {"aniXt": "false"}, "sev": {"aniXt": "false"}, "gev": {"aniXt": "false"}, "glev": {"aniXt": "false"}, "pev": {"aniXt": "false"}, "mev": {"aniXt": "false"}, "mlev": {"aniXt": "false"}, "shev": {"aniXt": "false"}, "khev": {"aniXt": "false"}, "plev": {"aniXt": "false"}, "kev": {"aniXt": "false"}, "rev": {"aniXt": "false"}, "mavy": {"aniXt": "false"}, "suurkXshy": {"aniXt": "false"}, "iirkXshy": {"aniXt": "false"}, "iirXshy": {"aniXt": "false"}, "hay": {"aniXt": "false"}, "shuchy": {"aniXt": "false"}, "chuchy": {"aniXt": "false"}, "hary": {"aniXt": "false"}, "al": {"aniXt": "false"}, "phalNca": {"aniXt": "false"}, "miil": {"aniXt": "false"}, "shmiil": {"aniXt": "false"}, "smiil": {"aniXt": "false"}, "kXshmiil": {"aniXt": "false"}, "piil": {"aniXt": "false"}, "niil": {"aniXt": "false"}, "shiil": {"aniXt": "false"}, "kiil": {"aniXt": "false"}, "kuul": {"aniXt": "false"}, "shuul": {"aniXt": "false"}, "tuul": {"aniXt": "false"}, "puul": {"aniXt": "false"}, "muul": {"aniXt": "false"}, "phal": {"aniXt": "false"}, "chull": {"aniXt": "false"}, "phull": {"aniXt": "false"}, "chill": {"aniXt": "false"}, "til": {"aniXt": "false"}, "till": {"aniXt": "false"}, "vel": {"aniXt": "false"}, "chel": {"aniXt": "false"}, "kel": {"aniXt": "false"}, "khel": {"aniXt": "false"}, "kXshvel": {"aniXt": "false"}, "vell": {"aniXt": "false"}, "vehl": {"aniXt": "false"}, "pel": {"aniXt": "false"}, "phel": {"aniXt": "false"}, "shel": {"aniXt": "false"}, "sel": {"aniXt": "false"}, "skhal": {"aniXt": "false"}, "khal": {"aniXt": "false"}, "gal": {"aniXt": "false"}, "sal": {"aniXt": "false"}, "dal": {"aniXt": "false"}, "shval": {"aniXt": "false"}, "shvall": {"aniXt": "false"}, "khol": {"aniXt": "false"}, "khor": {"aniXt": "false"}, "dhor": {"aniXt": "false"}, "tsar": {"aniXt": "false"}, "kmar": {"aniXt": "false"}, "abhr": {"aniXt": "false"}, "vabhr": {"aniXt": "false"}, "mabhr": {"aniXt": "false"}, "char": {"aniXt": "false"}, "XshXthiv": {"aniXt": "false"}, "ji": {"aniXt": "false"}, "jiiv": {"aniXt": "false"}, "piiv": {"aniXt": "false"}, "miiv": {"aniXt": "false"}, "tiiv": {"aniXt": "false"}, "niiv": {"aniXt": "false"}, "kXshev": {"aniXt": "false"}, "uurv": {"aniXt": "false"}, "tuurv": {"aniXt": "false"}, "thuurv": {"aniXt": "false"}, "duurv": {"aniXt": "false"}, "dhuurv": {"aniXt": "false"}, "guurv": {"aniXt": "false"}, "muurv": {"aniXt": "false"}, "puurv": {"aniXt": "false"}, "parv": {"aniXt": "false"}, "marv": {"aniXt": "false"}, "charv": {"aniXt": "false"}, "bharv": {"aniXt": "false"}, "bharb": {"aniXt": "false"}, "bharbh": {"aniXt": "false"}, "karv": {"aniXt": "false"}, "kharv": {"aniXt": "false"}, "garv": {"aniXt": "false"}, "arv": {"aniXt": "false"}, "sharv": {"aniXt": "false"}, "sarv": {"aniXt": "false"}, "inv": {"aniXt": "false"}, "pinv": {"aniXt": "false"}, "minv": {"aniXt": "false"}, "ninv": {"aniXt": "false"}, "sinv": {"aniXt": "false"}, "hinv": {"aniXt": "false"}, "dinv": {"aniXt": "false"}, "dhinv": {"aniXt": "false"}, "jinv": {"aniXt": "false"}, "rinv": {"aniXt": "false"}, "ranv": {"aniXt": "false"}, "dhanv": {"aniXt": "false"}, "kRinv": {"aniXt": "false"}, "mav": {"aniXt": "false"}, "av": {"aniXt": "false"}, "dhaav": {"aniXt": "false"}, "dhukXsh": {"aniXt": "false"}, "dhikXsh": {"aniXt": "false"}, "vRikXsh": {"aniXt": "false"}, "shikXsh": {"aniXt": "false"}, "bhikXsh": {"aniXt": "false"}, "klesh": {"aniXt": "false"}, "dakXsh": {"aniXt": "false"}, "diikXsh": {"aniXt": "false"}, "iikXsh": {"aniXt": "false"}, "iiXsh": {"aniXt": "false"}, "bhaaXsh": {"aniXt": "false"}, "varXsh": {"aniXt": "false"}, "geXsh": {"aniXt": "false"}, "gleXsh": {"aniXt": "false"}, "peXsh": {"aniXt": "false"}, "eXsh": {"aniXt": "false"}, "yeXsh": {"aniXt": "false"}, "jeXsh": {"aniXt": "false"}, "neXsh": {"aniXt": "false"}, "preXsh": {"aniXt": "false"}, "reXsh": {"aniXt": "false"}, "heXsh": {"aniXt": "false"}, "hreXsh": {"aniXt": "false"}, "kaas": {"aniXt": "false"}, "bhaas": {"aniXt": "false"}, "naas": {"aniXt": "false"}, "raas": {"aniXt": "false"}, "nas": {"aniXt": "false"}, "bhyas": {"aniXt": "false"}, "shaMs": {"aniXt": "false"}, "gras": {"aniXt": "false"}, "glas": {"aniXt": "false"}, "iih": {"aniXt": "false"}, "vaMh": {"aniXt": "false"}, "maMh": {"aniXt": "false"}, "ah": {"aniXt": "false"}, "garh": {"aniXt": "false"}, "galh": {"aniXt": "false"}, "barh": {"aniXt": "false"}, "balh": {"aniXt": "false"}, "varh": {"aniXt": "false"}, "valh": {"aniXt": "false"}, "plih": {"aniXt": "false"}, "veh": {"aniXt": "false"}, "jeh": {"aniXt": "false"}, "baah": {"aniXt": "false"}, "draah": {"aniXt": "false"}, "kaash": {"aniXt": "false"}, "uuh": {"aniXt": "false"}, "gaah": {"aniXt": "true"}, "gRih": {"aniXt": "true"}, "glah": {"aniXt": "false"}, "ghugha": {"aniXt": "true"}, "ghuXsh": {"aniXt": "false"}, "ghuXshgha": {"aniXt": "false"}, "akXsh": {"aniXt": "true"}, "takXsh": {"aniXt": "false"}, "tvakXsh": {"aniXt": "true"}, "ukXsh": {"aniXt": "false"}, "rakXsh": {"aniXt": "false"}, "nikXsh": {"aniXt": "false"}, "trakXsh": {"aniXt": "false"}, "strakXsh": {"aniXt": "false"}, "tRikXsh": {"aniXt": "false"}, "stRikXsh": {"aniXt": "false"}, "nakXsh": {"aniXt": "false"}, "vakXsh": {"aniXt": "false"}, "mRikXsh": {"aniXt": "false"}, "mrakXsh": {"aniXt": "false"}, "pakXsh": {"aniXt": "false"}, "suurkXsh": {"aniXt": "false"}, "sarkXsh": {"aniXt": "false"}, "kaaNgkXsh": {"aniXt": "false"}, "vaaNgkXsh": {"aniXt": "false"}, "maaNgkXsh": {"aniXt": "false"}, "draaNgkXsh": {"aniXt": "false"}, "dhraaNgkXsh": {"aniXt": "false"}, "dhvaaNgkXsh": {"aniXt": "false"}, "dhmaaNgkXsh": {"aniXt": "false"}, "chuuXsh": {"aniXt": "false"}, "tuuXsh": {"aniXt": "false"}, "puuXsh": {"aniXt": "false"}, "muuXsh": {"aniXt": "false"}, "luuXsh": {"aniXt": "false"}, "ruuXsh": {"aniXt": "false"}, "shuuXsh": {"aniXt": "false"}, "suuXsh": {"aniXt": "false"}, "yuuXsh": {"aniXt": "false"}, "juuXsh": {"aniXt": "false"}, "bhuuXsh": {"aniXt": "false"}, "taMs": {"aniXt": "false"}, "uuXsh": {"aniXt": "false"}, "kaXsh": {"aniXt": "false"}, "khaXsh": {"aniXt": "false"}, "shiXsh": {"aniXt": "false"}, "jaXsh": {"aniXt": "false"}, "jhaXsh": {"aniXt": "false"}, "shaXsh": {"aniXt": "false"}, "vaXsh": {"aniXt": "false"}, "maXsh": {"aniXt": "false"}, "ruXsh": {"aniXt": "false"}, "riXsh": {"aniXt": "false"}, "bhaXsh": {"aniXt": "false"}, "uXsh": {"aniXt": "false"}, "jiXsh": {"aniXt": "true"}, "viXsh": {"aniXt": "true"}, "miXsh": {"aniXt": "false"}, "niXsh": {"aniXt": "false"}, "puXsh": {"aniXt": "false"}, "shriXsh": {"aniXt": "false"}, "shliXsh": {"aniXt": "false"}, "pruXsh": {"aniXt": "false"}, "pluXsh": {"aniXt": "false"}, "pRiXsh": {"aniXt": "false"}, "vRiXsh": {"aniXt": "false"}, "mRiXsh": {"aniXt": "false"}, "ghRiXsh": {"aniXt": "false"}, "hRiXsh": {"aniXt": "false"}, "tus": {"aniXt": "false"}, "hras": {"aniXt": "false"}, "hlas": {"aniXt": "false"}, "ras": {"aniXt": "false"}, "las": {"aniXt": "false"}, "ghas": {"aniXt": "true"}, "jarj": {"aniXt": "false"}, "charch": {"aniXt": "false"}, "jharjh": {"aniXt": "false"}, "pis": {"aniXt": "false"}, "pes": {"aniXt": "false"}, "vis": {"aniXt": "false"}, "ves": {"aniXt": "false"}, "bis": {"aniXt": "false"}, "bes": {"aniXt": "false"}, "has": {"aniXt": "false"}, "nish": {"aniXt": "false"}, "mish": {"aniXt": "false"}, "mash": {"aniXt": "false"}, "shav": {"aniXt": "false"}, "shash": {"aniXt": "false"}, "shas": {"aniXt": "false"}, "shaMssha": {"aniXt": "false"}, "chah": {"aniXt": "false"}, "mah": {"aniXt": "false"}, "rah": {"aniXt": "false"}, "raMh": {"aniXt": "false"}, "dRih": {"aniXt": "false"}, "bRih": {"aniXt": "false"}, "tuhta": {"aniXt": "false"}, "duhda": {"aniXt": "false"}, "uhu": {"aniXt": "false"}, "arh": {"aniXt": "false"}, "dyut": {"aniXt": "false"}, "shvit": {"aniXt": "false"}, "midNca": {"aniXt": "false"}, "svidNca": {"aniXt": "false"}, "kXshvidNca": {"aniXt": "false"}, "ruch": {"aniXt": "false"}, "ghuXt": {"aniXt": "false"}, "ruXt": {"aniXt": "false"}, "kXshubh": {"aniXt": "false"}, "nabh": {"aniXt": "false"}, "tubh": {"aniXt": "false"}, "sraMss": {"aniXt": "false"}, "dhvaMsdh": {"aniXt": "false"}, "bhraMsbh": {"aniXt": "false"}, "bhraMshbh": {"aniXt": "false"}, "vRit": {"aniXt": "false"}, "vRidh": {"aniXt": "false"}, "shRidh": {"aniXt": "false"}, "syand": {"aniXt": "true"}, "kRip": {"aniXt": "false"}, "ghaXt": {"aniXt": "false"}, "vyath": {"aniXt": "false"}, "prath": {"aniXt": "false"}, "pras": {"aniXt": "false"}, "mrad": {"aniXt": "false"}, "skhad": {"aniXt": "false"}, "kXshaNcj": {"aniXt": "false"}, "krap": {"aniXt": "false"}, "kap": {"aniXt": "false"}, "kad": {"aniXt": "false"}, "krad": {"aniXt": "false"}, "klad": {"aniXt": "false"}, "tvarNca": {"aniXt": "false"}, "jvar": {"aniXt": "false"}, "gaXd": {"aniXt": "false"}, "stak": {"aniXt": "false"}, "rag": {"aniXt": "false"}, "lag": {"aniXt": "false"}, "hrag": {"aniXt": "false"}, "hlag": {"aniXt": "false"}, "sag": {"aniXt": "false"}, "sthag": {"aniXt": "false"}, "kag": {"aniXt": "false"}, "ak": {"aniXt": "false"}, "ag": {"aniXt": "false"}, "chaNn": {"aniXt": "false"}, "shaNn": {"aniXt": "false"}, "shraNn": {"aniXt": "false"}, "shrath": {"aniXt": "false"}, "shnath": {"aniXt": "false"}, "shlath": {"aniXt": "false"}, "knath": {"aniXt": "false"}, "krath": {"aniXt": "false"}, "klath": {"aniXt": "false"}, "chan": {"aniXt": "false"}, "jval": {"aniXt": "false"}, "hval": {"aniXt": "false"}, "hmal": {"aniXt": "false"}, "smRi": {"aniXt": "true"}, "dRii": {"aniXt": "false"}, "nRii": {"aniXt": "false"}, "shraa": {"aniXt": "true"}, "jNcaa": {"aniXt": "false"}, "chal": {"aniXt": "false"}, "chhad": {"aniXt": "false"}, "mad": {"aniXt": "false"}, "dhvan": {"aniXt": "false"}, "sham": {"aniXt": "false"}, "yam": {"aniXt": "false"}, "skhads": {"aniXt": "false"}, "svan": {"aniXt": "false"}, "phaNn": {"aniXt": "false"}, "raaj": {"aniXt": "false"}, "bhraajXta": {"aniXt": "false"}, "bhraashXta": {"aniXt": "false"}, "bhlaashXta": {"aniXt": "false"}, "syam": {"aniXt": "false"}, "sam": {"aniXt": "false"}, "stam": {"aniXt": "false"}, "jal": {"aniXt": "false"}, "Xtal": {"aniXt": "false"}, "Xtval": {"aniXt": "false"}, "sthal": {"aniXt": "false"}, "hal": {"aniXt": "false"}, "nal": {"aniXt": "false"}, "pal": {"aniXt": "false"}, "bal": {"aniXt": "false"}, "pul": {"aniXt": "false"}, "kul": {"aniXt": "false"}, "hul": {"aniXt": "false"}, "pat": {"aniXt": "false"}, "kvath": {"aniXt": "false"}, "path": {"aniXt": "false"}, "math": {"aniXt": "false"}, "vamXta": {"aniXt": "false"}, "bhram": {"aniXt": "false"}, "kXshar": {"aniXt": "false"}, "kXshur": {"aniXt": "false"}, "sah": {"aniXt": "false"}, "ram": {"aniXt": "true"}, "sad": {"aniXt": "false"}, "shad": {"aniXt": "true"}, "krush": {"aniXt": "true"}, "budh": {"aniXt": "true"}, "ruh": {"aniXt": "true"}, "kas": {"aniXt": "false"}, "hikk": {"aniXt": "false"}, "ach": {"aniXt": "false"}, "yaachXta": {"aniXt": "false"}, "reXt": {"aniXt": "false"}, "chat": {"aniXt": "false"}, "chad": {"aniXt": "false"}, "proth": {"aniXt": "false"}, "mid": {"aniXt": "false"}, "med": {"aniXt": "false"}, "mith": {"aniXt": "false"}, "meth": {"aniXt": "false"}, "midh": {"aniXt": "false"}, "medh": {"aniXt": "false"}, "nid": {"aniXt": "false"}, "ned": {"aniXt": "false"}, "mRidh": {"aniXt": "false"}, "budhba": {"aniXt": "false"}, "bundu": {"aniXt": "false"}, "veNn": {"aniXt": "false"}, "ven": {"aniXt": "false"}, "khan": {"aniXt": "false"}, "chiiv": {"aniXt": "false"}, "chiib": {"aniXt": "false"}, "chaay": {"aniXt": "false"}, "vyay": {"aniXt": "false"}, "daash": {"aniXt": "false"}, "bheXsh": {"aniXt": "false"}, "bhreXsh": {"aniXt": "false"}, "bhleXsh": {"aniXt": "false"}, "as": {"aniXt": "false"}, "aXsh": {"aniXt": "false"}, "spash": {"aniXt": "false"}, "laXsh": {"aniXt": "false"}, "chaXsh": {"aniXt": "false"}, "chhaXsh": {"aniXt": "false"}, "bhrakXsh": {"aniXt": "false"}, "bhlakXsh": {"aniXt": "false"}, "bhakXsh": {"aniXt": "false"}, "plakXsh": {"aniXt": "false"}, "daas": {"aniXt": "false"}, "maah": {"aniXt": "false"}, "guh": {"aniXt": "true"}, "shrish": {"aniXt": "false"}, "bhRibha": {"aniXt": "true"}, "hRiha": {"aniXt": "true"}, "dhRidha": {"aniXt": "true"}, "kRika": {"aniXt": "true"}, "niiNna": {"aniXt": "true"}, "dhedha": {"aniXt": "true"}, "glai": {"aniXt": "true"}, "mlai": {"aniXt": "true"}, "dyai": {"aniXt": "true"}, "drai": {"aniXt": "true"}, "dhrai": {"aniXt": "true"}, "dhyai": {"aniXt": "true"}, "rai": {"aniXt": "true"}, "styai": {"aniXt": "true"}, "khai": {"aniXt": "true"}, "kXshai": {"aniXt": "true"}, "jai": {"aniXt": "true"}, "sai": {"aniXt": "true"}, "kai": {"aniXt": "true"}, "gai": {"aniXt": "true"}, "shai": {"aniXt": "true"}, "shrai": {"aniXt": "true"}, "srai": {"aniXt": "true"}, "pai": {"aniXt": "true"}, "vaio": {"aniXt": "true"}, "stai": {"aniXt": "true"}, "snai": {"aniXt": "true"}, "daida": {"aniXt": "true"}, "paa": {"aniXt": "true"}, "ghraa": {"aniXt": "true"}, "dhmaa": {"aniXt": "true"}, "sthaa": {"aniXt": "true"}, "mnaa": {"aniXt": "true"}, "daada": {"aniXt": "true"}, "hvRi": {"aniXt": "true"}, "svRi": {"aniXt": "true"}, "vRi": {"aniXt": "true"}, "sRi": {"aniXt": "true"}, "Ri": {"aniXt": "true"}, "gRi": {"aniXt": "false"}, "ghRi": {"aniXt": "false"}, "dhvRi": {"aniXt": "true"}, "sru": {"aniXt": "true"}, "su": {"aniXt": "true"}, "shru": {"aniXt": "true"}, "dhru": {"aniXt": "true"}, "du": {"aniXt": "true"}, "dru": {"aniXt": "true"}, "jri": {"aniXt": "false"}, "juja": {"aniXt": "true"}, "smiXsh": {"aniXt": "false"}, "guga": {"aniXt": "true"}, "gaaga": {"aniXt": "true"}, "uu": {"aniXt": "true"}, "kuka": {"aniXt": "true"}, "khukha": {"aniXt": "true"}, "NguNga": {"aniXt": "true"}, "chyuch": {"aniXt": "true"}, "jyuj": {"aniXt": "true"}, "prup": {"aniXt": "true"}, "plup": {"aniXt": "true"}, "kluk": {"aniXt": "true"}, "rura": {"aniXt": "true"}, "mema": {"aniXt": "true"}, "deda": {"aniXt": "true"}, "shyaish": {"aniXt": "true"}, "pyaip": {"aniXt": "true"}, "trait": {"aniXt": "true"}, "puupa": {"aniXt": "false"}, "muuma": {"aniXt": "false"}, "XdiiXda": {"aniXt": "false"}, "tRii": {"aniXt": "false"}, "tij": {"aniXt": "false"}, "maan": {"aniXt": "false"}, "badh": {"aniXt": "false"}, "rabh": {"aniXt": "true"}, "labhXdu": {"aniXt": "true"}, "svaNcj": {"aniXt": "true"}, "had": {"aniXt": "true"}, "skands": {"aniXt": "true"}, "yabh": {"aniXt": "true"}, "nam": {"aniXt": "true"}, "gam": {"aniXt": "true"}, "sRip": {"aniXt": "true"}, "tap": {"aniXt": "false"}, "tyaj": {"aniXt": "true"}, "saNcj": {"aniXt": "true"}, "dRishda": {"aniXt": "true"}, "daMsh": {"aniXt": "false"}, "kRiXsh": {"aniXt": "true"}, "dah": {"aniXt": "true"}, "mih": {"aniXt": "true"}, "kit": {"aniXt": "true"}, "daan": {"aniXt": "false"}, "shaan": {"aniXt": "false"}, "pachXdu": {"aniXt": "true"}, "bhaj": {"aniXt": "false"}, "raNcj": {"aniXt": "true"}, "shap": {"aniXt": "true"}, "tviXsh": {"aniXt": "true"}, "yaj": {"aniXt": "true"}, "vapXda": {"aniXt": "true"}, "vah": {"aniXt": "true"}, "vas": {"aniXt": "false"}, "veva": {"aniXt": "true"}, "vyev": {"aniXt": "true"}, "hveh": {"aniXt": "true"}, "vad": {"aniXt": "false"}, "shviXtu": {"aniXt": "false"}, "Rit": {"aniXt": "false"}, "ad": {"aniXt": "true"}, "han": {"aniXt": "true"}, "dviXsh": {"aniXt": "true"}, "duh": {"aniXt": "true"}, "dih": {"aniXt": "true"}, "lih": {"aniXt": "true"}, "chakXshcha": {"aniXt": "false"}, "iir": {"aniXt": "false"}, "iiXd": {"aniXt": "false"}, "iish": {"aniXt": "false"}, "aas": {"aniXt": "false"}, "shaas": {"aniXt": "false"}, "kaMs": {"aniXt": "false"}, "kash": {"aniXt": "false"}, "nis": {"aniXt": "false"}, "niNcj": {"aniXt": "false"}, "shiNcj": {"aniXt": "false"}, "piNcj": {"aniXt": "false"}, "pRiNcj": {"aniXt": "false"}, "vRij": {"aniXt": "false"}, "vRiNcj": {"aniXt": "false"}, "pRich": {"aniXt": "false"}, "suuXsha": {"aniXt": "true"}, "shiisha": {"aniXt": "false"}, "yu": {"aniXt": "false"}, "ru": {"aniXt": "false"}, "tu": {"aniXt": "false"}, "nu": {"aniXt": "false"}, "kXshuXta": {"aniXt": "false"}, "kXshNnu": {"aniXt": "false"}, "snu": {"aniXt": "false"}, "uurNnuuu": {"aniXt": "false"}, "dyu": {"aniXt": "true"}, "ku": {"aniXt": "true"}, "stuXsh": {"aniXt": "true"}, "bruub": {"aniXt": "false"}, "ii": {"aniXt": "true"}, "vii": {"aniXt": "true"}, "yaa": {"aniXt": "true"}, "vaa": {"aniXt": "true"}, "bhaa": {"aniXt": "true"}, "snaa": {"aniXt": "true"}, "draa": {"aniXt": "true"}, "psaa": {"aniXt": "true"}, "raa": {"aniXt": "true"}, "laa": {"aniXt": "true"}, "khyaa": {"aniXt": "true"}, "praa": {"aniXt": "true"}, "maa": {"aniXt": "true"}, "vach": {"aniXt": "false"}, "vid": {"aniXt": "false"}, "mRij": {"aniXt": "false"}, "rudra": {"aniXt": "false"}, "svapNca": {"aniXt": "true"}, "shvas": {"aniXt": "false"}, "an": {"aniXt": "false"}, "jakXsh": {"aniXt": "false"}, "jaagRi": {"aniXt": "false"}, "daridraa": {"aniXt": "false"}, "chakaas": {"aniXt": "false"}, "diidhiida": {"aniXt": "false"}, "veviiva": {"aniXt": "false"}, "sas": {"aniXt": "false"}, "saMst": {"aniXt": "false"}, "vash": {"aniXt": "false"}, "hnuh": {"aniXt": "true"}, "hu": {"aniXt": "true"}, "bhiiNca": {"aniXt": "true"}, "hrii": {"aniXt": "true"}, "pRii": {"aniXt": "false"}, "pRi": {"aniXt": "true"}, "bhRiXdu": {"aniXt": "true"}, "maama": {"aniXt": "true"}, "haao": {"aniXt": "true"}, "daaXdu": {"aniXt": "true"}, "dhaaXdu": {"aniXt": "true"}, "nijNna": {"aniXt": "true"}, "vijva": {"aniXt": "true"}, "hRi": {"aniXt": "true"}, "bhas": {"aniXt": "false"}, "ki": {"aniXt": "true"}, "tur": {"aniXt": "false"}, "dhiXsh": {"aniXt": "false"}, "dhan": {"aniXt": "false"}, "jan": {"aniXt": "false"}, "gaa": {"aniXt": "true"}, "div": {"aniXt": "false"}, "siv": {"aniXt": "false"}, "sriv": {"aniXt": "false"}, "snus": {"aniXt": "false"}, "snas": {"aniXt": "false"}, "knas": {"aniXt": "false"}, "vyuXsh": {"aniXt": "false"}, "nRit": {"aniXt": "false"}, "tras": {"aniXt": "false"}, "kuth": {"aniXt": "false"}, "puth": {"aniXt": "false"}, "gudh": {"aniXt": "false"}, "kXship": {"aniXt": "true"}, "puXshp": {"aniXt": "false"}, "tim": {"aniXt": "false"}, "tiim": {"aniXt": "false"}, "stim": {"aniXt": "false"}, "stiim": {"aniXt": "false"}, "vriiXd": {"aniXt": "false"}, "iXsh": {"aniXt": "false"}, "suh": {"aniXt": "false"}, "jRiija": {"aniXt": "false"}, "jhRiijha": {"aniXt": "false"}, "duuda": {"aniXt": "false"}, "diida": {"aniXt": "true"}, "dhiidha": {"aniXt": "true"}, "miima": {"aniXt": "true"}, "riira": {"aniXt": "true"}, "liila": {"aniXt": "true"}, "vriiv": {"aniXt": "true"}, "piipa": {"aniXt": "true"}, "iiii": {"aniXt": "true"}, "priip": {"aniXt": "false"}, "sho": {"aniXt": "true"}, "chho": {"aniXt": "true"}, "so": {"aniXt": "true"}, "do": {"aniXt": "true"}, "diip": {"aniXt": "false"}, "puur": {"aniXt": "false"}, "tuur": {"aniXt": "false"}, "dhuur": {"aniXt": "false"}, "guur": {"aniXt": "false"}, "ghuur": {"aniXt": "false"}, "juur": {"aniXt": "false"}, "shuur": {"aniXt": "false"}, "chuur": {"aniXt": "false"}, "vaavRit": {"aniXt": "false"}, "klish": {"aniXt": "true"}, "vaash": {"aniXt": "false"}, "shuchii": {"aniXt": "false"}, "nah": {"aniXt": "true"}, "pad": {"aniXt": "true"}, "khid": {"aniXt": "true"}, "yudh": {"aniXt": "true"}, "rudh": {"aniXt": "true"}, "man": {"aniXt": "false"}, "yuj": {"aniXt": "false"}, "sRij": {"aniXt": "true"}, "lish": {"aniXt": "true"}, "raadh": {"aniXt": "true"}, "vyadh": {"aniXt": "true"}, "shuXsh": {"aniXt": "true"}, "tuXsh": {"aniXt": "true"}, "duXsh": {"aniXt": "true"}, "shak": {"aniXt": "true"}, "svid": {"aniXt": "true"}, "krudh": {"aniXt": "true"}, "kXshudh": {"aniXt": "true"}, "shudh": {"aniXt": "true"}, "radh": {"aniXt": "true"}, "nash": {"aniXt": "true"}, "tRip": {"aniXt": "false"}, "dRip": {"aniXt": "false"}, "druh": {"aniXt": "true"}, "muh": {"aniXt": "true"}, "snuh": {"aniXt": "true"}, "snih": {"aniXt": "false"}, "tam": {"aniXt": "false"}, "dam": {"aniXt": "false"}, "shram": {"aniXt": "false"}, "kXsham": {"aniXt": "true"}, "klam": {"aniXt": "false"}, "yas": {"aniXt": "false"}, "jas": {"aniXt": "false"}, "tas": {"aniXt": "false"}, "das": {"aniXt": "false"}, "bas": {"aniXt": "false"}, "vyus": {"aniXt": "false"}, "byus": {"aniXt": "false"}, "bus": {"aniXt": "false"}, "vus": {"aniXt": "false"}, "pyuXsh": {"aniXt": "false"}, "pyus": {"aniXt": "false"}, "kus": {"aniXt": "false"}, "kush": {"aniXt": "false"}, "mus": {"aniXt": "false"}, "mas": {"aniXt": "false"}, "uch": {"aniXt": "false"}, "bhRish": {"aniXt": "false"}, "bhRishbha": {"aniXt": "false"}, "vRish": {"aniXt": "false"}, "kRish": {"aniXt": "false"}, "tRiXshNca": {"aniXt": "false"}, "Xdip": {"aniXt": "false"}, "kup": {"aniXt": "false"}, "yup": {"aniXt": "false"}, "rup": {"aniXt": "false"}, "lup": {"aniXt": "true"}, "stup": {"aniXt": "false"}, "stuup": {"aniXt": "false"}, "lubh": {"aniXt": "false"}, "klid": {"aniXt": "true"}, "Ridh": {"aniXt": "false"}, "gRidh": {"aniXt": "false"}, "suXsha": {"aniXt": "true"}, "siXsha": {"aniXt": "true"}, "shisha": {"aniXt": "true"}, "miXdu": {"aniXt": "true"}, "chicha": {"aniXt": "false"}, "stRis": {"aniXt": "true"}, "vRiva": {"aniXt": "false"}, "dhudha": {"aniXt": "true"}, "dhuudha": {"aniXt": "false"}, "duXta": {"aniXt": "true"}, "hi": {"aniXt": "true"}, "spRi": {"aniXt": "true"}, "aap": {"aniXt": "false"}, "saadh": {"aniXt": "true"}, "ash": {"aniXt": "false"}, "stigh": {"aniXt": "false"}, "tig": {"aniXt": "false"}, "sagh": {"aniXt": "false"}, "dhRiXshNca": {"aniXt": "false"}, "dambh": {"aniXt": "false"}, "dagh": {"aniXt": "false"}, "ri": {"aniXt": "true"}, "chiri": {"aniXt": "false"}, "jiri": {"aniXt": "false"}, "dRi": {"aniXt": "true"}, "tud": {"aniXt": "true"}, "nud": {"aniXt": "true"}, "dish": {"aniXt": "true"}, "bhrasj": {"aniXt": "true"}, "RiXsh": {"aniXt": "false"}, "juXsh": {"aniXt": "false"}, "vijo": {"aniXt": "false"}, "lajo": {"aniXt": "false"}, "lasjo": {"aniXt": "false"}, "vrashcho": {"aniXt": "true"}, "vyach": {"aniXt": "false"}, "Richchh": {"aniXt": "false"}, "michchh": {"aniXt": "false"}, "tvach": {"aniXt": "false"}, "Rich": {"aniXt": "false"}, "ubj": {"aniXt": "false"}, "ujjh": {"aniXt": "false"}, "riph": {"aniXt": "false"}, "rih": {"aniXt": "false"}, "tRimp": {"aniXt": "false"}, "tRiph": {"aniXt": "false"}, "tRimph": {"aniXt": "false"}, "dRimp": {"aniXt": "false"}, "dRiph": {"aniXt": "false"}, "dRimph": {"aniXt": "false"}, "Riph": {"aniXt": "false"}, "Rimph": {"aniXt": "false"}, "guph": {"aniXt": "false"}, "gumph": {"aniXt": "false"}, "ubh": {"aniXt": "false"}, "umbh": {"aniXt": "false"}, "dRibh": {"aniXt": "false"}, "chRit": {"aniXt": "false"}, "vidh": {"aniXt": "false"}, "juXd": {"aniXt": "false"}, "jun": {"aniXt": "false"}, "mRiXd": {"aniXt": "false"}, "pRiXd": {"aniXt": "false"}, "pRiNn": {"aniXt": "false"}, "vRiNn": {"aniXt": "false"}, "mRiNn": {"aniXt": "false"}, "tuNn": {"aniXt": "false"}, "puNn": {"aniXt": "false"}, "muNn": {"aniXt": "false"}, "kuNn": {"aniXt": "false"}, "shun": {"aniXt": "false"}, "druNn": {"aniXt": "false"}, "sur": {"aniXt": "false"}, "kur": {"aniXt": "false"}, "khur": {"aniXt": "false"}, "mur": {"aniXt": "false"}, "ghur": {"aniXt": "false"}, "pur": {"aniXt": "false"}, "vRih": {"aniXt": "true"}, "tRih": {"aniXt": "false"}, "stRih": {"aniXt": "true"}, "tRihta": {"aniXt": "true"}, "kil": {"aniXt": "false"}, "chil": {"aniXt": "false"}, "il": {"aniXt": "false"}, "vil": {"aniXt": "false"}, "bil": {"aniXt": "false"}, "nil": {"aniXt": "false"}, "hil": {"aniXt": "false"}, "shil": {"aniXt": "false"}, "sil": {"aniXt": "false"}, "mil": {"aniXt": "false"}, "kuXt": {"aniXt": "false"}, "guXd": {"aniXt": "false"}, "chhur": {"aniXt": "false"}, "truXt": {"aniXt": "false"}, "tuXt": {"aniXt": "false"}, "chuXt": {"aniXt": "false"}, "chhuXt": {"aniXt": "false"}, "juXt": {"aniXt": "false"}, "kRiXd": {"aniXt": "false"}, "kuXd": {"aniXt": "false"}, "puXd": {"aniXt": "false"}, "thuXd": {"aniXt": "false"}, "sthuXd": {"aniXt": "false"}, "khuXd": {"aniXt": "false"}, "chhuXd": {"aniXt": "false"}, "sphur": {"aniXt": "false"}, "sphul": {"aniXt": "false"}, "sphar": {"aniXt": "false"}, "sphal": {"aniXt": "false"}, "sphuXd": {"aniXt": "false"}, "chuXd": {"aniXt": "false"}, "vruXd": {"aniXt": "false"}, "kruXd": {"aniXt": "false"}, "bhRiXd": {"aniXt": "false"}, "gur": {"aniXt": "false"}, "nuu": {"aniXt": "false"}, "dhuu": {"aniXt": "false"}, "gu": {"aniXt": "true"}, "kuuka": {"aniXt": "false"}, "pRipa": {"aniXt": "true"}, "mRima": {"aniXt": "true"}, "pi": {"aniXt": "true"}, "dhi": {"aniXt": "true"}, "suu": {"aniXt": "false"}, "kRii": {"aniXt": "false"}, "gRii": {"aniXt": "false"}, "dRida": {"aniXt": "true"}, "prachchh": {"aniXt": "true"}, "masjXta": {"aniXt": "true"}, "ruj": {"aniXt": "false"}, "bhuj": {"aniXt": "true"}, "chhup": {"aniXt": "true"}, "rush": {"aniXt": "false"}, "rish": {"aniXt": "true"}, "spRish": {"aniXt": "true"}, "vichchh": {"aniXt": "false"}, "vish": {"aniXt": "true"}, "mRish": {"aniXt": "true"}, "much": {"aniXt": "false"}, "lip": {"aniXt": "true"}, "sich": {"aniXt": "true"}, "kRit": {"aniXt": "false"}, "pish": {"aniXt": "false"}, "rudhra": {"aniXt": "true"}, "bhidbha": {"aniXt": "true"}, "chhidchha": {"aniXt": "true"}, "richra": {"aniXt": "true"}, "vichva": {"aniXt": "true"}, "kXshudk": {"aniXt": "true"}, "yujya": {"aniXt": "true"}, "chhRidu": {"aniXt": "false"}, "tRidu": {"aniXt": "false"}, "indhNca": {"aniXt": "false"}, "piXsh": {"aniXt": "true"}, "bhaNcj": {"aniXt": "false"}, "his": {"aniXt": "false"}, "und": {"aniXt": "false"}, "aNcj": {"aniXt": "false"}, "tan": {"aniXt": "false"}, "kXshaNn": {"aniXt": "false"}, "kXshiNn": {"aniXt": "false"}, "RiNn": {"aniXt": "false"}, "tRiNn": {"aniXt": "false"}, "ghRiNn": {"aniXt": "false"}, "kRiXdu": {"aniXt": "true"}, "kriiXdu": {"aniXt": "true"}, "shriish": {"aniXt": "true"}, "skus": {"aniXt": "true"}, "stumbh": {"aniXt": "false"}, "skumbh": {"aniXt": "false"}, "yuya": {"aniXt": "true"}, "knuuk": {"aniXt": "false"}, "druud": {"aniXt": "false"}, "luula": {"aniXt": "false"}, "stRiis": {"aniXt": "false"}, "kRiika": {"aniXt": "false"}, "vRiiva": {"aniXt": "false"}, "shRii": {"aniXt": "false"}, "vRii": {"aniXt": "false"}, "bhRii": {"aniXt": "false"}, "mRii": {"aniXt": "false"}, "jRii": {"aniXt": "false"}, "jhRii": {"aniXt": "false"}, "Rii": {"aniXt": "false"}, "jyaa": {"aniXt": "true"}, "rii": {"aniXt": "true"}, "lii": {"aniXt": "false"}, "vlii": {"aniXt": "true"}, "blii": {"aniXt": "true"}, "plii": {"aniXt": "true"}, "vrii": {"aniXt": "true"}, "bhrii": {"aniXt": "true"}, "kXshiik": {"aniXt": "true"}, "bandh": {"aniXt": "false"}, "mRid": {"aniXt": "false"}, "kuXsh": {"aniXt": "false"}, "dhrasu": {"aniXt": "false"}, "muXsh": {"aniXt": "false"}, "khach": {"aniXt": "false"}, "khav": {"aniXt": "false"}, "heXdh": {"aniXt": "false"}, "grah": {"aniXt": "false"}, "chur": {"aniXt": "false"}, "chint": {"aniXt": "false"}, "yantr": {"aniXt": "false"}, "lakXsh": {"aniXt": "false"}, "kundr": {"aniXt": "false"}, "kud": {"aniXt": "false"}, "mind": {"aniXt": "false"}, "laNnXd": {"aniXt": "false"}, "laXdo": {"aniXt": "false"}, "piiXd": {"aniXt": "false"}, "uurj": {"aniXt": "false"}, "varNn": {"aniXt": "false"}, "chuurNn": {"aniXt": "false"}, "pRith": {"aniXt": "false"}, "samb": {"aniXt": "false"}, "shamb": {"aniXt": "false"}, "saamb": {"aniXt": "false"}, "kuXtXt": {"aniXt": "false"}, "puXtXt": {"aniXt": "false"}, "chuXtXt": {"aniXt": "false"}, "suXtXt": {"aniXt": "false"}, "shvaXth": {"aniXt": "false"}, "shvaNnXth": {"aniXt": "false"}, "pij": {"aniXt": "false"}, "luNcj": {"aniXt": "false"}, "saantv": {"aniXt": "false"}, "shaantv": {"aniXt": "false"}, "shvalk": {"aniXt": "false"}, "valk": {"aniXt": "false"}, "sphiXtXt": {"aniXt": "false"}, "smiXt": {"aniXt": "false"}, "panth": {"aniXt": "false"}, "pichchh": {"aniXt": "false"}, "chhand": {"aniXt": "false"}, "taXd": {"aniXt": "false"}, "khaXd": {"aniXt": "false"}, "guNnXd": {"aniXt": "false"}, "guNnXth": {"aniXt": "false"}, "khuNnXd": {"aniXt": "false"}, "chhard": {"aniXt": "false"}, "pust": {"aniXt": "false"}, "bust": {"aniXt": "false"}, "chud": {"aniXt": "false"}, "nakk": {"aniXt": "false"}, "dhakk": {"aniXt": "false"}, "chakk": {"aniXt": "false"}, "chukk": {"aniXt": "false"}, "kXshal": {"aniXt": "false"}, "tal": {"aniXt": "false"}, "tul": {"aniXt": "false"}, "dul": {"aniXt": "false"}, "chul": {"aniXt": "false"}, "paal": {"aniXt": "false"}, "shulb": {"aniXt": "false"}, "shuurp": {"aniXt": "false"}, "paMs": {"aniXt": "false"}, "paMsh": {"aniXt": "false"}, "shulk": {"aniXt": "false"}, "champ": {"aniXt": "false"}, "kXshamp": {"aniXt": "false"}, "chhaNcj": {"aniXt": "false"}, "shvart": {"aniXt": "false"}, "svart": {"aniXt": "false"}, "shvabhr": {"aniXt": "false"}, "jNcap": {"aniXt": "false"}, "must": {"aniXt": "false"}, "khaXtXt": {"aniXt": "false"}, "saXtXt": {"aniXt": "false"}, "puurNn": {"aniXt": "false"}, "pus": {"aniXt": "false"}, "XtaNgk": {"aniXt": "false"}, "vyap": {"aniXt": "false"}, "vip": {"aniXt": "false"}, "dhuus": {"aniXt": "false"}, "dhuuXsh": {"aniXt": "false"}, "dhuush": {"aniXt": "false"}, "kiiXt": {"aniXt": "false"}, "puuj": {"aniXt": "false"}, "ark": {"aniXt": "false"}, "maarj": {"aniXt": "false"}, "march": {"aniXt": "false"}, "kRiit": {"aniXt": "false"}, "vardh": {"aniXt": "false"}, "kumbh": {"aniXt": "false"}, "hlap": {"aniXt": "false"}, "klap": {"aniXt": "false"}, "hrap": {"aniXt": "false"}, "chuNnXt": {"aniXt": "false"}, "mRiNnXd": {"aniXt": "false"}, "mrachchh": {"aniXt": "false"}, "bruus": {"aniXt": "false"}, "vruus": {"aniXt": "false"}, "vruuXsh": {"aniXt": "false"}, "gardh": {"aniXt": "false"}, "gurd": {"aniXt": "false"}, "jaMs": {"aniXt": "false"}, "piNnXth": {"aniXt": "false"}, "daMs": {"aniXt": "false"}, "Xdap": {"aniXt": "false"}, "tantr": {"aniXt": "false"}, "mantr": {"aniXt": "false"}, "bharts": {"aniXt": "false"}, "bast": {"aniXt": "false"}, "gandh": {"aniXt": "false"}, "vast": {"aniXt": "false"}, "hast": {"aniXt": "false"}, "viXshk": {"aniXt": "false"}, "hiXshk": {"aniXt": "false"}, "niXshk": {"aniXt": "false"}, "kuuNn": {"aniXt": "false"}, "tuuNn": {"aniXt": "false"}, "bhruuNn": {"aniXt": "false"}, "yakXsh": {"aniXt": "false"}, "kuts": {"aniXt": "false"}, "kuuXt": {"aniXt": "false"}, "kusm": {"aniXt": "false"}, "shabd": {"aniXt": "true"}, "jambh": {"aniXt": "false"}, "pash": {"aniXt": "false"}, "mokXsh": {"aniXt": "false"}, "rak": {"aniXt": "false"}, "ragh": {"aniXt": "false"}, "ghrasu": {"aniXt": "false"}, "chyu": {"aniXt": "false"}, "miNcj": {"aniXt": "false"}, "liNcj": {"aniXt": "false"}, "traMs": {"aniXt": "false"}, "ghaNnXt": {"aniXt": "false"}, "tark": {"aniXt": "false"}, "rus": {"aniXt": "false"}, "naNnXt": {"aniXt": "false"}, "puNnXt": {"aniXt": "false"}, "chi": {"aniXt": "false"}, "randh": {"aniXt": "false"}, "rich": {"aniXt": "false"}, "chhRid": {"aniXt": "false"}, "chRip": {"aniXt": "false"}, "chhRip": {"aniXt": "false"}, "mii": {"aniXt": "false"}, "chiik": {"aniXt": "false"}, "maarg": {"aniXt": "false"}, "dhRiXsh": {"aniXt": "false"}, "katha": {"aniXt": "false"}, "vara": {"aniXt": "false"}, "gaNna": {"aniXt": "false"}, "shaXtha": {"aniXt": "false"}, "shvaXtha": {"aniXt": "false"}, "paXta": {"aniXt": "false"}, "vaXta": {"aniXt": "false"}, "raha": {"aniXt": "false"}, "stana": {"aniXt": "false"}, "gada": {"aniXt": "false"}, "pata": {"aniXt": "false"}, "paXsha": {"aniXt": "false"}, "svara": {"aniXt": "false"}, "racha": {"aniXt": "false"}, "kala": {"aniXt": "false"}, "chaha": {"aniXt": "false"}, "maha": {"aniXt": "false"}, "saara": {"aniXt": "false"}, "kRipa": {"aniXt": "false"}, "shratha": {"aniXt": "false"}, "spRiha": {"aniXt": "false"}, "bhaama": {"aniXt": "false"}, "suucha": {"aniXt": "false"}, "kheXta": {"aniXt": "false"}, "kheXd": {"aniXt": "false"}, "khoXta": {"aniXt": "false"}, "kXshoXta": {"aniXt": "false"}, "goma": {"aniXt": "false"}, "kumaara": {"aniXt": "false"}, "shiila": {"aniXt": "false"}, "saama": {"aniXt": "false"}, "vela": {"aniXt": "false"}, "kaala": {"aniXt": "false"}, "palpuula": {"aniXt": "false"}, "vaata": {"aniXt": "false"}, "gaveXsha": {"aniXt": "false"}, "vaasa": {"aniXt": "false"}, "nivaasa": {"aniXt": "false"}, "bhaaja": {"aniXt": "false"}, "sabhaaja": {"aniXt": "false"}, "uuna": {"aniXt": "false"}, "dhvana": {"aniXt": "false"}, "kuuXta": {"aniXt": "false"}, "saNgketa": {"aniXt": "false"}, "graama": {"aniXt": "false"}, "kuNna": {"aniXt": "false"}, "guNna": {"aniXt": "false"}, "keta": {"aniXt": "false"}, "stena": {"aniXt": "false"}, "pada": {"aniXt": "false"}, "gRiha": {"aniXt": "false"}, "mRiga": {"aniXt": "false"}, "kuha": {"aniXt": "false"}, "shuura": {"aniXt": "false"}, "viira": {"aniXt": "false"}, "sthuula": {"aniXt": "false"}, "artha": {"aniXt": "false"}, "satra": {"aniXt": "false"}, "garva": {"aniXt": "false"}, "suutra": {"aniXt": "false"}, "muutra": {"aniXt": "false"}, "ruukXsha": {"aniXt": "false"}, "paara": {"aniXt": "false"}, "tiira": {"aniXt": "false"}, "puXta": {"aniXt": "false"}, "katra": {"aniXt": "false"}, "kart": {"aniXt": "false"}, "valka": {"aniXt": "false"}, "chitra": {"aniXt": "false"}, "asa": {"aniXt": "false"}, "laja": {"aniXt": "false"}, "mishra": {"aniXt": "false"}, "saNggraama": {"aniXt": "false"}, "stom": {"aniXt": "false"}, "chhidra": {"aniXt": "false"}, "karNn": {"aniXt": "false"}, "andha": {"aniXt": "false"}, "daNnXda": {"aniXt": "false"}, "aNgka": {"aniXt": "false"}, "aNgga": {"aniXt": "false"}, "sukha": {"aniXt": "false"}, "dukha": {"aniXt": "false"}, "rasa": {"aniXt": "false"}, "vyaya": {"aniXt": "false"}, "ruupa": {"aniXt": "false"}, "chheda": {"aniXt": "false"}, "chhada": {"aniXt": "false"}, "laabha": {"aniXt": "false"}, "vraNna": {"aniXt": "false"}, "varNna": {"aniXt": "false"}, "parNna": {"aniXt": "false"}, "viXshka": {"aniXt": "false"}, "kXshipa": {"aniXt": "false"}, "vasa": {"aniXt": "false"}, "tuttha": {"aniXt": "false"}, "palyuula": {"aniXt": "false"}, "dheka": {"aniXt": "false"}}'
    dhaatu_store= json.loads(dhaatu_store_str)
    #booleanise = lambda t : True if t == "true" else False
    #dhaatu_store = dict ( (k, booleanise(v)) for k,v in dhaatu_store.items())
    return dhaatu_store

global_dhaatu_store  = get_dhaatu_properties_dict()

def get_dhaatu_properties(string):
    global global_dhaatu_store
    #print ("Returning %s for %s " % (global_dhaatu_store[string],string))
    return global_dhaatu_store[string]

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


def list_past_rules_applied (nd):
    """
    Returns list of rules applied so far for the node:nd
    """
    return [int(x['rule'].__name__.split("_")[-1]) for x in nd._output if 'rule' in x]

class Node:
    def __init__(self,data,parent1,parent2=None):
        if all ( not isinstance(data,x) for x in list(get_supported_types()) + [list] ):
            raise ValueError("Unsupported type %s" % type(data))
        self._children=[]

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
    return (Suffix,Dhaatu)


def ach():
    return ("aa","ii","uu","Rii",'lRii') + pratyaahaara('a','ch')

def pratyaahaara(start,end):
    """
    Parameters
    ----------
    start : character
        The starting letter of the  pratyaahaara
    end : character
        The ending letter of the  pratyaahaara

    Raises
    ------
    ValueError
    RuntimeError

    Returns
    -------
    list
        characters in the pratyaahaara.

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


def hal():
    return ("kh","k","gh","g","Ng","Nc","NN","Nn","chh","ch","jh","j",
            "Xth","Xt","Xdh","Xd","Xsh","th","t","dh","d","n",
            "ph","p","bh","b","m","y","r","l","v","sh",
            "s","h")
def anunaasika():
    return ("Ng","Nc","Nn","M","m","NN")

def chu():
    return ("ch","chh","j","jh","Nc")

def Xtu():
    return ("Xt","Xth","Xd","Xdh","Nn")



def unclassified_pratyayaaH():
    return ('sNNch','chlNN','shap','taas','sya','aXt','iiXt','aaXt','yaasNNXt','sNNXt')

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
def kRit_pratyayaaH():
    return ("Nnvul","lyuXt","aniiyar","kta","ktavatu",
            "tavyat","tumun","tRich","ktvaa","Nnamul",
            "lyap","yat","Nnyat","kyap","ghaNc",'ach',
            "ap","ktin","a","yuch","shatRi","shaanach",
            "ka","Nnini","kvip")

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
    return ('ghan', 'khaNc', 'aNn', 'a', 'tyak', 'chhas', 'kan', 'Xdya', 'vuk', 'chphaNc', 'ti', 'chhaNn', 'snaNc', 'Nca', 'XdhakaNc', 'NgiiXsh', 'airak', 'vun', 'NciXtha', 'Xtaap', 'yan', 'phak', 'mayaXt', 'lup', 'chha', 'yat', 'phiNc', 'Xshpha', 'vuNc', 'Xdhak', 'Xdyat', 'ra', 'tyap', 'Ngiip', 'NcyaNg', 'phin', 'Xdmatup', 'ka', 'eNnya', 'Xtyul', 'ila', 'Xthach', 'iNc', 'Xthak', 'sa', 'XshXthan', 'Nna', 'phaNc', 'XdhaNc', 'XthaNc', 'valach', 'ini', 'Xdhrak', 'naNc', 'Nnya', 'aNc', 'Xtyu', 'Ncya', 'XshyaNg', 'bhaktal', 'uuNg', 'Ngiin', 'ruupya', 'Xthap', 'yaNc', 'vidhal', 'Xdaap', 'chaap', 'Xdvalach', 'gha', 'matup', 'vyan', 'Xshphak', 'luk', 'tal', 'ma', 'ya', 'kak', 'kha',)



def upadhaa(x):
    if not isinstance(x,list) or not all(isinstance(j,str) for j in x):
        raise ValueError("invalid input: %s" % x)
    if len(x)>=2:
        return len(x)-2
    else:
        raise ValueError("Insufficient length for upadhaa")


def diirgha(x):
    if x =="a":
        return "aa"
    elif x == "i":
        return "ii"
    elif x == "u":
        return "uu"
    else:
        return x


def guNna(x):
    if x =="i" or x=="i":
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
        return 'o'
    elif x=='uu':
        return 'au'
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

def next_possible_suffixes(suffix_arg):
    if isinstance(suffix_arg,str):
        suffix=Suffix(suffix_arg)
    else:
        suffix=suffix_arg

    if not isinstance(suffix,Suffix):
        raise ValueError("input must be a suffix")
    suffix_str = ''.join(suffix._suffix)
    subaadi = sup_pratyayaaH()
    taddhita = taddhita_pratyayaaH()
    suptaddhita = subaadi + taddhita
    tibaadi = tiNg_pratyayaaH()

    allowed_next_values = tuple(subaadi + taddhita + tibaadi)


    next_values_dict = {"Nnvul": suptaddhita , 'aniiyar':suptaddhita , 'tavyat': suptaddhita , 'tavya': suptaddhita ,
    "lyuXt":suptaddhita, 'kta': subaadi, 'ktavatu': subaadi, 'tumun': None, 'tRich':suptaddhita , 'ktvaa': None, 'Nnamul': subaadi,
    'lyap':subaadi, 'yat':suptaddhita,'Nnyat':suptaddhita, 'kyap':suptaddhita,'ghaNc':suptaddhita, 'ach':suptaddhita, 'ap':suptaddhita,
    'ktin':suptaddhita,'a': subaadi, 'yuch':suptaddhita, 'shatRi':suptaddhita, 'shaanach': suptaddhita, 'ka': suptaddhita, 
    'Nnini':suptaddhita,'kvip':suptaddhita,'ghan':suptaddhita,'khaNc':suptaddhita,'aNn':subaadi,'a':subaadi,'tyak':subaadi,
    'chhas':subaadi,'kan':suptaddhita, 'Xthak':suptaddhita,'kan':suptaddhita,'Xdya':suptaddhita,'vuk':subaadi,'chphaNc':subaadi,'ti':subaadi,
    'chhaNn':subaadi, 'snaNc': subaadi, 'Nca': subaadi, 'XdhakaNc': subaadi, 'NgiiXsh': subaadi, 'airak': subaadi, 'vun': subaadi, 'NciXtha': subaadi, 'Xtaap': subaadi, 'yan': subaadi, 'phak': subaadi, 'mayaXt': subaadi, 'lup': subaadi, 'chha': subaadi,  'phiNc': subaadi, 'Xshpha': subaadi, 'vuNc': subaadi, 'Xdhak': subaadi, 'Xdyat': subaadi, 'ra': subaadi, 'tyap': subaadi, 'Ngiip': subaadi, 'NcyaNg': subaadi, 'phin': subaadi, 'Xdmatup': subaadi, 'eNnya': subaadi, 'Xtyul': subaadi, 'ila': subaadi, 'Xthach': subaadi, 'iNc': subaadi, 'sa': subaadi, 'XshXthan': subaadi, 'Nna': subaadi, 'phaNc': subaadi, 'XdhaNc': subaadi, 'XthaNc': subaadi, 'valach': subaadi, 'ini': subaadi, 'Xdhrak': subaadi, 'naNc': subaadi, 'Nnya': subaadi, 'aNc': subaadi, 'Xtyu': subaadi, 'Ncya': subaadi, 'XshyaNg': subaadi, 'bhaktal': subaadi, 'uuNg': subaadi, 'Ngiin': subaadi, 'ruupya': subaadi, 'Xthap': subaadi, 'yaNc': subaadi, 'vidhal': subaadi, 'Xdaap': subaadi, 'chaap': subaadi, 'Xdvalach': subaadi, 'gha': subaadi, 'matup': subaadi, 'vyan': subaadi, 'Xshphak': subaadi, 'luk': subaadi, 'tal': subaadi, 'ma': subaadi, 'ya': subaadi, 'kak': subaadi, 'kha': subaadi,
    'sNN': None, 'au': None, 'jas': None, 'am': None, 'auXt': None, 'shas': None, 'Xtaa': None, 'bhyaam': None, 'bhis': None, 'Nge': None, 'bhyas': None, 'Ngasi': None, 'Ngas': None, 'os': None, 'aam': None, 'Ngi': None, 'sup': None,
    'tip': None, 'tas': None, 'jhi': None, 'sip': None, 'thas': None, 'tha': None, 'mip': None, 'vas': None, 'mas': None, 'ta': None, 'aataam': None, 'jha': None, 'thaas': None, 'aathaam': None, 'dhvam': None, 'iXt': None, 'vahi': None, 'mahiNg': None
    }    
  

    if suffix_str not in next_values_dict:
        raise ValueError("Unknown Suffix")
    next_suffixes = next_values_dict[suffix_str]
    
    # double-check
    if any ( next_suffix not in allowed_next_values for next_suffix in next_suffixes):
        raise ValueError("Invalid next suffix")
    return next_suffixes
