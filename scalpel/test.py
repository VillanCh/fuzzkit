#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test For Scalpel
  Created: 2016/12/20
"""

import unittest
import re
from core import Scalpel
from core import SVariable


########################################################################
class ScalpelTest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_regcheck(self):
        """Test For regex"""
        
        r1 = [
            '{[{N(name){4,6}}]}',
            '{[{N(name){6}}]}',    
            '{[{N(name){}}]}',
            '{[{N(name)}]}',
            '{[{N{4,5}}]}',
            '{[{N{4}}]}',
            '{[{N{}}]}',
            '{[{N}]}',
        ]
        
        r2 = [
            '{[{NC(name){4,6}}]}',
            '{[{NC(name){6}}]}',    
            '{[{NC(name){}}]}',
            '{[{NC(name)}]}',
            '{[{NC{4,5}}]}',
            '{[{NC{4}}]}',
            '{[{NC{}}]}',
            '{[{NC}]}',
        ]
        
        r3 = [
            '{[{X(name){4,6}}]}',
            '{[{X(name){6}}]}',    
            '{[{X(name){}}]}',
            '{[{X(name)}]}',
            '{[{X{4,5}}]}',
            '{[{X{4}}]}',
            '{[{X{}}]}',
            '{[{X}]}',
        ]
        
        r4 = [
            '{[{UUID(name){4,6}}]}',
            '{[{UUID(name){6}}]}',    
            '{[{UUID(name){}}]}',
            '{[{UUID(name)}]}',
            '{[{UUID{4,5}}]}',
            '{[{UUID{4}}]}',
            '{[{UUID{}}]}',
            '{[{UUID}]}',
            '{[{UUID{hex}}]}',
            '{[{UUID{raw}}]}'
        ]
        
        reg_number = r'(\{\[\{(N)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({([1-9]\d*)?,?([1-9]\d*)?})?\}\]\})'
        reg_randomstr = r'(\{\[\{(NS|NC|S|C)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({([1-9]\d*)?,?([1-9]\d*)?})?\}\]\})'
        reg_custom = r'(\{\[\{(X|ENUM)(\(([a-zA-z_][a-zA-Z_0-9]*)\))\}\]\})'
        reg_uuid = r'(\{\[\{(UUID)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({(hex|raw)})?\}\]\})'
        
        for i in r1:
            print re.findall(pattern=reg_number, string=i)
            print re.findall(pattern=reg_randomstr, string=i)
            print re.findall(pattern=reg_randomstr, string=i)
            print re.findall(pattern=reg_uuid, string=i)
            
        for i in r2:
            print re.findall(pattern=reg_randomstr, string=i)    
        
        for i in r3:
            print re.findall(pattern=reg_custom, string=i)
        
        for i in r4:
            print re.findall(pattern=reg_uuid, string=i)        
        
    #----------------------------------------------------------------------
    def test_scalpel_basic_api(self):
        """"""
        
        scalpel = Scalpel(template='{[{X(border)}]}<scr{[{ENUM(xxx)}]}ipt{[{N(asdf){444,997}}]}></scr{[{ENUM(enumt)}]}ip{[{ENUM(enumts)}]}t>',
                          enumt=['1','2','5','6'],
                          enumts=['7','a','c','6'],
                          xxx=['c','e3','adf','xss'],
                          border='Fuckin')
        table = scalpel.variable_table
        self.assertIsInstance(table['asdf'], SVariable)
        print table
        asdf = table['asdf']
        print "NAME", asdf.name
        print "VALUE", asdf.value
        print "TYPE", asdf.type
        #payloads = get_payloads()
        for i in scalpel.payloads:
            print i


if __name__ == '__main__':
    unittest.main()