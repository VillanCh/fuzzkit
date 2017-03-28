#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: code common
  Created: 03/28/17
"""

import unittest
import sys
import types

GBK = 'GBK'
UTF8 = 'UTF8'

DEFAULT_ENCODING = UTF8

s = ''

#----------------------------------------------------------------------
def unicode_to_hexstr(char, encoding=DEFAULT_ENCODING):
    """"""
    hexnum = None
    if isinstance(char, unicode):
        raw = repr(char)[2:]
        if 'u' in raw:
            hexnum = raw[2:-1]
        else:
            hexnum = hex(ord(char))[2:]
    elif isinstance(char, str):
        char = char.decode(encoding)
        hexnum = unicode_to_hexstr(char)
    
    return hexnum

#----------------------------------------------------------------------
def unicode_build_from_number(orig, hexable=True):
    """"""
    if isinstance(orig, int):
        return unichr(orig)
    elif isinstance(orig, types.StringTypes):
        if hexable:
            return unichr(eval('0x' + orig))
        else:
            return unichr(int(orig))

#----------------------------------------------------------------------
def unicode_escape(orig):
    """"""
    if isinstance(orig, unicode):
        raw = repr(orig)
        return raw[2:-1]
    else:
        return repr(orig)[1:-1]

#----------------------------------------------------------------------
def num_extend(orig, size=4, filled='0'):
    """"""
    if len(orig) >= size:
        return orig
    else:
        return filled * (size - len(orig)) + orig

if __name__ == '_ain__':
    unittest.main()