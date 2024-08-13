# -*- coding: UTF-8 -*-
# cython: language_level=3

class CTORATstpFensUserInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFensUserInfoField"
        self.LogInAccount = ""
        self.LogInAccountType = ""


class CTORATstpReqUserLoginField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqUserLoginField"
        self.LogInAccount = ""
        self.LogInAccountType = ""
        self.Password = ""
        self.UserProductInfo = ""
        self.InterfaceProductInfo = ""
        self.ProtocolInfo = ""
        self.MacAddress = ""
        self.Mobile = ""
        self.InnerIPAddress = ""
        self.Lang = ""
        self.TerminalInfo = ""
        self.GWMacAddress = ""
        self.GWInnerIPAddress = ""
        self.GWOuterIPAddress = ""
        self.DepartmentID = ""
        self.HDSerial = ""
        self.AuthMode = ""
        self.DeviceID = ""
        self.CertSerial = ""
        self.OuterIPAddress = ""
        self.DynamicPassword = ""


class CTORATstpRspUserLoginField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspUserLoginField"
        self.LoginTime = ""
        self.LogInAccount = ""
        self.LogInAccountType = ""
        self.SystemName = ""
        self.FrontID = 0
        self.SessionID = 0
        self.MaxOrderRef = ""
        self.PrivateFlowCount = 0
        self.PublicFlowCount = 0
        self.TradingDay = ""
        self.UserID = ""
        self.UserName = ""
        self.UserType = ""
        self.DepartmentID = ""
        self.InnerIPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.OrderInsertCommFlux = 0
        self.PasswordUpdatePeriod = 0
        self.PasswordRemainDays = 0
        self.NeedUpdatePassword = 0
        self.OrderActionCommFlux = 0
        self.Mobile = ""
        self.OuterIPAddress = ""
        self.CertSerial = ""


class CTORATstpRspInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInfoField"
        self.ErrorID = 0
        self.ErrorMsg = ""


class CTORATstpUserLogoutField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUserLogoutField"
        self.UserID = ""


class CTORATstpForceUserLogoutField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpForceUserLogoutField"
        self.UserID = ""


class CTORATstpUserPasswordUpdateField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUserPasswordUpdateField"
        self.UserID = ""
        self.OldPassword = ""
        self.NewPassword = ""


class CTORATstpReqInputDeviceSerialField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInputDeviceSerialField"
        self.UserID = ""
        self.DeviceID = ""
        self.CertSerial = ""


class CTORATstpRspInputDeviceSerialField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInputDeviceSerialField"
        self.UserID = ""


class CTORATstpActivateUserField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpActivateUserField"
        self.UserID = ""


class CTORATstpVerifyUserPasswordField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpVerifyUserPasswordField"
        self.UserID = ""
        self.Password = ""


class CTORATstpInputOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderRef = ""
        self.UserID = ""
        self.OrderPriceType = ""
        self.Direction = ""
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.MinVolume = 0
        self.ForceCloseReason = ""
        self.RequestID = 0
        self.UserForceClose = 0
        self.IsSwapOrder = 0
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.LotType = ""
        self.OrderSysID = ""
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.TransfereePbuID = ""
        self.Operway = ""
        self.CondCheck = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.GTDate = ""


class CTORATstpOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderRef = ""
        self.UserID = ""
        self.OrderPriceType = ""
        self.Direction = ""
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.MinVolume = 0
        self.ForceCloseReason = ""
        self.RequestID = 0
        self.OrderLocalID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.ExchangeInstID = ""
        self.TraderID = ""
        self.OrderSubmitStatus = ""
        self.TradingDay = ""
        self.OrderSysID = ""
        self.OrderStatus = ""
        self.OrderType = ""
        self.VolumeTraded = 0
        self.VolumeTotal = 0
        self.InsertDate = ""
        self.InsertTime = ""
        self.CancelTime = ""
        self.ActiveTraderID = ""
        self.FrontID = 0
        self.SessionID = 0
        self.UserProductInfo = ""
        self.StatusMsg = ""
        self.UserForceClose = 0
        self.ActiveUserID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.LotType = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.TransfereePbuID = ""
        self.Operway = ""
        self.DepartmentID = ""
        self.ProperCtrlBusinessType = ""
        self.ProperCtrlPassFlag = ""
        self.CondCheck = ""
        self.IsCacheOrder = 0
        self.Turnover = 0.0
        self.RtnFloatInfo = 0.0
        self.RtnIntInfo = 0
        self.HDSerial = ""
        self.Mobile = ""
        self.GTDate = ""


class CTORATstpUserRefField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUserRefField"
        self.UserID = ""


class CTORATstpInputOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputOrderActionField"
        self.InvestorID = ""
        self.OrderActionRef = ""
        self.OrderRef = ""
        self.RequestID = 0
        self.FrontID = 0
        self.SessionID = 0
        self.ExchangeID = ""
        self.OrderSysID = ""
        self.ActionFlag = ""
        self.Price = 0.0
        self.Volume = 0
        self.UserID = ""
        self.SecurityID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.CancelOrderLocalID = ""
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpOrderActionField"
        self.InvestorID = ""
        self.OrderActionRef = ""
        self.OrderRef = ""
        self.RequestID = 0
        self.FrontID = 0
        self.SessionID = 0
        self.ExchangeID = ""
        self.OrderSysID = ""
        self.ActionFlag = ""
        self.Price = 0.0
        self.Volume = 0
        self.ActionDate = ""
        self.ActionTime = ""
        self.TraderID = ""
        self.OrderLocalID = ""
        self.ActionLocalID = ""
        self.ShareholderID = ""
        self.OrderActionStatus = ""
        self.UserID = ""
        self.StatusMsg = ""
        self.SecurityID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.MarketID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""


class CTORATstpTradeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTradeField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.UserID = ""
        self.ExchangeID = ""
        self.TradeID = ""
        self.Direction = ""
        self.OrderSysID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.ExchangeInstID = ""
        self.OffsetFlag = ""
        self.HedgeFlag = ""
        self.Price = 0.0
        self.Volume = 0
        self.TradeDate = ""
        self.TradeTime = ""
        self.TraderID = ""
        self.OrderLocalID = ""
        self.TradingDay = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.OrderRef = ""
        self.DepartmentID = ""


class CTORATstpMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpMarketDataField"
        self.TradingDay = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.SecurityName = ""
        self.PreClosePrice = 0.0
        self.OpenPrice = 0.0
        self.Volume = 0
        self.Turnover = 0.0
        self.TradingCount = 0
        self.LastPrice = 0.0
        self.HighestPrice = 0.0
        self.LowestPrice = 0.0
        self.BidPrice1 = 0.0
        self.AskPrice1 = 0.0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.PERatio1 = 0.0
        self.PERatio2 = 0.0
        self.PriceUpDown1 = 0.0
        self.PriceUpDown2 = 0.0
        self.OpenInterest = 0.0
        self.BidVolume1 = 0
        self.AskVolume1 = 0
        self.BidPrice2 = 0.0
        self.BidVolume2 = 0
        self.AskPrice2 = 0.0
        self.AskVolume2 = 0
        self.BidPrice3 = 0.0
        self.BidVolume3 = 0
        self.AskPrice3 = 0.0
        self.AskVolume3 = 0
        self.BidPrice4 = 0.0
        self.BidVolume4 = 0
        self.AskPrice4 = 0.0
        self.AskVolume4 = 0
        self.BidPrice5 = 0.0
        self.BidVolume5 = 0
        self.AskPrice5 = 0.0
        self.AskVolume5 = 0
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.ClosePrice = 0.0
        self.MDSecurityStat = ""
        self.HWFlag = 0


class CTORATstpPHMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPHMarketDataField"
        self.TradingDay = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.SecurityName = ""
        self.Volume = 0
        self.Turnover = 0.0
        self.ClosePrice = 0.0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.BidVolume = 0
        self.AskVolume = 0
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.MDSecurityStat = ""
        self.HWFlag = 0


class CTORATstpMarketStatusField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpMarketStatusField"
        self.MarketID = ""
        self.MarketStatus = ""


class CTORATstpInputCondOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputCondOrderField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.TriggerOrderVolumeType = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.CondOrderRef = ""
        self.AccountID = ""
        self.UserID = ""
        self.RequestID = 0
        self.IPAddress = ""
        self.MacAddress = ""
        self.CondOrderID = 0
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.CondCheck = ""
        self.ContingentCondition = ""
        self.ConditionPrice = 0.0
        self.PriceTicks = 0
        self.VolumeMultiple = 0
        self.RelativeFrontID = 0
        self.RelativeSessionID = 0
        self.RelativeParam = ""
        self.AppendContingentCondition = ""
        self.AppendConditionPrice = 0.0
        self.AppendRelativeFrontID = 0
        self.AppendRelativeSessionID = 0
        self.AppendRelativeParam = ""
        self.HDSerial = ""
        self.LotType = ""
        self.Mobile = ""
        self.TriggerOrderPriceType = ""
        self.GTDate = ""


class CTORATstpConditionOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConditionOrderField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.TriggerOrderVolumeType = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.CondOrderRef = ""
        self.AccountID = ""
        self.UserID = ""
        self.RequestID = 0
        self.IPAddress = ""
        self.MacAddress = ""
        self.CondOrderID = 0
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.CondCheck = ""
        self.ContingentCondition = ""
        self.ConditionPrice = 0.0
        self.PriceTicks = 0
        self.VolumeMultiple = 0
        self.RelativeFrontID = 0
        self.RelativeSessionID = 0
        self.RelativeParam = ""
        self.AppendContingentCondition = ""
        self.AppendConditionPrice = 0.0
        self.AppendRelativeFrontID = 0
        self.AppendRelativeSessionID = 0
        self.AppendRelativeParam = ""
        self.TradingDay = ""
        self.CondOrderStatus = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.CancelTime = ""
        self.CancelUser = ""
        self.FrontID = 0
        self.SessionID = 0
        self.UserProductInfo = ""
        self.StatusMsg = ""
        self.DepartmentID = ""
        self.ProperCtrlBusinessType = ""
        self.ProperCtrlPassFlag = ""
        self.ActiveDate = ""
        self.ActiveTime = ""
        self.HDSerial = ""
        self.LotType = ""
        self.Mobile = ""
        self.TriggerOrderPriceType = ""
        self.TriggerRelativeParam = ""
        self.AppendCondParam = ""
        self.GTDate = ""


class CTORATstpInputCondOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputCondOrderActionField"
        self.RequestID = 0
        self.ExchangeID = ""
        self.CondOrderActionRef = ""
        self.CondOrderRef = ""
        self.FrontID = 0
        self.SessionID = 0
        self.CondOrderID = 0
        self.ActionFlag = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.UserID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.CancelCondOrderID = 0
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpInputNodeFundAssignmentField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputNodeFundAssignmentField"
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.InvestorID = ""
        self.NodeID1 = 0
        self.AmtRatio1 = 0.0
        self.NodeID2 = 0
        self.AmtRatio2 = 0.0
        self.NodeID3 = 0
        self.AmtRatio3 = 0.0
        self.NodeID4 = 0
        self.AmtRatio4 = 0.0
        self.NodeID5 = 0
        self.AmtRatio5 = 0.0


class CTORATstpReqInquiryNodeFundAssignmentField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInquiryNodeFundAssignmentField"
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.NodeID = 0


class CTORATstpRspInquiryNodeFundAssignmentField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInquiryNodeFundAssignmentField"
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.InvestorID = ""
        self.NodeID1 = 0
        self.AmtRatio1 = 0.0
        self.NodeID2 = 0
        self.AmtRatio2 = 0.0
        self.NodeID3 = 0
        self.AmtRatio3 = 0.0
        self.NodeID4 = 0
        self.AmtRatio4 = 0.0
        self.NodeID5 = 0
        self.AmtRatio5 = 0.0


class CTORATstpReqInquiryJZFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInquiryJZFundField"
        self.AccountID = ""
        self.CurrencyID = ""
        self.DepartmentID = ""


class CTORATstpRspInquiryJZFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInquiryJZFundField"
        self.AccountID = ""
        self.CurrencyID = ""
        self.UsefulMoney = 0.0
        self.FetchLimit = 0.0
        self.DepartmentID = ""


class CTORATstpInputTransferFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputTransferFundField"
        self.AccountID = ""
        self.CurrencyID = ""
        self.ApplySerial = ""
        self.TransferDirection = ""
        self.Amount = 0.0
        self.DepartmentID = ""
        self.BankID = ""
        self.AccountPassword = ""
        self.BankPassword = ""
        self.ExternalDepartmentID = ""
        self.ExternalAccountID = ""
        self.ExternalCurrencyID = ""
        self.ExternalBankID = ""
        self.ExternalAccountPassword = ""
        self.ExternalBankPassword = ""
        self.ExternalTradePassword = ""
        self.ExternalNodeID = 0


class CTORATstpInputTransferPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputTransferPositionField"
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.ApplySerial = ""
        self.TransferDirection = ""
        self.Volume = 0
        self.TransferPositionType = ""
        self.MarketID = ""
        self.ExternalNodeID = 0


class CTORATstpTransferFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTransferFundField"
        self.FundSerial = ""
        self.ApplySerial = ""
        self.FrontID = 0
        self.SessionID = 0
        self.AccountID = ""
        self.CurrencyID = ""
        self.TransferDirection = ""
        self.Amount = 0.0
        self.TransferStatus = ""
        self.OperatorID = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.DepartmentID = ""
        self.BankAccountID = ""
        self.BankID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.InvestorID = ""
        self.ExternalNodeID = 0


class CTORATstpTransferPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTransferPositionField"
        self.PositionSerial = ""
        self.ApplySerial = ""
        self.FrontID = 0
        self.SessionID = 0
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.TradingDay = ""
        self.TransferDirection = ""
        self.TransferPositionType = ""
        self.HistoryVolume = 0
        self.TodayBSVolume = 0
        self.TodayPRVolume = 0
        self.TransferStatus = ""
        self.OperatorID = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.ExternalNodeID = 0


class CTORATstpSpecificSecurityField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSpecificSecurityField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpInputTransferCollateralField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputTransferCollateralField"
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.ApplySerial = ""
        self.CollateralDirection = ""
        self.Volume = 0
        self.MarketID = ""


class CTORATstpReqInquiryBankAccountFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInquiryBankAccountFundField"
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.BankID = ""
        self.BankPassword = ""


class CTORATstpRspInquiryBankAccountFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInquiryBankAccountFundField"
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.BankID = ""
        self.BankAccountID = ""
        self.Balance = 0.0


class CTORATstpInquiryMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInquiryMarketDataField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpQryRspInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRspInfoField"
        self.EndFlag = ""
        self.ErrorID = 0
        self.ErrorMsg = ""


class CTORATstpReqModifyOpenPosCostField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqModifyOpenPosCostField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.OpenPosCost = 0.0


class CTORATstpLev2MarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2MarketDataField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.DataTimeStamp = 0
        self.PreClosePrice = 0.0
        self.OpenPrice = 0.0
        self.NumTrades = 0
        self.TotalVolumeTrade = 0
        self.TotalValueTrade = 0.0
        self.TotalBidVolume = 0
        self.AvgBidPrice = 0.0
        self.TotalAskVolume = 0
        self.AvgAskPrice = 0.0
        self.HighestPrice = 0.0
        self.LowestPrice = 0.0
        self.LastPrice = 0.0
        self.BidPrice1 = 0.0
        self.BidVolume1 = 0
        self.AskPrice1 = 0.0
        self.AskVolume1 = 0
        self.AskPrice2 = 0.0
        self.AskVolume2 = 0
        self.AskPrice3 = 0.0
        self.AskVolume3 = 0
        self.BidPrice2 = 0.0
        self.BidVolume2 = 0
        self.BidPrice3 = 0.0
        self.BidVolume3 = 0
        self.AskPrice4 = 0.0
        self.AskVolume4 = 0
        self.AskPrice5 = 0.0
        self.AskVolume5 = 0
        self.BidPrice4 = 0.0
        self.BidVolume4 = 0
        self.BidPrice5 = 0.0
        self.BidVolume5 = 0
        self.AskPrice6 = 0.0
        self.AskVolume6 = 0
        self.AskPrice7 = 0.0
        self.AskVolume7 = 0
        self.BidPrice6 = 0.0
        self.BidVolume6 = 0
        self.BidPrice7 = 0.0
        self.BidVolume7 = 0
        self.AskPrice8 = 0.0
        self.AskVolume8 = 0
        self.AskPrice9 = 0.0
        self.AskVolume9 = 0
        self.BidPrice8 = 0.0
        self.BidVolume8 = 0
        self.BidPrice9 = 0.0
        self.BidVolume9 = 0
        self.BidPrice10 = 0.0
        self.BidVolume10 = 0
        self.AskPrice10 = 0.0
        self.AskVolume10 = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.ClosePrice = 0.0
        self.MDSecurityStat = ""
        self.TotalBidNumber = 0
        self.TotalOfferNumber = 0
        self.BidTradeMaxDuration = 0
        self.OfferTradeMaxDuration = 0


class CTORATstpLev2IndexField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2IndexField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.DataTimeStamp = 0
        self.PreCloseIndex = 0.0
        self.OpenIndex = 0.0
        self.HighIndex = 0.0
        self.LowIndex = 0.0
        self.LastIndex = 0.0
        self.Turnover = 0.0
        self.TotalVolumeTraded = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.CloseIndex = 0.0


class CTORATstpLev2TransactionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2TransactionField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.TradeTime = 0
        self.TradePrice = 0.0
        self.TradeVolume = 0
        self.ExecType = ""
        self.MainSeq = 0
        self.SubSeq = 0
        self.BuyNo = 0
        self.SellNo = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.TradeBSFlag = ""


class CTORATstpLev2OrderDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2OrderDetailField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.OrderTime = 0
        self.Price = 0.0
        self.Volume = 0
        self.Side = ""
        self.OrderType = ""
        self.MainSeq = 0
        self.SubSeq = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0


class CTORATstpLev2PHMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2PHMarketDataField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.DataTimeStamp = 0
        self.ClosePrice = 0.0
        self.MDSecurityStat = ""
        self.NumTrades = 0
        self.TotalVolumeTrade = 0
        self.TotalValueTrade = 0.0
        self.TotalBidVolume = 0
        self.TotalAskVolume = 0
        self.WithdrawBuyNumber = 0
        self.WithdrawBuyAmount = 0
        self.WithdrawSellNumber = 0
        self.WithdrawSellAmount = 0
        self.BidOrderQty = 0
        self.BidNumOrders = 0
        self.AskOrderQty = 0
        self.AskNumOrders = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0


class CTORATstpLev2PHTransactionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2PHTransactionField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.TradeTime = 0
        self.TradePrice = 0.0
        self.TradeVolume = 0
        self.TradeMoney = 0.0
        self.ExecType = ""
        self.MainSeq = 0
        self.SubSeq = 0
        self.BuyNo = 0
        self.SellNo = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.TradeBSFlag = ""


class CTORATstpLev2ResendTransactionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2ResendTransactionField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.TradeTime = 0
        self.TradePrice = 0.0
        self.TradeVolume = 0
        self.ExecType = ""
        self.MainSeq = 0
        self.SubSeq = 0
        self.BuyNo = 0
        self.SellNo = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.TradeBSFlag = ""


class CTORATstpLev2ResendOrderDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLev2ResendOrderDetailField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.OrderTime = 0
        self.Price = 0.0
        self.Volume = 0
        self.Side = ""
        self.OrderType = ""
        self.MainSeq = 0
        self.SubSeq = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0


class CTORATstpReqInsSecurityPriorAuthField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInsSecurityPriorAuthField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.bForbidden = 0


class CTORATstpReqUpdSecurityPriorAuthField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqUpdSecurityPriorAuthField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.bForbidden = 0


class CTORATstpReqDelSecurityPriorAuthField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqDelSecurityPriorAuthField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""


class CTORATstpReqInsBrokerUserFunctionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInsBrokerUserFunctionField"
        self.UserID = ""
        self.FunctionID = ""
        self.RangeMode = ""


class CTORATstpReqDelBrokerUserFunctionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqDelBrokerUserFunctionField"
        self.UserID = ""
        self.FunctionID = ""


class CTORATstpUploadTradeDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUploadTradeDataField"
        self.ExchangeID = ""
        self.TradingDay = ""
        self.bForce = 0


class CTORATstpGuardSubPasswordUpdateField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpGuardSubPasswordUpdateField"
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.OldPassword = ""
        self.NewPassword = ""


class CTORATstpGuardSubItemField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpGuardSubItemField"
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.SubPassword = ""


class CTORATstpGuardUnSubItemField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpGuardUnSubItemField"
        self.ExchangeID = ""
        self.ShareholderID = ""


class CTORATstpGuardOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpGuardOrderField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.ShareholderID = ""
        self.Direction = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.OrderType = ""
        self.PbuID = ""
        self.OrderLocalID = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.LotType = ""


class CTORATstpGuardTradeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpGuardTradeField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.ShareholderID = ""
        self.TradeID = ""
        self.PbuID = ""
        self.OrderLocalID = ""
        self.Price = 0.0
        self.Volume = 0
        self.TradeDate = ""
        self.TradeTime = ""
        self.ExecType = ""
        self.CancelOrderLocalID = ""


class CTORATstpInputDesignationRegistrationField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputDesignationRegistrationField"
        self.InvestorID = ""
        self.UserID = ""
        self.DesignationType = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.OrderSysID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.TerminalInfo = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpInputCustodyTransferField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputCustodyTransferField"
        self.InvestorID = ""
        self.UserID = ""
        self.CustodyTransferType = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.OrderSysID = ""
        self.TransfereePbuID = ""
        self.SecurityID = ""
        self.OrignalOrderLocalID = ""
        self.OrderLocalID = ""
        self.VolumeTotalOriginal = 0
        self.IPAddress = ""
        self.MacAddress = ""
        self.TerminalInfo = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpInquiryTradeConcentrationField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInquiryTradeConcentrationField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.ShareholderID = ""
        self.ConcentrationRatio1 = 0.0
        self.ConcentrationRatio2 = 0.0


class CTORATstpSpecialMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSpecialMarketDataField"
        self.TradingDay = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.SecurityName = ""
        self.MovingAvgPrice = 0.0
        self.MovingAvgPriceSamplingNum = 0
        self.UpdateTime = ""
        self.UpdateMillisec = 0


class CTORATstpEffectPriceMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEffectPriceMarketDataField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.LastPrice = 0.0
        self.TradeVol = 0
        self.TradeTurnover = 0.0
        self.UpdateTime = ""
        self.UpdateMillisec = 0


class CTORATstpEffectVolumeMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEffectVolumeMarketDataField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.LastPrice = 0.0
        self.TradeVol = 0
        self.TradeTurnover = 0.0
        self.UpdateTime = ""
        self.UpdateMillisec = 0


class CTORATstpFundsFlowMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFundsFlowMarketDataField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.RetailBuyTurnover = 0.0
        self.RetailBuyVolume = 0
        self.RetailBuyAmount = 0
        self.RetailSellTurnover = 0.0
        self.RetailSellVolume = 0
        self.RetailSellAmount = 0
        self.MiddleBuyTurnover = 0.0
        self.MiddleBuyVolume = 0
        self.MiddleBuyAmount = 0
        self.MiddleSellTurnover = 0.0
        self.MiddleSellVolume = 0
        self.MiddleSellAmount = 0
        self.LargeBuyTurnover = 0.0
        self.LargeBuyVolume = 0
        self.LargeBuyAmount = 0
        self.LargeSellTurnover = 0.0
        self.LargeSellVolume = 0
        self.LargeSellAmount = 0
        self.InstitutionBuyTurnover = 0.0
        self.InstitutionBuyVolume = 0
        self.InstitutionBuyAmount = 0
        self.InstitutionSellTurnover = 0.0
        self.InstitutionSellVolume = 0
        self.InstitutionSellAmount = 0


class CTORATstpQryRightsAdjustmentInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRightsAdjustmentInfoField"
        self.BegDate = ""
        self.EndDate = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpQryHistoryRspInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryHistoryRspInfoField"
        self.ErrorID = 0
        self.ErrorMsg = ""
        self.bPageEnd = 0
        self.bResultEnd = 0


class CTORATstpRightsAdjustmentDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRightsAdjustmentDataField"
        self.TradingDay = ""
        self.ADJPreClose = 0.0
        self.ADJOpen = 0.0
        self.ADJHigh = 0.0
        self.ADJLow = 0.0
        self.ADJClose = 0.0
        self.ADJFactor = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0
        self.Open = 0.0
        self.High = 0.0
        self.Low = 0.0
        self.Close = 0.0
        self.CrncyCode = ""
        self.Change = 0.0
        self.PCTChange = 0.0
        self.Volume = 0.0
        self.Amount = 0.0
        self.AVGPrice = 0.0
        self.TradeStatus = ""


class CTORATstpQryHistoryFundsFlowInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryHistoryFundsFlowInfoField"
        self.BegDate = ""
        self.EndDate = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpHistoryFundsFlowDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpHistoryFundsFlowDataField"
        self.TradingDay = ""
        self.BuyValueExlargeOrder = 0.0
        self.SellValueExlargeOrder = 0.0
        self.BuyValueLargeOrder = 0.0
        self.SellValueLargeOrder = 0.0
        self.BuyValueMedOrder = 0.0
        self.SellValueMedOrder = 0.0
        self.BuyValueSmallOrder = 0.0
        self.SellValueSmallOrder = 0.0
        self.BuyVolumeExlargeOrder = 0.0
        self.SellVolumeExlargeOrder = 0.0
        self.BuyVolumeLargeOrder = 0.0
        self.SellVolumeLargeOrder = 0.0
        self.BuyVolumeMedOrder = 0.0
        self.SellVolumeMedOrder = 0.0
        self.BuyVolumeSmallOrder = 0.0
        self.SellVolumeSmallOrder = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryFinancialIndicatorInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryFinancialIndicatorInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpFinancialIndicatorDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFinancialIndicatorDataField"
        self.AnnouncementDate = ""
        self.EPSBasic = 0.0
        self.BPS = 0.0
        self.SurplusCapitalPS = 0.0
        self.UndistributedPS = 0.0
        self.OCFPS = 0.0
        self.ORPS = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryDividendInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryDividendInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpDividendDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDividendDataField"
        self.AnnouncementDate = ""
        self.Progress = ""
        self.ExDate = ""
        self.STKDvdPerSh = 0.0
        self.CashDvdPerShPreTax = 0.0
        self.CashDvdPerShAfterTax = 0.0
        self.EqyRecordDate = ""
        self.DvdPayoutDate = ""
        self.ListingDateOfDvdShr = ""
        self.PrelanDate = ""
        self.SMTGDate = ""
        self.DvdAnnDate = ""
        self.BaseDate = ""
        self.BaseShare = 0.0
        self.CrncyCode = ""
        self.IsChanged = 0
        self.ReportPeriod = ""
        self.Change = ""
        self.BonusRate = 0.0
        self.ConversedRate = 0.0
        self.Memo = ""
        self.PreAnnDate = ""
        self.DivObject = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryRightIssueInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRightIssueInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpRightIssueDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRightIssueDataField"
        self.AnnouncementDate = ""
        self.Progress = ""
        self.Price = 0.0
        self.Ratio = 0.0
        self.Amount = 0.0
        self.AmountAct = 0.0
        self.NetCollection = 0.0
        self.RegDateShare = ""
        self.ExDividendDate = ""
        self.ListedDate = ""
        self.PayStartDate = ""
        self.PayEndDate = ""
        self.PrePlanDate = ""
        self.SMTGAnnceDate = ""
        self.PassDate = ""
        self.ApprovedDate = ""
        self.AnnceDate = ""
        self.ResultDate = ""
        self.ListAnnDate = ""
        self.Guarantor = ""
        self.Guartype = 0.0
        self.Code = ""
        self.Year = ""
        self.Content = ""
        self.Name = ""
        self.RatioDenominator = 0.0
        self.RatioMolecular = 0.0
        self.SubscriptionMethod = ""
        self.ExpectedFundRaising = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryCompanyDescriptionInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryCompanyDescriptionInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpCompanyDescriptionDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpCompanyDescriptionDataField"
        self.CompName = ""
        self.ListDate = ""
        self.BusinessScope = ""
        self.IPOPrice = 0.0
        self.IPOAmount = 0.0
        self.AMTByPlacing = 0.0
        self.AMTToJur = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryEquityStructureInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryEquityStructureInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpEquityStructureDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEquityStructureDataField"
        self.TradingDay = ""
        self.TotalShareToday = 0.0
        self.FloatShareToday = 0.0
        self.HolderTotalNum = 0.0
        self.AnnouncementDate = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQrySalesSegmentInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySalesSegmentInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpSalesSegmentDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSalesSegmentDataField"
        self.ReportPeriod = ""
        self.CrncyCode = ""
        self.ItemCode = 0
        self.Item = ""
        self.Sales = 0.0
        self.Profit = 0.0
        self.Cost = 0.0
        self.IsPublishedValue = 0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryTopTenHoldersInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTopTenHoldersInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpTopTenHoldersDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTopTenHoldersDataField"
        self.AnnouncementDate = ""
        self.HolderName = ""
        self.HolderQuantity = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryTopTenFloatHoldersInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTopTenFloatHoldersInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpTopTenFloatHoldersDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTopTenFloatHoldersDataField"
        self.AnnouncementDate = ""
        self.HolderName = ""
        self.HolderQuantity = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryIndustryInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIndustryInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpIndustryDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIndustryDataField"
        self.EntryDate = ""
        self.RemoveDate = ""
        self.IndustriesCode = ""
        self.IndustriesName = ""
        self.LevelNum = 0
        self.Used = 0
        self.IndustriesAlias = ""
        self.Sequence = 0
        self.Memo = ""
        self.ChineseDfinition = ""
        self.IndustriesNameEng = ""
        self.IndexCode = ""
        self.Name = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryConceptionInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryConceptionInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpConceptionDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConceptionDataField"
        self.ConceptionCode = ""
        self.ConceptionName = ""
        self.EntryDate = ""
        self.RemoveDate = ""
        self.CurSign = ""
        self.IndustriesCode = ""
        self.IndustriesName = ""
        self.LevelNum = 0
        self.Used = 0
        self.IndustriesAlias = ""
        self.Sequence = 0
        self.Memo = ""
        self.ChineseDfinition = ""
        self.IndustriesNameEng = ""
        self.IndexCode = ""
        self.Name = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryRegionInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRegionInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpRegionDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRegionDataField"
        self.IndustriesCode = ""
        self.IndustriesName = ""
        self.LevelNum = 0
        self.Used = 0
        self.IndustriesAlias = ""
        self.Sequence = 0
        self.Memo = ""
        self.ChineseDfinition = ""
        self.IndustriesNameEng = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryIndexDescriptionInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIndexDescriptionInfoField"
        self.IndexID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpIndexDescriptionDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIndexDescriptionDataField"
        self.Name = ""
        self.IndustryCode = ""
        self.IndustryName = ""
        self.IndustryCode2 = ""
        self.IndustryNameEng = ""
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpQryIndustryConstituentsInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIndustryConstituentsInfoField"
        self.IndexID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpIndustryConstituentsDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIndustryConstituentsDataField"
        self.IndexID = ""
        self.EntryDate = ""
        self.RemoveDate = ""
        self.CurSign = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryConceptionConstituentsInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryConceptionConstituentsInfoField"
        self.IndexID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpConceptionConstituentsDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConceptionConstituentsDataField"
        self.IndexID = ""
        self.EntryDate = ""
        self.RemoveDate = ""
        self.CurSign = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryIndustryCodeListField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIndustryCodeListField"
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpIndustryCodeListDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIndustryCodeListDataField"
        self.ChineseDfinition = ""
        self.TradingDay = ""
        self.PreClosePoint = 0.0
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpQryConceptionCodeListField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryConceptionCodeListField"
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpConceptionCodeListDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConceptionCodeListDataField"
        self.ChineseDfinition = ""
        self.TradingDay = ""
        self.PreClosePoint = 0.0
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpQryFreeFloatSharesInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryFreeFloatSharesInfoField"
        self.BegDate = ""
        self.EndDate = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpFreeFloatSharesDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFreeFloatSharesDataField"
        self.FreeShares = 0.0
        self.ChangeDateEX = ""
        self.ChangeDateList = ""
        self.AnnouncementDate = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpEffectDetailItemField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEffectDetailItemField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.EffectRatio = 0.0


class CTORATstpEffectOrderDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEffectOrderDetailField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Price = 0.0
        self.Volume = 0
        self.OrderType = ""
        self.Side = ""
        self.EffectRatio = 0.0
        self.OrderSeq1 = 0
        self.OrderSeq2 = 0
        self.UpdateTime = ""
        self.UpdateMillisec = 0


class CTORATstpEffectTradeDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpEffectTradeDetailField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.TradePrice = 0.0
        self.TradeVolume = 0
        self.ExecType = ""
        self.EffectRatio = 0.0
        self.TradeSeq1 = 0
        self.TradeSeq2 = 0
        self.BuySideSeq = 0
        self.SelSideSeq = 0
        self.UpdateTime = ""
        self.UpdateMillisec = 0


class CTORATstpInquiryQueueingOrdersField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInquiryQueueingOrdersField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.QueuePrice = 0.0


class CTORATstpQueueingOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQueueingOrderField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Price = 0.0
        self.Volume = 0
        self.OrderType = ""
        self.Side = ""
        self.OrderSeq1 = 0
        self.OrderSeq2 = 0


class CTORATstpQryPriceDistributionInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPriceDistributionInfoField"
        self.BegDate = ""
        self.EndDate = ""
        self.PercentNum = 0
        self.DistributionType = 0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpPriceDistributionDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPriceDistributionDataField"
        self.DataDate = ""
        self.PercentNum = 0
        self.PercentValue = 0.0
        self.DistributionType = 0
        self.DistributionValue = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryPriceExtremumInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPriceExtremumInfoField"
        self.TradingDay = ""
        self.BegTime = ""
        self.EndTime = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpPriceExtremumDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPriceExtremumDataField"
        self.HighestTradingDay = ""
        self.HighestUpdateTime = ""
        self.HighestUpdateMillisec = 0
        self.HighestPrice = 0.0
        self.LowestTradingDay = ""
        self.LowestUpdateTime = ""
        self.LowestUpdateMillisec = 0
        self.LowestPrice = 0.0
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpQryRegionCodeListField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRegionCodeListField"
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpRegionCodeListDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRegionCodeListDataField"
        self.ChineseDfinition = ""
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpIndustryIndexDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIndustryIndexDataField"
        self.IndexPoint = 0.0
        self.PreClosePoint = 0.0
        self.OpenPoint = 0.0
        self.ClosePoint = 0.0
        self.HighestPoint = 0.0
        self.LowestPoint = 0.0
        self.TradingDay = ""
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpConceptionIndexDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConceptionIndexDataField"
        self.IndexPoint = 0.0
        self.PreClosePoint = 0.0
        self.OpenPoint = 0.0
        self.ClosePoint = 0.0
        self.HighestPoint = 0.0
        self.LowestPoint = 0.0
        self.TradingDay = ""
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpRegionIndexDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRegionIndexDataField"
        self.IndexPoint = 0.0
        self.PreClosePoint = 0.0
        self.OpenPoint = 0.0
        self.ClosePoint = 0.0
        self.HighestPoint = 0.0
        self.LowestPoint = 0.0
        self.TradingDay = ""
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.IndexID = ""
        self.PageLocate = 0


class CTORATstpInquirySpecialMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInquirySpecialMarketDataField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpRapidMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRapidMarketDataField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.DataTimeStamp = 0
        self.PreClosePrice = 0.0
        self.OpenPrice = 0.0
        self.NumTrades = 0
        self.TotalVolumeTrade = 0
        self.TotalValueTrade = 0.0
        self.TotalBidVolume = 0
        self.AvgBidPrice = 0.0
        self.TotalAskVolume = 0
        self.AvgAskPrice = 0.0
        self.HighestPrice = 0.0
        self.LowestPrice = 0.0
        self.LastPrice = 0.0
        self.BidPrice1 = 0.0
        self.BidVolume1 = 0
        self.AskPrice1 = 0.0
        self.AskVolume1 = 0
        self.AskPrice2 = 0.0
        self.AskVolume2 = 0
        self.AskPrice3 = 0.0
        self.AskVolume3 = 0
        self.BidPrice2 = 0.0
        self.BidVolume2 = 0
        self.BidPrice3 = 0.0
        self.BidVolume3 = 0
        self.AskPrice4 = 0.0
        self.AskVolume4 = 0
        self.AskPrice5 = 0.0
        self.AskVolume5 = 0
        self.BidPrice4 = 0.0
        self.BidVolume4 = 0
        self.BidPrice5 = 0.0
        self.BidVolume5 = 0
        self.AskPrice6 = 0.0
        self.AskVolume6 = 0
        self.AskPrice7 = 0.0
        self.AskVolume7 = 0
        self.BidPrice6 = 0.0
        self.BidVolume6 = 0
        self.BidPrice7 = 0.0
        self.BidVolume7 = 0
        self.AskPrice8 = 0.0
        self.AskVolume8 = 0
        self.AskPrice9 = 0.0
        self.AskVolume9 = 0
        self.BidPrice8 = 0.0
        self.BidVolume8 = 0
        self.BidPrice9 = 0.0
        self.BidVolume9 = 0
        self.BidPrice10 = 0.0
        self.BidVolume10 = 0
        self.AskPrice10 = 0.0
        self.AskVolume10 = 0
        self.Info1 = 0
        self.Info2 = 0
        self.Info3 = 0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.ClosePrice = 0.0
        self.MDSecurityStat = ""
        self.TotalBidNumber = 0
        self.TotalOfferNumber = 0
        self.BidTradeMaxDuration = 0
        self.OfferTradeMaxDuration = 0


class CTORATstpQryRegionConstituentsInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRegionConstituentsInfoField"
        self.IndexID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpRegionConstituentsDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRegionConstituentsDataField"
        self.IndexID = ""
        self.RegionName = ""
        self.EntryDate = ""
        self.RemoveDate = ""
        self.CurSign = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.PageLocate = 0


class CTORATstpInquiryFileOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInquiryFileOrderField"
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderSerialBeg = 0
        self.OrderSerialEnd = 0
        self.CommitStatus = ""


class CTORATstpFileOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFileOrderField"
        self.RequestID = 0
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderRef = ""
        self.FileOrderType = ""
        self.Direction = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.Operway = ""
        self.OrderActionRef = ""
        self.OrderSysID = ""
        self.CondCheck = ""
        self.OrderSerial = 0
        self.CommitStatus = ""
        self.StatusMsg = ""
        self.TimeStamp = 0


class CTORATstpReviewFileOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReviewFileOrderField"
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderSerialBeg = 0
        self.OrderSerialEnd = 0


class CTORATstpCommitInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpCommitInfoField"
        self.OrderSerial = 0
        self.CommitStatus = ""
        self.StatusMsg = ""


class CTORATstpReqInsTradingNoticeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInsTradingNoticeField"
        self.NoticeSerial = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.Content = ""
        self.OperatorID = ""


class CTORATstpTradingNoticeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTradingNoticeField"
        self.NoticeSerial = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.Content = ""
        self.OperatorID = ""


class CTORATstpLoadFileOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpLoadFileOrderField"
        self.InvestorID = ""
        self.bReview = 0


class CTORATstpFileOrderInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFileOrderInfoField"
        self.RequestID = 0
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderRef = ""
        self.FileOrderType = ""
        self.Direction = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.Operway = ""
        self.OrderActionRef = ""
        self.OrderSysID = ""
        self.CondCheck = ""
        self.OrderSerial = 0
        self.CommitStatus = ""
        self.StatusMsg = ""


class CTORATstpReqInquiryMaxOrderVolumeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpReqInquiryMaxOrderVolumeField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.ShareholderID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.LimitPrice = 0.0
        self.TransfereePbuID = ""
        self.MaxVolume = 0
        self.LotType = ""


class CTORATstpRspInquiryMaxOrderVolumeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInquiryMaxOrderVolumeField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.ShareholderID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.LimitPrice = 0.0
        self.TransfereePbuID = ""
        self.MaxVolume = 0
        self.LotType = ""


class CTORATstpRtnPeripheryTransferPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRtnPeripheryTransferPositionField"
        self.PositionSerial = 0
        self.ApplySerial = 0
        self.FrontID = 0
        self.SessionID = 0
        self.TransferDirection = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.TodayBSPos = 0
        self.TodayPRPos = 0
        self.HistoryPos = 0
        self.TradingDay = ""
        self.TransferReason = ""
        self.TransferStatus = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.RepealDate = ""
        self.RepealTime = ""
        self.RepealReason = ""
        self.StatusMsg = ""


class CTORATstpRtnPeripheryTransferFundField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRtnPeripheryTransferFundField"
        self.FundSerial = 0
        self.ApplySerial = 0
        self.FrontID = 0
        self.SessionID = 0
        self.TransferDirection = ""
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.Amount = 0.0
        self.InvestorID = ""
        self.TransferReason = ""
        self.TransferStatus = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.RepealDate = ""
        self.RepealTime = ""
        self.RepealReason = ""
        self.StatusMsg = ""


class CTORATstpQryHistoryOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryHistoryOrderField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BegDate = ""
        self.EndDate = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpHistoryOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpHistoryOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.OrderRef = ""
        self.UserID = ""
        self.OrderPriceType = ""
        self.Direction = ""
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.MinVolume = 0
        self.ForceCloseReason = ""
        self.RequestID = 0
        self.OrderLocalID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.ExchangeInstID = ""
        self.TraderID = ""
        self.OrderSubmitStatus = ""
        self.TradingDay = ""
        self.OrderSysID = ""
        self.OrderStatus = ""
        self.OrderType = ""
        self.VolumeTraded = 0
        self.VolumeTotal = 0
        self.InsertDate = ""
        self.InsertTime = ""
        self.CancelTime = ""
        self.ActiveTraderID = ""
        self.FrontID = 0
        self.SessionID = 0
        self.UserProductInfo = ""
        self.StatusMsg = ""
        self.UserForceClose = 0
        self.ActiveUserID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.LotType = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.TransfereePbuID = ""
        self.Operway = ""
        self.DepartmentID = ""
        self.ProperCtrlBusinessType = ""
        self.ProperCtrlPassFlag = ""
        self.CondCheck = ""
        self.IsCacheOrder = 0
        self.Turnover = 0.0
        self.RtnFloatInfo = 0.0
        self.RtnIntInfo = 0
        self.HDSerial = ""
        self.Mobile = ""
        self.GTDate = ""
        self.PageLocate = 0


class CTORATstpQryHistoryTradeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryHistoryTradeField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BegDate = ""
        self.EndDate = ""
        self.SecurityID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpHistoryTradeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpHistoryTradeField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.UserID = ""
        self.ExchangeID = ""
        self.TradeID = ""
        self.Direction = ""
        self.OrderSysID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.ExchangeInstID = ""
        self.OffsetFlag = ""
        self.HedgeFlag = ""
        self.Price = 0.0
        self.Volume = 0
        self.TradeDate = ""
        self.TradeTime = ""
        self.TraderID = ""
        self.OrderLocalID = ""
        self.TradingDay = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.OrderRef = ""
        self.DepartmentID = ""
        self.ActualBrokerage = 0.0
        self.PageLocate = 0


class CTORATstpInputRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInputRemarkEventField"
        self.SequenceNo = ""
        self.InvestorID = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Remark = ""


class CTORATstpRspInputRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspInputRemarkEventField"
        self.SequenceNo = ""
        self.EventDate = ""
        self.EventTime = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Remark = ""
        self.InvestorID = ""


class CTORATstpUpdateRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUpdateRemarkEventField"
        self.SequenceNo = ""
        self.EventDate = ""
        self.EventTime = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Remark = ""
        self.InvestorID = ""


class CTORATstpRspUpdateRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspUpdateRemarkEventField"
        self.SequenceNo = ""
        self.EventDate = ""
        self.EventTime = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Remark = ""
        self.InvestorID = ""


class CTORATstpDeleteRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDeleteRemarkEventField"
        self.SequenceNo = ""
        self.EventDate = ""
        self.EventTime = ""
        self.InvestorID = ""


class CTORATstpRspDeleteRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRspDeleteRemarkEventField"


class CTORATstpQryRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRemarkEventField"
        self.SequenceNo = ""
        self.InvestorID = ""
        self.EventDateStart = ""
        self.EventDateEnd = ""
        self.EventTimeStart = ""
        self.EventTimeEnd = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.PageCount = 0
        self.PageLocate = 0


class CTORATstpRemarkEventField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRemarkEventField"
        self.SequenceNo = ""
        self.EventDate = ""
        self.EventTime = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Remark = ""
        self.InvestorID = ""
        self.PageLocate = 0


class CTORATstpQryExchangeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryExchangeField"
        self.ExchangeID = ""


class CTORATstpExchangeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpExchangeField"
        self.ExchangeID = ""
        self.ExchangeName = ""
        self.TradingDay = ""


class CTORATstpQryPBUField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPBUField"
        self.PbuID = ""
        self.ExchangeID = ""
        self.MarketID = ""


class CTORATstpPBUField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPBUField"
        self.PbuID = ""
        self.PbuName = ""
        self.ExchangeID = ""
        self.MarketID = ""


class CTORATstpQryMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryMarketDataField"
        self.SecurityID = ""
        self.ExchangeID = ""


class CTORATstpQrySecurityField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySecurityField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.ExchangeInstID = ""
        self.ProductID = ""


class CTORATstpSecurityField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSecurityField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.SecurityName = ""
        self.ExchangeInstID = ""
        self.MarketID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.OrderUnit = ""
        self.BuyTradingUnit = 0
        self.SellTradingUnit = 0
        self.MaxMarketOrderBuyVolume = 0
        self.MinMarketOrderBuyVolume = 0
        self.MaxLimitOrderBuyVolume = 0
        self.MinLimitOrderBuyVolume = 0
        self.MaxMarketOrderSellVolume = 0
        self.MinMarketOrderSellVolume = 0
        self.MaxLimitOrderSellVolume = 0
        self.MinLimitOrderSellVolume = 0
        self.VolumeMultiple = 0
        self.PriceTick = 0.0
        self.OpenDate = ""
        self.PositionType = ""
        self.ParValue = 0.0
        self.SecurityStatus = 0
        self.BondInterest = 0.0
        self.ConversionRate = 0.0
        self.IsCollateral = 0
        self.PreClosePrice = 0.0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.TradingDay = ""
        self.ShortSecurityName = ""


class CTORATstpQryETFFileField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryETFFileField"
        self.ExchangeID = ""
        self.ETFSecurityID = ""
        self.ETFCreRedSecurityID = ""


class CTORATstpETFFileField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpETFFileField"
        self.TradingDay = ""
        self.ExchangeID = ""
        self.ETFSecurityID = ""
        self.ETFCreRedSecurityID = ""
        self.CreationRedemptionUnit = 0
        self.Maxcashratio = 0.0
        self.CreationStatus = 0
        self.RedemptionStatus = 0
        self.EstimateCashComponent = 0.0
        self.CashComponent = 0.0
        self.NAV = 0.0
        self.NAVperCU = 0.0
        self.DividendPerCU = 0.0
        self.ETFCreRedType = ""
        self.ETFSecurityName = ""


class CTORATstpQryETFBasketField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryETFBasketField"
        self.ExchangeID = ""
        self.ETFSecurityID = ""
        self.SecurityID = ""


class CTORATstpETFBasketField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpETFBasketField"
        self.TradingDay = ""
        self.ExchangeID = ""
        self.ETFSecurityID = ""
        self.SecurityID = ""
        self.SecurityName = ""
        self.Volume = 0
        self.ETFCurrenceReplaceStatus = ""
        self.Premium = 0.0
        self.CreationReplaceAmount = 0.0
        self.RedemptionReplaceAmount = 0.0
        self.MarketID = ""
        self.ETFCreRedType = ""


class CTORATstpQryDepartmentInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryDepartmentInfoField"
        self.DepartmentID = ""


class CTORATstpDepartmentInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDepartmentInfoField"
        self.DepartmentID = ""
        self.DepartmentName = ""


class CTORATstpQryIPOInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIPOInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpIPOInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIPOInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.MarketID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.OnlineLimit = 0
        self.Price = 0.0
        self.CurrencyID = ""
        self.SecurityName = ""
        self.UnderlyingSecurityID = ""
        self.UnderlyingSecurityName = ""
        self.OnlineMinVol = 0
        self.OnlineVolUnit = 0
        self.IssueMode = ""
        self.TradingDay = ""


class CTORATstpQryBrokerUserFunctionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBrokerUserFunctionField"
        self.UserID = ""


class CTORATstpBrokerUserFunctionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBrokerUserFunctionField"
        self.UserID = ""
        self.FunctionID = ""


class CTORATstpQryBUProxyField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBUProxyField"
        self.InvestorID = ""
        self.UserID = ""
        self.BusinessUnitID = ""


class CTORATstpBUProxyField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBUProxyField"
        self.InvestorID = ""
        self.UserID = ""
        self.BusinessUnitID = ""
        self.ManageDepartmentID = ""
        self.InnerBranchID = ""


class CTORATstpQryUserField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryUserField"
        self.UserID = ""
        self.UserType = ""


class CTORATstpUserField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpUserField"
        self.UserID = ""
        self.UserName = ""
        self.UserType = ""
        self.IsActive = 0
        self.LoginLimit = 0


class CTORATstpQryInvestorField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryInvestorField"
        self.InvestorID = ""


class CTORATstpInvestorField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInvestorField"
        self.InvestorID = ""
        self.InvestorName = ""
        self.IdCardType = ""
        self.IdCardNo = ""
        self.Telephone = ""
        self.Address = ""
        self.OpenDate = ""
        self.Mobile = ""
        self.Operways = ""
        self.CRiskLevel = ""
        self.ProfInvestorType = ""
        self.DepartmentID = ""
        self.InnerBranchID = ""
        self.ManageDepartmentID = ""
        self.IsActive = 0
        self.LoginLimit = 0


class CTORATstpQryShareholderAccountField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryShareholderAccountField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingCodeClass = ""


class CTORATstpShareholderAccountField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpShareholderAccountField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.ClientIDType = ""
        self.MarketID = ""


class CTORATstpQryBusinessUnitField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBusinessUnitField"
        self.InvestorID = ""


class CTORATstpBusinessUnitField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBusinessUnitField"
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.BusinessUnitName = ""


class CTORATstpQryBusinessUnitAndTradingAcctField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBusinessUnitAndTradingAcctField"
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ProductID = ""
        self.AccountID = ""
        self.CurrencyID = ""


class CTORATstpBusinessUnitAndTradingAcctField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBusinessUnitAndTradingAcctField"
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.ProductID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.UserID = ""


class CTORATstpQryOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.OrderSysID = ""
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""
        self.BusinessUnitID = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.IsCancel = 0


class CTORATstpQryOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryOrderActionField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0


class CTORATstpQryTradeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTradeField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradeID = ""
        self.TradeTimeStart = ""
        self.TradeTimeEnd = ""
        self.BusinessUnitID = ""


class CTORATstpQryTradingAccountField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTradingAccountField"
        self.InvestorID = ""
        self.CurrencyID = ""
        self.AccountID = ""
        self.AccountType = ""
        self.DepartmentID = ""


class CTORATstpTradingAccountField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTradingAccountField"
        self.AccountID = ""
        self.Available = 0.0
        self.WithdrawQuota = 0.0
        self.CurrencyID = ""
        self.Deposit = 0.0
        self.Withdraw = 0.0
        self.UnDeliveredMoney = 0.0
        self.FrozenCash = 0.0
        self.FrozenCommission = 0.0
        self.PreUnDeliveredMoney = 0.0
        self.Commission = 0.0
        self.AccountType = ""
        self.AccountOwner = ""
        self.DepartmentID = ""
        self.BankID = ""
        self.BankAccountID = ""
        self.UnDeliveredFrozenCash = 0.0
        self.UnDeliveredFrozenCommission = 0.0
        self.UnDeliveredCommission = 0.0


class CTORATstpQryPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPositionField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""


class CTORATstpPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPositionField"
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingDay = ""
        self.HistoryPos = 0
        self.HistoryPosFrozen = 0
        self.TodayBSPos = 0
        self.TodayBSFrozen = 0
        self.TodayPRPos = 0
        self.TodayPRFrozen = 0
        self.TotalPosCost = 0.0
        self.TodaySMPos = 0
        self.TodaySMPosFrozen = 0
        self.MarginBuyPos = 0
        self.ShortSellPos = 0
        self.PrePosition = 0
        self.AvailablePosition = 0
        self.CurrentPosition = 0
        self.LastPrice = 0.0
        self.OpenPosCost = 0.0
        self.SecurityName = ""


class CTORATstpQryTradingFeeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTradingFeeField"
        self.ExchangeID = ""


class CTORATstpTradingFeeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpTradingFeeField"
        self.ExchangeID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.SecurityID = ""
        self.BizClass = ""
        self.StampTaxRatioByAmt = 0.0
        self.StampTaxRatioByPar = 0.0
        self.StampTaxFeePerOrder = 0.0
        self.StampTaxFeeMin = 0.0
        self.StampTaxFeeMax = 0.0
        self.TransferRatioByAmt = 0.0
        self.TransferRatioByPar = 0.0
        self.TransferFeePerOrder = 0.0
        self.TransferFeeMin = 0.0
        self.TransferFeeMax = 0.0
        self.HandlingRatioByAmt = 0.0
        self.HandlingRatioByPar = 0.0
        self.HandlingFeePerOrder = 0.0
        self.HandlingFeeMin = 0.0
        self.HandlingFeeMax = 0.0
        self.RegulateRatioByAmt = 0.0
        self.RegulateRatioByPar = 0.0
        self.RegulateFeePerOrder = 0.0
        self.RegulateFeeMin = 0.0
        self.RegulateFeeMax = 0.0
        self.TransferFeeByVolume = 0.0
        self.HandlingFeeByVolume = 0.0
        self.SettlementRatioByAmt = 0.0
        self.SettlementRatioByPar = 0.0
        self.SettlementFeePerOrder = 0.0
        self.SettlementFeeByVolume = 0.0
        self.SettlementFeeMin = 0.0
        self.SettlementFeeMax = 0.0
        self.StampTaxFeeByVolume = 0.0
        self.RegulateFeeByVolume = 0.0


class CTORATstpQryInvestorTradingFeeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryInvestorTradingFeeField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.DepartmentID = ""


class CTORATstpInvestorTradingFeeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInvestorTradingFeeField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.SecurityID = ""
        self.BizClass = ""
        self.BrokerageType = ""
        self.RatioByAmt = 0.0
        self.RatioByPar = 0.0
        self.FeePerOrder = 0.0
        self.FeeMin = 0.0
        self.FeeMax = 0.0
        self.FeeByVolume = 0.0
        self.DepartmentID = ""
        self.OrderType = ""


class CTORATstpQryIPOQuotaField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIPOQuotaField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""


class CTORATstpIPOQuotaField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIPOQuotaField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.MaxVolume = 0
        self.KCMaxVolume = 0


class CTORATstpQryMarketField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryMarketField"
        self.ExchangeID = ""
        self.MarketID = ""


class CTORATstpMarketField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpMarketField"
        self.MarketID = ""
        self.MarketName = ""
        self.ExchangeID = ""
        self.MarketStatus = ""


class CTORATstpQryOrderFundDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryOrderFundDetailField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.OrderSysID = ""
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""
        self.BusinessUnitID = ""


class CTORATstpOrderFundDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpOrderFundDetailField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.TradingDay = ""
        self.OrderSysID = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.TotalFrozen = 0.0
        self.TotalFee = 0.0
        self.StampTaxFee = 0.0
        self.HandlingFee = 0.0
        self.TransferFee = 0.0
        self.RegulateFee = 0.0
        self.BrokerageFee = 0.0
        self.SettlementFee = 0.0
        self.TotalFeeFrozen = 0.0
        self.OrderAmount = 0.0


class CTORATstpQryFundTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryFundTransferDetailField"
        self.AccountID = ""
        self.CurrencyID = ""
        self.TransferDirection = ""
        self.DepartmentID = ""


class CTORATstpFundTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpFundTransferDetailField"
        self.FundSerial = ""
        self.ApplySerial = ""
        self.FrontID = 0
        self.SessionID = 0
        self.AccountID = ""
        self.CurrencyID = ""
        self.TransferDirection = ""
        self.Amount = 0.0
        self.TransferStatus = ""
        self.OperateSource = ""
        self.OperatorID = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.StatusMsg = ""
        self.DepartmentID = ""
        self.BankID = ""
        self.BankAccountID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.InvestorID = ""
        self.ExternalNodeID = 0


class CTORATstpQryPositionTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPositionTransferDetailField"
        self.ShareholderID = ""
        self.SecurityID = ""
        self.TransferDirection = ""


class CTORATstpPositionTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPositionTransferDetailField"
        self.PositionSerial = ""
        self.ApplySerial = ""
        self.FrontID = 0
        self.SessionID = 0
        self.InvestorID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.TradingDay = ""
        self.TransferDirection = ""
        self.TransferPositionType = ""
        self.TransferStatus = ""
        self.HistoryVolume = 0
        self.TodayBSVolume = 0
        self.TodayPRVolume = 0
        self.OperatorID = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.BusinessUnitID = ""
        self.StatusMsg = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""
        self.ExternalNodeID = 0


class CTORATstpQryPledgePositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPledgePositionField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""


class CTORATstpPledgePositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPledgePositionField"
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingDay = ""
        self.HisPledgePos = 0
        self.HisPledgePosFrozen = 0
        self.TodayPledgePos = 0
        self.TodayPledgePosFrozen = 0
        self.PreTotalPledgePos = 0
        self.preAvailablePledgePos = 0


class CTORATstpQryPledgeInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPledgeInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpPledgeInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPledgeInfoField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.PledgeOrderID = ""
        self.StandardBondID = ""
        self.AllowPledgeIn = 0
        self.AllowPledgeOut = 0
        self.ConversionRate = 0.0
        self.PledgeInTradingUnit = 0
        self.PledgeOutTradingUnit = 0
        self.PledgeInVolMax = 0
        self.PledgeInVolMin = 0
        self.PledgeOutVolMax = 0
        self.PledgeOutVolMin = 0
        self.IsTodayToPlegeOut = 0
        self.IsCancelOrder = 0
        self.PledgeName = ""


class CTORATstpQryConversionBondInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryConversionBondInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpConversionBondInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpConversionBondInfoField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.ConvertOrderID = ""
        self.ConvertPrice = 0.0
        self.ConvertVolUnit = 0
        self.ConvertVolMax = 0
        self.ConvertVolMin = 0
        self.BeginDate = ""
        self.EndDate = ""
        self.IsSupportCancel = 0
        self.ConvertName = ""


class CTORATstpQryBondPutbackInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBondPutbackInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpBondPutbackInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBondPutbackInfoField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.SecurityID = ""
        self.PutbackOrderID = ""
        self.PutbackPrice = 0.0
        self.PutbackVolUnit = 0
        self.PutbackVolMax = 0
        self.PutbackVolMin = 0
        self.BeginDate = ""
        self.EndDate = ""
        self.IsSupportCancel = 0
        self.PutbackName = ""


class CTORATstpQryStandardBondPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryStandardBondPositionField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""


class CTORATstpStandardBondPositionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpStandardBondPositionField"
        self.SecurityID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingDay = ""
        self.AvailablePosition = 0.0
        self.AvailablePosFrozen = 0.0
        self.TotalPosition = 0.0


class CTORATstpQryDesignationRegistrationField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryDesignationRegistrationField"
        self.InvestorID = ""
        self.ShareholderID = ""
        self.OrderSysID = ""
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""
        self.BusinessUnitID = ""


class CTORATstpDesignationRegistrationField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDesignationRegistrationField"
        self.InvestorID = ""
        self.UserID = ""
        self.DesignationType = ""
        self.OrderLocalID = ""
        self.ShareholderID = ""
        self.PbuID = ""
        self.OrderSubmitStatus = ""
        self.TradingDay = ""
        self.OrderSysID = ""
        self.OrderStatus = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.StatusMsg = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.DepartmentID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpQryCustodyTransferField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryCustodyTransferField"
        self.InvestorID = ""
        self.ShareholderID = ""
        self.OrderSysID = ""
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""
        self.BusinessUnitID = ""
        self.SecurityID = ""


class CTORATstpCustodyTransferField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpCustodyTransferField"
        self.InvestorID = ""
        self.UserID = ""
        self.CustodyTransferType = ""
        self.OrderLocalID = ""
        self.ShareholderID = ""
        self.PbuID = ""
        self.OrderSubmitStatus = ""
        self.TradingDay = ""
        self.OrderSysID = ""
        self.OrderStatus = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.StatusMsg = ""
        self.BusinessUnitID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.DepartmentID = ""
        self.TransfereePbuID = ""
        self.SecurityID = ""
        self.OrignalOrderLocalID = ""
        self.VolumeTotalOriginal = 0
        self.CancelTime = ""
        self.ActiveTraderID = ""
        self.ActiveUserID = ""
        self.IPAddress = ""
        self.MacAddress = ""
        self.HDSerial = ""
        self.Mobile = ""


class CTORATstpQryPrematurityRepoOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPrematurityRepoOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""
        self.OrderLocalID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.Direction = ""
        self.TradeID = ""


class CTORATstpPrematurityRepoOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPrematurityRepoOrderField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.InvestorID = ""
        self.ShareholderID = ""
        self.BusinessUnitID = ""
        self.TradeDay = ""
        self.ExpireDay = ""
        self.OrderLocalID = ""
        self.SecurityID = ""
        self.SecurityName = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.Direction = ""
        self.VolumeTraded = 0
        self.Price = 0.0
        self.Turnover = 0.0
        self.TradeID = ""
        self.RepoTotalMoney = 0.0
        self.InterestAmount = 0.0


class CTORATstpQryShareholderParamField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryShareholderParamField"
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingCodeClass = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.SecurityID = ""
        self.ParamType = ""
        self.ExchangeID = ""


class CTORATstpShareholderParamField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpShareholderParamField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.TradingCodeClass = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.SecurityID = ""
        self.ParamType = ""
        self.ParamValue = ""


class CTORATstpQryPeripheryPositionTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPeripheryPositionTransferDetailField"
        self.InvestorID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.TransferDirection = ""
        self.BusinessUnitID = ""


class CTORATstpPeripheryPositionTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPeripheryPositionTransferDetailField"
        self.PositionSerial = 0
        self.ApplySerial = 0
        self.FrontID = 0
        self.SessionID = 0
        self.TransferDirection = ""
        self.ExchangeID = ""
        self.MarketID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.TodayBSPos = 0
        self.TodayPRPos = 0
        self.HistoryPos = 0
        self.TradingDay = ""
        self.TransferReason = ""
        self.TransferStatus = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.RepealDate = ""
        self.RepealTime = ""
        self.RepealReason = ""
        self.StatusMsg = ""


class CTORATstpQryInvestorCondOrderLimitParamField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryInvestorCondOrderLimitParamField"
        self.InvestorID = ""


class CTORATstpInvestorCondOrderLimitParamField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInvestorCondOrderLimitParamField"
        self.InvestorID = ""
        self.MaxCondOrderLimitCnt = 0
        self.CurrCondOrderCnt = 0


class CTORATstpQryCondOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryCondOrderField"
        self.InvestorID = ""
        self.SecurityID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.CondOrderID = 0
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""
        self.BusinessUnitID = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0


class CTORATstpCondOrderField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpCondOrderField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.OrderPriceType = ""
        self.TriggerOrderVolumeType = ""
        self.TimeCondition = ""
        self.VolumeCondition = ""
        self.LimitPrice = 0.0
        self.VolumeTotalOriginal = 0
        self.CombOffsetFlag = ""
        self.CombHedgeFlag = ""
        self.CondOrderRef = ""
        self.AccountID = ""
        self.UserID = ""
        self.RequestID = 0
        self.IPAddress = ""
        self.MacAddress = ""
        self.CondOrderID = 0
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.CondCheck = ""
        self.ContingentCondition = ""
        self.ConditionPrice = 0.0
        self.PriceTicks = 0
        self.VolumeMultiple = 0
        self.RelativeFrontID = 0
        self.RelativeSessionID = 0
        self.RelativeParam = ""
        self.AppendContingentCondition = ""
        self.AppendConditionPrice = 0.0
        self.AppendRelativeFrontID = 0
        self.AppendRelativeSessionID = 0
        self.AppendRelativeParam = ""
        self.TradingDay = ""
        self.CondOrderStatus = ""
        self.InsertDate = ""
        self.InsertTime = ""
        self.CancelTime = ""
        self.CancelUser = ""
        self.FrontID = 0
        self.SessionID = 0
        self.UserProductInfo = ""
        self.StatusMsg = ""
        self.DepartmentID = ""
        self.ProperCtrlBusinessType = ""
        self.ProperCtrlPassFlag = ""
        self.ActiveDate = ""
        self.ActiveTime = ""
        self.HDSerial = ""
        self.LotType = ""
        self.Mobile = ""
        self.TriggerOrderPriceType = ""
        self.TriggerRelativeParam = ""
        self.AppendCondParam = ""
        self.GTDate = ""


class CTORATstpQryCondOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryCondOrderActionField"
        self.InvestorID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0


class CTORATstpCondOrderActionField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpCondOrderActionField"
        self.ExchangeID = ""
        self.RequestID = 0
        self.CondOrderActionRef = ""
        self.CondOrderRef = ""
        self.FrontID = 0
        self.SessionID = 0
        self.CondOrderID = 0
        self.ActionFlag = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.UserID = ""
        self.CancelCondOrderID = 0
        self.IPAddress = ""
        self.MacAddress = ""
        self.TerminalInfo = ""
        self.BInfo = ""
        self.SInfo = ""
        self.IInfo = 0
        self.Operway = ""
        self.BusinessUnitID = ""
        self.ShareholderID = ""
        self.ActionDate = ""
        self.ActionTime = ""


class CTORATstpQryBrokerUserRoleField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBrokerUserRoleField"
        self.RoleID = 0


class CTORATstpBrokerUserRoleField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBrokerUserRoleField"
        self.RoleID = 0
        self.RoleDescription = ""
        self.Functions = ""


class CTORATstpQryBrokerUserRoleAssignmentField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBrokerUserRoleAssignmentField"
        self.UserID = ""


class CTORATstpBrokerUserRoleAssignmentField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBrokerUserRoleAssignmentField"
        self.UserID = ""
        self.RoleID = 0
        self.RoleDescription = ""


class CTORATstpQryTradingNoticeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryTradingNoticeField"
        self.InvestorID = ""
        self.InsertDateStart = ""
        self.InsertDateEnd = ""
        self.InsertTimeStart = ""
        self.InsertTimeEnd = ""


class CTORATstpQryIPONumberResultField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIPONumberResultField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""


class CTORATstpIPONumberResultField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIPONumberResultField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Day = ""
        self.SecurityName = ""
        self.ShareholderID = ""
        self.SecurityType = ""
        self.BeginNumberID = ""
        self.Volume = 0


class CTORATstpQryIPOMatchNumberResultField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryIPOMatchNumberResultField"
        self.SecurityID = ""
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.MatchNumberID = ""


class CTORATstpIPOMatchNumberResultField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpIPOMatchNumberResultField"
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Day = ""
        self.SecurityName = ""
        self.ShareholderID = ""
        self.SecurityType = ""
        self.MatchNumberID = ""
        self.Volume = 0
        self.Price = 0.0
        self.Amout = 0.0


class CTORATstpQryInnerBranchInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryInnerBranchInfoField"
        self.InnerBranchID = ""


class CTORATstpInnerBranchInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInnerBranchInfoField"
        self.InnerBranchID = ""
        self.InnerBranchName = ""


class CTORATstpQryDepartmentBranchInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryDepartmentBranchInfoField"
        self.DepartmentID = ""
        self.InnerBranchID = ""


class CTORATstpDepartmentBranchInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDepartmentBranchInfoField"
        self.DepartmentID = ""
        self.DepartmentName = ""
        self.InnerBranchID = ""
        self.InnerBranchName = ""


class CTORATstpQryDepartmentManageInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryDepartmentManageInfoField"
        self.ManageDepartmentID = ""
        self.InnerBranchID = ""


class CTORATstpDepartmentManageInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpDepartmentManageInfoField"
        self.ManageDepartmentID = ""
        self.DepartmentName = ""
        self.InnerBranchID = ""
        self.InnerBranchName = ""


class CTORATstpQryBrokerUserField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryBrokerUserField"
        self.UserID = ""
        self.DepartmentID = ""


class CTORATstpBrokerUserField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpBrokerUserField"
        self.UserID = ""
        self.UserName = ""
        self.UserType = ""
        self.Status = ""
        self.LoginLimit = 0
        self.PasswordFailLimit = 0
        self.DepartmentID = ""
        self.InnerBranchID = ""
        self.PasswordUpdatePeriod = 0
        self.PasswordRemainDays = 0
        self.ManageDepartmentID = ""


class CTORATstpQrySZSEImcParamsField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySZSEImcParamsField"
        self.MarketID = ""


class CTORATstpSZSEImcParamsField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSZSEImcParamsField"
        self.MarketID = ""
        self.OpenFlag = 0
        self.ThresholdAmount = 0.0
        self.PosAmt = 0.0
        self.AmountStatus = 0


class CTORATstpQrySZSEImcExchangeRateField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySZSEImcExchangeRateField"
        self.FromCurrency = ""
        self.ToCurrency = ""


class CTORATstpSZSEImcExchangeRateField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSZSEImcExchangeRateField"
        self.FromCurrency = ""
        self.ToCurrency = ""
        self.BidRate = 0.0
        self.OfferRate = 0.0
        self.MidPointRate = 0.0


class CTORATstpQrySZSEHKPriceTickInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySZSEHKPriceTickInfoField"
        self.PriceTickID = ""


class CTORATstpSZSEHKPriceTickInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSZSEHKPriceTickInfoField"
        self.PriceTickID = ""
        self.PriceTickGroupID = 0
        self.PriceTickType = ""
        self.BeginPrice = 0.0
        self.EndPrice = 0.0
        self.PriceTick = 0.0


class CTORATstpQryShareholderSpecPrivilegeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryShareholderSpecPrivilegeField"
        self.ExchangeID = ""
        self.ShareholderID = ""


class CTORATstpShareholderSpecPrivilegeField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpShareholderSpecPrivilegeField"
        self.ExchangeID = ""
        self.ShareholderID = ""
        self.MarketID = ""
        self.SpecPrivilegeType = ""
        self.Direction = ""
        self.bForbidden = 0
        self.InvestorID = ""


class CTORATstpQryInvestorPositionLimitField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryInvestorPositionLimitField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.SecurityID = ""


class CTORATstpInvestorPositionLimitField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpInvestorPositionLimitField"
        self.ExchangeID = ""
        self.InvestorID = ""
        self.SecurityID = ""
        self.BuyLimit = 0
        self.BuyFrozen = 0
        self.SellLimit = 0
        self.SellFrozen = 0
        self.PurchaseLimit = 0
        self.PurchaseFrozen = 0
        self.RedeemLimit = 0
        self.RedeemFrozen = 0
        self.PledgeInLimit = 0
        self.PledgeInFrozen = 0
        self.PledgeOutLimit = 0
        self.PledgeOutFrozen = 0
        self.ConvertLimit = 0
        self.ConvertFrozen = 0
        self.PutbackLimit = 0
        self.PutbackFrozen = 0
        self.RationalLimit = 0
        self.RationalFrozen = 0
        self.TotalPositionLimit = 0
        self.TotalPositionFrozen = 0


class CTORATstpQryPHMarketDataField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPHMarketDataField"
        self.SecurityID = ""
        self.ExchangeID = ""


class CTORATstpQrySecurityPriorAuthField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySecurityPriorAuthField"
        self.ExchangeID = ""
        self.ShareholderID = ""


class CTORATstpSecurityPriorAuthField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSecurityPriorAuthField"
        self.ExchangeID = ""
        self.MarketID = ""
        self.ShareholderID = ""
        self.SecurityID = ""
        self.Direction = ""
        self.bForbidden = 0


class CTORATstpQryRationalInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryRationalInfoField"
        self.ExchangeID = ""
        self.SecurityID = ""


class CTORATstpRationalInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpRationalInfoField"
        self.TradingDay = ""
        self.ExchangeID = ""
        self.SecurityID = ""
        self.Price = 0.0
        self.MarketID = ""
        self.ProductID = ""
        self.SecurityType = ""
        self.RationalLimit = 0
        self.SecurityName = ""
        self.UnderlyingSecurityID = ""
        self.UnderlyingSecurityName = ""
        self.RationalMinVol = 0
        self.RationalVolUnit = 0


class CTORATstpQryPeripheryFundTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQryPeripheryFundTransferDetailField"
        self.InvestorID = ""
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.TransferDirection = ""


class CTORATstpPeripheryFundTransferDetailField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpPeripheryFundTransferDetailField"
        self.FundSerial = 0
        self.ApplySerial = 0
        self.FrontID = 0
        self.SessionID = 0
        self.DepartmentID = ""
        self.AccountID = ""
        self.CurrencyID = ""
        self.TransferDirection = ""
        self.Amount = 0.0
        self.InvestorID = ""
        self.TransferStatus = ""
        self.TransferReason = ""
        self.OperateDate = ""
        self.OperateTime = ""
        self.RepealDate = ""
        self.RepealTime = ""
        self.RepealReason = ""
        self.StatusMsg = ""


class CTORATstpQrySystemNodeInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpQrySystemNodeInfoField"
        self.NodeID = 0


class CTORATstpSystemNodeInfoField():
    def __init__(self):
        self._module_ = "mdapi"
        self._clazz_ = "CTORATstpSystemNodeInfoField"
        self.NodeID = 0
        self.NodeInfo = ""
        self.bCurrent = 0

