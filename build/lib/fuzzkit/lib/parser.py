#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Parser For tmpl
  Created: 03/19/17
"""

import unittest
import re
import random

from . import data
from . import taglib
from . import regs
from . import core
from .exceptions import UndefinedValue


VULNUS_OFFSET = 2

_TAG_TYPE_INDEX = 0 + VULNUS_OFFSET
_TAG_NAME_INDEX = 2 + VULNUS_OFFSET 
_TAG_PARAM_1_INDEX = 5 + VULNUS_OFFSET 
_TAG_PARAM_2_INDEX = 8 + VULNUS_OFFSET
_TAG_SUFFIX = 10 + VULNUS_OFFSET
_RAW = 0

TAG_CLASS_TABLE = {}
for tagtypename in data.TAG_LIST:
    if hasattr(taglib, tagtypename):
        TAG_CLASS_TABLE[tagtypename] = getattr(taglib, tagtypename)
        

#----------------------------------------------------------------------
def _parse_suffix(suffix):
    """"""
    options = {
        data.WRAPERED:False,
    }
    #
    # Parse suffix
    #
    if 'W' in suffix:
        options[data.WRAPERED] = True
        
    
    
    return options
    

#----------------------------------------------------------------------
def parse_template(raw, **keyword_args):
    """"""
    #
    # accept raw
    #
    render = core.TagRender(raw)
    
    #
    # parse
    #
    for i in re.findall(pattern=regs.TEMPLATE_PATTERN, string=raw):
        _suffix = i[_TAG_SUFFIX]
        _options = _parse_suffix(_suffix)
        render.feed(raw=i[_RAW], tag=_build_tag(i, **keyword_args), wraperable=_options.get(data.WRAPERED))
    
    return render

#----------------------------------------------------------------------
def _build_tag(reg_tuple, **var):
    """"""
    # 
    # get the part of tag!
    #
    _type = reg_tuple[_TAG_TYPE_INDEX]
    _name = reg_tuple[_TAG_NAME_INDEX] if reg_tuple[_TAG_NAME_INDEX] != '' else \
        ''.join(random.sample(data.LETTER_LOW_BASE, 8))
    _p1 = reg_tuple[_TAG_PARAM_1_INDEX]
    _p2 = reg_tuple[_TAG_PARAM_2_INDEX] if reg_tuple[_TAG_PARAM_2_INDEX] != "" else None
    
    
    
    if _type in [data.X, data.ENUM]:
        #
        # build X and ENUM TAG
        #
        _tag = TAG_CLASS_TABLE[_type](_name)
        _val = var.get(_name)
        if _val:
            _tag.value = _val
        else:
            raise UndefinedValue('[x] the TagType {_type} not be set a value!'\
                                 .format(_type=_type))
    
    else:
        #
        # build N/NS/NC/S/C
        #
        if _type == data.N:
            _p1 = _p1 if _p1 != '' else data.N_DEFAULT_MIN
            _p2 = _p2 if _p2 != '' else data.N_DEFAULT_MAX
        else:
            _p1 = _p1 if _p1 != '' else data.DEFAULT_LENGTH[_type]
            _p2 = _p2 if _p2 != '' else None
        _tag = TAG_CLASS_TABLE[_type](_name, _p1, _p2)
    
        
    return _tag

if __name__ == '__main__':
    unittest.main()