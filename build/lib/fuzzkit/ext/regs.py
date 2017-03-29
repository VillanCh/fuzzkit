#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Record regs
  Created: 03/29/17
"""

import unittest

from . import states

####################################################################################
## Encode reg
####################################################################################
HTMLENCODE_REG = r'(\&)(\#[0-9]+|\#x[0-9a-fA-F]+|[\w]+\;)(;)?'
HTMLENCODE_REG_LOOSE = r'(\&\#?)([\w]+)(;?)'

JSUNICODE_REG = '(\\\\u)([0-9a-fA-F]{4})'
JSUNICODE_REG_LOOSE = r'(\\\\u)([0-9a-fA-F]{1,4})'

CSSENCODE_REG = '(\\\\)([0-9a-fA-F]{2})'
CSSENCODE_REG_LOOSE = '(\\\\)([0-9a-fA-F]{2,4})'

ASCIIENCODE_REG = '(\\\\)((x[0-9a-fA-F]{2})|([0-9]{1,3}))'

URLENCODE_REG = '(\%)([0-9a-fA-F]{2})'

ENCODE_REG_TABLE = {
    states.HTML_ENCODE: HTMLENCODE_REG,
    states.ASCII_ENCODE: ASCIIENCODE_REG,
    states.CSS_ENCODE: CSSENCODE_REG,
    states.JSUNICODE_ENCODE: JSUNICODE_REG,
    states.URL_ENCODE: URLENCODE_REG
}

####################################################################################
## Filter reg
####################################################################################

SLASH_REG = '\\\\'

if __name__ == '__main__':
    unittest.main()