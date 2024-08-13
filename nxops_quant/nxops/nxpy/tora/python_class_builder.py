# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-09-10 09:28:06
LastEditTime : 2020-09-10 09:28:47
LastEditors  : yi.mt
Description  : 
'''
import inspect

import mdapi
import traderapi

FIELD_CLAZZ_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3
"""

FIELD_CLAZZ_TEMPLATE = """
class {field_clazz_name}():
    def __init__(self):
        self._module_ = "traderapi"
        self._clazz_ = "{field_clazz_name}"
{attrs_def_code}
"""

ATTR_DEF_TEMPLATE = """        self.{attr_name} = {attr_value}
"""

def build_api_fields():
    field_clazz_code = ""
    for field_clazz_name, clazz_obj in traderapi.__dict__.items():
        if field_clazz_name[-5:] == "Field":
            obj = clazz_obj()
            attrs_def_code = ""
            attrs_put_code = ""
            for attr_name in clazz_obj.__swig_setmethods__.keys():
                attr_value = obj.__getattr__(attr_name)
                if isinstance(attr_value, str):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value="\"\"")
                elif isinstance(attr_value, int):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value=0)
                elif isinstance(attr_value, float):
                    attrs_def_code += ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value=0.0)
                else:
                    print(f"{field_clazz_name} {attr_name} undefined type")

            field_clazz_code += FIELD_CLAZZ_TEMPLATE.format(field_clazz_name=field_clazz_name, attrs_def_code=attrs_def_code)

    with open(f"./build_python/fields.py", "w") as jf:
        jf.write(FIELD_CLAZZ_HEADER)
        jf.write(field_clazz_code)

AGENT_SPI_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3

import uuid
import time
import rapidjson
import asyncio

from autobahn.wamp.types import CallOptions
from autobahn.asyncio.component import run

from nxpy.log.logger import LoggerUtils
from nxpy.crossbar.wamp import EasyApplicationSession, EasyServiceUtils


class EasyAgentMainSession(EasyApplicationSession):
    def do_init(self):
        agent_name = "trader_agent_main"
        extra_config = self.config.extra

        self.easy_authid = agent_name + "_" + uuid.uuid4().hex[10:18]

    async def onJoin(self, details):
        super().onJoin(details)


class EasyAgentTraderSession(EasyApplicationSession):
    def do_init(self):
        extra_config = self.config.extra

        self.api = extra_config.get("api")

        self.node_id = extra_config.get("node_id", "tora")
        self.trader_id = extra_config.get("trader_id")
        self.agent_name = self.node_id + "_trader_agent_" + self.trader_id
        self.easy_authid = self.agent_name + "_" + uuid.uuid4().hex[10:18]

    async def onJoin(self, details):
        super().onJoin(details)

        if self.api:
            self.api.app = self
            await self.api.Init()


class EasyAgentTraderSpi():
    def __init__(self, api):
        super().__init__()
        
        self.api = api

    async def OnFrontConnected(self):
        pass

    async def OnFrontDisConnected(self, nReason):
        pass
            
    async def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        pass
"""

AGENT_API_HEADER = """
class EasyAgentTraderApi():
    def __init__(self, trader_id, node_id="tora"):
        super().__init__()

        self.app = None
        self.spi = None
        self.node_id = node_id
        self.trader_id = trader_id

        self._created = False

        self._run()

    def _run(self):
        extra_config = dict({}, node_id=self.node_id, trader_id=self.trader_id, agent_name="trader_agent_" + self.trader_id, api=self)
        component = EasyServiceUtils.create_component(extra=extra_config, session_factory=EasyAgentTraderSession)
        run([component], start_loop=False)

    def _on_create_tstp_trader_api(self):
        self._created = True

    def RegisterSpi(self, spi):
        self.spi = spi

    async def dispatch_response(self, procedure, *args, details=None):
        if len(args) == 4:
            rsp_info = args[1]
            request_id = args[2]
            is_last = args[3]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg, request_id, is_last))
        elif len(args) == 5:
            rsp_info = args[1]
            request_id = args[2]
            is_page_end = args[3]
            is_total_end = args[4]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg, request_id, is_page_end, is_total_end))
        else:
            LoggerUtils.debug("agent[{}] {}".format(self.app.authid, procedure))
        
        if self.spi:
            procedure_method = self.spi.__class__.__dict__.get(procedure)
            if procedure_method:
                await procedure_method(self.spi, *args)

    async def dispatch_return(self, procedure, *args, details=None):
        if len(args) == 2:
            rsp_info = args[1]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg))
        else:
            LoggerUtils.debug("agent[{}] {}".format(self.app.authid, procedure))
            
        if procedure == "OnCreateTstpTraderApi":
            self._on_create_tstp_trader_api()
        elif self.spi:
            procedure_method = self.spi.__class__.__dict__.get(procedure)
            if procedure_method:
                await procedure_method(self.spi, *args)

    async def Init(self):
        LoggerUtils.debug("agent[{}] call Init".format(self.app.authid))

        await self.app.subscribe(self.dispatch_response, self.node_id + "_trader_" + self.trader_id + ".RSP." + self.app.authid)
        await self.app.subscribe(self.dispatch_return, self.node_id + "_trader_" + self.trader_id + ".RTN")

        self.app.call("trader.CreateTstpTraderApi", self.node_id, self.trader_id, options=CallOptions())

        while not self._created:
            await asyncio.sleep(0)

        await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "Init", options=CallOptions())
"""

AGENT_COMPONENT_TAIL = """
component = EasyServiceUtils.create_component(session_factory=EasyAgentMainSession)
def get_components():
    return [component]
"""

AGENT_SPI_ON_RSP_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

AGENT_SPI_ON_RSPHISTORY_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

AGENT_SPI_ON_RTN_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

AGENT_SPI_ON_ERRRTN_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

AGENT_REQ_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "{method_name}", {method_args}, options=CallOptions())
        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.trader_id, result))
        return result
"""

def build_agent_file():
    api_methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderApi.__dict__.items():
        method_code = ""
        if type(method_obj).__name__ == "function":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if method_name[0:3] == "Req":
                method_args = ", ".join(list(args)[1:])
                method_code = AGENT_REQ_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                api_methods_code += method_code
    
    spi_methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderSpi.__dict__.items():
        method_code = ""
        if type(method_obj).__name__ == "function":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if len(args) >= 2:
                method_code = ""
                method_args = ", ".join(list(args))
                if method_name == "OnRspError":
                    pass
                elif method_name[0:19] == "OnRspInquiryHistory":
                    method_code = AGENT_SPI_ON_RSPHISTORY_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                elif method_name[0:5] == "OnRsp":
                    method_code = AGENT_SPI_ON_RSP_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                elif method_name[0:5] == "OnRtn":
                    method_code = AGENT_SPI_ON_RTN_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                elif method_name[0:8] == "OnErrRtn":
                    method_code = AGENT_SPI_ON_ERRRTN_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                spi_methods_code += method_code

    with open(f"./build_python/agent.py", "w") as jf:
        jf.write(AGENT_SPI_HEADER)
        jf.write(spi_methods_code)
        jf.write(AGENT_API_HEADER)
        jf.write(api_methods_code)
        jf.write(AGENT_COMPONENT_TAIL)

TRADER_SPI_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3

import time
import uuid
import rapidjson
import traderapi

from autobahn.wamp.types import RegisterOptions, PublishOptions

from nxpy.crossbar.wamp import EasyApplicationSession

from nxpy.log.logger import LoggerUtils


class EasyTraderSpi(traderapi.CTORATstpTraderSpi):
    def __init__(self, app, api):
        traderapi.CTORATstpTraderSpi.__init__(self)

        self.app = app
        self.api = api
        self.req_id = 0

        self.rsp_topic_id = self.app.node_id + "_trader_" + self.app.trader_id + ".RSP"
        self.rtn_topic_id = self.app.node_id + "_trader_" + self.app.trader_id + ".RTN"

        self.requests = {}

        self.connected = False

    def _gen_rsp_topic_id(self, caller_authid=None):
        return (self.rsp_topic_id + "." + caller_authid) if caller_authid else self.rsp_topic_id

    def OnFrontConnected(self):
        LoggerUtils.debug("service[{}] OnFrontConnected".format(self.app.authid))

        self.connected = True
        self.app.publish(self.rtn_topic_id, "OnFrontConnected")

    def OnFrontDisconnected(self, nReason):
        LoggerUtils.debug("service[{}] OnFrontDisconnected: [reason={}]".format(self.app.authid, nReason))

        self.connected = False
        self.app.publish(self.rtn_topic_id, "OnFrontDisconnected")

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspError: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsLast:
            self.requests.pop(nRequestID, None)

        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspError", pRspInfo, s_request_id, bIsLast)
"""

TRADER_ON_RSP_METHOD_TEMPLATE = """
    def {method_name}(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}, RequestID={{}}, IsLast={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({{"_module_": "traderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"}})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "{method_name}", pRspField, pRspInfo, s_request_id, bIsLast)
"""

TRADER_ON_RSPHISTORY_METHOD_TEMPLATE = """
    def {method_name}(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}, RequestID={{}}, bIsPageEnd={{}}, bIsTotalEnd={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({{"_module_": "traderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"}})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "{method_name}", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)
"""

TRADER_ON_RTN_METHOD_TEMPLATE = """
    def {method_name}(self, pRtnField):
        LoggerUtils.debug("service[{{}}] {method_name}".format(self.app.authid))

        if pRtnField:
            pRtnField.update({{"_module_": "traderagent", "_clazz_": "{field_arg_class}"}})

        self.app.publish(self.rtn_topic_id, "{method_name}", pRtnField)
"""

TRADER_ON_ERRRTN_METHOD_TEMPLATE = """
    def {method_name}(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({{"_module_": "traderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"}})

        self.app.publish(self.rtn_topic_id, "{method_name}", pRtnField, pRspInfo)
"""

TRADER_SESSION_HEADER = """
class EasyTraderSession(EasyApplicationSession):
    trader_apis = {}

    def __init__(self, config=None):
        super().__init__(config)

    def do_init(self):
        extra_config = self.config.extra

        self.node_id = extra_config.get("node_id")
        self.trader_id = extra_config.get("trader_id")
        self.service_name = "easy_" + self.node_id + "_trader_" + self.trader_id
        self.easy_authid = self.service_name + "_" + uuid.uuid4().hex[10:18]
        self.front = extra_config.get("front")
        self.fens = extra_config.get("fens")

        self.api = None
        self.spi = None

    def get_request_id(self):
        self.spi.req_id += 1
        return self.spi.req_id

    def onJoin(self, details):
        LoggerUtils.debug("service[{}] joined: [realm={}, role={}]".format(self.authid, self.realm, self.authrole))

        self.register(self.dispatch_request, f"{self.node_id}_trader_{self.trader_id}.REQ", options=RegisterOptions(details=True))

        self.publish(f"{self.node_id}_trader_{self.trader_id}.RTN", "OnCreateTstpTraderApi")

    def _init_trader_api(self):
        LoggerUtils.debug("service[{}] trader api version: {}".format(self.authid, traderapi.CTORATstpTraderApi_GetApiVersion()))
        self.api = traderapi.CTORATstpTraderApi.CreateTstpTraderApi(self.trader_id)
        self.spi = EasyTraderSpi(self, self.api)
        self.api.RegisterSpi(self.spi)
        self.api.RegisterFront(self.front)

        self.api.SubscribePrivateTopic(traderapi.TORA_TERT_QUICK)
        self.api.SubscribePublicTopic(traderapi.TORA_TERT_QUICK)

        self.api.Init()

    def dispatch_request(self, procedure, *args, details):
        LoggerUtils.debug("caller[{}] calling service[{}] {}".format(details.caller_authid, self.authid, procedure))

        procedure_method = self.__class__.__dict__.get(procedure)
        if procedure_method:
            result = procedure_method(self, *args, details)

            LoggerUtils.debug("caller[{}] calling service[{}] {}: [result={}]".format(details.caller_authid, self.authid, procedure, result))
        return result

    def Init(self, details):
        if self.api and self.spi:
            if self.spi.connected:
                self.publish(self.spi._gen_rsp_topic_id(details.caller_authid), "OnFrontConnected")
        else:
            if self.trader_id not in self.trader_apis:
                self._init_trader_api()
                self.trader_apis.update({self.trader_id: {"api": self.api, "spi": self.spi}})
            else:
                exists = self.trader_apis.get(self.trader_id)
                self.api = exists.get("api")
                self.spi = exists.get("spi")
"""

TRADER_REQ_METHOD_TEMPLATE = """
    def {method_name}(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.{method_name}(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({{r_request_id: {{"caller": details.caller_authid, "request_id": request_id}}}})

        return result
"""

TRADER_UTILS_TAIL = """
class EasyTraderUtils():
    trader_settings = {}

    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.trader_settings = rapidjson.load(cf)

    @classmethod
    def get_settings(cls, node_id="tora"):
        return cls.trader_settings.get(node_id)
"""

def build_trader_file():
    session_methods_code = ""
    for method_name in traderapi.CTORATstpTraderApi.__dict__.keys():
        if method_name[0:3] == "Req":
            method_code = TRADER_REQ_METHOD_TEMPLATE.format(method_name=method_name)
            session_methods_code += method_code

    spi_methods_code = ""
    for method_name, method_obj in traderapi.CTORATstpTraderSpi.__dict__.items():
        method_code = ""
        if type(method_obj).__name__ == "function":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if len(args) >= 2:
                field_arg_name = args[1]
                field_arg_class = "CTORATstp" + field_arg_name[1:] + ("" if field_arg_name[-5:] == "Field" else "Field")

                if method_name == "OnRspError":
                    pass
                elif method_name[0:5] == "OnRsp":
                    if len(args) == 5:
                        method_code = TRADER_ON_RSP_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                    elif len(args) == 6:
                        method_code = TRADER_ON_RSPHISTORY_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                elif method_name[0:5] == "OnRtn":
                    method_code = TRADER_ON_RTN_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                elif method_name[0:8] == "OnErrRtn":
                    method_code = TRADER_ON_ERRRTN_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                spi_methods_code +=method_code

    with open(f"./build_python/trader.py", "w") as jf:
        jf.write(TRADER_SPI_HEADER)
        jf.write(spi_methods_code)
        jf.write(TRADER_SESSION_HEADER)
        jf.write(session_methods_code)
        jf.write(TRADER_UTILS_TAIL)

CONSTANTS_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3

"""

CONSTANTS_TEMPLATE = """{constant_name} = {constant_value}
"""

def build_constants():
    constants_code = ""
    for constant_name, constant_value in traderapi.__dict__.items():
        if constant_name[0:5] == "TORA_":
            if isinstance(constant_value, str):
                constant_value = f"\"{constant_value}\""
            constants_code += CONSTANTS_TEMPLATE.format(constant_name=constant_name, constant_value=constant_value)
        
    with open(f"./build_python/constants.py", "w") as jf:
        jf.write(CONSTANTS_HEADER)
        jf.write(constants_code)

MDER_SPI_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3

import time
import uuid
import rapidjson
import mdapi

from autobahn.wamp.types import RegisterOptions, PublishOptions

from nxpy.crossbar.wamp import EasyApplicationSession

from nxpy.log.logger import LoggerUtils


class EasyMdSpi(mdapi.CTORATstpMdSpi):
    def __init__(self, app, api):
        mdapi.CTORATstpMdSpi.__init__(self)

        self.app = app
        self.api = api
        self.req_id = 0

        self.rsp_topic_id = self.app.node_id + "_mder.RSP"
        self.rtn_topic_id = self.app.node_id + "_mder.RTN"

        self.requests = {}

        self.connected = False
        self.logined = False

    def _gen_rsp_topic_id(self, caller_authid=None):
        return (self.rsp_topic_id + "." + caller_authid) if caller_authid else self.rsp_topic_id

    def OnFrontConnected(self):
        LoggerUtils.debug("service[{}] OnFrontConnected".format(self.app.authid))

        self.connected = True
        self.app.publish(self.rtn_topic_id, "OnFrontConnected")

        req_field = mdapi.CTORATstpReqUserLoginField()
        req_field.LogInAccountID = self.app.mder_id
        req_field.LogInAccountType = "0"
        req_field.Password = self.app.mder_pwd

        request_id = self.app.get_request_id()
        self.api.ReqUserLogin(req_field, request_id)

    def OnFrontDisconnected(self, nReason):
        LoggerUtils.debug("service[{}] OnFrontDisconnected: [reason={}]".format(self.app.authid, nReason))

        self.connected = False
        self.logined = False
        self.app.publish(self.rtn_topic_id, "OnFrontDisconnected")

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspError: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsLast:
            self.requests.pop(nRequestID, None)

        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspError", pRspInfo, s_request_id, bIsLast)

    def OnRspUserLogin(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUserLogin: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspUserLoginField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if pRspInfo["ErrorID"] == 0:
            self.logined = True

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUserLogin", pRspField, pRspInfo, s_request_id, bIsLast)
"""

MDER_ON_RSP_METHOD_TEMPLATE = """
    def {method_name}(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}, RequestID={{}}, IsLast={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({{"_module_": "mderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"}})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "{method_name}", pRspField, pRspInfo, s_request_id, bIsLast)
"""

MDER_ON_RSPINQUIRY_METHOD_TEMPLATE = """
    def {method_name}(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}, RequestID={{}}, bIsPageEnd={{}}, bIsTotalEnd={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({{"_module_": "mderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"}})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "{method_name}", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)
"""

MDER_ON_RTN_METHOD_TEMPLATE = """
    def {method_name}(self, pRtnField):
        LoggerUtils.debug("service[{{}}] {method_name}".format(self.app.authid))

        if pRtnField:
            pRtnField.update({{"_module_": "mderagent", "_clazz_": "{field_arg_class}"}})

        self.app.publish(self.rtn_topic_id + ".{method_name}." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "{method_name}", pRtnField)
"""

MDER_ON_ERRRTN_METHOD_TEMPLATE = """
    def {method_name}(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{{}}] {method_name}: [ErrorID={{}}, ErrorMsg={{}}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({{"_module_": "mderagent", "_clazz_": "{field_arg_class}"}})
        if pRspInfo:
            pRspInfo.update({{"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"}})

        self.app.publish(self.rtn_topic_id, "{method_name}", pRtnField, pRspInfo)
"""

MDER_SESSION_HEADER = """
class EasyMderSession(EasyApplicationSession):
    mder_apis = {}

    def __init__(self, config=None):
        super().__init__(config)

    def do_init(self):
        extra_config = self.config.extra

        self.node_id = extra_config.get("node_id", "tora")
        self.mder_id = extra_config.get("mder_id")
        self.mder_pwd = extra_config.get("mder_pwd")
        self.service_name = "easy_" + self.node_id +"_mder_" + self.mder_id
        self.easy_authid = self.service_name + "_" + uuid.uuid4().hex[10:18]
        self.front = extra_config.get("front")
        self.fens = extra_config.get("fens")

        self.api = None
        self.spi = None

    def get_request_id(self):
        self.spi.req_id += 1
        return self.spi.req_id

    def onJoin(self, details):
        LoggerUtils.debug("service[{}] joined: [realm={}, role={}]".format(self.authid, self.realm, self.authrole))

        self.register(self.dispatch_request, f"{self.node_id}_mder.REQ", options=RegisterOptions(details=True))

        self.publish(f"{self.node_id}_mder.RTN", "OnCreateTstpMdApi")

    def _init_mder_api(self):
        LoggerUtils.debug("service[{}] md api version: {}".format(self.authid, mdapi.CTORATstpMdApi_GetApiVersion()))
        self.api = mdapi.CTORATstpMdApi.CreateTstpMdApi()
        self.spi = EasyMdSpi(self, self.api)
        self.api.RegisterSpi(self.spi)
        self.api.RegisterFront(self.front)

        self.api.Init()

    def dispatch_request(self, procedure, *args, details):
        LoggerUtils.debug("caller[{}] calling service[{}] {}".format(details.caller_authid, self.authid, procedure))

        procedure_method = self.__class__.__dict__.get(procedure)
        if procedure_method:
            result = procedure_method(self, *args, details)

            LoggerUtils.debug("caller[{}] calling service[{}] {}: [result={}]".format(details.caller_authid, self.authid, procedure, result))
        return result

    def Init(self, details):
        if self.api and self.spi:
            if self.spi.connected:
                self.publish(self.spi._gen_rsp_topic_id(details.caller_authid), "OnFrontConnected")
        else:
            if self.mder_id not in self.mder_apis:
                self._init_mder_api()
                self.mder_apis.update({self.mder_id: {"api": self.api, "spi": self.spi}})
            else:
                exists = self.mder_apis.get(self.mder_id)
                self.api = exists.get("api")
                self.spi = exists.get("spi")
    
    def ReqUserLogin(self, req_field, request_id, details):
        if self.spi.logined:
            self.publish(self.spi._gen_rsp_topic_id(details.caller_authid), "OnRspUserLogin", {}, {"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField", "ErrorID": 0, "ErrorMsg": "VIP:正确"}, request_id, True)
        else:
            self.publish(self.spi._gen_rsp_topic_id(details.caller_authid), "OnRspUserLogin", {}, {"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField", "ErrorID": -1, "ErrorMsg": "VIP:未登录"}, request_id, True)
        return 0

    def ReqUserLogout(self, req_field, request_id, details):
        self.publish(self.spi._gen_rsp_topic_id(details.caller_authid), "ReqUserLogout", {}, {"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField", "ErrorID": 0, "ErrorMsg": "VIP:正确"}, request_id, True)
        return 0
"""

MDER_REQ_METHOD_TEMPLATE = """
    def {method_name}(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.{method_name}(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({{r_request_id: {{"caller": details.caller_authid, "request_id": request_id}}}})

        return result
"""

MDER_SUB_METHOD_TEMPLATE = """
    def {method_name}(self, {method_args}, details):
        result = self.api.{method_name}({method_args})

        return result
"""

MDER_UNSUB_METHOD_TEMPLATE = """
    def {method_name}({method_args}, details):
        return 0
"""

MDER_UTILS_TAIL = """
class EasyMderUtils():
    mder_settings = {}

    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.mder_settings = rapidjson.load(cf)

    @classmethod
    def get_settings(cls, node_id="tora"):
        return cls.mder_settings.get(node_id)
"""
def build_md_file():
    session_methods_code = ""
    for method_name, method_obj in mdapi.CTORATstpMdApi.__dict__.items():
        if type(method_obj).__name__ == "function":
            method_code = ""
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if method_name[0:3] == "Req" and method_name not in ["ReqUserLogin", "ReqUserLogout"]:
                method_code = MDER_REQ_METHOD_TEMPLATE.format(method_name=method_name)
                session_methods_code += method_code
            elif method_name[0:3] == "Sub":
                method_args = ", ".join(list(args)[1:])
                method_code = MDER_SUB_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                session_methods_code += method_code
            elif method_name[0:5] == "UnSub":
                method_args = ", ".join(list(args))
                method_code = MDER_UNSUB_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
            
            session_methods_code += method_code

    spi_methods_code = ""
    for method_name, method_obj in mdapi.CTORATstpMdSpi.__dict__.items():
        method_code = ""
        if type(method_obj).__name__ == "function":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if len(args) >= 2:
                field_arg_name = args[1]
                field_arg_class = "CTORATstp" + field_arg_name[1:] + ("" if field_arg_name[-5:] == "Field" else "Field")
                field_arg_class = field_arg_class if field_arg_class != "CTORATstpDepthMarketDataField" else "CTORATstpMarketDataField"

                if method_name == "OnRspError":
                    pass
                elif method_name[0:5] == "OnRsp" and method_name not in["OnRspUserLogin"]:
                    if len(args) == 5:
                        method_code = MDER_ON_RSP_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                    elif len(args) == 6:
                        method_code = MDER_ON_RSPINQUIRY_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                elif method_name[0:5] == "OnRtn":
                    method_code = MDER_ON_RTN_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                elif method_name[0:8] == "OnErrRtn":
                    method_code = MDER_ON_ERRRTN_METHOD_TEMPLATE.format(method_name=method_name, field_arg_class=field_arg_class)
                spi_methods_code +=method_code

    with open(f"./build_python/mder.py", "w") as jf:
        jf.write(MDER_SPI_HEADER)
        jf.write(spi_methods_code)
        jf.write(MDER_SESSION_HEADER)
        jf.write(session_methods_code)
        jf.write(MDER_UTILS_TAIL)


MD_FIELD_CLAZZ_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3
"""

MD_FIELD_CLAZZ_TEMPLATE = """
class {field_clazz_name}():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "{field_clazz_name}"
{attrs_def_code}
"""

MD_ATTR_DEF_TEMPLATE = """        self.{attr_name} = {attr_value}
"""

def build_mdapi_fields():
    field_clazz_code = ""
    for field_clazz_name, clazz_obj in mdapi.__dict__.items():
        if field_clazz_name[-5:] == "Field":
            obj = clazz_obj()
            attrs_def_code = ""
            attrs_put_code = ""
            for attr_name in clazz_obj.__swig_setmethods__.keys():
                attr_value = obj.__getattr__(attr_name)
                if isinstance(attr_value, str):
                    attrs_def_code += MD_ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value="\"\"")
                elif isinstance(attr_value, int):
                    attrs_def_code += MD_ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value=0)
                elif isinstance(attr_value, float):
                    attrs_def_code += MD_ATTR_DEF_TEMPLATE.format(attr_name=attr_name, attr_value=0.0)
                else:
                    print(f"{field_clazz_name} {attr_name} undefined type")

            field_clazz_code += MD_FIELD_CLAZZ_TEMPLATE.format(field_clazz_name=field_clazz_name, attrs_def_code=attrs_def_code)

    with open(f"./build_python/mdfields.py", "w") as jf:
        jf.write(MD_FIELD_CLAZZ_HEADER)
        jf.write(field_clazz_code)


MDER_AGENT_SPI_HEADER = """# -*- coding: UTF-8 -*-
# cython: language_level=3

import uuid
import time
import rapidjson
import asyncio

from autobahn.wamp.types import CallOptions, SubscribeOptions
from autobahn.asyncio.component import run

from nxpy.log.logger import LoggerUtils
from nxpy.crossbar.wamp import EasyApplicationSession, EasyServiceUtils


class EasyAgentMainSession(EasyApplicationSession):
    def do_init(self):
        agent_name = "mder_agent_main"
        extra_config = self.config.extra

        self.easy_authid = agent_name + "_" + uuid.uuid4().hex[10:18]

    async def onJoin(self, details):
        super().onJoin(details)


class EasyAgentMderSession(EasyApplicationSession):
    def do_init(self):
        extra_config = self.config.extra

        self.api = extra_config.get("api")

        self.node_id = extra_config.get("node_id", "tora")
        self.mder_id = extra_config.get("mder_id")
        self.agent_name = self.node_id + "_mder_agent_" + self.mder_id
        self.easy_authid = self.agent_name + "_" + uuid.uuid4().hex[10:18]

    async def onJoin(self, details):
        super().onJoin(details)

        if self.api:
            self.api.app = self
            await self.api.Init()


class EasyAgentMdSpi():
    def __init__(self, api):
        super().__init__()
        
        self.api = api

    async def OnFrontConnected(self):
        pass

    async def OnFrontDisConnected(self, nReason):
        pass
            
    async def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        pass
"""

MDER_AGENT_API_HEADER = """
class EasyAgentMdApi():
    def __init__(self, mder_id, node_id="tora"):
        super().__init__()

        self.app = None
        self.spi = None
        self.node_id = node_id
        self.mder_id = mder_id

        self._created = False

        self._run()

    def _run(self):
        extra_config = dict({}, node_id=self.node_id, mder_id=self.mder_id, agent_name="mder_agent_" + self.mder_id, api=self)
        component = EasyServiceUtils.create_component(extra=extra_config, session_factory=EasyAgentMderSession)
        run([component], start_loop=False)

    def _on_create_tstp_md_api(self):
        self._created = True

    def RegisterSpi(self, spi):
        self.spi = spi

    async def dispatch_response(self, procedure, *args, details=None):
        if len(args) == 4:
            rsp_info = args[1]
            request_id = args[2]
            is_last = args[3]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg, request_id, is_last))
        elif len(args) == 5:
            rsp_info = args[1]
            request_id = args[2]
            is_page_end = args[3]
            is_total_end = args[4]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg, request_id, is_page_end, is_total_end))
        else:
            LoggerUtils.debug("agent[{}] {}".format(self.app.authid, procedure))
        
        if self.spi:
            procedure_method = self.spi.__class__.__dict__.get(procedure)
            if procedure_method:
                await procedure_method(self.spi, *args)

    async def dispatch_return(self, procedure, *args, details=None):
        if len(args) == 2:
            rsp_info = args[1]
            LoggerUtils.debug("agent[{}] {}: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, procedure, rsp_info.ErrorID, rsp_info.ErrorMsg))
        else:
            LoggerUtils.debug("agent[{}] {}".format(self.app.authid, procedure))
            
        if procedure == "OnCreateTstpMdApi":
            self._on_create_tstp_md_api()
        elif self.spi:
            procedure_method = self.spi.__class__.__dict__.get(procedure)
            if procedure_method:
                await procedure_method(self.spi, *args)

    async def Init(self):
        LoggerUtils.debug("agent[{}] call Init".format(self.app.authid))

        await self.app.subscribe(self.dispatch_response, self.node_id + "_mder.RSP." + self.app.authid)
        await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN", )

        self.app.call("mder.CreateTstpMdApi", self.node_id, self.mder_id, options=CallOptions())

        while not self._created:
            await asyncio.sleep(0)

        await self.app.call(self.node_id + "_mder.REQ", "Init", options=CallOptions())
"""

MDER_AGENT_COMPONENT_TAIL = """
component = EasyServiceUtils.create_component(session_factory=EasyAgentMainSession)
def get_components():
    return [component]
"""

MDER_AGENT_SPI_ON_RSP_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

MDER_AGENT_SPI_ON_RSPHISTORY_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

MDER_AGENT_SPI_ON_RTN_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

MDER_AGENT_SPI_ON_ERRRTN_METHOD_TEMPLATE = """
    async def {method_name}({method_args}):
        return None
"""

MDER_AGENT_REQ_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "{method_name}", {method_args}, options=CallOptions())
        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.mder_id, result))
        return result
"""

MDER_AGENT_SUB_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "{method_name}", {method_args}, options=CallOptions())

        if {pp_para_name} and not (len({pp_para_name}) == 1 and ({pp_para_name}[0] == b"000000" or {pp_para_name}[0] == b"00000000")):
            for security_id in {pp_para_name}:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.mder_id, result))
        return result
"""

MDER_AGENT_SUBOT_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "{method_name}", {method_args}, options=CallOptions())

        await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.mder_id, result))
        return result
"""

MDER_AGENT_UNSUB_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.mder_id))
        result = 0

        if {pp_para_name} and not (len({pp_para_name}) == 1 and ({pp_para_name}[0] == b"000000" or {pp_para_name}[0] == b"00000000")):
            for security_id in {pp_para_name}:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchageID)

        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.mder_id, result))
        return result
"""

MDER_AGENT_UNSUBOT_METHOD_TEMPLATE = """
    async def {method_name}(self, {method_args}):
        LoggerUtils.debug("agent[{{}}] call {method_name}".format(self.mder_id))
        result = 0

        await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.{rtn_method_name}." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{{}}] call {method_name}: [result={{}}]".format(self.mder_id, result))
        return result
"""

def build_mdagent_file():
    api_methods_code = ""
    for method_name, method_obj in mdapi.CTORATstpMdApi.__dict__.items():
        if type(method_obj).__name__ == "function":
            method_code = ""
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if method_name[0:3] == "Req":
                method_args = ", ".join(list(args)[1:])
                method_code = MDER_AGENT_REQ_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
            elif method_name[0:3] == "Sub" and method_name[-6:] == "Detail":
                method_args = ", ".join(list(args)[1:])
                pp_para_name = args[1]
                rtn_method_name = "OnRtn" + (method_name[9:] if method_name[9:] != "MarketData" else "DepthMarketData")
                method_code = MDER_AGENT_SUBOT_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, pp_para_name=pp_para_name, rtn_method_name=rtn_method_name)
            elif method_name[0:3] == "Sub":
                method_args = ", ".join(list(args)[1:])
                pp_para_name = args[1]
                rtn_method_name = "OnRtn" + (method_name[9:] if method_name[9:] != "MarketData" else "DepthMarketData")
                method_code = MDER_AGENT_SUB_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, pp_para_name=pp_para_name, rtn_method_name=rtn_method_name)
            elif method_name[0:5] == "UnSub" and method_name[-6:] == "Detail":
                method_args = ", ".join(list(args)[1:])
                pp_para_name = args[1]
                rtn_method_name = "OnRtn" + (method_name[12:] if method_name[12:] != "MarketData" else "DepthMarketData")
                method_code = MDER_AGENT_UNSUBOT_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, pp_para_name=pp_para_name, rtn_method_name=rtn_method_name)
            elif method_name[0:5] == "UnSub":
                method_args = ", ".join(list(args)[1:])
                pp_para_name = args[1]
                rtn_method_name = "OnRtn" + (method_name[12:] if method_name[12:] != "MarketData" else "DepthMarketData")
                method_code = MDER_AGENT_UNSUB_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, pp_para_name=pp_para_name, rtn_method_name=rtn_method_name)
            api_methods_code += method_code
            
    spi_methods_code = ""
    for method_name, method_obj in mdapi.CTORATstpMdSpi.__dict__.items():
        method_code = ""
        if type(method_obj).__name__ == "function":
            arguments = inspect.getargs(method_obj.__code__)
            args = arguments.args
            if len(args) >= 2:
                field_arg_name = args[1]
                field_arg_class = "CTORATstp" + field_arg_name[1:] + ("" if field_arg_name[-5:] == "Field" else "Field")

                if method_name == "OnRspError":
                    pass
                elif method_name[0:5] == "OnRsp":
                    if len(args) == 5:
                        method_args = ", ".join(list(args))
                        method_code = MDER_AGENT_SPI_ON_RSP_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                    elif len(args) == 6:
                        method_args = ", ".join(list(args))
                        method_code = MDER_AGENT_SPI_ON_RSPHISTORY_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args)
                elif method_name[0:5] == "OnRtn":
                    method_args = ", ".join(list(args))
                    method_code = MDER_AGENT_SPI_ON_RTN_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, field_arg_class=field_arg_class)
                elif method_name[0:8] == "OnErrRtn":
                    method_args = ", ".join(list(args))
                    method_code = MDER_AGENT_SPI_ON_ERRRTN_METHOD_TEMPLATE.format(method_name=method_name, method_args=method_args, field_arg_class=field_arg_class)
                spi_methods_code +=method_code

    with open(f"./build_python/mdagent.py", "w") as jf:
        jf.write(MDER_AGENT_SPI_HEADER)
        jf.write(spi_methods_code)
        jf.write(MDER_AGENT_API_HEADER)
        jf.write(api_methods_code)
        jf.write(MDER_AGENT_COMPONENT_TAIL)

if __name__ == "__main__":
    build_api_fields()
    build_agent_file()
    build_trader_file()
    build_constants()
    build_md_file()
    build_mdapi_fields()
    build_mdagent_file()
