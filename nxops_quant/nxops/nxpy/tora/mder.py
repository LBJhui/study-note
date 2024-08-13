# -*- coding: UTF-8 -*-
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

    def OnRspUserLogout(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUserLogout: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpUserLogoutField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUserLogout", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubPHMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubPHMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubPHMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubPHMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubPHMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubPHMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubSpecialMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubSpecialMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubSpecialMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubSpecialMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubSpecialMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubSpecialMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryMarketDataMirror(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryMarketDataMirror: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpMarketDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryMarketDataMirror", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryPHMarketDataMirror(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryPHMarketDataMirror: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpPHMarketDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryPHMarketDataMirror", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquirySpecialMarketDataMirror(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquirySpecialMarketDataMirror: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpMarketDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquirySpecialMarketDataMirror", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubRapidMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubRapidMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubRapidMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubRapidMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubRapidMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubRapidMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubFundsFlowMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubFundsFlowMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubFundsFlowMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubFundsFlowMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubFundsFlowMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubFundsFlowMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubIndustryIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubIndustryIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubIndustryIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubIndustryIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubIndustryIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubIndustryIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubConceptionIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubConceptionIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubConceptionIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubConceptionIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubConceptionIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubConceptionIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubRegionIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubRegionIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubRegionIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubRegionIndexData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubRegionIndexData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubRegionIndexData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubEffectOrderDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubEffectOrderDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectDetailItemField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubEffectOrderDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubEffectOrderDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubEffectOrderDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubEffectOrderDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspSubEffectTradeDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspSubEffectTradeDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectDetailItemField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspSubEffectTradeDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUnSubEffectTradeDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUnSubEffectTradeDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecificSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUnSubEffectTradeDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnDepthMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnDepthMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnDepthMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnDepthMarketData", pRtnField)

    def OnRtnPHMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnPHMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpPHMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnPHMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnPHMarketData", pRtnField)

    def OnRtnSpecialMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnSpecialMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSpecialMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnSpecialMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnSpecialMarketData", pRtnField)

    def OnRtnRapidMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnRapidMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRapidMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnRapidMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnRapidMarketData", pRtnField)

    def OnRtnFundsFlowMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnFundsFlowMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpFundsFlowMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnFundsFlowMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnFundsFlowMarketData", pRtnField)

    def OnRtnEffectPriceMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnEffectPriceMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectPriceMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnEffectPriceMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnEffectPriceMarketData", pRtnField)

    def OnRtnEffectVolumeMarketData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnEffectVolumeMarketData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectVolumeMarketDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnEffectVolumeMarketData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnEffectVolumeMarketData", pRtnField)

    def OnRtnEffectOrderDetail(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnEffectOrderDetail".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectOrderDetailField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnEffectOrderDetail." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnEffectOrderDetail", pRtnField)

    def OnRtnEffectTradeDetail(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnEffectTradeDetail".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEffectTradeDetailField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnEffectTradeDetail." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnEffectTradeDetail", pRtnField)

    def OnRtnIndustryIndexData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnIndustryIndexData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpIndustryIndexDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnIndustryIndexData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnIndustryIndexData", pRtnField)

    def OnRtnConceptionIndexData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnConceptionIndexData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpConceptionIndexDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnConceptionIndexData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnConceptionIndexData", pRtnField)

    def OnRtnRegionIndexData(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnRegionIndexData".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRegionIndexDataField"})

        self.app.publish(self.rtn_topic_id + ".OnRtnRegionIndexData." + str(pRtnField["ExchangeID"], encoding="UTF-8") + "." + pRtnField["SecurityID"], "OnRtnRegionIndexData", pRtnField)

    def OnRspInquiryRightsAdjustment(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryRightsAdjustment: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRightsAdjustmentDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryRightsAdjustment", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryHistoryFundsFlow(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryHistoryFundsFlow: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpHistoryFundsFlowDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryHistoryFundsFlow", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryFinancialIndicator(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryFinancialIndicator: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpFinancialIndicatorDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryFinancialIndicator", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryDividend(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryDividend: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpDividendDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryDividend", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryRightIssue(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryRightIssue: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRightIssueDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryRightIssue", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryCompanyDescription(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryCompanyDescription: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpCompanyDescriptionDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryCompanyDescription", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquirySalesSegment(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquirySalesSegment: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpSalesSegmentDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquirySalesSegment", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryEquityStructure(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryEquityStructure: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpEquityStructureDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryEquityStructure", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryTopTenHolders(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryTopTenHolders: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpTopTenHoldersDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryTopTenHolders", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryTopTenFloatHolders(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryTopTenFloatHolders: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpTopTenFloatHoldersDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryTopTenFloatHolders", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryIndustry(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryIndustry: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpIndustryDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryIndustry", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryConception(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryConception: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpConceptionDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryConception", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryRegion(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryRegion: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRegionDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryRegion", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryIndexDescription(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryIndexDescription: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpIndexDescriptionDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryIndexDescription", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryIndustryConstituents(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryIndustryConstituents: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpIndustryConstituentsDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryIndustryConstituents", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryConceptionConstituents(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryConceptionConstituents: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpConceptionConstituentsDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryConceptionConstituents", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryRegionConstituents(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryRegionConstituents: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRegionConstituentsDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryRegionConstituents", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryIndustryCodeList(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryIndustryCodeList: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpIndustryIndexDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryIndustryCodeList", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryConceptionCodeList(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryConceptionCodeList: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpConceptionIndexDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryConceptionCodeList", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryRegionCodeList(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryRegionCodeList: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpRegionCodeListDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryRegionCodeList", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryFreeFloatShares(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryFreeFloatShares: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpFreeFloatSharesDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryFreeFloatShares", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryQueueingOrders(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryQueueingOrders: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpQueueingOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryQueueingOrders", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryPriceDistribution(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryPriceDistribution: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpPriceDistributionDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryPriceDistribution", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryPriceExtremum(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryPriceExtremum: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "mderagent", "_clazz_": "CTORATstpPriceExtremumDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "mderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryPriceExtremum", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

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

    def SubscribeMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeMarketData(ppSecurityID, ExchageID)

        return result

    def SubscribeMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeMarketData(ppSecurityID, ExchageID)

        return result

    def UnSubscribeMarketData(self, ppSecurityID, ExchageID, details):
        return 0

    def SubscribePHMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribePHMarketData(ppSecurityID, ExchageID)

        return result

    def SubscribePHMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribePHMarketData(ppSecurityID, ExchageID)

        return result

    def UnSubscribePHMarketData(self, ppSecurityID, ExchageID, details):
        return 0

    def SubscribeSpecialMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeSpecialMarketData(ppSecurityID, ExchageID)

        return result

    def SubscribeSpecialMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeSpecialMarketData(ppSecurityID, ExchageID)

        return result

    def UnSubscribeSpecialMarketData(self, ppSecurityID, ExchageID, details):
        return 0

    def ReqInquiryMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryPHMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryPHMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryPHMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryPHMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquirySpecialMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquirySpecialMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquirySpecialMarketDataMirror(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquirySpecialMarketDataMirror(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def SubscribeRapidMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeRapidMarketData(ppSecurityID, ExchageID)

        return result

    def SubscribeRapidMarketData(self, ppSecurityID, ExchageID, details):
        result = self.api.SubscribeRapidMarketData(ppSecurityID, ExchageID)

        return result

    def UnSubscribeRapidMarketData(self, ppSecurityID, ExchageID, details):
        return 0

    def SubscribeFundsFlowMarketData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeFundsFlowMarketData(ppInstrumentID, nCount, ExchageID)

        return result

    def SubscribeFundsFlowMarketData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeFundsFlowMarketData(ppInstrumentID, nCount, ExchageID)

        return result

    def UnSubscribeFundsFlowMarketData(self, ppInstrumentID, nCount, ExchageID, details):
        return 0

    def SubscribeIndustryIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeIndustryIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def SubscribeIndustryIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeIndustryIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def UnSubscribeIndustryIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        return 0

    def SubscribeConceptionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeConceptionIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def SubscribeConceptionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeConceptionIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def UnSubscribeConceptionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        return 0

    def SubscribeRegionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeRegionIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def SubscribeRegionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        result = self.api.SubscribeRegionIndexData(ppInstrumentID, nCount, ExchageID)

        return result

    def UnSubscribeRegionIndexData(self, ppInstrumentID, nCount, ExchageID, details):
        return 0

    def SubscribeEffectOrderDetail(self, ExchangeID, SecurityID, Ratio, details):
        result = self.api.SubscribeEffectOrderDetail(ExchangeID, SecurityID, Ratio)

        return result

    def SubscribeEffectOrderDetail(self, ExchangeID, SecurityID, Ratio, details):
        result = self.api.SubscribeEffectOrderDetail(ExchangeID, SecurityID, Ratio)

        return result

    def UnSubscribeEffectOrderDetail(self, ExchangeID, SecurityID, details):
        return 0

    def SubscribeEffectTradeDetail(self, ExchangeID, SecurityID, Ratio, details):
        result = self.api.SubscribeEffectTradeDetail(ExchangeID, SecurityID, Ratio)

        return result

    def SubscribeEffectTradeDetail(self, ExchangeID, SecurityID, Ratio, details):
        result = self.api.SubscribeEffectTradeDetail(ExchangeID, SecurityID, Ratio)

        return result

    def UnSubscribeEffectTradeDetail(self, ExchangeID, SecurityID, details):
        return 0

    def ReqQryRightsAdjustmentInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRightsAdjustmentInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRightsAdjustmentInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRightsAdjustmentInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryHistoryFundsFlowInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryHistoryFundsFlowInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryHistoryFundsFlowInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryHistoryFundsFlowInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryFinancialIndicatorInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryFinancialIndicatorInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryFinancialIndicatorInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryFinancialIndicatorInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryDividendInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryDividendInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryDividendInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryDividendInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRightIssueInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRightIssueInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRightIssueInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRightIssueInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryCompanyDescriptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryCompanyDescriptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryCompanyDescriptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryCompanyDescriptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySalesSegmentInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySalesSegmentInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySalesSegmentInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySalesSegmentInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryEquityStructureInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryEquityStructureInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryEquityStructureInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryEquityStructureInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTopTenHoldersInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTopTenHoldersInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTopTenHoldersInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTopTenHoldersInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTopTenFloatHoldersInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTopTenFloatHoldersInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTopTenFloatHoldersInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTopTenFloatHoldersInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndexDescriptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndexDescriptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndexDescriptionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndexDescriptionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionConstituentsInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionConstituentsInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIndustryCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIndustryCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConceptionCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConceptionCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRegionCodeList(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRegionCodeList(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryFreeFloatSharesInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryFreeFloatSharesInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryFreeFloatSharesInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryFreeFloatSharesInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryQueueingOrders(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryQueueingOrders(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryQueueingOrders(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryQueueingOrders(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPriceDistributionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPriceDistributionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPriceDistributionInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPriceDistributionInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPriceExtremumInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPriceExtremumInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPriceExtremumInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPriceExtremumInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

class EasyMderUtils():
    mder_settings = {}

    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.mder_settings = rapidjson.load(cf)

    @classmethod
    def get_settings(cls, node_id="tora"):
        return cls.mder_settings.get(node_id)
