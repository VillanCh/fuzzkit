#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Define the encode state
  Created: 03/29/17
"""

import unittest

####################################################################################
## common
####################################################################################
ORDINARY = 'ORDINARY'
UNKONWN = 'UNKNOWN'

####################################################################################
## encode state
####################################################################################
HTML_ENCODE = 'HTML_ENCODE'
CSS_ENCODE = 'CSS_ENCODE'
JSUNICODE_ENCODE = 'JAVASCRIPT'
URL_ENCODE = 'URL_ENCODE'
ASCII_ENCODE = 'ASCII'

ASCII_LIKE = tuple([CSS_ENCODE, ASCII_ENCODE])
UNICODE_LIKE = tuple([JSUNICODE_ENCODE,])

####################################################################################
## Filtered
####################################################################################
SLASHED = 'SLASHED'
VANISH = 'VANISHED'
NOCHANGE = 'NOCHANGED'

#----------------------------------------------------------------------
def get_add_slashed_reg():
    """"""
    
 

if __name__ == '__main__':
    unittest.main()