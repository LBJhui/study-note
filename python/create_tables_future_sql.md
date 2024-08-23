```sql
CREATE TABLE quant.`t_future_quantmarketdata`
(
    `TradingDay`          VARCHAR(8)     NOT NULL COMMENT '交易日',
    `ExchangeID`          VARCHAR(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`        VARCHAR(32)    NOT NULL COMMENT '合约代码',
    `FullInstrumentID`    VARCHAR(32)    NOT NULL COMMENT 'Full合约代码',
    `InstrumentName`      VARCHAR(128) NULL COMMENT '合约名称',
    `LastClosingPrice`    DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `OpeningPrice`        DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `ClosingPrice`        DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `TopPrice`            DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `FloorPrice`          DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `SettlementPrice`     DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `LastSettlementPrice` DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `UpperLimitPrice`     DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `LowerLimitPrice`     DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `TradingVolume`       DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `TradingAmount`       DECIMAL(26, 7) NOT NULL DEFAULT '0',
    `LastTradingDay`      VARCHAR(8) NULL COMMENT '上一交易日',
    PRIMARY KEY (`TradingDay`, `ExchangeID`, `InstrumentID`)
) COMMENT='期货回测行情信息';

SELECT @rowno1:=0;
SELECT @rowno2:=1;
update quant.t_future_quantmarketdata t,
    (select t1.tradingday, t2.tradingday as lasttradingday
    from
    (select tradingday, @rowno1 := @rowno1 + 1 as rowno from quant.t_future_quantmarketdata where exchangeid = '1' and securityid = '000001' order by tradingday) t1,
    (select tradingday, @rowno2 := @rowno2 + 1 as rowno from quant.t_future_quantmarketdata where exchangeid = '1' and securityid = '000001' order by tradingday) t2
    WHERE t1.rowno = t2.rowno) t3
set t.lasttradingday = t3.lasttradingday
where t.tradingday = t3.tradingday;






CREATE TABLE quant.`t_Future_QuantTrade`
(
    `HistoryNo`              BIGINT(10) NOT NULL COMMENT '回测ID',
    `TradingDay`             VARCHAR(8)     NOT NULL COMMENT '交易日',
    `TradeID`                VARCHAR(32)    NOT NULL COMMENT '成交ID',
    `TradeDate`              VARCHAR(8)     NOT NULL COMMENT '成交日期',
    `TradeTime`              VARCHAR(8)     NOT NULL COMMENT '成交时间',
    `ExchangeID`             VARCHAR(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`           VARCHAR(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`         VARCHAR(128) NULL COMMENT '合约名称',
    `FullInstrumentID`       VARCHAR(32)    NOT NULL COMMENT 'Full合约代码',
    `SpecInstrumentID`       VARCHAR(32)    NOT NULL COMMENT '标准合约代码',
    `Direction`              CHAR(1)        NOT NULL COMMENT '方向',
    `OffsetFlag`             CHAR(1)        NOT NULL COMMENT '开平标识',
    `HedgeFlag`              CHAR(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `Price`                  DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '成交价格',
    `Volume`                 BIGINT(16) NOT NULL DEFAULT '0' COMMENT '数量',
    `VolumeMultiple`         INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
    `OrderLocalID`           VARCHAR(32) NULL COMMENT '报单本地代码',
    `OrderSysID`             VARCHAR(32) NULL COMMENT '报单系统代码',
    `TradingAmount`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '成交金额',
    `TotalPosCost`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '成本',
    `TradingFee`             DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '交易费用',
    `BeforeTradeTodayAmount` DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '交易前今日资金',
    `AfterTradeTodayAmount`  DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '交易后今日资金',
    PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`,
                 `TradeID`)
) COMMENT='期货回测成交信息';


CREATE TABLE quant.`t_Future_QuantPosition`
(
    `HistoryNo`           BIGINT(10) NOT NULL COMMENT '回测ID',
    `TradingDay`          VARCHAR(8)     NOT NULL COMMENT '交易日',
    `ExchangeID`          VARCHAR(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`        VARCHAR(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`      VARCHAR(128) NULL COMMENT '合约名称',
    `FullInstrumentID`    VARCHAR(32)    NOT NULL COMMENT 'Full合约代码',
    `SpecInstrumentID`    VARCHAR(32)    NOT NULL COMMENT '标准合约代码',
    `PosiDirection`       CHAR(1)        NOT NULL DEFAULT '0' COMMENT '持仓方向',
    `HedgeFlag`           CHAR(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `PositionDate`        CHAR(1)        NOT NULL COMMENT '持仓日期 今日持仓 1 历史持仓 2',
    `Position`            BIGINT(16) NOT NULL DEFAULT '0' COMMENT '今日持仓',
    `YdPosition`          BIGINT(16) NOT NULL DEFAULT '0' COMMENT '上日持仓',
    `OpenVolume`          BIGINT(16) NOT NULL DEFAULT '0' COMMENT '开仓量',
    `CloseVolume`         BIGINT(16) NOT NULL DEFAULT '0' COMMENT '平仓量',
    `VolumeMultiple`      INTEGER(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
    `OpenAmount`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '开仓金额',
    `CloseAmount`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '平仓金额',
    `PositionCost`        DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '成本',
    `PreMargin`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '昨保证金',
    `UseMargin`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '保证金',
    `ExchangeMargin`      DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '交易所保证金',
    `Commission`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '手续费',
    `CloseProfit`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '平仓盈亏',
    `PositionProfit`      DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '持仓盈亏',
    `SettlementPrice`     DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '结算价',
    `LastSettlementPrice` DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '昨结算价',
    `OpenCost`            DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '开仓成本',
    `CloseProfitByDate`   DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '逐日盯市平仓盈亏',
    `CloseProfitByTrade`  DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '逐笔对冲平仓盈亏',
    `TodayPosition`       DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日持仓',
    `MarginRateByMoney`   DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '保证金率',
    `MarginRateByVolume`  DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '保证金率(按手数)',
    `Profit`              DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '盈亏',
    `TodayProfit`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日盈亏',
    `TodayBuyCapital`     DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日买金额',
    `TodaySellCapital`    DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日卖金额',
    `BuyCapital`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '买金额',
    `SellCapital`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '卖金额',
    `ReturnRatio`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '收益率',
    `ContributionRatio`   DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '贡献率',
    PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`,
                 `PosiDirection`, `HedgeFlag`)
) COMMENT='期货回测持仓信息'
;

CREATE TABLE quant.`t_Future_QuantAsset`
(
    `HistoryNo`           BIGINT(10) NOT NULL COMMENT '回测ID',
    `TradingDay`          VARCHAR(8)     NOT NULL COMMENT '交易日',
    `InitAmount`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '初始资金',
    `InitMargin`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '初始保证金',
    `InitAsset`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '初始总资产',
    `PreAmount`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '昨资金',
    `PreMargin`           DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '昨保证金',
    `PreAsset`            DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '昨总资产',
    `Amount`              DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '资金',
    `Margin`              DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '保证金',
    `TodayBuyCapital`     DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日买金额',
    `TodaySellCapital`    DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日卖金额',
    `TodayProfit`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '当日收益',
    `Profit`              DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '总收益',
    `TotalAsset`          DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '总资产',
    `ProfitRatio`         DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '收益率',
    `MaxTodayLongAmount`  DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日最大多头资产',
    `MaxTodayShortAmount` DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '今日最大空头资产',
    PRIMARY KEY (`HistoryNo`, `TradingDay`)
) COMMENT='期货回测资产信息'
;

CREATE TABLE quant.`t_Future_QuantProfit`
(
    `HistoryNo`         BIGINT(10) NOT NULL COMMENT '回测ID',
    `ExchangeID`        VARCHAR(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`      VARCHAR(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`    VARCHAR(128) NULL COMMENT '合约名称',
    `FullInstrumentID`  VARCHAR(32)    NOT NULL COMMENT 'Full合约代码',
    `SpecInstrumentID`  VARCHAR(32)    NOT NULL COMMENT '标准合约代码',
    `PosiDirection`     CHAR(1)        NOT NULL DEFAULT '0' COMMENT '持仓方向',
    `HedgeFlag`         CHAR(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `TradingCount`      BIGINT(10) NOT NULL DEFAULT '0' COMMENT '交易次数',
    `TradingFee`        DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '交易费用',
    `Profit`            DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '盈亏',
    `BuyCapital`        DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '买金额',
    `SellCapital`       DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '卖金额',
    `ReturnRatio`       DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '收益率',
    `ContributionRatio` DECIMAL(26, 7) NOT NULL DEFAULT '0' COMMENT '贡献率',
    PRIMARY KEY (`HistoryNo`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `PosiDirection`,
                 `HedgeFlag`)
) COMMENT='期货回测盈亏信息'
;


create table quant.t_QuantTestHistory
(
    HistoryNo                  bigInt(10) not null COMMENT '序列号',
    TestID                     varchar(20) binary not null COMMENT '客户回测历史标识',
    TestInvestorID             varchar(10) binary not null COMMENT '回测账号代码',
    TestUserID                 varchar(20) binary not null COMMENT '网站用户代码',
    StrategyName               varchar(60) binary not null COMMENT '策略名称',
    TestDate                   varchar(8) binary not null COMMENT '回测日期',
    TestTime                   varchar(8) binary not null COMMENT '回测时间',
    TestTradeDateBegin         varchar(8) binary not null COMMENT '策略回测起始日期',
    TestTradeDateEnd           varchar(8) binary not null COMMENT '策略回测终止日期',
    TestTradeDays              varchar(8) binary not null COMMENT '策略回测天数',
    TestKind                   char(1) binary not null COMMENT '回测类型',
    InitAsset                  decimal(19, 3) not null COMMENT '回测期初资金',
    Asset                      decimal(19, 3) not null COMMENT '回测期末资金',
    TestDataStatus             char(1) binary not null COMMENT '回测数据处理状态',
    TestDataFileStatus         char(1) binary not null COMMENT '回测数据文件状态',
    TestFimDataStatus          char(1) binary not null COMMENT 'fim数据状态',
    RiskfreeRate               decimal(14, 8) COMMENT '无风险收益率',
    RiskfreeDailyRate          decimal(14, 8) COMMENT '无风险每日利率均值',
    TotalReturns               decimal(14, 8) COMMENT '策略收益率',
    TotalAnnualizedReturns     decimal(14, 8) COMMENT '策略年化收益率',
    BenchmarkReturns           decimal(14, 8) COMMENT '基准收益率',
    BenchmarkAnnualizedReturns decimal(14, 8) COMMENT '基准年化收益率',
    Alpha                      decimal(14, 8) COMMENT 'Alpha',
    Beta                       decimal(14, 8) COMMENT 'Beta',
    Sharpe                     decimal(14, 8) COMMENT 'Sharpe',
    Retracement                decimal(14, 8) COMMENT '最大回撤率',
    PRIMARY KEY (HistoryNo)
) COMMENT='回测历史';

create table quant.t_ClientQuantTestProfit
(
    HistoryNo        bigInt(10) not null COMMENT '回测历史序列号',
    TradingDay       varchar(8) binary not null COMMENT '交易日',
    TradingTime      varchar(8) binary not null COMMENT '交易时间',
    LastAsset        decimal(19, 3) not null COMMENT '期初资金',
    Asset            decimal(19, 3) not null COMMENT '期末资金',
    DayProfit        decimal(19, 3) not null COMMENT '当日盈亏',
    DayBuyCapital    decimal(19, 3) not null COMMENT '当日买入',
    DaySellCapital   decimal(19, 3) not null COMMENT '当日卖出',
    TotalProfit      decimal(19, 3) not null COMMENT '累计收益',
    TotalProfitRatio decimal(14, 8) not null COMMENT '累计收益率',
    PRIMARY KEY (HistoryNo, TradingDay, TradingTime)
) COMMENT='客户回测资产收益';

```