# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-15 17:37:30
@LastEditTime : 2020-07-15 18:08:30
@LastEditors  : yi.mt
@Description  : 
'''

import json
import decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o, markers)
