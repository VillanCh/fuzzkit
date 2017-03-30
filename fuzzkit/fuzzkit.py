#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Scalpel main
  Created: 03/19/17
"""

import unittest
from .lib import parser
from .lib import data

########################################################################
class FuzzerConfig:
    """"""

    NC_DEFUALT_LENGTH = '8'
    NS_DEFUALT_LENGTH = '8'
    S_DEFUALT_LENGTH = '8'
    C_DEFUALT_LENGTH = '8'  
    
    DEFAULT_LENGTH = {
        data.NC: NC_DEFUALT_LENGTH,
        data.NS: NS_DEFUALT_LENGTH,
        data.S: S_DEFUALT_LENGTH,
        data.C: C_DEFUALT_LENGTH
    }    
    
    N_DEFAULT_MIN = '10000'
    N_DEFAULT_MAX = '99999'    
    
    VULNUS_START = '_S_S'
    VULNUS_END = '_E_E'
    
    WRAPER_START = 'VULNUS_S'
    WRAPER_END = 'VULNUS_E'        
    

########################################################################
class Fuzzer():
    """"""

    #----------------------------------------------------------------------
    def __init__(self, template, config=None, **render_value):
        """Constructor"""
        #
        # config file
        #
        self._conf = config if config else FuzzerConfig
        
        self._render = parser.parse_template(template, self._conf, **render_value)
        
        self._gen = self._render.render()
        
        
    #----------------------------------------------------------------------
    def __iter__(self):
        """"""
        return self
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        return self._gen.next()
        
        
        
    
    



if __name__ == '__main__':
    unittest.main()