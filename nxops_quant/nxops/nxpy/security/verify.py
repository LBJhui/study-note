# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-08-11 14:09:20
@LastEditTime : 2020-08-11 14:48:07
@LastEditors  : yi.mt
@Description  : 
'''

import time


class VerifyUtils():
    @staticmethod
    def push_verification(session, goal, code, timeout=60):
        verification_session_key = f"_{goal}_verification"
        session[verification_session_key] = {"code": code, "timeout": 60, "timestamp": int(time.time())}

    @staticmethod
    def pop_verification(session, goal):
        verification_session_key = f"_{goal}_verification"

        verification = None
        if session and verification_session_key in session:
            verification = session[verification_session_key]
            del session[verification_session_key]

            timestamp = int(time.time())
            if timestamp - verification["timestamp"] <= verification["timeout"]:
                verification = verification["code"]
            else:
                verification = None
        return verification