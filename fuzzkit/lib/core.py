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
from . import data
from . import regs

from g3ar.utils.iter_utils import iter_mix

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
class TagRender(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig):
        """Constructor"""
        
        self._orig = orig
        
        self._replace_table = {}
        self._replace_table_with_wraper = {}
    
    #----------------------------------------------------------------------
    def feed(self, raw, tag, wraperable=False):
        """"""
        assert isinstance(raw, types.StringTypes)
        
        if wraperable:
            self._replace_table_with_wraper[raw] = tag
            self._replace_keys_with_wraper = self._replace_table_with_wraper.keys()
        else:
            self._replace_table[raw] = tag
            self._replace_keys = self._replace_table.keys()
    
    #----------------------------------------------------------------------
    def _render_no_wraper(self):
        """"""
        _ksn = self._replace_table.values()
        _ksn = tuple(_ksn)
        if _ksn == tuple():
            raise GeneratorExit
        nw_items = iter_mix(*_ksn)
        for _i in nw_items:
            _ret = self._orig
            for i in range(len(self._replace_table)):
                _ret = _ret.replace(self._replace_keys[i], _i[i])
            yield _ret
    
    #----------------------------------------------------------------------
    def _render_wraper(self):
        """"""
        _ks = self._replace_table_with_wraper.values()
        _ks = tuple(_ks)
        if _ks == tuple():
            w_items = []
        else:   
            w_items = iter_mix(*_ks)
        for _i in w_items:
            for _orig in self._render_no_wraper():
                for index in range(len(self._replace_table_with_wraper)):
                    _orig = _orig.replace(self._replace_keys_with_wraper[index], self._wrap(_i[index]))
                yield _orig
        else:
            for _orig in self._render_no_wraper():
                yield _orig
    
    #----------------------------------------------------------------------
    def _wrap(self, i):
        """"""
        return data.WRAPER_START + i + data.WRAPER_END
        
    
    #----------------------------------------------------------------------
    def render(self):
        """"""
        return self._render_wraper()
    

if __name__ == '__main__':
    unittest.main()