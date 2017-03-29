#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Define Char
  Created: 03/28/17
"""

import unittest

from . import encoder, decoder
from . import recogizer
from . import states
from . import transformer

########################################################################
class Char(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, orig_char, encoding='utf8', standard=True,\
                 htmlentity_suffix=';'):
        """Constructor"""
        self._encoding = encoding
        
        #
        # analyze input
        #
        self._orig_raw = orig_char
        
        self._orig_type = recogizer.recognize_type(self._orig_raw, encoding)
        if not self._orig_type == states.ORDINARY:
            try:
                self._orig_base = decoder.DECODE_FUNCTION_TABLE[self._orig_type]
            except:
                self._orig_base = self._orig_raw
        else:
            self._orig_base = self._orig_raw
        
        #
        # encode force
        #
        try:
            self.css = encoder.css_encode_raw(self._orig_raw)
        except:
            self.css = None
            
        try:
            self.jsunicode = encoder.jsunicode_encode_raw(self._orig_raw, encoding, standard)
        except:
            self.jsunicode = None
            
        try:
            self.urlencode = encoder.urlencode_encode_raw(self._orig_raw, encoding)
        except:
            self.urlencode = None
            
        try:
            self.asciicode = encoder.ascii_encode_raw(self._orig_raw, encoding, standard)
        except:
            self.asciicode = None
        
        try:
            self.htmlentitycode = encoder.htmlentity_encode_raw(self._orig_raw, encoding, \
                                                           htmlentity_suffix, standard)
        except:
            self.htmlentitycode = None
            
        
        #
        # decode force
        #
        try:
            self.css_r = decoder.css_decode_from_raw(self._orig_raw)
        except:
            self.css_r = None
            
        try:
            self.jsunicode_r = decoder.jsunicode_decode_from_raw(self._orig_raw, encoding, standard)
        except:
            self.jsunicode_r = None
            
        try:
            self.urlencode_r = decoder.urlencode_decode_from_raw(self._orig_raw, encoding)
        except:
            self.urlencode_r = None
            
        try:
            self.asciicode_r = decoder.ascii_decode_from_raw(self._orig_raw, encoding, standard)
        except:
            self.asciicode_r = None
        
        try:
            self.htmlentitycode_r = decoder.html_decode_from_raw(self._orig_raw, encoding, \
                                                           htmlentity_suffix, standard)
        except:
            self.htmlentitycode_r = None
        
        
        #
        # define public
        #
        self.transformations = [self.css, self.jsunicode, self.urlencode, self.asciicode, self.htmlentitycode,
                                self.css_r, self.jsunicode_r, self.urlencode_r, self.asciicode_r,
                                self.htmlentitycode_r]
        self.base = self._orig_base
        self.orig = self._orig_raw
        self.type = self._orig_type
        
        
    #----------------------------------------------------------------------
    def compare(self, target):
        """"""
        #
        # define the rule of compare
        #     1. check transformations
        #     2. check slash
        #     
        
        _target = target
        _type = recogizer.recognize_type(orig=target, encoding=self._encoding)
        
        
        #
        # check empty target 
        #     state: VANISH
        #
        if _target == '' or _target == None:
            return transformer.Filtered(self.orig, self.type, None, states.VANISH)
        
        #
        # check the same target and orig
        #
        if _target == self.orig:
            return transformer.NoChange(self.orig, self.type)
        
        #
        # check transformations
        #     state: XXX_ENCODE
        #
        if target in self.transformations:
            return transformer.Transformer(self.orig, self.type, _target, _type)
        
        #
        # check slash
        #     state: SLASHED
        #
        if '\\' == self.orig:
            if 2 >= list(self.orig).count('\\'):
                _type = states.SLASHED
                return transformer.Filtered(self.orig, self.type, _target, _type)
            else:
                return transformer.UnknowChange(self.orig, self.type, _target, _type)
        else:
            if 1 >= list(self.orig).count('\\'):
                _type = states.SLASHED
                return transformer.Filtered(self.orig, self.type, _target, _type)
            else:
                return transformer.UnknowChange(self.orig, self.type, _target, _type)
        
        
        
    
    

if __name__ == '__main__':
    unittest.main()