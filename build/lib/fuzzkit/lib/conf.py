#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Store Conf for fuzzkit
  Created: 03/30/17
"""

from .data import *

####################################################################################
## DEFAULT VALUE
####################################################################################

NC_DEFUALT_LENGTH = '8'
NS_DEFUALT_LENGTH = '8'
S_DEFUALT_LENGTH = '8'
C_DEFUALT_LENGTH = '8'

DEFAULT_LENGTH = {
    NC: NC_DEFUALT_LENGTH,
    NS: NS_DEFUALT_LENGTH,
    S: S_DEFUALT_LENGTH,
    C: C_DEFUALT_LENGTH
}

N_DEFAULT_MIN = '10000'
N_DEFAULT_MAX = '99999'



####################################################################################
## Define keyword
####################################################################################

VULNUS_START = '_S_S'
VULNUS_END = '_E_E'

WRAPER_START = 'VULNUS_S'
WRAPER_END = 'VULNUS_E'