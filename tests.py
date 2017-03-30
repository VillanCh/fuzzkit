#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Test for scalpel_new
  Created: 03/19/17
"""

import unittest
import re
import types

from fuzzkit.lib import regs
from fuzzkit.lib import parser
from fuzzkit.lib import taglib
from fuzzkit.lib import extractor
from fuzzkit.lib import data
from fuzzkit.ext import codecs_common
from fuzzkit.ext import encoder
from fuzzkit.ext import decoder
from fuzzkit.ext import regs as extargs
from fuzzkit.ext import recogizer, states
from fuzzkit.ext import chars
from fuzzkit.fuzzkit import FuzzerConfig, Fuzzer


########################################################################
class FuzzkitTester(unittest.case.TestCase):
    """"""

    #----------------------------------------------------------------------
    def test_regs(self):
        """"""
        raw = 'adfasdfasdf' + regs.VULNUS_START + 'v1ll4n><>?LL:"{PPKLJL}' + regs.VULNUS_END + 'asdfasdfasdf'
    
    #----------------------------------------------------------------------
    def test_taglib(self):
        """"""
        e1 = taglib.ENUM('e1')
        e1.value = [1,2,3,5,4]
        for i in e1:
            self.assertIsInstance(i, types.StringTypes)
        
        self.assertRaises(StopIteration, e1.next)
        
        e1.reset()
        for i in e1:
            self.assertIsInstance(i, types.StringTypes)
            
        x1 = taglib.X('x1')
        x1.value = 'XXXX'
        
        for i in x1:
            self.assertEqual('XXXX', i)
        
        x1.reset()
        for i in x1:
            self.assertEqual('XXXX', i)
            
        for i in taglib.N(name='s', min_value=333, max_value=6666):
            self.assertTrue(int(i) < 6666 and int(i) >= 333)
        
        for i in taglib.NS(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.NS('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7)
        
        for i in taglib.NC(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.NC('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7) 
        
        for i in taglib.S(name='s', length_1=5):
            self.assertTrue(len(i) == 5)
                        
        for i in taglib.S('s', 5, 7):
            _l = len(i)
            self.assertTrue(_l >= 5 and _l <= 7)         
            
    #----------------------------------------------------------------------
    def test_parsetag_by_reg(self):
        """"""
        _l = [
            'X(xxx)',
            "ENUM(sdsf)",
            'C(s)',
            'S',
            "N(asd){3}",
            "NS{2}",
            "NS{3,6}",
            "NS(){4}",
            'NC(){5,7}'
        ]
        
        for i in _l:
            _lis = re.findall(regs.TAG_PATTERN, i).pop()
            print(_lis)
            self.assertEqual(11, len(_lis))
    
    #----------------------------------------------------------------------
    def test_parse(self):
        """"""
        self.assertEqual(len(data.TAG_LIST), len(parser.TAG_CLASS_TABLE))
        
        raw = 'asdfasdfaHHHHHH_SX(asd){1,3}HHHHHH_EsdfaaM<L:?<"OP{IO"P{K:HKJ}}>>dfa'
        #print re.findall(regs.TEMPLATE_PATTERN, raw)
        for i in re.findall(regs.get_template_pattern(FuzzerConfig.VULNUS_START,
                                                      FuzzerConfig.VULNUS_END), raw):
            print i
    
    #----------------------------------------------------------------------
    def test_render(self):
        """"""
        render = parser.parse_template('ad_S_SENUM(tt)_E_Efausdg_S_SS(tag){4}:W_E_Efad_S_SX(x1)_E_Efk_S_SENUM(rag)_E_Ealhsidf',
                                       x1='V!LL$NNNSDF^%%&^$$$$^',
                                       rag=data.ASCII_START_128_BASE,
                                       tt=range(333),
                                       fuzzkitconfig=FuzzerConfig)
        
        gen = render.render()
        for i in range(222):
            print gen.next()
    
    #----------------------------------------------------------------------
    def test_extractor(self):
        """"""
        _l = [
            "adf_S_SN()_E_Ea",
            "HVJGHVBJVULNUS_SBNVULNUS_Ebjbkjbkj"
        ]
        
        for i in _l:
            for j in extractor.extract_vulnus(i, FuzzerConfig.WRAPER_START, FuzzerConfig.WRAPER_END):
                print j
    
    #----------------------------------------------------------------------
    def test_unicode_op(self):
        """"""
        u2hex = codecs_common.unicode_to_hexstr
        assert '71' == u2hex('\x71')
        assert '7302' == u2hex(unichr(0x7302))
        
        ufromnum = codecs_common.unicode_build_from_number
        
        assert u'\u7302' == ufromnum('7302')
        assert u'\x03' == ufromnum('03')
        assert u'\x65' == ufromnum('65')
        
        ue = codecs_common.unicode_escape
        
        assert '\\u7302' == ue(u'\u7302')
    
    #----------------------------------------------------------------------
    def test_encoder(self):
        """"""
        print encoder.encode_unichar_to_hexlist(u'你你好')
        print encoder.encode_unichar_to_hexlist(u'你')
        print encoder.encode_unichar_to_hexlist(u'你你好', 'gbk')        
        print encoder.encode_unichar_to_hexlist(u'好', 'gbk')        
        print encoder.encode_unichar_to_hexlist(u's')
        print encoder.encode_unichar_to_hexlist(u'ssdaf')
        print encoder.encode_unichar_to_hexlist(u'\x45')
        print encoder.css_encode_raw('helloworld')
        print encoder.css_encode_raw('helloworld你好')
        print encoder.jsunicode_encode_raw('Helloworld')
        print encoder.jsunicode_encode_raw('Helloworld你好')
        print encoder.unicode_encode_raw('hellworld')
        print encoder.unicode_encode_raw('hellworld你好')
        print encoder.htmlentity_encode_raw('hellworld')
        print encoder.htmlentity_encode_raw('hellworld你好')
        print encoder.urlencode_encode_raw('hellowrld')
        print encoder.urlencode_encode_raw('hellowrld你好')
        print encoder.ascii_encode_raw('adsfasdwqgadd')
        print encoder.ascii_encode_raw('adsfasdwqgadd你好')
        print 'zhtest', encoder.css_encode_raw('你好')
        
        print 'symbol test'
        _test = ',./<>?;:\'"[]{}-=_+()&*%^#$!@`~`'
        print encoder.css_encode_raw(_test)
        print encoder.ascii_encode_raw(_test)
        print encoder.urlencode_encode_raw(_test)
        print encoder.htmlentity_encode_raw(_test)
        print encoder.unicode_encode_raw(_test)
        print encoder.jsunicode_encode_raw(_test)        
        
    #----------------------------------------------------------------------
    def test_decoder(self):
        """"""
        print decoder.css_decode_from_raw(encoder.css_encode_raw('你好'))
        print decoder.css_decode_from_raw(encoder.css_encode_raw('Hello你好'))
        print decoder.jsunicode_decode_from_raw(encoder.jsunicode_encode_raw('HelloWorld'))
        print decoder.jsunicode_decode_from_raw(encoder.jsunicode_encode_raw('HelloWorld你好'))
        print decoder.html_decode_from_raw(encoder.htmlentity_encode_raw('HelloWorld'))
        print decoder.html_decode_from_raw(encoder.htmlentity_encode_raw('HelloWorld你好'))
        print decoder.unicode_decode_from_raw(encoder.unicode_encode_raw('HelloWorld'))
        print decoder.unicode_decode_from_raw(encoder.unicode_encode_raw('HelloWorld你好'))
        print decoder.urlencode_decode_from_raw(encoder.urlencode_encode_raw('HelloWorld'))
        print decoder.urlencode_decode_from_raw(encoder.urlencode_encode_raw('HelloWorld你好'))
        print decoder.ascii_decode_from_raw(encoder.ascii_encode_raw('helloworld'))
        print decoder.ascii_decode_from_raw(encoder.ascii_encode_raw('helloworld你好'))

    #----------------------------------------------------------------------
    def test_extregs(self):
        """"""
        #
        # list all html entity char!
        #
        self.assertEqual(1, len(re.findall(extargs.HTMLENCODE_REG, '&#3452;')))
        self.assertEqual(1, len(re.findall(extargs.HTMLENCODE_REG_LOOSE, '&#3452')))
        self.assertEqual(1, len(re.findall(extargs.HTMLENCODE_REG, '&amp;')))
        self.assertEqual(1, len(re.findall(extargs.HTMLENCODE_REG_LOOSE, '&ampasdfa')))
        
        self.assertEqual(1, len(re.findall(extargs.JSUNICODE_REG, '\\u3467')))
        self.assertEqual(0, len(re.findall(extargs.JSUNICODE_REG, '\\u347')))
        self.assertEqual(1, len(re.findall(extargs.JSUNICODE_REG, '\\u34674')))
        
        self.assertEqual(1, len(re.findall(extargs.CSSENCODE_REG, '\\34674')))
        self.assertEqual(0, len(re.findall(extargs.CSSENCODE_REG, '\\4')))
        
        self.assertEqual(1, len(re.findall(extargs.ASCIIENCODE_REG, '\\x34674')))
        self.assertEqual(0, len(re.findall(extargs.ASCIIENCODE_REG, '\\x3')))
        self.assertEqual(1, len(re.findall(extargs.ASCIIENCODE_REG, '\\3')))
        
        self.assertEqual(0, len(re.findall(extargs.URLENCODE_REG, '%f')))
        self.assertEqual(1, len(re.findall(extargs.URLENCODE_REG, '%ff')))
        self.assertEqual(1, len(re.findall(extargs.URLENCODE_REG, '%faf')))
        
        self.assertEqual(1, len(re.findall(extargs.SLASH_REG, 'asdfasd\\&%adfa')))
        self.assertEqual(2, len(re.findall(extargs.SLASH_REG, 'asdfasd\\[\\&%adfa')))
        self.assertEqual(2, len(re.findall(extargs.SLASH_REG, 'asdfasd\\[\\&%adfa')))
        
    #----------------------------------------------------------------------
    def test_recognizer(self):
        """"""
        self.assertIn(recogizer.recognize_type('\\3456'), states.ASCII_LIKE)
        self.assertIn(recogizer.recognize_type('\\af'), states.ASCII_LIKE)
        self.assertIn(recogizer.recognize_type('\\u2345'), states.UNICODE_LIKE)
        self.assertIn(recogizer.recognize_type('&#24534'), states.HTML_ENCODE)
        self.assertIn(recogizer.recognize_type('&asag;'), states.HTML_ENCODE)
        self.assertIn(recogizer.recognize_type('\\xaf'), states.ASCII_ENCODE)
        self.assertIn(recogizer.recognize_type('%af'), states.URL_ENCODE)
        
    #----------------------------------------------------------------------
    def test_charuse(self):
        """"""
        c = chars.Char('[')
        print c.transformations
        print c.compare('\[')
        print c.compare(None)
        print c.compare('&#91;') #should be recognized as Transformer
        print c.compare('&#x005b;')
        print c.compare('%5b')
        print c.compare('\\91') # slashed error
        print c.compare('\\x5b')
        
        c = chars.Char('\\')
        print c.transformations
        print c.compare('\\\\')
        print c.compare(None)
        print c.compare('&#92;') #should be recognized as Transformer
        print c.compare('&#x005c;')
        print c.compare('%5c')
        print c.compare('\\92')
        print c.compare('\\x5c')
        
        c = chars.Char('&#x005c;')
        print c.transformations
        print c.compare('\\\\')
        print c.compare(None)
        print c.compare('&#92;') #should be recognized as Transformer
        print c.compare('&#x005c;')
        print c.compare('%5c')
        print c.compare('\\92')
        print c.compare('\\x5c')
        print c.compare('\\')
        
    #----------------------------------------------------------------------
    def test_fuzzer(self):
        """"""
        
        for i in Fuzzer(template='_S_SENUM(x):W_E_E', x=map(str, range(444))):
            print i

if __name__ == '__main__':
    unittest.main()