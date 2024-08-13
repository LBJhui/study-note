# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-21 17:10:35
LastEditTime : 2024-03-28 11:20:23
LastEditors  : yi.mt
@Description  : 
'''

import uuid
import traceback

from nxpy.web.errors import *

from nxpy.log.logger import LoggerUtils
from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.security.realm import AUTH_LEVEL_PLAIN_USER, Securable
from nxpy.security.models import auth_required
from nxpy.tornado.handlers import AsyncServiceHandler, EasyTransactionServiceHandler


class ServiceModule():
    def __init__(self):
        super().__init__()
        
class SecurableServiceModule(Securable):
    def __init__(self, secure_id=None):
        if secure_id:
            super().__init__(secure_id)
        else:
            super().__init__()


class Dispatcher():
    def __init__(self):
        super().__init__()
        self.routers = {}
        self.instances = {}

    def add_module(self, module, clazz, *args, **kwargs):
        self.routers.update({module: clazz})
        module_instance = clazz(*args, **kwargs)
        self.instances.update({module: module_instance})

    def get_action(self, module, action, *args, **kwargs):
        module_clazz = self.routers.get(module, None)
        if module_clazz:
            if action in module_clazz.actions:
                module_instance = self.instances.get(module)
                action_target = getattr(module_instance, action)
                return module_instance, action_target
        return None, None


class DispatchUtils():
    dispatchers = {"default": Dispatcher()}

    @classmethod
    def get_dispatcher(cls, dispatcher_id=None):
        dispatcher_id = dispatcher_id if dispatcher_id else "default"
        if dispatcher_id in cls.dispatchers:
            return cls.dispatchers.get(dispatcher_id)
        dispatcher = Dispatcher()
        cls.dispatchers.update({dispatcher_id: dispatcher})
        return dispatcher


class DispatchEasyTransactionServiceHandler(EasyTransactionServiceHandler):

    def initialize(self, *args, **kwargs):
        super().initialize(*args, **kwargs)
        self.dispatcher_id = kwargs.get("dispatcher_id", None)

    def get_dispatcher(self):
        return DispatchUtils.get_dispatcher(self.dispatcher_id)

    @auth_required(AUTH_LEVEL_PLAIN_USER)
    def do_execute(self, *args, **kwargs):
        module = kwargs.get("module")
        action = kwargs.get("action")

        module_instance, action_target = self.get_dispatcher().get_action(module, action)

        if not module_instance or not action_target:
            self.response.update({"success": False, "code": ERROR_WEB_API_NOT_FOUND})
            return False

        if isinstance(module_instance, Securable) and not module_instance.is_accessable():
            self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
            return False

        return action_target(self, *args, **kwargs)


class EasyTransactionChainServiceHandler(AsyncServiceHandler):
    def initialize(self, *args, **kwargs):
        super().initialize(*args, **kwargs)
        self.dispatcher_id = kwargs.get("dispatcher_id", None)
        self.db_executor_id = kwargs.get("executor_id")
        self.db_executor = EasyDBExecutorUtils.get_executor(executor_id=self.db_executor_id)

    def get_dispatcher(self):
        return DispatchUtils.get_dispatcher(self.dispatcher_id)

    def do_service(self, *args, **kwargs):
        return self.do_execute(*args, **kwargs)

    @auth_required(AUTH_LEVEL_PLAIN_USER)
    def do_execute(self, *args, **kwargs):
        version = kwargs.get("version")
        actions = kwargs.get("actions")
        if actions:
            action_items = actions.split(">")
            for action_item in action_items:
                [action_type, action_id] = action_item.split(":")
                if action_type == "s":
                    try:
                        self.set_transaction()
                        if self.transaction:
                            self.transaction.begin()
                        error, exec_result = self.transaction.execute(action_id, paras=self.parameters, batch_paras={})
                        self.response.update_content({action_item: exec_result})
                        if error:
                            self.response.update(error)
                            self.response.set_success(False)
                            return False
                        else:
                            if self.transaction:
                                self.transaction.commit()
                    except Exception as e:
                        traceback.print_exc()
                        error_id = uuid.uuid4().hex
                        LoggerUtils.error("raised Exception [{}] [{}]".format(error_id, str(e)))
                        if self.transaction:
                            self.transaction.rollback()
                        return False
                    finally:
                        if self.transaction:
                            self.transaction.close()
                            self.transaction = None
                elif action_type == "c":
                    [module, action] = action_id.split(".")
                    module_instance, action_target = self.get_dispatcher().get_action(module, action)
                    if not module_instance or not action_target:
                        self.response.update({"success": False, "code": ERROR_WEB_API_NOT_FOUND})
                        return False
                    if isinstance(module_instance, Securable) and not module_instance.is_accessable():
                        self.response.update({"success": False, "code": ERROR_WEB_API_NOT_ALLOWED})
                        return False
                    if not action_target(self, *args, **kwargs):
                        return False
        return True

    def set_transaction(self):
        self.transaction = self.db_executor.get_transaction()