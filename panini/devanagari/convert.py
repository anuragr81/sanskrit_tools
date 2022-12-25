import re


"""
Matras sorted by length of string to parse
"""
def matras():
    return  ( ('Rii',"\u0944"), ('Ri',"\u0943"),  ('au',"\u094C"),('ai',"\u0948"),\
        ('ii',"\u0940"),('aa',"\u093E"),('uu',"\u0942"),('i',"\u093F"), ('u',"\u0941"),\
         ('e',"\u0947"), ('o',"\u094B"), )

"""
matra-combined-hals sorted by length of string to parse
"""
def hals_to_combine():
    return tuple([('kh',True),('k',True),('gh',True),('g',True),('Ng',True),\
        ('Nc',True),('NN',False),('Nn',True) ,( 'chh',True ), ('ch',True),\
        ('jh',True),('j',True), ('Xth',True), ('Xt',True), ('Xdh',True),\
        ('Xd',True), ('Xsh',True), ('th',True), ('t',True), ('dh',True),\
        ('d',True), ('n',True), ('ph',True), ('p',True), ('bh',True),('b',True),\
        ('m',True), ('y',True), ('r',True),('l',True), ('v',True), ('sh',True),\
        ('s',True), ('h',True) ])


"""
Combine hals with matras
"""
def hals_combined():
    mts = [k for k,_ in matras()]+['a']
    combined_list =[]
    for ch, togen in hals_to_combine():
        if togen:
            combined_list = combined_list  + [ ch+x for x in mts] +[ch]
            
    return combined_list 

def parse_string_for_devanagari(input_str):
    """
    build a list of aksharas from the string - unknown letters are ignored
    """
    sorted_achs= ('lRii','Rii', 'lRi', 'Ri','ai', "ii","uu",'au',"aa",'a', 'i', 'u', 'e', 'o','M')
    match_re = "("+'|'.join(tuple(hals_combined()) + sorted_achs)+")" + "(.*)"


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
    mainmap =  {
            'NN': "\u0901",
            'M': "\u0902",
            'a': "\u0905",
            'aa': "\u0906",
            'i': "\u0907",
            'ii': "\u0908",
            'u': "\u0909",
            'uu': "\u090A",
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
            'chha':"\u091B",
            'chh':"\u091B\u094D",
            'cha': "\u091A",
            'ch': "\u091A\u094D",
            'ja': "\u091C",
            'j': "\u091C\u094D",
            'jha': "\u091D",
            'jh': "\u091D\u094D",
            'Nca': "\u091E",
            'Nc': "\u091E\u094D",
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
            'p': "\u092A\u094D",
            'pha': "\u092B",
            'ph': "\u092B\u094D",
            'ba': "\u092C",
            'b': "\u092C\u094D",
            'bha': "\u092D",
            'bh': "\u092D\u094D",
            'ma': "\u092E",
            'm': "\u092E\u094D",
            'ya': "\u092F",
            'y': "\u092F\u094D",
            'ra': "\u0930",
            'r': "\u0930\u094D",
            'la': "\u0932",
            'l': "\u0932\u094D",
            'va': "\u0935",
            'v': "\u0935\u094D",
            'sha': "\u0936",
            'sh': "\u0937\u094D",
            'Xsha': "\u0937",
            'Xsh': "\u0937\u094D",
            'sa': "\u0938",
            's': "\u0938\u094D",
            'ha': "\u0939",
            'h': "\u0939\u094D",
            'S': "\u093D",
            }


    for lhs,togen in hals_to_combine():
        # only take first element onf mainmap[lhs] because the second element is halant
        if togen:
            entry = [(lhs+k,mainmap[lhs][0]+v) for k,v in matras() ]
            #print (entry)
            mainmap.update(dict(entry))

    return mainmap


def convert_to_devanagari(strParse):
    strparsed = parse_string_for_devanagari(strParse)
    m = devanagari_map()
    return ''.join(m[ch] for ch in strparsed)   
    



def test():
    print(convert_to_devanagari('uXshXtraM laabhaM labhyate'))

