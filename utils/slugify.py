# coding=utf-8

import re
import unicodedata
from htmlentitydefs import name2codepoint
from django.utils.encoding import smart_unicode, force_unicode


def slugify(s, entities=True, decimal=True, hexadecimal=True,
   instance=None, slug_field='slug', filter_dict=None):

    s = s.encode("utf8")
    s = s.replace("\xc3","")
    special_chars = [r"[àáâãäåæ]",r"[èéêë]",r"[ìíîï]",r"[òóôõöø]",r"[ùúûü]",r"[ç]",r"[ñ]",r"[ð]",r"[ýÿ]",r"[þ]",r"[ÀÁÂÃÄÅÆ]",r"[ÈÉÊË]",r"[ÌÍÎÏ]",r"[ÒÓÔÕÖØ]",r"[ÙÚÛÜ]",r"[Ž]",r"[Ç]",r"[Ñ]",r"[«»·]",r"[‡±™¿?!¡„]"];
    convert_chars = ['a','e','i','o','u','c','n','d','y','b',
                      'A','E','I','O','U','Z','C','N','-',''];
    for i in range(len(convert_chars)):
         s = re.sub(special_chars[i],convert_chars[i], s)
         #s = s.replace(special_chars[i],convert_chars[i]);

    s.decode("utf8")

    s = smart_unicode(s)

    #character entity reference
    if entities:
        s = re.sub('&(%s);' % '|'.join(name2codepoint), lambda m: unichr(name2codepoint[m.group(1)]), s)

    #decimal character reference
    if decimal:
        try:
            s = re.sub('&#(\d+);', lambda m: unichr(int(m.group(1))), s)
        except:
            pass

    #hexadecimal character reference
    if hexadecimal:
        try:
            s = re.sub('&#x([\da-fA-F]+);', lambda m: unichr(int(m.group(1), 16)), s)
        except:
            pass

    #translate
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    #replace unwanted characters
    s = re.sub(r'[^-a-z0-9]+', '-', s.lower())

    #remove redundant -
    s = re.sub('-{2,}', '-', s).strip('-')

    slug = s

    s = re.sub(r"[^-\w\s]", '', s)
    s = re.sub(r"^\s+|\s+$", '',s)
    s = re.sub(r"[\s]+", '_',s)
    s = s.lower();

    return s
