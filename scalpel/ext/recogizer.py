#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Recogize code
  Created: 03/29/17
"""

import unittest
import re

from . import regs
from . import states

#----------------------------------------------------------------------
def recognize_type(orig, encoding='utf8'):
    """"""
    try:
        _orig = unicode(orig)
    except:
        try:
            _orig = orig.decode(encoding)
        except:
            _orig = ''
        
    for type_and_reg in regs.ENCODE_REG_TABLE.items():
        _type = type_and_reg[0]
        _reg = type_and_reg[1]
        
        if re.match(_reg, orig):
            return _type
        
        if re.match(_reg, _orig):
            return _type
        
    return states.ORDINARY
        

if __name__ == '__main__':
    unittest.main()