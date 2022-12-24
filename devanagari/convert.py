import re

def hal():
    return ('kha',"kh",'ka',"k",'gha',"gh",'ga',"g",'Nga',"Ng",'Nca',"Nc","NN",'Nna',"Nn",\
            'chha',"chh",'cha',"ch",'jha',"jh",'ja',"j",
            'Xtha',"Xth",'Xta',"Xt",'Xdha',"Xdh",'Xda',"Xd",'Xsha',"Xsh",\
            'tha',"th",'ta',"t",'dha',"dh",'da',"d",'na',"n",\
            'pha',"ph",'pa',"p",'bha',"bh",'ba',"b",'ma',"m",'ya',"y",'ra',"r",\
            'la',"l",'va',"v",'sha',"sh",
            'sa',"s",'ha',"h")

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


"""
Devanagari map taken from  https://everythingfonts.com/unicode/devanagari
"""
def devanagari_map():
    return {
            'NN': "\u0901",
            'a': "\u0905",
            'aa': "\u0906",
            'i': "\u0907",
            'ii': "\u0908",
            'u': "\u0909",
            'U': "\u090A",
            'Ri': "\u090B",
            'lRi': "\u090C",
            'e': "\u090F",
            'ai': "\u0910",
            'o': "\u0913",
            'au': "\u0914",
            'ka': "\u0915",
            'k': "\u0915\u094D",
            'kha': "\u0916",
            'kh': "\u0916\u094D",
            'ga': "\u0917",
            'g': "\u0917\u094D",
            'gha': "\u0918",
            'gh': "\u0918\u094D",
            'Nga': "\u0919",
            'Ng': "\u0919\u094D",
            'cha': "\u091A",
            'ch': "\u091A\u094D",
            'ja': "\u091C",
            'j': "\u091C\u094D",
            'jha': "\u091D",
            'jh': "\u091D\u094D",
            'Nca': "\u091E",
            'Nca': "\u091E\u094D",
            'Xta': "\u091F\u094D",
            'Xt': "\u091F\u094D",
            'Xtha': "\u0920",
            'Xth': "\u0920\u094D",
            'Xda': "\u0921",
            'Xd': "\u0921\u094D",
            'Xdha': "\u0922",
            'Xdh': "\u0922\u094D",
            'Nna': "\u0923",
            'Nn': "\u0923\u094D",
            'ta': "\u0924",
            't': "\u0924\u094D",
            'tha': "\u0925",
            'th': "\u0925\u094D",
            'da': "\u0926",
            'd': "\u0926\u094D",
            'dha': "\u0927",
            'dh': "\u0927\u094D",
            'na': "\u0928",
            'n': "\u0928\u094D",
            'pa': "\u092A",
            'p': "\u092A",
            'pha': "\u092B",
            'ph': "\u092B\u094D",
            'ba': "\u092C",
            'b': "\u092C\u094D",
            'bha': "\u092D",
            'bh': "\u092D\u094D",
            'ma': "\u092E",
            'm': "\u092E\u094D",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902",
            'M': "\u0902"}

print(parse_string("aaka"))

