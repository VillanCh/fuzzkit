#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: 
  Created: 2016/12/22
"""

import unittest
 

#----------------------------------------------------------------------
def ascii_range_dec(start, end):
    """"""
    return map(chr, range(start, end))

#----------------------------------------------------------------------
def ascii_range_hex(start, end):
    """"""
    return map(chr, range(start, end))

#----------------------------------------------------------------------
def htmlencodechar_range(start, end, is_hex=True):
    """
    &#1235;
    &#xff35;
    """
    def htmlencode(num):
        if is_hex:
            return '&#' + str(hex(num))[1:] + ';'
        else:
            return '&#' + str(int(num)) + ';'
        
    return map(htmlencode, range(start, end))

#----------------------------------------------------------------------
def jsunicode_range(start, end):
    """"""
    def jsunicode(num):
        return '\\u' + str(hex(num))[2:]
    return map(jsunicode, range(start, end))

#----------------------------------------------------------------------
def cssencode_range(start, end):
    """"""
    def cssencode(num):
        return '\\' + str(hex(num))[2:]
    return map(cssencode, range(start, end))    
    
#----------------------------------------------------------------------
def byte_range(start, end, is_hex=False):
    """"""
    def byteencode(num):
        if is_hex:
            return '\\' + str(hex(num))[1:]
        else:
            return '\\' + str(int(num))
    return map(byteencode, range(start, end))  
        
    
    
########################################################################
class CharRangeGenerator(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def runTest(self):
        """"""
        print(ascii_range_dec(44,88))
        print(ascii_range_hex(0x00, 0xf0))
        print(htmlencodechar_range(0, 54))
        print(jsunicode_range(0, 66))
        print(cssencode_range(0, 0xff))
        print(byte_range(0, 0xff, is_hex=True))
        print(byte_range(0, 0xff, is_hex=False))
        
        
    
    

if __name__ == '__main__':
    unittest.main()