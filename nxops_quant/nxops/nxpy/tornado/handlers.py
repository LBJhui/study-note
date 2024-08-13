# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-10 17:42:30
LastEditTime : 2024-03-27 14:20:34
LastEditors  : yi.mt
@Description  : 
'''

import uuid
import json
import traceback

from abc import ABC, abstractmethod

import tornado
import tornado.web
import tornado.httputil
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from nxpy.context import AppRuntime

from nxpy.json.coder import DecimalEncoder

import nxpy.web.session

from nxpy.log.logger import LoggerUtils

from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.security.realm import AUTH_LEVEL_PLAIN_USER
from nxpy.security.models import auth_required

from nxpy.security.cipher import EasyCipherUtils
from nxpy.security.verify import VerifyUtils

from nxpy.exception.exceptions import NxBaseSecurityException

from nxpy.web.constants import *
from nxpy.web.errors import *


def with_web_runtime(keys):
    def wrapper(func):
        def do_with_web_runtime(self, *args, **kwargs):
            AppRuntime.set_value("session", self.session)
            if "_reserved_" in self.session:
                reserveds = self.session["_reserved_"]
                for key in keys:
                    AppRuntime.set_value(key, reserveds.get(key, None))
            result = func(self, *args, **kwargs)
            for key in keys:
                AppRuntime.del_value(key)
            AppRuntime.del_value("session")
            return result
        return do_with_web_runtime
    return wrapper


class NxResponse():
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.success = data.get("success", True)
            self.code = data.get("code", 0)
            self.message = data.get("message", None)
            self.content = data.get("content", {})
        else:
            self.success = True
            self.code = 0
            self.message = None
            self.content = {}

    def set_success(self, success):
        self.success = success

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message

    def set_content(self, content):
        self.content = content

    def update(self, data):
        self.success = data.get("success", True)
        self.code = data.get("code", 0)
        if "msg" in data:
            self.message = data.get("msg", None)
        if "message" in data:
            self.message = data.get("message", None)
        self.content = data.get("content", {})

    def update_content(self, content):
        self.content.update(content)

    def to_dict(self):
        return {"success": self.success, "code": self.code, "message": self.message, "content": self.content}


class NxBaseRequestHandler(tornado.web.RequestHandler):
    def initialize(self, *args, **kwargs):
        self._headers["Server"] = ""


class AsyncServiceHandler(NxBaseRequestHandler):
    executor = ThreadPoolExecutor(4096)

    def initialize(self, *args, **kwargs):
        super().initialize(*args, **kwargs)

        self.allowed_hosts = kwargs.get("hosts", None)
        self.allowed_ports = kwargs.get("ports", None)
        self.allowed_origin = kwargs.get("origin", None)
        self.client_hosts = kwargs.get("client_hosts", None)

        self.token_goals = ["logon"]

        self.verify_required = kwargs.get("verify_required", False)

        self.cipher = EasyCipherUtils.get_cipher("data")

    def json_encode(self, dict_obj):
        return json.dumps(dict_obj, cls=DecimalEncoder).replace("</", "<\\/")

    def _get_real_remote_ip(self):
        return self.request.headers.get("X-Real-IP") if "X-Real-IP" in self.request.headers else self.request.remote_ip

    def _generate_token(self):
        return uuid.uuid4().hex[0:16]

    def _push_token(self, goal, token):
        token_session_key = f"_{goal}_token"
        self.session[token_session_key] = token

    def _pop_token(self, goal):
        token_session_key = f"_{goal}_token"
        if token_session_key in self.session:
            return self.session[token_session_key]
        return None
    
    def _set_cros_headers(self):
        self.set_header("Access-Control-Allow-Headers", "Token-Handshake,Encrypt-Algorithm,Verification")
        self.set_header("Access-Control-Allow-Credentials", "true")
        if self.allowed_origin:
            self.set_header("Access-Control-Allow-Origin", self.allowed_origin)

    @tornado.gen.coroutine
    def options(self, *args, **kwargs):
        self._set_cros_headers()
        self.finish()

    @tornado.gen.coroutine  # 异步、协程处理；增加并发量
    def post(self, *args, **kwargs):
        host, port = tornado.httputil.split_host_and_port(self.request.host)

        real_remote_ip = self._get_real_remote_ip()

        if (self.allowed_hosts and host not in self.allowed_hosts) or (self.allowed_ports and port not in self.allowed_ports) or (self.client_hosts and real_remote_ip not in self.client_hosts):
            LoggerUtils.warning("{} posting {}".format(real_remote_ip, self.request.uri))
            response = NxResponse({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
            self.write(self.json_encode(response.to_dict()))
            self.finish()
            return

        LoggerUtils.info("{} posting {} from {}".format(real_remote_ip, self.request.uri, self.request.headers["Origin"] if "Origin" in self.request.headers else "None"))

        self.session = None
        self.parameters = {}
        self.response = NxResponse()

        self.get_session()

        try:
            if (yield self.prepare(*args, **kwargs)):
                if self.token_handshake() and self.check_verification():
                    self.parse_parameters()

                    yield self.prepare(*args, **kwargs)

                    if (yield self.before(*args, **kwargs)):
                        if (yield self.service(*args, **kwargs)):
                            yield self.after(*args, **kwargs)
                        else:
                            yield self.fail(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            error_id = uuid.uuid4().hex
            LoggerUtils.error("raised Exception [{}] [{}]".format(error_id, str(e)))
            self.response.update({"success": False, "code": ERROR_INTERNAL_SERVER_ERROR, "message": "系统内部错误", "content": error_id})
            yield self.error(*args, **kwargs)
        finally:
            yield self.final(*args, **kwargs)
            
            self._set_cros_headers()
            self.write(self.json_encode(self.response.to_dict()))  # 写入返回信息写入response
            self.finish()  # 结束服务

    @tornado.gen.coroutine  # 异步、协程处理；增加并发量
    def get(self, *args, **kwargs):
        real_remote_ip = self._get_real_remote_ip()
        LoggerUtils.warning("{} getting {}".format(real_remote_ip, self.request.uri))
        response = NxResponse({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
        self.write(self.json_encode(response.to_dict()))
        self.finish()

    def parse_parameters(self):
        if len(self.request.body) > 0:
            body = str(self.request.body, encoding="UTF-8")
            if "Encrypt-Algorithm" in self.request.headers:
                if self.token:
                    body = EasyCipherUtils.symmetric_decrypt(body, self.token)
                elif self.cipher:
                    body = self.cipher.private_decrypt(body)

            self.parameters = tornado.escape.json_decode(body)

    def token_handshake(self):
        if "Token-Handshake" in self.request.headers:
            token_handshake = self.request.headers.get("Token-Handshake")
            handshake_options = token_handshake.split(":")
            if handshake_options[0] == "1":
                goal = handshake_options[1]
                if goal not in self.token_goals:
                    self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
                else:
                    client_token = self.cipher.private_decrypt(handshake_options[2])
                    server_token = self._generate_token()
                    self._push_token(goal, client_token + server_token)

                    encrypted_token = EasyCipherUtils.symmetric_encrypt(server_token, client_token)
                    self.response.set_content(encrypted_token)
                return False
            else:
                goal = handshake_options[1]
                token = self._pop_token(goal)
                self.token = token
        return True

    def check_verification(self):
        if self.verify_required:
            if "Verification" in self.request.headers:
                verification = self.request.headers.get("Verification")
                verification_options = verification.split(":")
                
                goal = verification_options[0]
                client_code = verification_options[1]

                server_code = VerifyUtils.pop_verification(self.get_session(), goal)
                if not client_code or not server_code or client_code.lower() != server_code.lower():
                    self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED, "message": "验证码错误"})
                    return False
            else:
                self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED, "message": "验证码错误"})
                return False
        return True

    @run_on_executor
    @with_web_runtime(["realm"])
    def service(self, *args, **kwargs):
        try:
            result = self.do_service(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            error_id = uuid.uuid4().hex
            LoggerUtils.error("raised Exception [{}] [{}]".format(error_id, str(e)))
            self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED if isinstance(e, NxBaseSecurityException) else ERROR_INTERNAL_SERVER_ERROR,
                                  "message": "权限不足" if isinstance(e, NxBaseSecurityException) else "系统内部错误", "content": error_id})
            result = False
        return result

    @run_on_executor
    def prepare(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_prepare(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def before(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_before(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def after(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_after(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def fail(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_fail(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def error(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_error(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def final(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_final(*args, **kwargs)
        if self.session:
            self.session.save()
            self.session.persist()

        # self.clear_runtime_context()
        return result

    def get_session(self):
        if not self.session:
            self.session = nxpy.web.session.SessionUtils.get_session(self)

        return self.session

    def get_security_realm(self):
        if "_reserved_" in self.session:
            return self.session["_reserved_"].get("realm", None)
        return None

    def update_security_realm(self, realm):
        if "_reserved_" not in self.session:
            self.session["_reserved_"] = {}
        self.session["_reserved_"]["realm"] = realm
        if AppRuntime.get_value("realm"):
            AppRuntime.set_value("realm", realm)

    def do_prepare(self, *args, **kwargs):
        return True

    def do_before(self, *args, **kwargs):
        return True

    def do_after(self, *args, **kwargs):
        return True

    def do_fail(self, *args, **kwargs):
        return True

    def do_error(self, *args, **kwargs):
        return True

    def do_final(self, *args, **kwargs):
        return True

    def do_service(self, *args, **kwargs):
        return True


class EasyQueryServiceHandler(AsyncServiceHandler):
    def initialize(self, *args, **kwargs):
        super().initialize(*args, **kwargs)
        self.executor_id = kwargs.get("executor_id")

    def do_service(self, *args, **kwargs):
        return self.do_query(*args, **kwargs)

    def do_query(self, *args, **kwargs):
        executor = EasyDBExecutorUtils.get_executor(executor_id=self.executor_id)

        version = kwargs.get("version")
        pkg = kwargs.get("pkg")
        stmt = kwargs.get("stmt")

        error, result = executor.querylist(f"{pkg}.{stmt}", self.parameters)

        if error:
            self.response.update(error)
            self.response.set_success(False)
        self.response.set_content(result)

        return True


class EasyUserQueryServiceHandler(EasyQueryServiceHandler):
    @auth_required(AUTH_LEVEL_PLAIN_USER)
    def do_query(self, *args, **kwargs):
        return super().do_query(*args, **kwargs)


class NotFoundServiceHandler(AsyncServiceHandler):
    def not_found(self):
        real_remote_ip = self._get_real_remote_ip()
        LoggerUtils.warning("{} accessing {}".format(real_remote_ip, self.request.uri))
        response = NxResponse({"success": False, "code": ERROR_WEB_API_NOT_FOUND})
        self.write(tornado.escape.json_encode(response.to_dict()))
        self.finish()

    @tornado.gen.coroutine  # 异步、协程处理；增加并发量
    def post(self):
        self.not_found()

    @tornado.gen.coroutine  # 异步、协程处理；增加并发量
    def get(self):
        self.not_found()


class AsyncTransactionServiceHandler(AsyncServiceHandler):
    @run_on_executor
    def prepare(self, *args, **kwargs):
        # self.build_runtime_context()

        self.set_transaction()
        if self.transaction:
            self.transaction.begin()

        result = self.do_prepare(*args, **kwargs)

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def error(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_error(*args, **kwargs)
        if result and self.transaction:
            self.transaction.rollback()

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def fail(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_fail(*args, **kwargs)
        if result and self.transaction:
            self.transaction.rollback()

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def after(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_after(*args, **kwargs)
        if self.transaction:
            self.transaction.commit()

        # self.clear_runtime_context()
        return result

    @run_on_executor
    def final(self, *args, **kwargs):
        # self.build_runtime_context()

        result = self.do_final(*args, **kwargs)
        if self.session:
            self.session.save()
            self.session.persist()
        if self.transaction:
            self.transaction.close()
            self.transaction = None

        # self.clear_runtime_context()
        return result

    @abstractmethod
    def set_transaction(self):
        self.transaction = None


class EasyTransactionServiceHandler(AsyncTransactionServiceHandler):
    def initialize(self, *args, **kwargs):
        super().initialize(*args, **kwargs)
        self.db_executor_id = kwargs.get("executor_id")
        self.db_executor = EasyDBExecutorUtils.get_executor(executor_id=self.db_executor_id)

    def do_service(self, *args, **kwargs):
        return self.do_execute(*args, **kwargs)

    @auth_required(AUTH_LEVEL_PLAIN_USER)
    def do_execute(self, *args, **kwargs):
        result = True

        version = kwargs.get("version")
        pkg = kwargs.get("pkg")
        stmt = kwargs.get("stmt")

        error, exec_result = self.transaction.execute(f"{pkg}.{stmt}", paras=self.parameters, batch_paras={})

        if error:
            result = False
            self.response.update(error)
            self.response.set_success(False)
        self.response.set_content(exec_result)

        return result

    def set_transaction(self):
        super().set_transaction()
        if self.db_executor:
            self.transaction = self.db_executor.get_transaction()
