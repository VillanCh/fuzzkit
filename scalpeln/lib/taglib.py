#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: TagLib
  Created: 03/19/17
"""

import unittest
import random

from .core import TagBase
from . import data


########################################################################
class N(TagBase):
    """"""
    
    _type = data.N

    #----------------------------------------------------------------------
    def __init__(self, name, min_value, max_value):
        """Constructor"""
        self._name = name
        
        self._min = int(min_value)
        self._max = int(max_value)
        
        if isinstance(self._min, int) and isinstance(self._max, int):
            self._value = str(random.randint(self._min, self._max))
        else:
            self._value = 13453
    
    #----------------------------------------------------------------------
    @property
    def type(self):
        """"""
        return self._type
    
    #----------------------------------------------------------------------
    @property
    def value(self):
        """"""
        return 
        

########################################################################
class NS(TagBase):
    """"""

    _type = data.NS

    #----------------------------------------------------------------------
    def __init__(self, name, length_1, length_2=None):
        """Constructor"""
        
        
    
    
        
    
    

if __name__ == '__main__':
    unittest.main()