#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test for scalpel_new
  Created: 03/19/17
"""

import unittest
import re

from scalpeln.lib import regs
from scalpeln.lib import parser


########################################################################
class ScalpelTester(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_regs(self):
        """"""
        raw = 'adfasdfasdf' + regs.VULNUS_START + 'v1ll4n><>?LL:"{PPKLJL}' + regs.VULNUS_END + 'asdfasdfasdf'
        
    

if __name__ == '__main__':
    unittest.main()