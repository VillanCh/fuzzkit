#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: HTML Lexer
  Created: 2016/12/22
"""

import unittest

from ply import lex

#
# Define TOKEN
#
tokens = (
    'IDENTIFIER',
    'PUNCTUATION',
    'HTMLENCODEID',
    'HTMLENTIRY',
    'DUOBLEBYTE',
    'DIGIT'
)

t_ignore = ' \t\n'
t_DUOBLEBYTE = '[^\x00-\xff]+'
t_HTMLENTIRY = r'&[a-zA-Z]+;?'
t_HTMLENCODEID = r'&\#[0-9]+;?'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_PUNCTUATION = r"[\`\!\@\#\$\%\^\&\*\(\)\-\_\\\=\+\[\]\{\}\|\;\:\"'\/\?\.\>\,\<]"
t_DIGIT = r'[0-9]'


#----------------------------------------------------------------------
def t_error(t):
    """"""
    print('ILLEGAL CHARACTER!', t.value[0])
    print(t.value[0])
    t.lexer.skip(1)
    


#----------------------------------------------------------------------
def get_general_lexer():
    """"""
    return lex.lex()

########################################################################
class LexerTest(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_basic_parse(self):
        """"""
        text = '''  return self.run(*args, **kwds)
File "C:\Python27\Lib\unittest\suite.py", line 108, in run
  test(result)
File "C:\Python27\Lib\unittest\case.py", line 393, in __call__
  return self.run(*args, **kwds)
File "C:\Python27\Lib\unittest\case.py", line 329, in run
  testMethod()
￼ File "c:\Users\villa\OneDrive\github\TDD\scalpel\scalpel\lexs\htmllex.py", line 73, in test_basic_parse
  htmllexer = get_general_lexer()
￼ File "c:\Users\villa\OneDrive\github\TDD\scalpel\scalpel\lexs\htmllex.py", line 43, in get_general_lexer
  return lex.lex()
File "C:\Python27\Lib\site-packages\ply\lex.py", line 907, in lex
  raise SyntaxError("Can't build lexer")'''
        
        htmllexer = get_general_lexer()
        htmllexer.input(text)
        
        for i in htmllexer:
            pass
            
        
        
        
    
    

if __name__ == '__main__':
    unittest.main()