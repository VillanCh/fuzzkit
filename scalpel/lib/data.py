#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Taglib for scalpel
  Created: 03/19/17
"""

####################################################################################
## DEFINE THE TAG
####################################################################################

#
# build in
#
NS = 'NS'
N = 'N'
NC = 'NC'
S = 'S'
C = 'C'
UUID = 'UUID'

#
# define
#
ENUM = 'ENUM'

#
# custom
#
X = 'X'

TAG_LIST = [NS, N, NC, S, C, UUID, ENUM, X]

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
## BASE STRING
####################################################################################

NUMBER_BASE = list('0123456789')
LETTER_LOW_BASE = list('abcdefghijklmnopqrstuvwxyz')
LETTER_HIGH_BASE = list('abcdefghijklmnopqrstuvwxyz'.upper())
WORD_BASE = NUMBER_BASE + LETTER_HIGH_BASE + LETTER_LOW_BASE
WORD_BASE_WITH_UNDERSCORE = WORD_BASE + ['_',]
CONTROL_BASE = map(chr, range(0x21))
SYMBOL_BASE = map(chr, range(0x21, 48)) + \
    map(chr, range(58, 65)) + \
    map(chr, range(91, 97)) + \
    map(chr, range(123, 128))
ASCII_BASE = map(chr, range(256))
ASCII_START_128_BASE = map(chr, range(129))
ASCII_END_128_BASE = map(chr, range(129, 256))

####################################################################################
## Define Const
####################################################################################

WRAPERED = 'wrapered'

####################################################################################
## Define keyword
####################################################################################

VULNUS_START = '_S_S'
VULNUS_END = '_E_E'

WRAPER_S = 'VULNUS_S'
WRAPER_E = 'VULNUS_E'