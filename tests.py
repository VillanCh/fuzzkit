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

from scalpel.lib import regs
from scalpel.lib import parser
from scalpel.lib import taglib
from scalpel.lib import data


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
            
    #----------------------------------------------------------------------
    def test_parsetag_by_reg(self):
        """"""
        _l = [
            'X(xxx)',
            "ENUM(sdsf)",
            'C(s)',
            'S',
            "N(asd){3}",
            "NS{2}",
            "NS{3,6}",
            "NS(){4}",
            'NC(){5,7}'
        ]
        
        for i in _l:
            _lis = re.findall(regs.TAG_PATTERN, i).pop()
            print(_lis)
            self.assertEqual(11, len(_lis))
    
    #----------------------------------------------------------------------
    def test_parse(self):
        """"""
        self.assertEqual(len(data.TAG_LIST), len(parser.TAG_CLASS_TABLE))
        
        raw = 'asdfasdfaHHHHHH_SX(asd){1,3}HHHHHH_EsdfaaM<L:?<"OP{IO"P{K:HKJ}}>>dfa'
        #print re.findall(regs.TEMPLATE_PATTERN, raw)
        for i in re.findall(regs.TEMPLATE_PATTERN, raw):
            print i
    
    #----------------------------------------------------------------------
    def test_render(self):
        """"""
        render = parser.parse_template('ad_S_SENUM(tt)_E_Efausdg_S_SS(tag){4}_E_Efad_S_SX(x1)_E_Efk_S_SENUM(rag)_E_Ealhsidf',
                                       x1='V!LL$NNNSDF^%%&^$$$$^',
                                       rag=data.ASCII_START_128_BASE,
                                       tt=range(333))
        
        gen = render.render()
        for i in range(666):
            gen.next()
    
    #----------------------------------------------------------------------
    def test_scalpel_instance(self):
        """"""
        
        

if __name__ == '__main__':
    unittest.main()