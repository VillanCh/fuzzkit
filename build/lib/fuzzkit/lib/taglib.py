#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: TagLib
  Created: 03/19/17
"""

import unittest
import random
import types
import uuid

from .core import TagBase
from . import data


########################################################################
class N(TagBase):
    """"""
    
    _type = data.N

    #----------------------------------------------------------------------
    def __init__(self, name, min_value, max_value):
        TagBase.__init__(self, name, param1=min_value, param2=max_value)
    
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        self._value = str(random.randint(self._min, self._max))
    


########################################################################
class NC(TagBase):
    """"""
    
    _type = data.NC

    #----------------------------------------------------------------------
    def __init__(self, name, length_1, length_2=None):
        """Constructor"""
        
        TagBase.__init__(self, name, param1=length_1, param2=length_2)
        
        
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        if self._min < 0:
            smpl = random.sample(k=self._max, population=data.LETTER_LOW_BASE + \
                                 data.NUMBER_BASE)
        else:
            smpl = random.sample(k=random.randint(self._min, self._max),
                                 population=data.LETTER_LOW_BASE + data.NUMBER_BASE)
        
        self._value = ''.join(smpl)


########################################################################
class NS(TagBase):
    """"""
    
    _type = data.NS

    #----------------------------------------------------------------------
    def __init__(self, name, length_1, length_2=None):
        """Constructor"""
        
        TagBase.__init__(self, name, param1=length_1, param2=length_2)
        
        
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        if self._min < 0:
            smpl = random.sample(k=self._max, 
                                 population=data.NUMBER_BASE)
        else:
            smpl = random.sample(k=random.randint(self._min, self._max),
                                 population=data.NUMBER_BASE)
        
        self._value = ''.join(smpl)
        
        
########################################################################
class S(TagBase):
    """"""
    
    _type = data.S  

    #----------------------------------------------------------------------
    def __init__(self, name, length_1, length_2=None):
        """Constructor"""
        TagBase.__init__(self, name, length_1, length_2)
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        if self._min < 0:
            smpl = random.sample(k=self._max, population=data.LETTER_LOW_BASE)
        else:
            smpl = random.sample(k=random.randint(self._min, self._max),
                                 population=data.LETTER_LOW_BASE)
        self._value = ''.join(smpl)
        
        
########################################################################
class C(S):
    """"""
    
    _type = data.C

    pass


########################################################################
class UUID(TagBase):
    """"""

    _type = data.UUID

    #----------------------------------------------------------------------
    def __init__(self, name):
        """Constructor"""
        TagBase.__init__(self, name, 0, 0)
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        self._value = uuid.uuid1().hex
        

########################################################################
class ENUM(TagBase):
    """"""

    _type = data.ENUM

    #----------------------------------------------------------------------
    def __init__(self, name):
        """Constructor"""
        TagBase.__init__(self, name, 0, 0)
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    def next(self):
        """"""
        if hasattr(self, '_value'):
            _value = getattr(self, '_value')

            #
            # handle generator
            #
            if isinstance(_value, tuple([types.GeneratorType,])):
                #
                # generator
                #
                return str(self._iterbuffer.next())
            
            
            #
            # handle iter
            #
            if self._iterbuffer == []:
                if isinstance(_value, tuple([list, tuple])):
                    #
                    # select and reset by index
                    #
                    self._iterbuffer = _value
                else:
                    #
                    # add _value to self._iterbuffer
                    #
                    self._iterbuffer.append(object)            
            
            
            if self._iter_index >= len(self._iterbuffer):
                raise StopIteration()
            else:
                self._iter_index = self._iter_index + 1
                return str(self._iterbuffer[self._iter_index - 1])                
                    
        else:
            raise StopIteration()    
    
    #----------------------------------------------------------------------
    @property    
    def value(self):
        """"""
        return self._value if hasattr(self, '_value') else ''
    
    #----------------------------------------------------------------------
    @value.setter
    def value(self, args):
        """"""
        self._value = args
        
        
########################################################################
class X(TagBase):
    """"""
    
    _type = data.X

    #----------------------------------------------------------------------
    def __init__(self, name):
        """Constructor"""
        TagBase.__init__(self, name, 0, 0)
        
    #----------------------------------------------------------------------
    def _set_value(self):
        """"""
        pass
    
    #----------------------------------------------------------------------
    @property    
    def value(self):
        """"""
        return self._value if hasattr(self, '_value') else None
    
    #----------------------------------------------------------------------
    @value.setter    
    def value(self, args):
        """"""
        self._value = args
        
    
    
    
        
    
    
    
        
    
    

if __name__ == '__main__':
    unittest.main()