#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: define regs
  Created: 03/19/17
"""

from . import data
from . import conf

VULNUS_START = conf.VULNUS_START
VULNUS_END = conf.VULNUS_END

WRAPER_START = conf.WRAPER_START
WRAPER_END = conf.WRAPER_END

#EXTRACT_TAG_PATTERN = "(" + VULNUS_START + '(.*)' + VULNUS_END + ")"
#EXTRACT_RSP_PATTERN = "(" + WRAPER_START + '(.*)' + WRAPER_END + ")"


#----------------------------------------------------------------------
def get_extract_tag_pattern(vulnus_start, vulnus_end):
    """"""
    return "({start}(.*){end})".format(start=vulnus_start, end=vulnus_end)

#----------------------------------------------------------------------
def get_extract_rsp_pattern(wraper_start, wraper_end):
    """"""
    return "({start}(.*){end})".format(start=wraper_start, end=wraper_end)

#
# Tag Parser Regs
#
####################################################################################
_PARSE_TAG = "(\(([a-zA-Z0-9_]*)\))"
_PARSE_PARAMS = "(\{(([0-9]+)(,([ ]+)?([0-9]+)?)?)\})"
_SUFFIX = "(\:([a-zA-Z0-9]+))"
####################################################################################

TAG_PATTERN = "(" + '|'.join(data.TAG_LIST) + ")" + _PARSE_TAG + '?' + _PARSE_PARAMS + '?' +\
    _SUFFIX + "?"
#TEMPLATE_PATTERN = "((" + VULNUS_START + ")" + TAG_PATTERN + "(" + VULNUS_END + "))"


#----------------------------------------------------------------------
def get_template_pattern(vulnus_start, vulnus_end):
    """"""
    return "((" + vulnus_start + ")" + TAG_PATTERN + "(" + vulnus_end + "))"
    