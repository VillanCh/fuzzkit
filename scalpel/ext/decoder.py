#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Decoder
  Created: 03/29/17
"""

import unittest
from .encoder import DEFAULT_ENCODING

#----------------------------------------------------------------------
def _decode_unicode(raw, divider, callback, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    _raw_list = raw.split(divider)
    _raw_list = filter(lambda x: False if x == '' or x == None\
                       else True, _raw_list)
    _hex_list = map(callback, _raw_list)
    _hex_list = map(lambda x: str(x), _hex_list)
    
    
    if hexable:
        pass
    else:
        _hex_list = map(lambda x: hex(int(x))[2:], _hex_list)
    
    def _p(x):
        while x.startswith('x'):
            x = x[1:]
        return unichr(eval('0x' + x))
        
    
    _hex_list = map(_p, _hex_list)
    raw = ''.join(_hex_list)    
    return raw

#----------------------------------------------------------------------
def _decode(raw, divider, callback, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    _raw_list = raw.split(divider)
    _raw_list = filter(lambda x: False if x == '' or x == None\
                       else True, _raw_list)
    _hex_list = map(callback, _raw_list)
    _hex_list = map(lambda x: str(x), _hex_list)
    
    
    if hexable:
        pass
    else:
        _hex_list = map(lambda x: hex(int(x))[2:], _hex_list)
    
    def _p(x):
        return chr(eval('0x' + x))
        
    
    _hex_list = map(_p, _hex_list)
    raw = ''.join(_hex_list)    
    return raw.decode(encoding)

#----------------------------------------------------------------------
def css_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        return char
    
    _divider = '\\'
    
    return _decode(orig, _divider, _cb, encoding, hexable)

#----------------------------------------------------------------------
def jsunicode_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        while True:
            if char.startswith('0'):
                char = char[1:]
            else:
                break
        return char
    
    _divider = '\\u'
    
    return _decode_unicode(orig, _divider, _cb, encoding, hexable)

#----------------------------------------------------------------------
def unicode_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        while True:
            if char.startswith('0'):
                char = char[1:]
            else:
                break
        return char
    
    _divider = '\\u'
    
    return _decode_unicode(orig, _divider, _cb, encoding, hexable)

#----------------------------------------------------------------------
def urlencode_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        return char
    
    _divider = '%'
    
    return _decode(orig, _divider, _cb, encoding, hexable)

#----------------------------------------------------------------------
def ascii_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        return char
    
    if hexable:
        _divider = '\\x'
    else:
        _divider = '\\'
        
    return _decode(orig, _divider, _cb, encoding, hexable)   
        
#----------------------------------------------------------------------
def html_decode_from_raw(orig, encoding=DEFAULT_ENCODING, hexable=True):
    """"""
    def _cb(char):
        if char.endswith(';'):
            char = char[:-1]
            
        if 'x' in char:
            return char[char.index('x'):]
        else:
            return hex(int(char[char.index('&#'):]))[2:]
    
    _divider = '&#'
    
    return _decode_unicode(orig, _divider, _cb, encoding, hexable)


if __name__ == '__main__':
    unittest.main()