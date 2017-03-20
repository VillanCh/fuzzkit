#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Core classes for scalpel
  Created: 03/19/17
"""

import unittest
import types
import abc

########################################################################
class TagBase(object):
    """"""
    
    __metaclass__ = abc.ABCMeta


    #----------------------------------------------------------------------
    def __init__(self, name, param1, param2=None):
        """Constructor"""
        self._name = name
        
        self._iter_index = 0
        
        if param2 == None:
            param2 = -1
        
        _p1 = int(param1)
        _p2 = int(param2)
        self._min = min(_p1, _p2)
        self._max = max(_p1, _p2)
        
        self._iterbuffer = []
        self._set_value()
    
    #----------------------------------------------------------------------
    @abc.abstractmethod    
    def _set_value(self):
        """"""
        pass

    #----------------------------------------------------------------------    
    @property
    def type(self):
        """"""
        if hasattr(self, '_type'):
            return getattr(self, '_type')
        else:
            raise NotImplementedError('[x] No Type Set!')
    
    #----------------------------------------------------------------------
    @property
    def value(self):
        """"""
        if hasattr(self, '_value'):
            return self._value
        else:
            return ''
    
    #----------------------------------------------------------------------
    @property    
    def str_value(self):
        """"""
        return str(self._value)
    
    #----------------------------------------------------------------------
    def __iter__(self):
        """"""
        return self
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        if not hasattr(self, '_value'):
            raise StopIteration()
        
        if self._iterbuffer == []:
            if hasattr(self, '_value'):
                self._iterbuffer.append(getattr(self, '_value'))
            else:
                raise StopIteration()
        
        if self._iter_index < len(self._iterbuffer):
            self._iter_index = self._iter_index + 1
            return str(self._iterbuffer[self._iter_index - 1])
        else:
            raise StopIteration()
    
    #----------------------------------------------------------------------
    def reset(self):
        """"""
        self._iter_index = 0
        if isinstance(self._iterbuffer, types.GeneratorType):
            if hasattr(self._iterbuffer, 'reset'):
                getattr(self._iterbuffer, 'reset')()
            else:
                pass
        
        
    #----------------------------------------------------------------------
    @property    
    def name(self):
        """"""
        return self._name
    
    #----------------------------------------------------------------------
    @property    
    def id(self):
        """"""
        return self._name
    

########################################################################
class Template(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        
    
    

if __name__ == '__main__':
    unittest.main()