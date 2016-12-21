#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Render The Template
  Created: 2016/12/20
"""

import unittest
import types
import random
import time
import warnings
import uuid
import re
import itertools

REG_N = r'(\{\[\{(N)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({([1-9]\d*)?,?([1-9]\d*)?})?\}\]\})'
REG_NS_NC_S_C = r'(\{\[\{(NS|NC|S|C)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({([1-9]\d*)?,?([1-9]\d*)?})?\}\]\})'
REG_ENUM_X = r'(\{\[\{(X|ENUM)(\(([a-zA-z_][a-zA-Z_0-9]*)\))\}\]\})'
REG_UUID = r'(\{\[\{(UUID)(\(([a-zA-z_][a-zA-Z_0-9]*)?\))?({(hex|raw)})?\}\]\})'

SVTYPE_LIST = ['N', 'NC', 'S', 'C', 'NS', 'ENUM', 'UUID', 'X']

NS = 'NS'
NC = 'NC'
N = 'N'
S = 'S'
C = 'C'
ENUM = 'ENUM'
UUID = 'UUID'
X = 'X'

random.seed(time.time())

#----------------------------------------------------------------------
def get_random_digit():
    """"""
    base = '0123456789'
    return random.choice(base)
    
#----------------------------------------------------------------------
def get_random_word():
    """"""
    number = range(48, 58)
    small_c = range(97, 123)
    big_c = range(65, 91)
    return chr(random.choice(random.choice([number, small_c, big_c])))

#----------------------------------------------------------------------
def get_random_char():
    """"""
    small_c = range(97, 123)
    big_c = range(65, 91)
    return chr(random.choice(random.choice([small_c, big_c])))    

#----------------------------------------------------------------------
def get_uuid(type='raw'):
    """"""
    if type == 'raw':
        return str(uuid.uuid1())
    elif type == 'hex':
        return str(uuid.uuid1().hex)

#----------------------------------------------------------------------
def findall(template, reg):
    """"""
    return re.findall(reg, template)
    

########################################################################
class Scalpel(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, template, random_every_time=True, **kwargs):
        """Constructor"""
        assert isinstance(template, (str, unicode)), "Error payload " + \
               "tempate, should be a str or unicode"
        self._template = template
        self._random_every_time = random_every_time
        self._kwarfs = kwargs
        self._variable_table = {}
    
        self._parse_scalpel_variables()
        
        self._payloads = []
    
    #----------------------------------------------------------------------
    def _parse_scalpel_variables(self):
        """"""
        self._parse_variable_n_s(REG_N)
        self._parse_variable_n_s(REG_NS_NC_S_C)
        self._parse_variable_e_x(REG_ENUM_X)
        
    
    #----------------------------------------------------------------------
    def _parse_variable_n_s(self, reg):
        """"""
        
        results = findall(self._template, reg)
        if results != []:
            for orig, svtype, _, name, __, _min, _max in results:
                if _max == '':
                    ret = SVariable(orig, svtype, name, 
                                    params={'length':int(_min)}, 
                                    value=self._kwarfs[name] if self._kwarfs.has_key(name) \
                                    else '',
                                    random_every_time=self._random_every_time)
                else:
                    ret = SVariable(orig, svtype, name, 
                                    params={'min':int(_min), 'max':int(_max)}, 
                                    value=self._kwarfs[name] if self._kwarfs.has_key(name) \
                                    else '',
                                    random_every_time=self._random_every_time)
                self._variable_table[ret.name] = ret
    
    #----------------------------------------------------------------------
    def _parse_variable_u(self, reg):
        """"""
        
        results = findall(self._template, reg)
        if results != []:
            for orig, svtype, _, name, __, uuid_param in results:
                ret = SVariable(orig, svtype, name, 
                                params={'uuid':uuid_param}, 
                                value=self._kwarfs[name] if self._kwarfs.has_key(name) \
                                else '',
                                random_every_time=self._random_every_time)
                self._variable_table[ret.name] = ret
    
    #----------------------------------------------------------------------
    def _parse_variable_e_x(self, reg):
        """"""
        
        results = findall(self._template, reg)
        if results != []:
            for orig, svtype, _, name in results:
                ret = SVariable(orig, svtype, name, 
                                params={}, 
                                value=self._kwarfs[name] if self._kwarfs.has_key(name) \
                                else '',
                                random_every_time=self._random_every_time)
                self._variable_table[ret.name] = ret
    
    #----------------------------------------------------------------------
    def _render(self):
        """"""
        def remove_none_from_list(ret):
            while True:
                try:
                    ret.remove(None)
                except:
                    break
        
        enum_variable = map(lambda x: x if x.type == ENUM else None, 
                            self._variable_table.values())
        ordinary_variable = map(lambda x: x if x.type != ENUM else None,
                                self._variable_table.values())
        
        remove_none_from_list(enum_variable)
        remove_none_from_list(ordinary_variable)
        

        
        def render_enums(ret):
            result = []
            def render(result, ret, depth, tmp):
                if depth == len(ret):
                    return
                else:
                    varialbe = ret[depth]
                for i in varialbe.value:
                    buff = tmp.replace(varialbe.orig, i)
                    if depth + 1 == len(ret):
                        result.append(buff)
                    else:
                        render(result, ret, depth + 1, buff)
            render(result, ret, depth=0, tmp=self._template)
            return result

        
        for ret in render_enums(enum_variable):
            for i in ordinary_variable:
                ret = ret.replace(i.orig, str(i.value))            
            yield ret
    
    #----------------------------------------------------------------------
    @property
    def payloads(self):
        """"""
        return self._render()
        
    
    #----------------------------------------------------------------------
    @property
    def variable_table(self):
        """"""
        return self._variable_table
        


########################################################################
class SVariable(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig, svtype, name='', params={}, value='', random_every_time=True):
        """Constructor"""
        
        assert svtype in SVTYPE_LIST, '[!] Error Template Variable Type' + \
               'Should be in [N,NS,NC,S,C,ENUM,UUID,X].'
        assert isinstance(name, (str, unicode)), '[!] Error name shuold be a str' + \
               'or unicode.'
        assert isinstance(value, (types.StringType, unicode,
                                  types.TupleType,
                                  types.ListType,
                                  types.GeneratorType)), '[!] Values Type Error!'
        
        self._type = svtype
        self._name = name if name != '' else get_uuid('hex')
        self._orig = orig
        self._param = {}

        self._random_every_time = random_every_time
        
        if self._param.has_key('length'):
            self._param['min'] = 8
            self._param['max'] = 9
        else:
            self._param['min'] = params['min'] if params.has_key('min') else 8
            self._param['max'] = params['max'] + 1 if params.has_key('max') else 9

        if self._param.has_key('uuid'):
            self._param['uuid'] = self._param['uuid'] if params['uuid'] in \
                ['raw', 'hex'] else 'raw'
        else:
            self._param['uuid'] = 'raw'
        self._min = self._param['min']
        self._max = self._param['max']
        
        self._uservalue = value
        
        self._value = self._get_value(smin=self._min, smax=self._max, value=self._uservalue)
    
    
    #----------------------------------------------------------------------
    def _get_value(self, smin, smax, value):
        """"""
        _min = smin
        _max = smax
        
        if self._type == N:
            if self._param['min'] == 8 and self._param['max'] == 9:
                value = random.randint(0, 999)
            else:
                value = random.randint(_min, _max)
        elif self._type == NS:
            tmp = ''
            for i in xrange(random.randint(xrange(_min, _max))):
                tmp = tmp + get_random_digit()
            value = tmp
        elif self._type == NC:
            for i in xrange(random.randint(xrange(_min, _max))):
                tmp = tmp + get_random_word()
            value = tmp
        elif self._type in S + C:
            for i in xrange(random.randint(xrange(_min, _max))):
                tmp = tmp + get_random_char()  
            value = tmp
        elif self._type == ENUM:
            value = value if isinstance(value, (types.GeneratorType, 
                                                types.ListType,
                                                types.TupleType)) else []
            if value == []:
                warnings.warn('[!] The enum\' s value is emtpy(default is [])'+\
                              'Are you sure that you did this?')
        elif self._type == X:
            value = value if isinstance(value, types.StringTypes) else ''
        elif self._type == UUID:
            value = get_uuid(self._param['uuid'])
        else:
            raise ValueError('[!] Type Error!')
    
        return value
    
    #----------------------------------------------------------------------
    @property    
    def name(self):
        """"""
        return self._name
    
    #----------------------------------------------------------------------
    @property    
    def value(self):
        """"""
        if self._random_every_time:
            return self._get_value(smin=self._min, smax=self._max, value=self._uservalue)
        else:
            return self._value
    
    #----------------------------------------------------------------------
    @property    
    def type(self):
        """"""
        return self._type

    #----------------------------------------------------------------------
    @property
    def orig(self):
        """"""
        return self._orig
        


if __name__ == '__main__':
    unittest.main()