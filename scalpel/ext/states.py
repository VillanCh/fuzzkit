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
ORDINARY = 'ordinary'

####################################################################################
## encode state
####################################################################################
HTML_ENCODE = 'html'
CSS_ENCODE = 'css'
JSUNICODE_ENCODE = 'javascript'
URL_ENCODE = 'url'
ASCII_ENCODE = 'ascii'

ASCII_LIKE = tuple([CSS_ENCODE, ASCII_ENCODE])
UNICODE_LIKE = tuple([JSUNICODE_ENCODE,])

####################################################################################
## Filtered
####################################################################################
SLASHED = 'slashed'
VANISH = 'vanish'

#----------------------------------------------------------------------
def get_add_slashed_reg():
    """"""
    
 

if __name__ == '__main__':
    unittest.main()