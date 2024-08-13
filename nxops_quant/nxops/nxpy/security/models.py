# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-03 18:09:18
@LastEditTime : 2020-07-23 13:29:07
@LastEditors  : yi.mt
@Description  : 
'''

from nxpy.context import AppRuntime

from nxpy.web.constants import *
from nxpy.web.errors import *

import nxpy.security.realm

def auth_required(level):
    def wrapper(func):
        def check(self, *args, **kwargs):
            realm = AppRuntime.get_value("realm")
            if realm and realm.auth_level >= level:
                return func(self, *args, **kwargs)
            self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
            return False
        return check
    return wrapper

