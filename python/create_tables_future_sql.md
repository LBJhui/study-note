```sql






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