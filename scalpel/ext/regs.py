#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Record regs
  Created: 03/29/17
"""

import unittest

####################################################################################
## Encode reg
####################################################################################
HTMLENCODE_REG = r'(\&\#)([\w]+)(;)'
HTMLENCODE_REG_LOOSE = r'(\&\#)([\w]+)(;?)'

JSUNICODE_REG = r'(\\u)([0-9a-fA-F]{4})'
JSUNICODE_REG_LOOSE = r'(\\u)([0-9a-fA-F]{1,4})'

CSSENCODE_REG = r'(\\)([0-9a-fA-F]{2,4})'
CSSENCODE_REG = r'(\\)([0-9a-fA-F]{2,4})'

ASCIIENCODE_REG = r'\\((x[0-9a-fA-F]{2})|([0-9]{1,3}))'

URLENCODE_REG = r'(\%)([0-9a-fA-F]{2})'

####################################################################################
## Filter reg
####################################################################################
_ADDED_SLASH_TEMPLATE = r'\\({orig})'
#----------------------------------------------------------------------
def get_added_slash_reg(orig):
    """"""
    return _ADDED_SLASH_TEMPLATE.format(orig=orig)

raise NotImplemented('NOT TEST REGS!')

if __name__ == '__main__':
    unittest.main()