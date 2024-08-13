# -*- coding: UTF-8 -*-
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

    async def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubPHMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubPHMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubSpecialMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubSpecialMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryMarketDataMirror(self, pMarketDataField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquiryPHMarketDataMirror(self, pPHMarketDataField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspInquirySpecialMarketDataMirror(self, pMarketDataField, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubRapidMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubRapidMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubFundsFlowMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubFundsFlowMarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubIndustryIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubIndustryIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubConceptionIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubConceptionIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubRegionIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubRegionIndexData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubEffectOrderDetail(self, pEffectDetailItem, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubEffectOrderDetail(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspSubEffectTradeDetail(self, pEffectDetailItem, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRspUnSubEffectTradeDetail(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        return None

    async def OnRtnDepthMarketData(self, pDepthMarketData):
        return None

    async def OnRtnPHMarketData(self, pPHMarketData):
        return None

    async def OnRtnSpecialMarketData(self, pSpecialMarketData):
        return None

    async def OnRtnRapidMarketData(self, pRapidMarketData):
        return None

    async def OnRtnFundsFlowMarketData(self, pFundsFlowMarketData):
        return None

    async def OnRtnEffectPriceMarketData(self, pEffectPriceMarketData):
        return None

    async def OnRtnEffectVolumeMarketData(self, pEffectVolumeMarketData):
        return None

    async def OnRtnEffectOrderDetail(self, pEffectOrderDetail):
        return None

    async def OnRtnEffectTradeDetail(self, pEffectTradeDetail):
        return None

    async def OnRtnIndustryIndexData(self, pIndustryIndexData):
        return None

    async def OnRtnConceptionIndexData(self, pConceptionIndexData):
        return None

    async def OnRtnRegionIndexData(self, pRegionIndexData):
        return None

    async def OnRspInquiryRightsAdjustment(self, pRightsAdjustmentData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryHistoryFundsFlow(self, pHistoryFundsFlowData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryFinancialIndicator(self, pFinancialIndicatorData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryDividend(self, pDividendData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryRightIssue(self, pRightIssueData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryCompanyDescription(self, pCompanyDescriptionData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquirySalesSegment(self, pSalesSegmentData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryEquityStructure(self, pEquityStructureData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryTopTenHolders(self, pTopTenHoldersData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryTopTenFloatHolders(self, pTopTenFloatHoldersData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryIndustry(self, pIndustryData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryConception(self, pConceptionData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryRegion(self, pRegionData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryIndexDescription(self, pIndexDescriptionData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryIndustryConstituents(self, pIndustryConstituentsData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryConceptionConstituents(self, pConceptionConstituentsData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryRegionConstituents(self, pRegionConstituentsData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryIndustryCodeList(self, pIndustryIndexData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryConceptionCodeList(self, pConceptionIndexData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryRegionCodeList(self, pRegionCodeListData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryFreeFloatShares(self, pFreeFloatSharesData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryQueueingOrders(self, pQueueingOrder, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryPriceDistribution(self, pPriceDistributionData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

    async def OnRspInquiryPriceExtremum(self, pPriceExtremumData, pRspInfo, nRequestID, bIsPageLast, bIsTotalLast):
        return None

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

    async def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUserLogin".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqUserLogin", pReqUserLoginField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUserLogin: [result={}]".format(self.mder_id, result))
        return result

    async def ReqUserLogout(self, pUserLogout, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqUserLogout".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqUserLogout", pUserLogout, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqUserLogout: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeMarketData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeMarketData", ppSecurityID, ExchageID, options=CallOptions())

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnDepthMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnDepthMarketData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnDepthMarketData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeMarketData".format(self.mder_id))
        result = 0

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnarketData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnarketData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribePHMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribePHMarketData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribePHMarketData", ppSecurityID, ExchageID, options=CallOptions())

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnPHMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnPHMarketData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnPHMarketData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribePHMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribePHMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribePHMarketData".format(self.mder_id))
        result = 0

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnHMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnHMarketData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnHMarketData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribePHMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeSpecialMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeSpecialMarketData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeSpecialMarketData", ppSecurityID, ExchageID, options=CallOptions())

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnSpecialMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnSpecialMarketData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnSpecialMarketData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeSpecialMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeSpecialMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeSpecialMarketData".format(self.mder_id))
        result = 0

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnpecialMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnpecialMarketData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnpecialMarketData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeSpecialMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def ReqInquiryMarketDataMirror(self, pInquiryMarketDataField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryMarketDataMirror".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqInquiryMarketDataMirror", pInquiryMarketDataField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryMarketDataMirror: [result={}]".format(self.mder_id, result))
        return result

    async def ReqInquiryPHMarketDataMirror(self, pInquiryMarketDataField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquiryPHMarketDataMirror".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqInquiryPHMarketDataMirror", pInquiryMarketDataField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquiryPHMarketDataMirror: [result={}]".format(self.mder_id, result))
        return result

    async def ReqInquirySpecialMarketDataMirror(self, pInquirySpecialMarketDataField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqInquirySpecialMarketDataMirror".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqInquirySpecialMarketDataMirror", pInquirySpecialMarketDataField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqInquirySpecialMarketDataMirror: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeRapidMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeRapidMarketData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeRapidMarketData", ppSecurityID, ExchageID, options=CallOptions())

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRapidMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRapidMarketData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRapidMarketData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeRapidMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeRapidMarketData(self, ppSecurityID, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeRapidMarketData".format(self.mder_id))
        result = 0

        if ppSecurityID and not (len(ppSecurityID) == 1 and (ppSecurityID[0] == b"000000" or ppSecurityID[0] == b"00000000")):
            for security_id in ppSecurityID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnapidMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnapidMarketData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnapidMarketData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeRapidMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeFundsFlowMarketData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeFundsFlowMarketData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeFundsFlowMarketData", ppInstrumentID, nCount, ExchageID, options=CallOptions())

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnFundsFlowMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnFundsFlowMarketData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnFundsFlowMarketData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeFundsFlowMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeFundsFlowMarketData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeFundsFlowMarketData".format(self.mder_id))
        result = 0

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnundsFlowMarketData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnundsFlowMarketData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnundsFlowMarketData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeFundsFlowMarketData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeIndustryIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeIndustryIndexData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeIndustryIndexData", ppInstrumentID, nCount, ExchageID, options=CallOptions())

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnIndustryIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnIndustryIndexData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnIndustryIndexData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeIndustryIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeIndustryIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeIndustryIndexData".format(self.mder_id))
        result = 0

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnndustryIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnndustryIndexData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnndustryIndexData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeIndustryIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeConceptionIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeConceptionIndexData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeConceptionIndexData", ppInstrumentID, nCount, ExchageID, options=CallOptions())

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnConceptionIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnConceptionIndexData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnConceptionIndexData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeConceptionIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeConceptionIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeConceptionIndexData".format(self.mder_id))
        result = 0

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnonceptionIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnonceptionIndexData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnonceptionIndexData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeConceptionIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeRegionIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call SubscribeRegionIndexData".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeRegionIndexData", ppInstrumentID, nCount, ExchageID, options=CallOptions())

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRegionIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRegionIndexData", options=SubscribeOptions(match="prefix"))
            else:
                await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnRegionIndexData." + ExchageID, options=SubscribeOptions(match="prefix"))

        LoggerUtils.debug("agent[{}] call SubscribeRegionIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeRegionIndexData(self, ppInstrumentID, nCount, ExchageID):
        LoggerUtils.debug("agent[{}] call UnSubscribeRegionIndexData".format(self.mder_id))
        result = 0

        if ppInstrumentID and not (len(ppInstrumentID) == 1 and (ppInstrumentID[0] == b"000000" or ppInstrumentID[0] == b"00000000")):
            for security_id in ppInstrumentID:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnegionIndexData." + ExchageID + "." + str(security_id, encoding="UTF-8"))
        else:
            if ExchageID == "0":
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnegionIndexData")
            else:
                await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnegionIndexData." + ExchageID)

        LoggerUtils.debug("agent[{}] call UnSubscribeRegionIndexData: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeEffectOrderDetail(self, ExchangeID, SecurityID, Ratio):
        LoggerUtils.debug("agent[{}] call SubscribeEffectOrderDetail".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeEffectOrderDetail", ExchangeID, SecurityID, Ratio, options=CallOptions())

        await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnEffectOrderDetail." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{}] call SubscribeEffectOrderDetail: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeEffectOrderDetail(self, ExchangeID, SecurityID):
        LoggerUtils.debug("agent[{}] call UnSubscribeEffectOrderDetail".format(self.mder_id))
        result = 0

        await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnffectOrderDetail." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{}] call UnSubscribeEffectOrderDetail: [result={}]".format(self.mder_id, result))
        return result

    async def SubscribeEffectTradeDetail(self, ExchangeID, SecurityID, Ratio):
        LoggerUtils.debug("agent[{}] call SubscribeEffectTradeDetail".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "SubscribeEffectTradeDetail", ExchangeID, SecurityID, Ratio, options=CallOptions())

        await self.app.subscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnEffectTradeDetail." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{}] call SubscribeEffectTradeDetail: [result={}]".format(self.mder_id, result))
        return result

    async def UnSubscribeEffectTradeDetail(self, ExchangeID, SecurityID):
        LoggerUtils.debug("agent[{}] call UnSubscribeEffectTradeDetail".format(self.mder_id))
        result = 0

        await self.app.unsubscribe(self.dispatch_return, self.node_id + "_mder.RTN.OnRtnffectTradeDetail." + ExchangeID + "." + SecurityID)

        LoggerUtils.debug("agent[{}] call UnSubscribeEffectTradeDetail: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryRightsAdjustmentInfo(self, pQryRightsAdjustmentField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRightsAdjustmentInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryRightsAdjustmentInfo", pQryRightsAdjustmentField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRightsAdjustmentInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryHistoryFundsFlowInfo(self, pQryHistoryFundsFlowField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryHistoryFundsFlowInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryHistoryFundsFlowInfo", pQryHistoryFundsFlowField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryHistoryFundsFlowInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryFinancialIndicatorInfo(self, pQryFinancialIndicatorField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryFinancialIndicatorInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryFinancialIndicatorInfo", pQryFinancialIndicatorField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryFinancialIndicatorInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryDividendInfo(self, pQryDividendInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryDividendInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryDividendInfo", pQryDividendInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryDividendInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryRightIssueInfo(self, pQryRightIssueInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRightIssueInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryRightIssueInfo", pQryRightIssueInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRightIssueInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryCompanyDescriptionInfo(self, pQryCompanyDescriptionInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryCompanyDescriptionInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryCompanyDescriptionInfo", pQryCompanyDescriptionInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryCompanyDescriptionInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQrySalesSegmentInfo(self, pQrySalesSegmentInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQrySalesSegmentInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQrySalesSegmentInfo", pQrySalesSegmentInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQrySalesSegmentInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryEquityStructureInfo(self, pQryEquityStructureInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryEquityStructureInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryEquityStructureInfo", pQryEquityStructureInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryEquityStructureInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryTopTenHoldersInfo(self, pQryTopTenHoldersInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTopTenHoldersInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryTopTenHoldersInfo", pQryTopTenHoldersInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTopTenHoldersInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryTopTenFloatHoldersInfo(self, pQryTopTenFloatHoldersInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryTopTenFloatHoldersInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryTopTenFloatHoldersInfo", pQryTopTenFloatHoldersInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryTopTenFloatHoldersInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryIndustryInfo(self, pQryIndustryInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIndustryInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryIndustryInfo", pQryIndustryInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIndustryInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryConceptionInfo(self, pQryConceptionInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryConceptionInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryConceptionInfo", pQryConceptionInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryConceptionInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryRegionInfo(self, pQryRegionInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRegionInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryRegionInfo", pQryRegionInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRegionInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryIndexDescriptionInfo(self, pQryIndexDescriptionInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIndexDescriptionInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryIndexDescriptionInfo", pQryIndexDescriptionInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIndexDescriptionInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryIndustryConstituentsInfo(self, pQryIndustryConstituentsInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIndustryConstituentsInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryIndustryConstituentsInfo", pQryIndustryConstituentsInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIndustryConstituentsInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryConceptionConstituentsInfo(self, pQryConceptionConstituentsInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryConceptionConstituentsInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryConceptionConstituentsInfo", pQryConceptionConstituentsInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryConceptionConstituentsInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryRegionConstituentsInfo(self, pQryRegionConstituentsInfoField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRegionConstituentsInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryRegionConstituentsInfo", pQryRegionConstituentsInfoField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRegionConstituentsInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryIndustryCodeList(self, pQryIndustryCodeListField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryIndustryCodeList".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryIndustryCodeList", pQryIndustryCodeListField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryIndustryCodeList: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryConceptionCodeList(self, pQryConceptionCodeListField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryConceptionCodeList".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryConceptionCodeList", pQryConceptionCodeListField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryConceptionCodeList: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryRegionCodeList(self, pQryRegionCodeListField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryRegionCodeList".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryRegionCodeList", pQryRegionCodeListField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryRegionCodeList: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryFreeFloatSharesInfo(self, pQryFreeFloatSharesField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryFreeFloatSharesInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryFreeFloatSharesInfo", pQryFreeFloatSharesField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryFreeFloatSharesInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryQueueingOrders(self, pInquiryQueueingOrdersField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryQueueingOrders".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryQueueingOrders", pInquiryQueueingOrdersField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryQueueingOrders: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryPriceDistributionInfo(self, pQryPriceDistributionField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPriceDistributionInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryPriceDistributionInfo", pQryPriceDistributionField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPriceDistributionInfo: [result={}]".format(self.mder_id, result))
        return result

    async def ReqQryPriceExtremumInfo(self, pQryPriceExtremumField, nRequestID):
        LoggerUtils.debug("agent[{}] call ReqQryPriceExtremumInfo".format(self.mder_id))
        result = await self.app.call(self.node_id + "_mder.REQ", "ReqQryPriceExtremumInfo", pQryPriceExtremumField, nRequestID, options=CallOptions())
        LoggerUtils.debug("agent[{}] call ReqQryPriceExtremumInfo: [result={}]".format(self.mder_id, result))
        return result

component = EasyServiceUtils.create_component(session_factory=EasyAgentMainSession)
def get_components():
    return [component]
