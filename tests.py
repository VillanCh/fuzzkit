#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test for scalpel_new
  Created: 03/19/17
"""

import unittest
import re
import types

from scalpeln.lib import regs
from scalpeln.lib import parser
from scalpeln.lib import taglib


########################################################################
class ScalpelTester(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_regs(self):
        """"""
        raw = 'adfasdfasdf' + regs.VULNUS_START + 'v1ll4n><>?LL:"{PPKLJL}' + regs.VULNUS_END + 'asdfasdfasdf'
    
    #----------------------------------------------------------------------
    def test_taglib(self):
        """"""
        e1 = taglib.ENUM('e1')
        e1.value = [1,2,3,5,4]
        for i in e1:
            self.assertIsInstance(i, types.StringTypes)
        
        self.assertRaises(StopIteration, e1.next)
        
        e1.reset()
        for i in e1:
            self.assertIsInstance(i, types.StringTypes)
            
        x1 = taglib.X('x1')
        x1.value = 'XXXX'
        
        for i in x1:
            self.assertEqual('XXXX', i)
        
        x1.reset()
        for i in x1:
            self.assertEqual('XXXX', i)
            
        for i in taglib.N(name='s', min_value=333, max_value=6666):
            self.assertTrue(int(i) < 6666 and int(i) >= 333)
        
        for i in taglib.NS(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.NS('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7)
        
        for i in taglib.NC(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.NC('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7) 
        
        for i in taglib.S(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.S('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7)         
            
            
        

if __name__ == '__main__':
    unittest.main()