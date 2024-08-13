# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-08-21 09:51:03
LastEditTime : 2020-08-21 15:43:43
LastEditors  : yi.mt
Description  : 
'''

import uuid
import hashlib
import rapidjson

from autobahn.wamp.types import RegisterOptions
from autobahn.asyncio.component import Component
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from autobahn.wamp.message import Call, Invocation, Event
from autobahn.wamp.interfaces import ISerializer, IObjectSerializer
from autobahn.wamp.serializer import Serializer, CBORObjectSerializer, CBORSerializer, SERID_TO_OBJSER, SERID_TO_SER

from nxpy.context import AppContext
from nxpy.web.session import SessionUtils
from nxpy.log.logger import LoggerUtils
from nxpy.module.easy_import import EasyImportUtils

def parse_field_to_dict(arg):
    new_arg = arg
    if arg:
        if type(arg).__module__ == "traderapi" or type(arg).__module__ == "mdapi":
            new_arg = {key : arg.__getattr__(key) for key in arg.__swig_setmethods__.keys()}
            new_arg.update({"_module_": arg.__class__.__module__, "_clazz_": arg.__class__.__name__})
        elif type(arg).__module__ == "nxpy.tora.fields" or type(arg).__module__ == "nxpy.tora.mdfields":
            new_arg = arg.__dict__.copy()
    return new_arg

def parse_dict_to_field(arg):
    field = arg
    if isinstance(arg, dict) and "_module_" in arg and "_clazz_" in arg:
        module_name = arg.get("_module_")
        if module_name == "traderagent":
            module_name = "nxpy.tora.fields"
        elif module_name == "mderagent":
            module_name = "nxpy.tora.mdfields"
        module = EasyImportUtils.import_module(module_name)
        field = module.__dict__[arg.get("_clazz_")]()

        for key, value in arg.items():
            if key != "_module_" and key != "_clazz_":
                field.__setattr__(key, value)
    return field


class CFieldCBORObjectSerializer(CBORObjectSerializer):
    def serialize(self, obj):
        if obj[0] == Call.MESSAGE_TYPE:
            if len(obj) >= 5 and isinstance(obj[4], tuple):
                new_args = [parse_field_to_dict(arg) for arg in obj[4]]
                obj[4] = tuple(new_args)
        return super().serialize(obj)


class CFieldCBORSerializer(CBORSerializer):
    def __init__(self, batched=False):
        Serializer.__init__(self, CFieldCBORObjectSerializer(batched=batched))
        if batched:
            self.SERIALIZER_ID = "cbor.batched"

    def unserialize(self, payload, isBinary=None):
        msgs = super().unserialize(payload, isBinary)
        for msg in msgs:
            if msg.MESSAGE_TYPE == Invocation.MESSAGE_TYPE or msg.MESSAGE_TYPE == Event.MESSAGE_TYPE:
                new_args = []
                if msg.args:
                    for arg in msg.args:
                        new_args.append(parse_dict_to_field(arg))
                    msg.args = tuple(new_args)
        return msgs


class EasyApplicationSession(ApplicationSession):
    def __init__(self, config=None):
        super().__init__(config)

        self.do_init()

    def do_init(self):
        service_name = "easy_service"
        extra_config = self.config.extra

        if extra_config and isinstance(extra_config, dict) and "service_name" in extra_config:
            service_name = extra_config.get("service_name")

        self.easy_authid = service_name + "_" + uuid.uuid4().hex[10:18]

    def onConnect(self):
        self.join(self.config.realm, ["ticket"], self.easy_authid)

    def onChallenge(self, challenge):
        if challenge.method == "ticket":
            return hashlib.md5(bytes(self.easy_authid, encoding="UTF-8")).hexdigest()
        else:
            raise Exception("Invalid authmethod {}".format(challenge.method))

    def onJoin(self, details):
        LoggerUtils.info("service[{}] joined: [realm={}, role={}]".format(self.authid, self.realm, self.authrole))


class EasyServiceComponent(Component):
    def __init__(self, *args, **kwargs):
        if "session_factory" in kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(*args, **dict(kwargs, session_factory=EasyApplicationSession))

    def publish(self, topic, *args, **kwargs):
        self._session.publish(topic, *args, **kwargs)

    @staticmethod
    def create_component(*args, **kwargs):
        return EasyServiceComponent(*args, **kwargs)


class EasyApplicationRunner(ApplicationRunner):
    def __init__(self, url, realm=None, extra=None, serializers=None, ssl=None, proxy=None, headers=None):
        if not serializers:
            serializers = [CFieldCBORSerializer()]
        super().__init__(url, realm, extra, serializers, ssl, proxy, headers)

class EasyServiceUtils():
    service_settings = {}
    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.service_settings = rapidjson.load(cf)

        IObjectSerializer.register(CFieldCBORObjectSerializer)
        SERID_TO_OBJSER[CBORObjectSerializer.NAME] = CFieldCBORObjectSerializer

        ISerializer.register(CFieldCBORSerializer)
        SERID_TO_SER[CBORSerializer.SERIALIZER_ID] = CFieldCBORSerializer

    @classmethod
    def create_component(cls, name=None, crossbar=None, *args, **kwargs):
        crossbar = crossbar if crossbar else "crossbar"
        crossbar_settings = cls.service_settings.get(crossbar, {}).copy()
        crossbar_settings.update(kwargs)

        if name:
            extra_settings = crossbar_settings.get("extra", {})
            extra_settings.update({"service_name": name})

            crossbar_settings.update({"extra": extra_settings})

        return EasyServiceComponent(**crossbar_settings)

    @classmethod
    def load_components(cls, *args, **kwargs):
        components_settings = cls.service_settings.get("components", [])

        components = []
        for component_module in components_settings:
            module = EasyImportUtils.import_module(component_module)
            if "get_components" in module.__dict__:
                components.extend(module.get_components())

        return components

    @classmethod
    def create_app_runner(cls):
        crossbar_settings = cls.service_settings.get("crossbar", {})
        runner = EasyApplicationRunner(crossbar_settings.get("url"), crossbar_settings.get("realm"))
        return runner

    @staticmethod
    def get_web_session(call_details):
        caller_authid = call_details["caller_authid"]

        sep_idx = caller_authid.find("-")
        session_id = caller_authid if sep_idx == -1 else caller_authid[:sep_idx]
        web_session = SessionUtils.get_session(None, id=session_id, use_cookies=False)
        
        return web_session


