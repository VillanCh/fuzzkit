#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Core classes for scalpel
  Created: 03/19/17
"""

import unittest
import abc

########################################################################
class TagBase(object):
    """"""
    
    __metaclass__ = abc.ABCMeta

    #----------------------------------------------------------------------
    @abc.abstractproperty    
    def type(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    @abc.abstractproperty
    def value(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    @abc.abstractproperty    
    def str(self):
        """"""
        pass
        
        
    
    

########################################################################
class Template(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        
    
    

if __name__ == '__main__':
    unittest.main()