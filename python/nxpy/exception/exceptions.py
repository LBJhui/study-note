# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 15:42
# @Author: LBJ辉
# @File: exceptions
# @Project: python

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