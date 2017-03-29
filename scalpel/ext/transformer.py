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
    
    name = 'Change'
    
    #----------------------------------------------------------------------
    def __repr__(self):
        """"""
        return "<{name} (\"{orig}\"-{otype}) => (\"{target}\"={ttype})>".format(
            orig=self.orig,
            otype=self.orig_type,
            target=self.target,
            ttype=self.state,
            name=self.name
        )
    
    

########################################################################
class Transformer(Change):
    """"""

    name = 'Transformer'

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

    name = 'Filtered'

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
    
    name = 'NoChange'    
    
    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type):
        """"""
        self.orig = orig
        self.orig_type = orig_type
        self.target = orig
        self.state = states.NOCHANGE

########################################################################
class UnknownChange(Change):
    """"""
    
    name = 'UnknownChange'
    
    #----------------------------------------------------------------------
    def __init__(self, orig, orig_type, target, target_type):
        """Constructor"""
        self.orig = orig
        self.orig_type = orig_type
        
        self.target = target
        self.state = target_type
        
    
    
        
    

if __name__ == '__main__':
    unittest.main()