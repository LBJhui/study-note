# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-07 10:52:17
@LastEditTime : 2020-07-22 13:39:44
@LastEditors  : yi.mt
@Description  : 
'''

class NxBaseException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.error_code = kwargs.get("code", None)
        self.error_msg = kwargs.get("msg", None)

    def __str__(self):
        return self.error_msg

class NxBaseSecurityException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.error_code = kwargs.get("code", None)
        self.error_msg = kwargs.get("msg", None)

    def __str__(self):
        return self.error_msg

class DbStatementNotFoundException(NxBaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stmt_id = args[0]

    def __str__(self):
        return f"[{self.stmt_id}] not found"

class DbStatementNotAllowedException(NxBaseSecurityException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stmt_id = args[0]

    def __str__(self):
        return f"[{self.stmt_id}] not allowed"