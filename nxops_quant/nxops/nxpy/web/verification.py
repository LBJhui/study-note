# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-08-06 14:47:21
@LastEditTime : 2020-08-13 10:05:02
@LastEditors  : yi.mt
@Description  : 
'''

import io
import uuid
import base64

import nxpy.tornado.handlers

from nxpy.log.logger import LoggerUtils
from nxpy.security.verify import VerifyUtils

from nxpy.pil.validation_img import ValidationImg


verification_goals = ["logon"]


class VerificationServiceHandler(nxpy.tornado.handlers.AsyncServiceHandler):
    def do_service(self, *args, **kwargs):
        goal = kwargs.get("goal")
        if goal not in verification_goals:
            return False

        style = kwargs.get("style")
        if style == "img":
            img, code = ValidationImg.create_validation_img()
            VerifyUtils.push_verification(self.get_session(), goal, code)

            buff = io.BytesIO()
            img.save(buff, "png")
            self.response.update({"content": base64.b64encode(buff.getvalue()).decode("UTF-8")})
            return True
        return False
