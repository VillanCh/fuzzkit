#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Define the transformer
  Created: 03/29/17
"""

import unittest

from . import states

########################################################################
class Change(object):
    """"""
    pass
    
    

########################################################################
class Transformer(Change):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type, target, transform_type):
        """Constructor"""
        self.orig = orig
        self.orig_type = orig_type
        
        self.target = target
        self.state = transform_type

        
########################################################################
class Filtered(Change):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type, target, filter_type):
        """Constructor"""
        self.orig = orig
        self.orig_type = orig_type
        
        self.target = target
        self.state = filter_type
            
########################################################################
class NoChange(Change):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type):
        """"""
        self.orig = orig
        self.orig_type = orig_type
        self.target = orig
        self.state = 

########################################################################
class UnknowChange(Change):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type, target, target_type):
        """Constructor"""
        self.orig = orig
        self.orig_type = orig_type
        
        self.target = target
        self.state = target_type
        
    
    
        
    

if __name__ == '__main__':
    unittest.main()