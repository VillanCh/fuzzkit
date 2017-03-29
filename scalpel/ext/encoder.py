#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Encoder
  Created: 03/21/17
"""

import unittest
import types
import re

from ..lib import data
from . import codecs_common



#
# URL encoder
#
# !*'();:@&=+$,/?#[]
URL_SAFE_CHAR = data.LETTER_HIGH_BASE + data.LETTER_LOW_BASE + list('0123456789') + list("-_.+,")

GBK = 'GBK'
UTF8 = 'UTF8'

DEFAULT_ENCODING = UTF8

####################################################################################
## DIVIDE TEMP
####################################################################################

CSS_DIVIDER = '\\'
JSUNICODE_DIVIDER = '\\u'
UNICODE_DIVIDER = '\\u'
HTML_DIVIDER = '&#x'
URLENCODE_DIVIDER = '%'
PERCENT_DIVIDER = URLENCODE_DIVIDER
ASCII_DIVIDER = '\\x'

#----------------------------------------------------------------------
def encode_unichar_to_hexlist(char, encoding=DEFAULT_ENCODING):
    """"""
    assert isinstance(char, unicode)
    
    raw = repr(char.encode(encoding))[1:-1]
    _raw = ''
    if '\\x' not in raw:
        for i in raw:
            _raw = _raw + hex(ord(i)).replace('0x', '\\x')
        raw = _raw
        
    return filter(lambda x: False if x == '' or x == None else True,
                  raw.split('\\x'))
    
    

#----------------------------------------------------------------------
def _str2unicode_list(orig, encoding=DEFAULT_ENCODING):
    """"""
    try:
        return list(unicode(orig))
    except:
        return list(orig.decode(encoding))


    

#----------------------------------------------------------------------
def css_encode_raw(orig, encoding=DEFAULT_ENCODING, standard=False):
    """"""
    
    origlist = _str2unicode_list(orig, encoding)
    
    def _reduce_iter(x, y):
        """"""
        if isinstance(x, list):
            return x + encode_unichar_to_hexlist(y, encoding)
        else:
            return encode_unichar_to_hexlist(x, encoding) + \
                   encode_unichar_to_hexlist(y, encoding)
        
    _hex_list = reduce(_reduce_iter, origlist)
    #_hex_list = map(codecs_common.num_extend, _hex_list)
    
    def _p(c):
        return CSS_DIVIDER + c
    _hex_list = map(_p, _hex_list)
    return ''.join(_hex_list)

#----------------------------------------------------------------------
def jsunicode_encode_raw(orig, encoding=DEFAULT_ENCODING, standard=True):
    """"""
    origlist = _str2unicode_list(orig, encoding)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)
    
    if standard:
        _hex_list = map(codecs_common.num_extend, _hex_list)
    
    def _p(char):
        return JSUNICODE_DIVIDER + char
    _hex_list = map(_p, _hex_list)
    
    return ''.join(_hex_list)

#----------------------------------------------------------------------
def unicode_encode_raw(orig, encoding=DEFAULT_ENCODING, standard=True):
    """"""
    origlist = _str2unicode_list(orig, encoding)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)

    if standard:
        _hex_list = map(codecs_common.num_extend, _hex_list)
    def _p(c):
        return UNICODE_DIVIDER + c
    
    _hex_list = map(_p, _hex_list)
    return ''.join(_hex_list)

#----------------------------------------------------------------------
def urlencode_encode_raw(orig, encoding=DEFAULT_ENCODING):
    """"""
    origlist = _str2unicode_list(orig, encoding)
    def _reduce_iter(x, y):
        """"""
        if isinstance(x, list):
            return x + encode_unichar_to_hexlist(y, encoding)
        else:
            return encode_unichar_to_hexlist(x, encoding) + \
                   encode_unichar_to_hexlist(y, encoding)
        
    _hex_list = reduce(_reduce_iter, origlist)

    _hexstr = ''.join(_hex_list)
    assert len(_hexstr) % 2 == 0
    
    _hex_list = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", ' ', _hexstr).split()
    
    def _p(c):
        return PERCENT_DIVIDER + c
        
    _hex_list = map(_p, _hex_list)
    
    return ''.join(_hex_list)

#----------------------------------------------------------------------
def ascii_encode_raw(orig, encoding=DEFAULT_ENCODING):
    """"""
    origlist = _str2unicode_list(orig, encoding)
    def _reduce_iter(x, y):
        """"""
        if isinstance(x, list):
            return x + encode_unichar_to_hexlist(y, encoding)
        else:
            return encode_unichar_to_hexlist(x, encoding) + \
                   encode_unichar_to_hexlist(y, encoding)
        
    _hex_list = reduce(_reduce_iter, origlist)
    _hexstr = ''.join(_hex_list)
    assert len(_hexstr) % 2 == 0
    
    _hex_list = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", ' ', _hexstr).split()
    
    def _p(c):
        return ASCII_DIVIDER + c
        
    _hex_list = map(_p, _hex_list)
    
    return ''.join(_hex_list)
     

#----------------------------------------------------------------------
def htmlentity_encode_raw(orig, encoding=DEFAULT_ENCODING, suffix=';', standard=True):
    """"""
    origlist = _str2unicode_list(orig, encoding)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)

    if standard:
        _hex_list = map(codecs_common.num_extend, _hex_list)
    def _html_char_encode(char):
        if suffix:
            return HTML_DIVIDER + char + ';'
        else:
            return HTML_DIVIDER + char
    
    _hex_list = map(_html_char_encode, _hex_list)
        
    return ''.join(_hex_list)



if __name__ == '__main__':
    unittest.main()