#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Encoder
  Created: 03/21/17
"""

import unittest
from ..lib import data

#
# URL encoder
#
# !*'();:@&=+$,/?#[]
URL_SAFE_CHAR=data.LETTER_HIGH_BASE + data.LETTER_LOW_BASE + \
    '0123456789' + '._-'


if __name__ == '__main__':
    unittest.main()