#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Extract the data
  Created: 03/21/17
"""

import unittest
import re

from . import regs

_TAG_INDEX = 1
_RSP_INDEX = 1

#----------------------------------------------------------------------
def extract_vulnus(raw):
    """"""
    for i in re.findall(regs.EXTRACT_RSP_PATTERN, string=raw):
        yield i
    

if __name__ == '__main__':
    unittest.main()