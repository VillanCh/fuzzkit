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

