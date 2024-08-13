# -*- coding: UTF-8 -*-
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

    async def OnRspUserLogin(self, pRspUserLoginField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUserLogout(self, pUserLogoutField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUserPasswordUpdate(self, pUserPasswordUpdateField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInputDeviceSerial(self, pRspInputDeviceSerialField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspOrderInsert(self, pInputOrderField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnOrder(self, pOrder):
        return None

    async def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        return None

    async def OnRspOrderAction(self, pInputOrderActionField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        return None

    async def OnRtnTrade(self, pTrade):
        return None

    async def OnRtnMarketStatus(self, pMarketStatus):
        return None

    async def OnRspCondOrderInsert(self, pInputCondOrderField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnCondOrder(self, pConditionOrder):
        return None

    async def OnErrRtnCondOrderInsert(self, pInputCondOrder, pRspInfo):
        return None

    async def OnRspCondOrderAction(self, pInputCondOrderActionField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnErrRtnCondOrderAction(self, pInputCondOrderAction, pRspInfo):
        return None

    async def OnRspInputNodeFundAssignment(self, pInputNodeFundAssignmentField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryNodeFundAssignment(self, pRspInquiryNodeFundAssignmentField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryJZFund(self, pRspInquiryJZFundField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspTransferFund(self, pInputTransferFundField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspTransferPosition(self, pInputTransferPositionField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnTransferFund(self, pTransferFund):
        return None

    async def OnErrRtnTransferFund(self, pInputTransferFund, pRspInfo):
        return None

    async def OnRtnTransferPosition(self, pTransferPosition):
        return None

    async def OnErrRtnTransferPosition(self, pInputTransferPosition, pRspInfo):
        return None

    async def OnRspTransferCollateral(self, pInputTransferCollateralField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryBankAccountFund(self, pRspInquiryBankAccountFundField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspModifyOpenPosCost(self, pReqModifyOpenPosCostField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryTradeConcentration(self, pInquiryTradeConcentrationField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnTradingNotice(self, pTradingNotice):
        return None

    async def OnRspInquiryMaxOrderVolume(self, pRspInquiryMaxOrderVolumeField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnPeripheryTransferPosition(self, pRtnPeripheryTransferPosition):
        return None

    async def OnRtnPeripheryTransferFund(self, pRtnPeripheryTransferFund):
        return None

    async def OnRspInquiryHistoryOrder(self, pHistoryOrderField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        return None

    async def OnRspInquiryHistoryTrade(self, pHistoryTradeField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        return None

    async def OnRspInputRemarkEvent(self, pRspInputRemarkEventField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUpdateRemarkEvent(self, pRspUpdateRemarkEventField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspDeleteRemarkEvent(self, pRspDeleteRemarkEventField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryHistoryRemarkEvent(self, pRemarkEventField, pRspInfo, nRequestID, bIsPageEnd, bIsTotalEnd):
        return None

    async def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryMarketData(self, pMarketData, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQrySecurity(self, pSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryETFFile(self, pETFFile, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryETFBasket(self, pETFBasket, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryIPOInfo(self, pIPOInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryBUProxy(self, pBUProxy, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryUser(self, pUser, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryShareholderAccount(self, pShareholderAccount, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryOrderAction(self, pOrderAction, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPosition(self, pPosition, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryTradingFee(self, pTradingFee, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryInvestorTradingFee(self, pInvestorTradingFee, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryIPOQuota(self, pIPOQuota, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryMarket(self, pMarket, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryOrderFundDetail(self, pOrderFundDetail, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryFundTransferDetail(self, pFundTransferDetail, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPositionTransferDetail(self, pPositionTransferDetail, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPledgePosition(self, pPledgePosition, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPledgeInfo(self, pPledgeInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryConversionBondInfo(self, pConversionBondInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryBondPutbackInfo(self, pBondPutbackInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryStandardBondPosition(self, pStandardBondPosition, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPrematurityRepoOrder(self, pPrematurityRepoOrder, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryShareholderParam(self, pShareholderParam, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPeripheryPositionTransferDetail(self, pPeripheryPositionTransferDetail, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryInvestorCondOrderLimitParam(self, pInvestorCondOrderLimitParam, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryCondOrder(self, pCondOrder, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryCondOrderAction(self, pCondOrderAction, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryIPONumberResult(self, pIPONumberResult, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryIPOMatchNumberResult(self, pIPOMatchNumberResult, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQrySZSEImcParams(self, pSZSEImcParams, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQrySZSEImcExchangeRate(self, pSZSEImcExchangeRate, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQrySZSEHKPriceTickInfo(self, pSZSEHKPriceTickInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryShareholderSpecPrivilege(self, pShareholderSpecPrivilege, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryInvestorPositionLimit(self, pInvestorPositionLimit, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPHMarketData(self, pPHMarketData, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryRationalInfo(self, pRationalInfo, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQryPeripheryFundTransferDetail(self, pPeripheryFundTransferDetail, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspQrySystemNodeInfo(self, pSystemNodeInfo, pRspInfo, nRequestID, bIsLast):
        return None

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

    async def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUserLogin".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqUserLogin", pReqUserLoginField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUserLogin: [result={}]".format(self.trader_id, result))
        return result

    async def ReqUserLogout(self, pUserLogoutField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUserLogout".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqUserLogout", pUserLogoutField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUserLogout: [result={}]".format(self.trader_id, result))
        return result

    async def ReqUserPasswordUpdate(self, pUserPasswordUpdateField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUserPasswordUpdate".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqUserPasswordUpdate", pUserPasswordUpdateField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUserPasswordUpdate: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInputDeviceSerial(self, pReqInputDeviceSerialField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInputDeviceSerial".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInputDeviceSerial", pReqInputDeviceSerialField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInputDeviceSerial: [result={}]".format(self.trader_id, result))
        return result

    async def ReqOrderInsert(self, pInputOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqOrderInsert".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqOrderInsert", pInputOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqOrderInsert: [result={}]".format(self.trader_id, result))
        return result

    async def ReqOrderAction(self, pInputOrderActionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqOrderAction".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqOrderAction", pInputOrderActionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqOrderAction: [result={}]".format(self.trader_id, result))
        return result

    async def ReqCondOrderInsert(self, pInputCondOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqCondOrderInsert".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqCondOrderInsert", pInputCondOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqCondOrderInsert: [result={}]".format(self.trader_id, result))
        return result

    async def ReqCondOrderAction(self, pInputCondOrderActionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqCondOrderAction".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqCondOrderAction", pInputCondOrderActionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqCondOrderAction: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInputNodeFundAssignment(self, pInputNodeFundAssignmentField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInputNodeFundAssignment".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInputNodeFundAssignment", pInputNodeFundAssignmentField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInputNodeFundAssignment: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryNodeFundAssignment(self, pReqInquiryNodeFundAssignmentField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryNodeFundAssignment".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryNodeFundAssignment", pReqInquiryNodeFundAssignmentField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryNodeFundAssignment: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryJZFund(self, pReqInquiryJZFundField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryJZFund".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryJZFund", pReqInquiryJZFundField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryJZFund: [result={}]".format(self.trader_id, result))
        return result

    async def ReqTransferFund(self, pInputTransferFundField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqTransferFund".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqTransferFund", pInputTransferFundField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqTransferFund: [result={}]".format(self.trader_id, result))
        return result

    async def ReqTransferPosition(self, pInputTransferPositionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqTransferPosition".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqTransferPosition", pInputTransferPositionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqTransferPosition: [result={}]".format(self.trader_id, result))
        return result

    async def ReqTransferCollateral(self, pInputTransferCollateralField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqTransferCollateral".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqTransferCollateral", pInputTransferCollateralField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqTransferCollateral: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryBankAccountFund(self, pReqInquiryBankAccountFundField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryBankAccountFund".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryBankAccountFund", pReqInquiryBankAccountFundField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryBankAccountFund: [result={}]".format(self.trader_id, result))
        return result

    async def ReqModifyOpenPosCost(self, pReqModifyOpenPosCostField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqModifyOpenPosCost".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqModifyOpenPosCost", pReqModifyOpenPosCostField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqModifyOpenPosCost: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryTradeConcentration(self, pInquiryTradeConcentrationField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryTradeConcentration".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryTradeConcentration", pInquiryTradeConcentrationField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryTradeConcentration: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryMaxOrderVolume(self, pReqInquiryMaxOrderVolumeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryMaxOrderVolume".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryMaxOrderVolume", pReqInquiryMaxOrderVolumeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryMaxOrderVolume: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryHistoryOrder(self, pQryHistoryOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryOrder".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryHistoryOrder", pQryHistoryOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryOrder: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryHistoryTrade(self, pQryHistoryTradeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryTrade".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryHistoryTrade", pQryHistoryTradeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryTrade: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInputRemarkEvent(self, pInputRemarkEventField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInputRemarkEvent".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInputRemarkEvent", pInputRemarkEventField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInputRemarkEvent: [result={}]".format(self.trader_id, result))
        return result

    async def ReqUpdateRemarkEvent(self, pUpdateRemarkEventField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUpdateRemarkEvent".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqUpdateRemarkEvent", pUpdateRemarkEventField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUpdateRemarkEvent: [result={}]".format(self.trader_id, result))
        return result

    async def ReqDeleteRemarkEvent(self, pDeleteRemarkEventField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqDeleteRemarkEvent".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqDeleteRemarkEvent", pDeleteRemarkEventField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqDeleteRemarkEvent: [result={}]".format(self.trader_id, result))
        return result

    async def ReqInquiryHistoryRemarkEvent(self, pQryRemarkEventField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryRemarkEvent".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqInquiryHistoryRemarkEvent", pQryRemarkEventField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryHistoryRemarkEvent: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryExchange(self, pQryExchangeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryExchange".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryExchange", pQryExchangeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryExchange: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryMarketData(self, pQryMarketDataField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryMarketData".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryMarketData", pQryMarketDataField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryMarketData: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQrySecurity(self, pQrySecurityField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySecurity".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQrySecurity", pQrySecurityField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySecurity: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryETFFile(self, pQryETFFileField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryETFFile".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryETFFile", pQryETFFileField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryETFFile: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryETFBasket(self, pQryETFBasketField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryETFBasket".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryETFBasket", pQryETFBasketField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryETFBasket: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryIPOInfo(self, pQryIPOInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIPOInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryIPOInfo", pQryIPOInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIPOInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryBUProxy(self, pQryBUProxyField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryBUProxy".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryBUProxy", pQryBUProxyField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryBUProxy: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryUser(self, pQryUserField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryUser".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryUser", pQryUserField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryUser: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryInvestor(self, pQryInvestorField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryInvestor".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryInvestor", pQryInvestorField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryInvestor: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryShareholderAccount(self, pQryShareholderAccountField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryShareholderAccount".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryShareholderAccount", pQryShareholderAccountField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryShareholderAccount: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryOrder(self, pQryOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryOrder".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryOrder", pQryOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryOrder: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryOrderAction(self, pQryOrderActionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryOrderAction".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryOrderAction", pQryOrderActionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryOrderAction: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryTrade(self, pQryTradeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTrade".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryTrade", pQryTradeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTrade: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryTradingAccount(self, pQryTradingAccountField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTradingAccount".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryTradingAccount", pQryTradingAccountField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTradingAccount: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPosition(self, pQryPositionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPosition".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPosition", pQryPositionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPosition: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryTradingFee(self, pQryTradingFeeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTradingFee".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryTradingFee", pQryTradingFeeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTradingFee: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryInvestorTradingFee(self, pQryInvestorTradingFeeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryInvestorTradingFee".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryInvestorTradingFee", pQryInvestorTradingFeeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryInvestorTradingFee: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryIPOQuota(self, pQryIPOQuotaField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIPOQuota".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryIPOQuota", pQryIPOQuotaField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIPOQuota: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryMarket(self, pQryMarketField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryMarket".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryMarket", pQryMarketField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryMarket: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryOrderFundDetail(self, pQryOrderFundDetailField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryOrderFundDetail".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryOrderFundDetail", pQryOrderFundDetailField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryOrderFundDetail: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryFundTransferDetail(self, pQryFundTransferDetailField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryFundTransferDetail".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryFundTransferDetail", pQryFundTransferDetailField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryFundTransferDetail: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPositionTransferDetail(self, pQryPositionTransferDetailField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPositionTransferDetail".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPositionTransferDetail", pQryPositionTransferDetailField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPositionTransferDetail: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPledgePosition(self, pQryPledgePositionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPledgePosition".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPledgePosition", pQryPledgePositionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPledgePosition: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPledgeInfo(self, pQryPledgeInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPledgeInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPledgeInfo", pQryPledgeInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPledgeInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryConversionBondInfo(self, pQryConversionBondInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryConversionBondInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryConversionBondInfo", pQryConversionBondInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryConversionBondInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryBondPutbackInfo(self, pQryBondPutbackInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryBondPutbackInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryBondPutbackInfo", pQryBondPutbackInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryBondPutbackInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryStandardBondPosition(self, pQryStandardBondPositionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryStandardBondPosition".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryStandardBondPosition", pQryStandardBondPositionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryStandardBondPosition: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPrematurityRepoOrder(self, pQryPrematurityRepoOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPrematurityRepoOrder".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPrematurityRepoOrder", pQryPrematurityRepoOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPrematurityRepoOrder: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryShareholderParam(self, pQryShareholderParamField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryShareholderParam".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryShareholderParam", pQryShareholderParamField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryShareholderParam: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPeripheryPositionTransferDetail(self, pQryPeripheryPositionTransferDetailField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPeripheryPositionTransferDetail".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPeripheryPositionTransferDetail", pQryPeripheryPositionTransferDetailField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPeripheryPositionTransferDetail: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryInvestorCondOrderLimitParam(self, pQryInvestorCondOrderLimitParamField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryInvestorCondOrderLimitParam".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryInvestorCondOrderLimitParam", pQryInvestorCondOrderLimitParamField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryInvestorCondOrderLimitParam: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryCondOrder(self, pQryCondOrderField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryCondOrder".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryCondOrder", pQryCondOrderField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryCondOrder: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryCondOrderAction(self, pQryCondOrderActionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryCondOrderAction".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryCondOrderAction", pQryCondOrderActionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryCondOrderAction: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryTradingNotice(self, pQryTradingNoticeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTradingNotice".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryTradingNotice", pQryTradingNoticeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTradingNotice: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryIPONumberResult(self, pQryIPONumberResultField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIPONumberResult".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryIPONumberResult", pQryIPONumberResultField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIPONumberResult: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryIPOMatchNumberResult(self, pQryIPOMatchNumberResultField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIPOMatchNumberResult".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryIPOMatchNumberResult", pQryIPOMatchNumberResultField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIPOMatchNumberResult: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQrySZSEImcParams(self, pQrySZSEImcParamsField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySZSEImcParams".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQrySZSEImcParams", pQrySZSEImcParamsField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySZSEImcParams: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQrySZSEImcExchangeRate(self, pQrySZSEImcExchangeRateField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySZSEImcExchangeRate".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQrySZSEImcExchangeRate", pQrySZSEImcExchangeRateField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySZSEImcExchangeRate: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQrySZSEHKPriceTickInfo(self, pQrySZSEHKPriceTickInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySZSEHKPriceTickInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQrySZSEHKPriceTickInfo", pQrySZSEHKPriceTickInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySZSEHKPriceTickInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryShareholderSpecPrivilege(self, pQryShareholderSpecPrivilegeField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryShareholderSpecPrivilege".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryShareholderSpecPrivilege", pQryShareholderSpecPrivilegeField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryShareholderSpecPrivilege: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryInvestorPositionLimit(self, pQryInvestorPositionLimitField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryInvestorPositionLimit".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryInvestorPositionLimit", pQryInvestorPositionLimitField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryInvestorPositionLimit: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPHMarketData(self, pQryPHMarketDataField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPHMarketData".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPHMarketData", pQryPHMarketDataField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPHMarketData: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryRationalInfo(self, pQryRationalInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRationalInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryRationalInfo", pQryRationalInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRationalInfo: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQryPeripheryFundTransferDetail(self, pQryPeripheryFundTransferDetailField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPeripheryFundTransferDetail".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQryPeripheryFundTransferDetail", pQryPeripheryFundTransferDetailField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPeripheryFundTransferDetail: [result={}]".format(self.trader_id, result))
        return result

    async def ReqQrySystemNodeInfo(self, pQrySystemNodeInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySystemNodeInfo".format(self.trader_id))
        result = await self.app.call(self.node_id + "_trader_" + self.trader_id + ".REQ", "ReqQrySystemNodeInfo", pQrySystemNodeInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySystemNodeInfo: [result={}]".format(self.trader_id, result))
        return result

component = EasyServiceUtils.create_component(session_factory=EasyAgentMainSession)
def get_components():
    return [component]
