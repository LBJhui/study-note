CREATE TABLE quant.`t_future_quantmarketdata` (
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`FullInstrumentID` VARCHAR(32) NOT NULL COMMENT 'Full合约代码',
	`InstrumentName` VARCHAR(128) NULL COMMENT '合约名称',
	`LastClosingPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`OpeningPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`ClosingPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`TopPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`FloorPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`SettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`LastSettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`UpperLimitPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`LowerLimitPrice` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`TradingVolume` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`TradingAmount` DECIMAL(26,7) NOT NULL DEFAULT '0',
	`LastTradingDay` VARCHAR(8) NULL COMMENT '上一交易日',
	PRIMARY KEY (`TradingDay`, `ExchangeID`, `InstrumentID`)
)
COMMENT='期货回测行情信息'
;

SELECT @rowno1:=0;
SELECT @rowno2:=1;
update quant.t_future_quantmarketdata t,
(select t1.tradingday, t2.tradingday as lasttradingday
from
(select tradingday, @rowno1:=@rowno1 + 1 as rowno from quant.t_future_quantmarketdata where exchangeid = '1' and securityid = '000001' order by tradingday) t1, 
(select tradingday, @rowno2:=@rowno2 + 1 as rowno from quant.t_future_quantmarketdata where exchangeid = '1' and securityid = '000001' order by tradingday) t2 
WHERE t1.rowno = t2.rowno) t3
set t.lasttradingday = t3.lasttradingday
where t.tradingday = t3.tradingday;

CREATE TABLE quant.`t_Future_SimTestInfo` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测编号',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`UserID` VARCHAR(20) NOT NULL COMMENT '用户代码',
	`InvestorID` VARCHAR(20) NOT NULL COMMENT '投资者代码',
	`QuantID` VARCHAR(32) NOT NULL COMMENT '回测ID',
	`TestID` VARCHAR(128) NOT NULL COMMENT '测试ID',
	`TestName` VARCHAR(128) NOT NULL COMMENT '测试名称',
	`MDFrequency` VARCHAR(20) NOT NULL COMMENT '行情频率',
	`InitalAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '初始资金',
	`TestBeginTime` VARCHAR(20) NOT NULL COMMENT '测试开始时间',
	`TestEndTime` VARCHAR(20) NOT NULL COMMENT '测试结束时间',
	`ActualMDBeginDate` VARCHAR(8) NOT NULL COMMENT '行情实际开始日期',
	`ActualMDEndDate` VARCHAR(8) NOT NULL COMMENT '行情实际结束日期',
	`SetMDBeginDate` VARCHAR(8) NOT NULL COMMENT '行情设置开始日期',
	`SetMDEndDate` VARCHAR(8) NOT NULL COMMENT '行情设置结束日期',
	`ManualID` BIGINT(10) NULL DEFAULT NULL COMMENT '成交单回测编号',
	PRIMARY KEY (`HistoryNo`, `BrokerID`, `UserID`, `QuantID`, `TestID`)
)
COMMENT='期货回测信息'
;

CREATE TABLE quant.`t_Future_SimTestInitPosition` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`OpenDate` VARCHAR(8) NOT NULL COMMENT '开仓交易日',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`PosiDirection` CHAR(1) NOT NULL COMMENT '持仓方向',
	`Volume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '持仓数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OpenPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓价格',
	`InstrumentType` CHAR(1) NOT NULL COMMENT '合约类型',
	PRIMARY KEY (`HistoryNo`, `OpenDate`, `ExchangeID`, `InstrumentID`, `PosiDirection`)
)
COMMENT='期货回测初始持仓信息'
;

CREATE TABLE quant.`t_Future_SimTestTrade` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`TradeDate` VARCHAR(8) NOT NULL COMMENT '成交日期',
	`TradeTime` VARCHAR(8) NOT NULL COMMENT '成交时间',
	`TradeID` VARCHAR(32) NOT NULL COMMENT '成交ID',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`InvestorID` VARCHAR(20) NOT NULL COMMENT '投资者代码',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`Direction` CHAR(1) NOT NULL COMMENT '买卖方向',
	`OffsetFlag` CHAR(1) NOT NULL COMMENT '开平标识',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识',
	`TradingRole` CHAR(1) NOT NULL COMMENT '交易角色 代理 1 自营 2 做市商 3',
	`Volume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '成交数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`Price` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成交价格',
	`Commission` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '手续费',
	`TradeMDUpTime` VARCHAR(20) NOT NULL COMMENT '回测中驱动本次成交的行情',
	`PriceSource` CHAR(1) NOT NULL COMMENT '成交价来源 前成交价 0 买委托价 1 卖委托价 2',
	`OrderLocalID` VARCHAR(32) NOT NULL COMMENT '报单本地代码',
	`OrderSysID` VARCHAR(32) NOT NULL COMMENT '报单系统代码',
	`OrderRef` VARCHAR(32) NOT NULL COMMENT '报单引用',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `TradeID`, `ExchangeID`, `InstrumentID`, `OrderSysID`)
)
COMMENT='期货回测成交信息'
;

CREATE TABLE quant.`t_Future_SimTestOrder` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`InvestorID` VARCHAR(20) NOT NULL COMMENT '投资者代码',
	`AccountID` VARCHAR(20) NOT NULL COMMENT '资金账号',
	`CurrencyID` VARCHAR(20) NOT NULL COMMENT '币种代码',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`Direction` CHAR(1) NOT NULL COMMENT '买卖方向',
	`OffsetFlag` CHAR(1) NOT NULL COMMENT '开平标识',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识',
	`OrderPriceType` CHAR(1) NOT NULL COMMENT '报单价格类型',
	`TimeCondition` CHAR(1) NOT NULL COMMENT '报单有效期类型 立即完成，否则撤销  1 本节有效  2 当日有效  3 指定日期前有效  4 撤销前有效  5 集合竞价有效  6',
	`VolumeCondition` CHAR(1) NOT NULL COMMENT '报单成交数量类型 任何数量 1 最小数量 2 全部数量 3',
	`ContingentCondition` CHAR(1) NOT NULL COMMENT '触发条件 立即 1 止损 2 止赢 3 预埋单 4 最新价大于条件价 5 最新价大于等于条件价 6 最新价小于条件价 7 最新价小于等于条件价 8 卖一价大于条件价 9 卖一价大于等于条件价 A 卖一价小于条件价 B 卖一价小于等于条件价 C 买一价大于条件价 D 买一价大于等于条件价 E 买一价小于条件价 F 买一价小于等于条件价 H',
	`LimitPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '价格',
	`StopPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '止损价',
	`VolumeTotalOriginal` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '委托数量',
	`ForceCloseReason` CHAR(1) NOT NULL COMMENT '强平原因 非强平 0 资金不足 1 客户超仓 2 会员超仓 3 持仓非整数倍 4 违规 5 其它 6 自然人临近交割 7',
	`OrderLocalID` VARCHAR(32) NOT NULL COMMENT '报单本地代码',
	`OrderSysID` VARCHAR(32) NOT NULL COMMENT '报单系统代码',
	`OrderRef` VARCHAR(32) NOT NULL COMMENT '报单引用',
	`OrderStatus` CHAR(1) NOT NULL COMMENT '报单状态',
	`OrderSource` CHAR(1) NOT NULL COMMENT '报单来源 来自参与者 0 来自管理员 1',
	`OrderType` CHAR(1) NOT NULL COMMENT '报单类型 正常 0 报价衍生 1 组合衍生 2 组合报单 3 条件单 4 互换单 5 大宗交易成交衍生 6 期转现成交衍生 7',
	`MinVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '最小成交量',
	`VolumeTraded` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '成交数量',
	`VolumeTotal` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '成交数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`RequestID` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '请求编号',
	`GTDDate` VARCHAR(8) NULL COMMENT 'GTD日期',
	`InsertDate` VARCHAR(8) NOT NULL COMMENT '报单日期',
	`InsertTime` VARCHAR(8) NOT NULL COMMENT '报单时间',
	`UpdateTime` VARCHAR(8) NULL COMMENT '更新时间',
	`CancelTime` VARCHAR(8) NULL COMMENT '撤单时间',
	`TradeAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成交金额',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `OrderLocalID`, `OrderSysID`)
)
COMMENT='期货回测报单信息'
;

CREATE TABLE quant.`t_Future_SimTestPosition` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`InvestorID` VARCHAR(20) NOT NULL COMMENT '投资者代码',
	`InvestUnitID` VARCHAR(20) NULL COMMENT '投资单位代码',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`PosiDirection` CHAR(1) NOT NULL COMMENT '持仓方向',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识',
	`PositionDate` CHAR(1) NOT NULL COMMENT '持仓日期',
	`YdPosition` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '昨持仓数量',
	`Position` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '持仓数量',
	`OpenVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '开仓数量',
	`CloseVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '平仓数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OpenAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓金额',
	`CloseAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓金额',
	`ClosePrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '合约收盘价',
	`PositionCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '持仓成本',
	`PreMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨保证金',
	`UseMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金',
	`CashIn` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '资金差额',
	`Commission` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易费用',
	`CloseProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓收益',
	`PositionProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '持仓收益',
	`PreSettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨结算价格',
	`SettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '结算价格',
	`SettlementID` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '结算编号',
	`OpenCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓成本',
	`ExchangeMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易所保证金',
	`CombPosition` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '组合成交形成的持仓',
	`CloseProfitByDate` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐日盯市平仓盈亏',
	`CloseProfitByTrade` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐笔对冲平仓收益',
	`TodayPosition` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '今日持仓',
	`MarginRateByMoney` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金率',
	`MarginRateByVolume` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '按手保证金率',
	`PositionCostOffset` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '持仓成本差值',
	`TasPosition` BIGINT(16) NOT NULL DEFAULT '0' COMMENT 'tas持仓手数',
	`TasPositionCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT 'tas持仓成本',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `BrokerID`, `InvestorID`, `ExchangeID`, `InstrumentID`, `PosiDirection`)
)
COMMENT='期货回测持仓信息'
;

CREATE TABLE quant.`t_Future_SimTestPositionDetail` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`InvestorID` VARCHAR(20) NOT NULL COMMENT '投资者代码',
	`InvestUnitID` VARCHAR(20) NULL COMMENT '投资单位代码',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`Direction` CHAR(1) NOT NULL COMMENT '买卖方向',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识',
	`OpenDate` VARCHAR(8) NOT NULL COMMENT '开仓日期',
	`TradeID` VARCHAR(32) NOT NULL COMMENT '成交ID',
	`Volume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OpenPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓价格',
	`SettlementID` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '结算编号',
	`CloseProfitByDate` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐日盯市平仓盈亏',
	`CloseProfitByTrade` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐笔对冲平仓收益',
	`PositionProfitByDate` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐日盯市持仓盈亏',
	`PositionProfitByTrade` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐笔对冲持仓盈亏',
	`Margin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '投资者保证金',
	`ExchMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易所保证金',
	`MarginRateByMoney` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金率',
	`MarginRateByVolume` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '按手保证金率',
	`LastSettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨结算价格',
	`SettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '结算价格',
	`CloseVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '平仓数量',
	`CloseAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓金额',
	`TimeFirstVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '先开先平剩余数量',
	`SpecPosiType` CHAR(1) NOT NULL COMMENT '特殊持仓标志 普通持仓明细 # TAS合约成交产生的标的合约持仓明细 0',
	`CombInstrumentID` VARCHAR(32) NULL COMMENT '组合合约代码',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `BrokerID`, `InvestorID`, `ExchangeID`, `InstrumentID`, `Direction`, `OpenDate`, `TradeID`)
)
COMMENT='期货回测持仓明细信息'
;

CREATE TABLE quant.`t_Future_SimTestSubMD` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`InstrumentType` CHAR(1) NOT NULL COMMENT '合约类型',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`)
)
COMMENT='期货回测行情订阅信息'
;

CREATE TABLE quant.`t_Future_SimTestTradingAccount` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`BrokerID` VARCHAR(8) NOT NULL COMMENT '会员代码',
	`AccountID` VARCHAR(20) NOT NULL COMMENT '资金账号',
	`CurrencyID` VARCHAR(20) NOT NULL COMMENT '币种代码',
	`BizType` CHAR(1) NOT NULL COMMENT '业务类型 期货：1 证券：2',
	`PreMortgage` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次质押金额',
	`PreCredit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次信用额度',
	`PreDeposit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次存款额',
	`PreBalance` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次结算准备金',
	`PreMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次占用的保证金',
	`InterestBase` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '利息基数',
	`Interest` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '利息收入',
	`Deposit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '入金金额',
	`Withdraw` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '出金金额',
	`CurrMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '当前保证金总额',
	`CashIn` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '资金差额',
	`Commission` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '手续费',
	`CloseProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓盈亏',
	`PositionProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '持仓盈亏',
	`Balance` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '期货结算准备金',
	`Available` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '可用资金',
	`WithdrawQuota` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '可取资金',
	`Reserve` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '基本准备金',
	`Credit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '信用额度',
	`Mortgage` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '质押金额',
	`ExchangeMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易所保证金',
	`DeliveryMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '投资者交割保证金',
	`ExchangeDeliveryMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易所交割保证金',
	`ReserveBalance` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保底期货结算准备',
	`PreFundMortgageIn` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次货币质入金额',
	`PreFundMortgageOut` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '上次货币质出金额',
	`FundMortgageIn` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '货币质入金额',
	`FundMortgageOut` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '货币质出金额',
	`FundMortgageAvailable` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '货币质押余额',
	`MortgageableFund` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '可质押货币金额',
	`SpecProductMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '特殊产品占用保证金',
	`SpecProductCommission` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '特殊产品手续费',
	`SpecProductPositionProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '特殊产品持仓盈亏',
	`SpecProductCloseProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '特殊产品平仓盈亏',
	`SpecProductPositionProfitByAlg` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '根据持仓盈亏算法计算的特殊产品持仓盈亏',
	`SpecProductExchangeMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '特殊产品交易所保证金',
	`FrozenSwap` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '延时换汇冻结金额',
	`RemainSwap` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '剩余换汇额度',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `BrokerID`, `AccountID`, `CurrencyID`)
)
COMMENT='期货回测账户信息'
;

CREATE TABLE quant.`t_Future_QuantOrder` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`InstrumentName` VARCHAR(128) NULL COMMENT '合约名称',
	`FullInstrumentID` VARCHAR(32) NOT NULL COMMENT 'Full合约代码',
	`SpecInstrumentID` VARCHAR(32) NOT NULL COMMENT '标准合约代码',
	`Direction` CHAR(1) NOT NULL COMMENT '方向 买 0 卖 1',
	`OffsetFlag` CHAR(1) NOT NULL COMMENT '开平标识 开仓 0 平仓 1 强平 2 平今 3 平昨 4 强减 5 本地强平 6',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
	`OrderPriceType` CHAR(1) NOT NULL COMMENT '报单价格类型 任意价 1 限价 2 最优价 3 最新价 4 卖一价 8 买一价  C 五档价  G',
	`TimeCondition` CHAR(1) NOT NULL COMMENT '报单有效期类型 立即完成，否则撤销  1 本节有效  2 当日有效  3 指定日期前有效  4 撤销前有效  5 集合竞价有效  6',
	`VolumeCondition` CHAR(1) NOT NULL COMMENT '报单成交数量类型 任何数量 1 最小数量 2 全部数量 3',
	`ContingentCondition` CHAR(1) NOT NULL COMMENT '触发条件 立即 1 止损 2 止赢 3 预埋单 4 最新价大于条件价 5 最新价大于等于条件价 6 最新价小于条件价 7 最新价小于等于条件价 8 卖一价大于条件价 9 卖一价大于等于条件价 A 卖一价小于条件价 B 卖一价小于等于条件价 C 买一价大于条件价 D 买一价大于等于条件价 E 买一价小于条件价 F 买一价小于等于条件价 H',
	`SimOrderType` CHAR(1) NULL COMMENT '报单类型',
	`LimitPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '价格',
	`Volume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OrderLocalID` VARCHAR(32) NOT NULL COMMENT '报单本地代码',
	`OrderSysID` VARCHAR(32) NOT NULL COMMENT '报单系统代码',
	`OrderStatus` CHAR(1) NOT NULL COMMENT '报单状态',
	`VolumeTraded` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '成交数量',
	`InsertTime` VARCHAR(8) NOT NULL COMMENT '报单时间',
	`InsertMillisec` INTEGER(3) NOT NULL COMMENT '报单时间毫秒',
	`CancelTime` VARCHAR(8) NULL COMMENT '撤单时间',
	`Turnover` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成交金额',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `OrderLocalID`, `OrderSysID`)
)
COMMENT='期货回测报单信息'
;

CREATE TABLE quant.`t_Future_QuantTrade` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`TradeID` VARCHAR(32) NOT NULL COMMENT '成交ID',
	`TradeDate` VARCHAR(8) NOT NULL COMMENT '成交日期',
	`TradeTime` VARCHAR(8) NOT NULL COMMENT '成交时间',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`InstrumentName` VARCHAR(128) NULL COMMENT '合约名称',
	`FullInstrumentID` VARCHAR(32) NOT NULL COMMENT 'Full合约代码',
	`SpecInstrumentID` VARCHAR(32) NOT NULL COMMENT '标准合约代码',
	`Direction` CHAR(1) NOT NULL COMMENT '方向',
	`OffsetFlag` CHAR(1) NOT NULL COMMENT '开平标识',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
	`Price` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成交价格',
	`Volume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '数量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OrderLocalID` VARCHAR(32) NULL COMMENT '报单本地代码',
	`OrderSysID` VARCHAR(32) NULL COMMENT '报单系统代码',
	`TradingAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成交金额',
	`TotalPosCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成本',
	`TradingFee` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易费用',
	`BeforeTradeTodayAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易前今日资金',
	`AfterTradeTodayAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易后今日资金',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `TradeID`)
)
COMMENT='期货回测成交信息'
;


CREATE TABLE quant.`t_Future_QuantPosition` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`InstrumentName` VARCHAR(128) NULL COMMENT '合约名称',
	`FullInstrumentID` VARCHAR(32) NOT NULL COMMENT 'Full合约代码',
	`SpecInstrumentID` VARCHAR(32) NOT NULL COMMENT '标准合约代码',
	`PosiDirection` CHAR(1) NOT NULL DEFAULT '0' COMMENT '持仓方向',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
	`PositionDate` CHAR(1) NOT NULL COMMENT '持仓日期 今日持仓 1 历史持仓 2',
	`Position` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '今日持仓',
	`YdPosition` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '上日持仓',
	`OpenVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '开仓量',
	`CloseVolume` BIGINT(16) NOT NULL DEFAULT '0' COMMENT '平仓量',
	`VolumeMultiple` INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
	`OpenAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓金额',
	`CloseAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓金额',
	`PositionCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '成本',
	`PreMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨保证金',
	`UseMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金',
	`ExchangeMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易所保证金',
	`Commission` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '手续费',
	`CloseProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '平仓盈亏',
	`PositionProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '持仓盈亏',
	`SettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '结算价',
	`LastSettlementPrice` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨结算价',
	`OpenCost` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '开仓成本',
	`CloseProfitByDate` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐日盯市平仓盈亏',
	`CloseProfitByTrade` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '逐笔对冲平仓盈亏',
	`TodayPosition` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日持仓',
	`MarginRateByMoney` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金率',
	`MarginRateByVolume` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金率(按手数)',
	`Profit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '盈亏',
	`TodayProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日盈亏',
	`TodayBuyCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日买金额',
	`TodaySellCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日卖金额',
	`BuyCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '买金额',
	`SellCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '卖金额',
	`ReturnRatio` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '收益率',
	`ContributionRatio` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '贡献率',
	PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `PosiDirection`, `HedgeFlag`)
)
COMMENT='期货回测持仓信息'
;

CREATE TABLE quant.`t_Future_QuantAsset` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`TradingDay` VARCHAR(8) NOT NULL COMMENT '交易日',
	`InitAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '初始资金',
	`InitMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '初始保证金',
	`InitAsset` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '初始总资产',
	`PreAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨资金',
	`PreMargin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨保证金',
	`PreAsset` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '昨总资产',
	`Amount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '资金',
	`Margin` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '保证金',
	`TodayBuyCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日买金额',
	`TodaySellCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日卖金额',
	`TodayProfit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '当日收益',
	`Profit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '总收益',
	`TotalAsset` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '总资产',
	`ProfitRatio` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '收益率',
	`MaxTodayLongAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日最大多头资产',
	`MaxTodayShortAmount` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '今日最大空头资产',
	PRIMARY KEY (`HistoryNo`, `TradingDay`)
)
COMMENT='期货回测资产信息'
;

CREATE TABLE quant.`t_Future_QuantProfit` (
	`HistoryNo` BIGINT(10) NOT NULL COMMENT '回测ID',
	`ExchangeID` VARCHAR(8) NOT NULL COMMENT '交易所代码',
	`InstrumentID` VARCHAR(32) NOT NULL COMMENT '合约代码',
	`InstrumentName` VARCHAR(128) NULL COMMENT '合约名称',
	`FullInstrumentID` VARCHAR(32) NOT NULL COMMENT 'Full合约代码',
	`SpecInstrumentID` VARCHAR(32) NOT NULL COMMENT '标准合约代码',
	`PosiDirection` CHAR(1) NOT NULL DEFAULT '0' COMMENT '持仓方向',
	`HedgeFlag` CHAR(1) NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
	`TradingCount` BIGINT(10) NOT NULL DEFAULT '0' COMMENT '交易次数',
	`TradingFee` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '交易费用',
	`Profit` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '盈亏',
	`BuyCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '买金额',
	`SellCapital` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '卖金额',
	`ReturnRatio` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '收益率',
	`ContributionRatio` DECIMAL(26,7) NOT NULL DEFAULT '0' COMMENT '贡献率',
	PRIMARY KEY (`HistoryNo`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `PosiDirection`, `HedgeFlag`)
)
COMMENT='期货回测盈亏信息'
;
