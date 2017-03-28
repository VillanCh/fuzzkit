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
def css_encode_raw(orig, encoding=DEFAULT_ENCODING, standard=False):
    """"""
    origlist = list(orig)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)
    #_hex_list = map(codecs_common.num_extend, _hex_list)
    
    def _p(c):
        return CSS_DIVIDER + c
    _hex_list = map(_p, _hex_list)
    return ''.join(_hex_list)

#----------------------------------------------------------------------
def jsunicode_encode_raw(orig, encoding=DEFAULT_ENCODING, standard=True):
    """"""
    origlist = list(orig)
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
    origlist = list(orig)
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
    origlist = list(orig)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)
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
    origlist = list(orig)
    _hex_list = map(lambda x: codecs_common.unicode_to_hexstr(x, encoding), origlist)
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
    origlist = list(orig)
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