# -*- coding: UTF-8 -*-
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

    def OnRspUserLogin(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUserLogin: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspUserLoginField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

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
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpUserLogoutField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUserLogout", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUserPasswordUpdate(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUserPasswordUpdate: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpUserPasswordUpdateField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUserPasswordUpdate", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInputDeviceSerial(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInputDeviceSerial: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInputDeviceSerialField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInputDeviceSerial", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspOrderInsert(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspOrderInsert: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspOrderInsert", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnOrder(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnOrder".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpOrderField"})

        self.app.publish(self.rtn_topic_id, "OnRtnOrder", pRtnField)

    def OnErrRtnOrderInsert(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnOrderInsert: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnOrderInsert", pRtnField, pRspInfo)

    def OnRspOrderAction(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspOrderAction: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspOrderAction", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnErrRtnOrderAction(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnOrderAction: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnOrderAction", pRtnField, pRspInfo)

    def OnRtnTrade(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnTrade".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradeField"})

        self.app.publish(self.rtn_topic_id, "OnRtnTrade", pRtnField)

    def OnRtnMarketStatus(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnMarketStatus".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpMarketStatusField"})

        self.app.publish(self.rtn_topic_id, "OnRtnMarketStatus", pRtnField)

    def OnRspCondOrderInsert(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspCondOrderInsert: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputCondOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspCondOrderInsert", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnCondOrder(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnCondOrder".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpConditionOrderField"})

        self.app.publish(self.rtn_topic_id, "OnRtnCondOrder", pRtnField)

    def OnErrRtnCondOrderInsert(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnCondOrderInsert: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputCondOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnCondOrderInsert", pRtnField, pRspInfo)

    def OnRspCondOrderAction(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspCondOrderAction: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputCondOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspCondOrderAction", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnErrRtnCondOrderAction(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnCondOrderAction: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputCondOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnCondOrderAction", pRtnField, pRspInfo)

    def OnRspInputNodeFundAssignment(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInputNodeFundAssignment: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputNodeFundAssignmentField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInputNodeFundAssignment", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryNodeFundAssignment(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryNodeFundAssignment: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInquiryNodeFundAssignmentField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryNodeFundAssignment", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryJZFund(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryJZFund: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInquiryJZFundField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryJZFund", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspTransferFund(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspTransferFund: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputTransferFundField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspTransferFund", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspTransferPosition(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspTransferPosition: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputTransferPositionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspTransferPosition", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnTransferFund(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnTransferFund".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTransferFundField"})

        self.app.publish(self.rtn_topic_id, "OnRtnTransferFund", pRtnField)

    def OnErrRtnTransferFund(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnTransferFund: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputTransferFundField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnTransferFund", pRtnField, pRspInfo)

    def OnRtnTransferPosition(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnTransferPosition".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTransferPositionField"})

        self.app.publish(self.rtn_topic_id, "OnRtnTransferPosition", pRtnField)

    def OnErrRtnTransferPosition(self, pRtnField, pRspInfo):
        LoggerUtils.debug("service[{}] OnErrRtnTransferPosition: [ErrorID={}, ErrorMsg={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"]))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputTransferPositionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        self.app.publish(self.rtn_topic_id, "OnErrRtnTransferPosition", pRtnField, pRspInfo)

    def OnRspTransferCollateral(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspTransferCollateral: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInputTransferCollateralField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspTransferCollateral", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryBankAccountFund(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryBankAccountFund: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInquiryBankAccountFundField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryBankAccountFund", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspModifyOpenPosCost(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspModifyOpenPosCost: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpReqModifyOpenPosCostField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspModifyOpenPosCost", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryTradeConcentration(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryTradeConcentration: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInquiryTradeConcentrationField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryTradeConcentration", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnTradingNotice(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnTradingNotice".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradingNoticeField"})

        self.app.publish(self.rtn_topic_id, "OnRtnTradingNotice", pRtnField)

    def OnRspInquiryMaxOrderVolume(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInquiryMaxOrderVolume: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInquiryMaxOrderVolumeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryMaxOrderVolume", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRtnPeripheryTransferPosition(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnPeripheryTransferPosition".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRtnPeripheryTransferPositionField"})

        self.app.publish(self.rtn_topic_id, "OnRtnPeripheryTransferPosition", pRtnField)

    def OnRtnPeripheryTransferFund(self, pRtnField):
        LoggerUtils.debug("service[{}] OnRtnPeripheryTransferFund".format(self.app.authid))

        if pRtnField:
            pRtnField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRtnPeripheryTransferFundField"})

        self.app.publish(self.rtn_topic_id, "OnRtnPeripheryTransferFund", pRtnField)

    def OnRspInquiryHistoryOrder(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryHistoryOrder: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpHistoryOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryHistoryOrder", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInquiryHistoryTrade(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryHistoryTrade: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpHistoryTradeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryHistoryTrade", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspInputRemarkEvent(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspInputRemarkEvent: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInputRemarkEventField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInputRemarkEvent", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspUpdateRemarkEvent(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspUpdateRemarkEvent: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspUpdateRemarkEventField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspUpdateRemarkEvent", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspDeleteRemarkEvent(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspDeleteRemarkEvent: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspDeleteRemarkEventField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspDeleteRemarkEvent", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspInquiryHistoryRemarkEvent(self, pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        LoggerUtils.debug("service[{}] OnRspInquiryHistoryRemarkEvent: [ErrorID={}, ErrorMsg={}, RequestID={}, bIsPageEnd={}, bIsTotalEnd={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsPageEnd, bIsTotalEnd))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRemarkEventField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})
            
        if bIsTotalEnd:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspInquiryHistoryRemarkEvent", pRspField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd)

    def OnRspQryExchange(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryExchange: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpExchangeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryExchange", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpMarketDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQrySecurity(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQrySecurity: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpSecurityField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQrySecurity", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryETFFile(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryETFFile: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpETFFileField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryETFFile", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryETFBasket(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryETFBasket: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpETFBasketField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryETFBasket", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryIPOInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryIPOInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpIPOInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryIPOInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryBUProxy(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryBUProxy: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpBUProxyField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryBUProxy", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryUser(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryUser: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpUserField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryUser", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryInvestor(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryInvestor: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInvestorField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryInvestor", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryShareholderAccount(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryShareholderAccount: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpShareholderAccountField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryShareholderAccount", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryOrder(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryOrder: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryOrder", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryOrderAction(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryOrderAction: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryOrderAction", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryTrade(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryTrade: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryTrade", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryTradingAccount(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryTradingAccount: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradingAccountField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryTradingAccount", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPosition(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPosition: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPositionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPosition", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryTradingFee(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryTradingFee: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradingFeeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryTradingFee", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryInvestorTradingFee(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryInvestorTradingFee: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInvestorTradingFeeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryInvestorTradingFee", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryIPOQuota(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryIPOQuota: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpIPOQuotaField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryIPOQuota", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryMarket(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryMarket: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpMarketField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryMarket", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryOrderFundDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryOrderFundDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpOrderFundDetailField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryOrderFundDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryFundTransferDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryFundTransferDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpFundTransferDetailField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryFundTransferDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPositionTransferDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPositionTransferDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPositionTransferDetailField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPositionTransferDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPledgePosition(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPledgePosition: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPledgePositionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPledgePosition", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPledgeInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPledgeInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPledgeInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPledgeInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryConversionBondInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryConversionBondInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpConversionBondInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryConversionBondInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryBondPutbackInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryBondPutbackInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpBondPutbackInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryBondPutbackInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryStandardBondPosition(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryStandardBondPosition: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpStandardBondPositionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryStandardBondPosition", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPrematurityRepoOrder(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPrematurityRepoOrder: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPrematurityRepoOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPrematurityRepoOrder", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryShareholderParam(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryShareholderParam: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpShareholderParamField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryShareholderParam", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPeripheryPositionTransferDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPeripheryPositionTransferDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPeripheryPositionTransferDetailField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPeripheryPositionTransferDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryInvestorCondOrderLimitParam(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryInvestorCondOrderLimitParam: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInvestorCondOrderLimitParamField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryInvestorCondOrderLimitParam", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryCondOrder(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryCondOrder: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpCondOrderField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryCondOrder", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryCondOrderAction(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryCondOrderAction: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpCondOrderActionField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryCondOrderAction", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryTradingNotice(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryTradingNotice: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpTradingNoticeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryTradingNotice", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryIPONumberResult(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryIPONumberResult: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpIPONumberResultField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryIPONumberResult", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryIPOMatchNumberResult(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryIPOMatchNumberResult: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpIPOMatchNumberResultField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryIPOMatchNumberResult", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQrySZSEImcParams(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQrySZSEImcParams: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpSZSEImcParamsField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQrySZSEImcParams", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQrySZSEImcExchangeRate(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQrySZSEImcExchangeRate: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpSZSEImcExchangeRateField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQrySZSEImcExchangeRate", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQrySZSEHKPriceTickInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQrySZSEHKPriceTickInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpSZSEHKPriceTickInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQrySZSEHKPriceTickInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryShareholderSpecPrivilege(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryShareholderSpecPrivilege: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpShareholderSpecPrivilegeField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryShareholderSpecPrivilege", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryInvestorPositionLimit(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryInvestorPositionLimit: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpInvestorPositionLimitField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryInvestorPositionLimit", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPHMarketData(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPHMarketData: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPHMarketDataField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPHMarketData", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryRationalInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryRationalInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpRationalInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryRationalInfo", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQryPeripheryFundTransferDetail(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQryPeripheryFundTransferDetail: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpPeripheryFundTransferDetailField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQryPeripheryFundTransferDetail", pRspField, pRspInfo, s_request_id, bIsLast)

    def OnRspQrySystemNodeInfo(self, pRspField, pRspInfo, nRequestID, bIsLast):
        LoggerUtils.debug("service[{}] OnRspQrySystemNodeInfo: [ErrorID={}, ErrorMsg={}, RequestID={}, IsLast={}]".format(self.app.authid, pRspInfo["ErrorID"], pRspInfo["ErrorMsg"], nRequestID, bIsLast))
        s_request_id = nRequestID
        caller_authid = None
        if nRequestID in self.requests:
            req_info = self.requests.get(nRequestID)
            s_request_id = req_info.get("request_id")
            caller_authid = req_info.get("caller")

        if pRspField:
            pRspField.update({"_module_": "traderagent", "_clazz_": "CTORATstpSystemNodeInfoField"})
        if pRspInfo:
            pRspInfo.update({"_module_": "traderagent", "_clazz_": "CTORATstpRspInfoField"})

        if bIsLast:
            self.requests.pop(nRequestID, None)
        self.app.publish(self._gen_rsp_topic_id(caller_authid), "OnRspQrySystemNodeInfo", pRspField, pRspInfo, s_request_id, bIsLast)

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

    def ReqUserLogin(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqUserLogin(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqUserLogout(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqUserLogout(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqUserPasswordUpdate(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqUserPasswordUpdate(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInputDeviceSerial(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInputDeviceSerial(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqOrderInsert(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqOrderInsert(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqOrderAction(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqOrderAction(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqCondOrderInsert(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqCondOrderInsert(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqCondOrderAction(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqCondOrderAction(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInputNodeFundAssignment(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInputNodeFundAssignment(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryNodeFundAssignment(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryNodeFundAssignment(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryJZFund(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryJZFund(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqTransferFund(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqTransferFund(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqTransferPosition(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqTransferPosition(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqTransferCollateral(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqTransferCollateral(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryBankAccountFund(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryBankAccountFund(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqModifyOpenPosCost(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqModifyOpenPosCost(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryTradeConcentration(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryTradeConcentration(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryMaxOrderVolume(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryMaxOrderVolume(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryHistoryOrder(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryHistoryOrder(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryHistoryTrade(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryHistoryTrade(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInputRemarkEvent(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInputRemarkEvent(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqUpdateRemarkEvent(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqUpdateRemarkEvent(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqDeleteRemarkEvent(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqDeleteRemarkEvent(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqInquiryHistoryRemarkEvent(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqInquiryHistoryRemarkEvent(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryExchange(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryExchange(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryMarketData(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryMarketData(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySecurity(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySecurity(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryETFFile(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryETFFile(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryETFBasket(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryETFBasket(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIPOInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIPOInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryBUProxy(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryBUProxy(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryUser(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryUser(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryInvestor(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryInvestor(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryShareholderAccount(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryShareholderAccount(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryOrder(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryOrder(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryOrderAction(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryOrderAction(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTrade(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTrade(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTradingAccount(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTradingAccount(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPosition(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPosition(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTradingFee(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTradingFee(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryInvestorTradingFee(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryInvestorTradingFee(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIPOQuota(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIPOQuota(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryMarket(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryMarket(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryOrderFundDetail(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryOrderFundDetail(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryFundTransferDetail(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryFundTransferDetail(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPositionTransferDetail(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPositionTransferDetail(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPledgePosition(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPledgePosition(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPledgeInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPledgeInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryConversionBondInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryConversionBondInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryBondPutbackInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryBondPutbackInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryStandardBondPosition(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryStandardBondPosition(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPrematurityRepoOrder(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPrematurityRepoOrder(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryShareholderParam(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryShareholderParam(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPeripheryPositionTransferDetail(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPeripheryPositionTransferDetail(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryInvestorCondOrderLimitParam(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryInvestorCondOrderLimitParam(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryCondOrder(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryCondOrder(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryCondOrderAction(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryCondOrderAction(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryTradingNotice(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryTradingNotice(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIPONumberResult(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIPONumberResult(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryIPOMatchNumberResult(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryIPOMatchNumberResult(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySZSEImcParams(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySZSEImcParams(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySZSEImcExchangeRate(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySZSEImcExchangeRate(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySZSEHKPriceTickInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySZSEHKPriceTickInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryShareholderSpecPrivilege(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryShareholderSpecPrivilege(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryInvestorPositionLimit(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryInvestorPositionLimit(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPHMarketData(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPHMarketData(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryRationalInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryRationalInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQryPeripheryFundTransferDetail(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQryPeripheryFundTransferDetail(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

    def ReqQrySystemNodeInfo(self, req_field, request_id, details):
        r_request_id = self.get_request_id()
        result = self.api.ReqQrySystemNodeInfo(req_field, r_request_id)

        if result == 0:
            self.spi.requests.update({r_request_id: {"caller": details.caller_authid, "request_id": request_id}})

        return result

class EasyTraderUtils():
    trader_settings = {}

    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.trader_settings = rapidjson.load(cf)

    @classmethod
    def get_settings(cls, node_id="tora"):
        return cls.trader_settings.get(node_id)
