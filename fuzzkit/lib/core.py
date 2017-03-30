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

from . import conf

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
    def __init__(self, orig, wraper_start=conf.WRAPER_START, wraper_end=conf.WRAPER_END):
        """Constructor"""
        
        #
        # init conf
        #
        self._wraper_start = wraper_start
        self._wraper_end = wraper_end
        
        
        self._orig = orig
        
        self._wraper_flag = {}
        
        self._replace_table_without_enum = {}
        self._replace_table_with_enum = {}
        
        self._finished_empty_finishedtable = False
    
    #----------------------------------------------------------------------
    def feed(self, raw, tag, wraperable=False):
        """"""
        assert isinstance(raw, types.StringTypes)
        self._wraper_flag[tag] = wraperable
        
        if tag._type == 'ENUM':
            self._replace_table_with_enum[raw] = tag
            self._replace_keys_with_enum = self._replace_table_with_enum.keys()
        else:
            self._replace_table_without_enum[raw] = tag
            self._replace_keys_without_enum = self._replace_table_without_enum.keys()
            
        
    
    #----------------------------------------------------------------------
    def _render_without_enums(self, rendered_by_wraper):
        """"""
        _ksn = self._replace_table_without_enum.values()
        _ksn = tuple(_ksn)
        
        
        for i in self._replace_table_without_enum:
            _target = self._replace_table_without_enum[i].value
            _tag = self._replace_table_without_enum[i]
            if self._wraper_flag[_tag]:
                rendered_by_wraper = rendered_by_wraper.replace(i, self._wrap(_target))
            else:
                rendered_by_wraper = rendered_by_wraper.replace(i, _target)

            
        return rendered_by_wraper

    
    #----------------------------------------------------------------------
    def _wrap(self, i):
        """"""
        return self._wraper_start + i + self._wraper_end
        
    
    #----------------------------------------------------------------------
    def render(self):
        """"""
        return self._render()
    
    #----------------------------------------------------------------------
    def _render(self):
        """"""
        for _pre in self._render_with_enums():
            yield self._render_without_enums(_pre)
    
    #----------------------------------------------------------------------
    def _render_with_enums(self):
        """"""
        #
        # render with 
        #
        _ks = self._replace_table_with_enum.values()
        _ks = tuple(_ks)
        if _ks == tuple():
            yield self._orig
        else:   
            w_items = iter_mix(*_ks)
            
        for _mixer in w_items:
            _ret = self._orig
            for index in range(len(self._replace_table_with_enum)):
                _tag = self._replace_table_with_enum[self._replace_keys_with_enum[index]]
                if self._wraper_flag[_tag]:
                    _ret = _ret.replace(self._replace_keys_with_enum[index],
                                        self._wrap(_mixer[index]))
                else:
                    _ret = _ret.replace(self._replace_keys_with_enum[index],
                                        _mixer[index])
            yield _ret
            
    

if __name__ == '__main__':
    unittest.main()