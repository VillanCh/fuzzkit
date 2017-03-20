#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: define regs
  Created: 03/19/17
"""

from . import data

VULNUS_START = 'sc41p3l5t4rt'
VULNUS_END = 'sc41p3l3nd'

EXTRACT_PATTERN = VULNUS_START + '(.*)' + VULNUS_END

#
# Tag Parser Regs
#

####################################################################################
_PARSE_TAG = "(\(([a-zA-Z0-9_]*)\))"
_PARSE_PARAMS = "(\{([0-9]+(,([0-9]+)?)?)\})"
####################################################################################

NS_PATTERN = data.NS + _PARSE_TAG + '?' + _PARSE_PARAMS + '?'
