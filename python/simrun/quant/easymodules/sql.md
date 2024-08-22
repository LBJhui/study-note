# 回测报单信息 t_future_quantorder

```sql
CREATE TABLE `t_future_quantorder`
(
    `HistoryNo`           bigint(10) NOT NULL COMMENT '回测ID',
    `TradingDay`          varchar(8)     NOT NULL COMMENT '交易日',
    `ExchangeID`          varchar(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`        varchar(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`      varchar(128)            DEFAULT NULL COMMENT '合约名称',
    `FullInstrumentID`    varchar(32)    NOT NULL COMMENT 'Full合约代码',
    #                     InstrumentID + '.' + ExchangeID
        `SpecInstrumentID` varchar (32) NOT NULL COMMENT '标准合约代码',
    #                     InstrumentID + '.' + ExchangeID
        `Direction` char (1) NOT NULL COMMENT '方向 买 0 卖 1',
    `OffsetFlag`          char(1)        NOT NULL COMMENT '开平标识 开仓 0 平仓 1 强平 2 平今 3 平昨 4 强减 5 本地强平 6',
    `HedgeFlag`           char(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `OrderPriceType`      char(1)        NOT NULL COMMENT '报单价格类型 任意价 1 限价 2 最优价 3 最新价 4 卖一价 8 买一价  C 五档价  G',
    `TimeCondition`       char(1)        NOT NULL COMMENT '报单有效期类型 立即完成，否则撤销  1 本节有效  2 当日有效  3 指定日期前有效  4 撤销前有效  5 集合竞价有效  6',
    `VolumeCondition`     char(1)        NOT NULL COMMENT '报单成交数量类型 任何数量 1 最小数量 2 全部数量 3',
    `ContingentCondition` char(1)        NOT NULL COMMENT '触发条件 立即 1 止损 2 止赢 3 预埋单 4 最新价大于条件价 5 最新价大于等于条件价 6 最新价小于条件价 7 最新价小于等于条件价 8 卖一价大于条件价 9 卖一价大于等于条件价 A 卖一价小于条件价 B 卖一价小于等于条件价 C 买一价大于条件价 D 买一价大于等于条件价 E 买一价小于条件价 F 买一价小于等于条件价 H',
    `SimOrderType`        char(1)                 DEFAULT NULL COMMENT '报单类型',
    `LimitPrice`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '价格',
    `Volume`              bigint(16) NOT NULL DEFAULT '0' COMMENT '数量',
    #                     VolumeTotalOriginal
        `VolumeMultiple` int (6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
    `OrderLocalID`        varchar(32)    NOT NULL COMMENT '报单本地代码',
    `OrderSysID`          varchar(32)    NOT NULL COMMENT '报单系统代码',
    `OrderStatus`         char(1)        NOT NULL COMMENT '报单状态',
    `VolumeTraded`        bigint(16) NOT NULL DEFAULT '0' COMMENT '成交数量',
    `InsertTime`          varchar(8)     NOT NULL COMMENT '报单时间',
    `InsertMillisec`      int(3) NOT NULL COMMENT '报单时间毫秒',
    `CancelTime`          varchar(8)              DEFAULT NULL COMMENT '撤单时间',
    `Turnover`            decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '成交金额',
    #                     TradeAmount
        PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`,
        `SpecInstrumentID`, `OrderLocalID`, `OrderSysID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回测报单信息';
```

# 回测成交信息 t_future_quanttrade

```sql
CREATE TABLE `t_future_quanttrade`
(
    `HistoryNo`             bigint(10) NOT NULL COMMENT '回测ID',
    `TradingDay`            varchar(8)     NOT NULL COMMENT '交易日',
    `TradeID`               varchar(32)    NOT NULL COMMENT '成交ID',
    `TradeDate`             varchar(8)     NOT NULL COMMENT '成交日期',
    `TradeTime`             varchar(8)     NOT NULL COMMENT '成交时间',
    `ExchangeID`            varchar(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`          varchar(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`        varchar(128)            DEFAULT NULL COMMENT '合约名称',
    `FullInstrumentID`      varchar(32)    NOT NULL COMMENT 'Full合约代码',
    #                       CONCAT(t.InstrumentID, '.', t.ExchangeID)
        `SpecInstrumentID` varchar (32) NOT NULL COMMENT '标准合约代码',
    #                       CONCAT(t.InstrumentID, '.', t.ExchangeID)
        `Direction` char (1) NOT NULL COMMENT '方向',
    `OffsetFlag`            char(1)        NOT NULL COMMENT '开平标识',
    `HedgeFlag`             char(1)        NOT NULL,
    `Price`                 decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '成交价格',
    `Volume`                bigint(16) NOT NULL DEFAULT '0' COMMENT '数量',
    `VolumeMultiple`        int(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
    `OrderLocalID`          varchar(32)             DEFAULT NULL COMMENT '报单本地代码',
    `OrderSysID`            varchar(32)             DEFAULT NULL COMMENT '报单系统代码',
    `TradingAmount`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '成交金额',
    #                       t.Price * t.Volume * t.VolumeMultiple
        `TotalPosCost` decimal (26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '成本',
    #                       t.Price * t.Volume * t.VolumeMultiple + t.Commission
        `TradingFee` decimal (26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '交易费用',
    #                       Commission
        `BeforeTradeTodayAmount` decimal (26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '交易前今日资金',
    `AfterTradeTodayAmount` decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '交易后今日资金',
    PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`,
                 `TradeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回测成交信息';
```

# 回测资产信息 t_future_quantasset

```sql
CREATE TABLE `t_future_quantasset`
(
    `HistoryNo`           bigint(10) NOT NULL COMMENT '回测ID',
    `TradingDay`          varchar(8)     NOT NULL COMMENT '交易日',
    `InitAmount`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '初始资金',
    `InitMargin`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '初始保证金',
    `InitAsset`           decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '初始总资产',
    `PreAmount`           decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '昨资金',
    `PreMargin`           decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '昨保证金',
    `PreAsset`            decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '昨总资产',
    `Amount`              decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '资金',
    `Margin`              decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '保证金',
    `TodayBuyCapital`     decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日买金额',
    `TodaySellCapital`    decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日卖金额',
    `TodayProfit`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '当日收益',
    `Profit`              decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '总收益',
    `TotalAsset`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '总资产',
    `ProfitRatio`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '收益率',
    `MaxTodayLongAmount`  decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日最大多头资产',
    `MaxTodayShortAmount` decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日最大空头资产',
    PRIMARY KEY (`HistoryNo`, `TradingDay`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回测资产信息';
```

```sql
INSERT INTO quant.t_Future_QuantAsset(HistoryNo, TradingDay, InitAmount, InitMargin, InitAsset, PreAmount, PreMargin,
                                      PreAsset, Amount, Margin, TodayBuyCapital, TodaySellCapital, TodayProfit, Profit,
                                      TotalAsset, ProfitRatio, MaxTodayLongAmount, MaxTodayShortAmount)
SELECT t.HistoryNo,
       t.TradingDay,
       SUM(t.InitAmount)                                             AS InitAmount,
       SUM(t.InitMargin)                                             AS InitMargin,
       SUM(t.InitAsset)                                              AS InitAsset,
       SUM(t.PreAmount)                                              AS PreAmount,
       SUM(t.PreMargin)                                              AS PreMargin,
       SUM(t.PreAsset)                                               AS PreAsset,
       SUM(t.Amount)                                                 AS Amount,
       SUM(t.Margin)                                                 AS Margin,
       SUM(IFNULL(tt.TodayBuyCapital, 0))                            AS TodayBuyCapital,
       SUM(IFNULL(tt.TodaySellCapital, 0))                           AS TodaySellCapital,
       SUM(t.TodayProfit)                                            AS TodayProfit,
       SUM(t.Profit)                                                 AS Profit,
       SUM(t.TotalAsset)                                             AS TotalAsset,
       IF(SUM(t.InitAsset) = 0, 0, SUM(t.Profit) / SUM(t.InitAsset)) AS ProfitRatio,
       SUM(t.MaxTodayLongAmount)                                     AS MaxTodayLongAmount,
       SUM(t.MaxTodayShortAmount)                                    AS MaxTodayShortAmount
FROM (SELECT t.HistoryNo,
             t.TradingDay,
             SUM(t.InitAmount)          AS InitAmount,
             SUM(t.InitMargin)          AS InitMargin,
             SUM(t.InitAsset)           AS InitAsset,
             SUM(t.PreAmount)           AS PreAmount,
             SUM(t.PreMargin)           AS PreMargin,
             SUM(t.PreAsset)            AS PreAsset,
             SUM(t.Amount)              AS Amount,
             SUM(t.Margin)              AS Margin,
             SUM(t.TodayProfit)         AS TodayProfit,
             SUM(t.Profit)              AS Profit,
             SUM(t.TotalAsset)          AS TotalAsset,
             SUM(t.MaxTodayLongAmount)  AS MaxTodayLongAmount,
             SUM(t.MaxTodayShortAmount) AS MaxTodayShortAmount
      FROM (SELECT t.HistoryNo,
                   t.TradingDay,
                   t4.InitAmount,
                   t4.InitMargin,
                   t4.InitAmount             AS InitAsset,
                   t.PreBalance              AS PreAmount,
                   0                         AS PreMargin,
                   t.PreBalance              AS PreAsset,
                   t.Balance                 AS Amount,
                   t.CurrMargin              AS Margin,
                   t.Balance - t.PreBalance  AS TodayProfit,
                   t.Balance - t4.InitAmount AS Profit,
                   t.Balance                 AS TotalAsset,
                   0                         AS MaxTodayLongAmount,
                   0                         AS MaxTodayShortAmount
            FROM quant.t_Future_SimTestTradingAccount t
                     JOIN (SELECT DISTINCT TradingDay FROM quant.t_future_quantmarketdata WHERE ExchangeID = 'SHFE') t3
                          ON (t.TradingDay = t3.TradingDay)
                     JOIN (SELECT t.TradingDay, t.PreBalance AS InitAmount, t.PreMargin AS InitMargin
                           FROM quant.t_Future_SimTestTradingAccount t
                           WHERE t.HistoryNo = #{history_no}
                           ORDER BY t.TradingDay Limit 1) t4
            WHERE t.HistoryNo = #{history_no}) t
      GROUP BY t.HistoryNo, t.TradingDay) t
         LEFT JOIN (SELECT t.HistoryNo,
                           t.TradingDay,
                           SUM(IFNULL(IF((t.Direction = '0' AND t.OffsetFlag = '0') OR
                                         (t.Direction = '1' AND t.OffsetFlag = '1'),
                                         t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodayBuyCapital,
                           SUM(IFNULL(IF((t.Direction = '0' AND t.OffsetFlag = '1') OR
                                         (t.Direction = '1' AND t.OffsetFlag = '0'),
                                         t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodaySellCapital
                    FROM quant.t_Future_QuantTrade t
                    WHERE t.HistoryNo = #{history_no}
                    GROUP BY t.HistoryNo, t.TradingDay) tt
                   ON (t.HistoryNo = tt.HistoryNo AND t.TradingDay = tt.TradingDay)
GROUP BY t.HistoryNo, t.TradingDay
```

# 回测持仓信息 t_future_quantposition

```sql
CREATE TABLE `t_future_quantposition`
(
    `HistoryNo`           bigint(10) NOT NULL COMMENT '回测ID',
    `TradingDay`          varchar(8)     NOT NULL COMMENT '交易日',
    `ExchangeID`          varchar(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`        varchar(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`      varchar(128)            DEFAULT NULL COMMENT '合约名称',
    `FullInstrumentID`    varchar(32)    NOT NULL COMMENT 'Full合约代码',
    `SpecInstrumentID`    varchar(32)    NOT NULL COMMENT '标准合约代码',
    `PosiDirection`       char(1)        NOT NULL DEFAULT '0' COMMENT '持仓方向',
    `HedgeFlag`           char(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `PositionDate`        char(1)        NOT NULL COMMENT '持仓日期 今日持仓 1 历史持仓 2',
    `Position`            bigint(16) NOT NULL DEFAULT '0' COMMENT '今日持仓',
    `YdPosition`          bigint(16) NOT NULL DEFAULT '0' COMMENT '上日持仓',
    `OpenVolume`          bigint(16) NOT NULL DEFAULT '0' COMMENT '开仓量',
    `CloseVolume`         bigint(16) NOT NULL DEFAULT '0' COMMENT '平仓量',
    `VolumeMultiple`      int(6) NOT NULL DEFAULT '1' COMMENT '标的乘数',
    `OpenAmount`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '开仓金额',
    `CloseAmount`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '平仓金额',
    `PositionCost`        decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '成本',
    `PreMargin`           decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '昨保证金',
    `UseMargin`           decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '保证金',
    `ExchangeMargin`      decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '交易所保证金',
    `Commission`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '手续费',
    `CloseProfit`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '平仓盈亏',
    `PositionProfit`      decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '持仓盈亏',
    `SettlementPrice`     decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '结算价',
    `LastSettlementPrice` decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '昨结算价',
    `OpenCost`            decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '开仓成本',
    `CloseProfitByDate`   decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '逐日盯市平仓盈亏',
    `CloseProfitByTrade`  decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '逐笔对冲平仓盈亏',
    `TodayPosition`       decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日持仓',
    `MarginRateByMoney`   decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '保证金率',
    `MarginRateByVolume`  decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '保证金率(按手数)',
    `Profit`              decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '盈亏',
    `TodayProfit`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日盈亏',
    `TodayBuyCapital`     decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日买金额',
    `TodaySellCapital`    decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '今日卖金额',
    `BuyCapital`          decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '买金额',
    `SellCapital`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '卖金额',
    `ReturnRatio`         decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '收益率',
    `ContributionRatio`   decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '贡献率',
    PRIMARY KEY (`HistoryNo`, `TradingDay`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`,
                 `PosiDirection`, `HedgeFlag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回测持仓信息';
```

```sql
INSERT INTO quant.t_Future_QuantPosition(HistoryNo, TradingDay, ExchangeID, InstrumentID, InstrumentName,
                                         FullInstrumentID, SpecInstrumentID, PosiDirection, HedgeFlag, PositionDate,
                                         Position, YdPosition, OpenVolume, CloseVolume, VolumeMultiple, OpenAmount,
                                         CloseAmount, PositionCost, PreMargin, UseMargin, ExchangeMargin, Commission,
                                         CloseProfit, PositionProfit, SettlementPrice, LastSettlementPrice, OpenCost,
                                         CloseProfitByDate, CloseProfitByTrade, TodayPosition, MarginRateByMoney,
                                         MarginRateByVolume, Profit, TodayProfit, TodayBuyCapital, TodaySellCapital,
                                         BuyCapital, SellCapital, ReturnRatio, ContributionRatio)
SELECT t.HistoryNo,
       t.TradingDay,
       t.ExchangeID,
       t.InstrumentID,
       t3.InstrumentName                                                                           AS InstrumentName,
       CONCAT(t.InstrumentID, '.', t.ExchangeID)                                                   AS FullInstrumentID,
       CONCAT(t.InstrumentID, '.', t.ExchangeID)                                                   AS SpecInstrumentID,
       t.PosiDirection,
       t.HedgeFlag,
       t.PositionDate,
       t.Position,
       t.YdPosition,
       t.OpenVolume,
       t.CloseVolume,
       t.VolumeMultiple,
       t.OpenAmount,
       t.CloseAmount,
       t.PositionCost,
       t.PreMargin,
       t.UseMargin,
       t.ExchangeMargin,
       t.Commission,
       t.CloseProfit,
       t.PositionProfit,
       t.SettlementPrice,
       t3.LastSettlementPrice,
       t.OpenCost,
       t.CloseProfitByDate,
       t.CloseProfitByTrade,
       t.TodayPosition,
       t.MarginRateByMoney,
       t.MarginRateByVolume,
       t.CloseProfit + t.PositionProfit                                                            AS Profit,
       t.CloseProfit + t.PositionProfit - IFNULL(t4.CloseProfit, 0) - IFNULL(t4.PositionProfit, 0) AS TodayProfit,
       IFNULL(t5.TodayBuyCapital, 0)                                                               AS TodayBuyCapital,
       IFNULL(t5.TodaySellCapital, 0)                                                              AS TodaySellCapital,
       IFNULL(t5.BuyCapital, 0)                                                                    AS BuyCapital,
       IFNULL(t5.SellCapital, 0)                                                                   AS SellCapital,
       IF(IFNULL(t5.BuyCapital, 0) = 0, 0, (t.CloseProfit + t.PositionProfit) / t5.BuyCapital)     AS ReturnRatio,
       IF(t6.AbsProfit = 0, 0, (t.CloseProfit + t.PositionProfit) / t6.AbsProfit)                  AS ContributionRatio
FROM quant.t_future_simtestposition t
         JOIN quant.t_future_simtestinfo t2 ON (t.HistoryNo = t2.HistoryNo)
         JOIN quant.t_future_quantmarketdata t3
              ON (t.TradingDay = t3.TradingDay AND t.ExchangeID = t3.ExchangeID AND t.InstrumentID = t3.InstrumentID)
         LEFT JOIN quant.t_future_simtestposition t4
                   ON (t.HistoryNo = t4.HistoryNo AND t3.LastTradingDay = t4.Tradingday AND
                       t.ExchangeID = t3.ExchangeID AND t.InstrumentID = t4.InstrumentID AND
                       t.PosiDirection = t4.PosiDirection AND t.HedgeFlag = t4.HedgeFlag)
         LEFT JOIN (SELECT t1.HistoryNo,
                           t1.TradingDay,
                           t1.ExchangeID,
                           t1.InstrumentID,
                           t1.HedgeFlag,
                           SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '0', 1, 0) * t1.Volume *
                               t1.Price * t1.VolumeMultiple)                                            AS TodayBuyCapital,
                           SUM(IF(t1.Direction = '0', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS BuyCapital,
                           SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '1', 1, 0) * t1.Volume *
                               t1.Price *
                               t1.VolumeMultiple)                                                       AS TodaySellCapital,
                           SUM(IF(t1.Direction = '1', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS SellCapital
                    FROM (SELECT t2.HistoryNo,
                                 t1.TradingDay,
                                 t2.TradeID,
                                 t2.TradingDay AS TradeDay,
                                 t2.TradeDate,
                                 t2.TradeTime,
                                 t2.ExchangeID,
                                 t2.InstrumentID,
                                 t2.Direction,
                                 t2.HedgeFlag,
                                 t2.Volume,
                                 t2.VolumeMultiple,
                                 t2.Price,
                                 t2.Commission,
                                 t2.OrderLocalID,
                                 t2.OrderSysID
                          FROM (SELECT tm.TradingDay
                                FROM quant.t_future_simtestinfo ti,
                                     quant.t_future_quantmarketdata tm
                                WHERE ti.HistoryNo = #{history_no}
                                  AND tm.ExchangeID = 'SHFE'
                                  AND tm.Tradingday >= ti.SetMDBeginDate
                                  AND tm.TradingDay <= ti.SetMDEndDate) t1,
                               quant.t_future_simtesttrade t2
                          WHERE t2.HistoryNo = #{history_no}
                            AND t1.TradingDay >= t2.TradingDay) t1,
                         quant.t_future_quantmarketdata t2
                    WHERE t1.TradingDay = t2.TradingDay
                      AND t1.ExchangeID = t2.ExchangeID
                      AND t1.InstrumentID = t2.InstrumentID
                    GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.InstrumentID, t1.HedgeFlag) t5
                   ON (t.HistoryNo = t5.HistoryNo AND t.TradingDay = t5.TradingDay AND t.ExchangeID = t5.ExchangeID AND
                       t.InstrumentID = t5.InstrumentID AND t.HedgeFlag = t5.HedgeFlag)
         JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(ABS(t.Profit)) AS AbsProfit
               FROM (SELECT t.HistoryNo, t.TradingDay, t.CloseProfit + t.PositionProfit AS Profit
                     FROM quant.t_future_simtestposition t
                     WHERE t.HistoryNo = #{history_no}) t
               GROUP BY t.HistoryNO, t.TradingDay) t6 ON (t.HistoryNo = t6.HistoryNo AND t.TradingDay = t6.TradingDay)
WHERE t.HistoryNo = #{history_no}
```

# 期货回测盈亏信息 t_future_quantprofit

```sql

CREATE TABLE `t_future_quantprofit`
(
    `HistoryNo`         bigint(10) NOT NULL COMMENT '回测ID',
    `ExchangeID`        varchar(8)     NOT NULL COMMENT '交易所代码',
    `InstrumentID`      varchar(32)    NOT NULL COMMENT '合约代码',
    `InstrumentName`    varchar(128)            DEFAULT NULL COMMENT '合约名称',
    `FullInstrumentID`  varchar(32)    NOT NULL COMMENT 'Full合约代码',
    `SpecInstrumentID`  varchar(32)    NOT NULL COMMENT '标准合约代码',
    `PosiDirection`     char(1)        NOT NULL DEFAULT '0' COMMENT '持仓方向',
    `HedgeFlag`         char(1)        NOT NULL COMMENT '套保标识 Speculation 1 Arbitrage 2 Hedge 3',
    `TradingCount`      bigint(10) NOT NULL DEFAULT '0' COMMENT '交易次数',
    `TradingFee`        decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '交易费用',
    `Profit`            decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '盈亏',
    `BuyCapital`        decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '买金额',
    `SellCapital`       decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '卖金额',
    `ReturnRatio`       decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '收益率',
    `ContributionRatio` decimal(26, 7) NOT NULL DEFAULT '0.0000000' COMMENT '贡献率',
    PRIMARY KEY (`HistoryNo`, `ExchangeID`, `InstrumentID`, `FullInstrumentID`, `SpecInstrumentID`, `PosiDirection`,
                 `HedgeFlag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='期货回测盈亏信息';
```

```sql
INSERT INTO quant.t_Future_QuantProfit(HistoryNo, ExchangeID, InstrumentID, InstrumentName, FullInstrumentID,
                                       SpecInstrumentID, PosiDirection, HedgeFlag, TradingCount, TradingFee, Profit,
                                       BuyCapital, SellCapital, ReturnRatio, ContributionRatio)
SELECT t.HistoryNo,
       t.ExchangeID,
       t.InstrumentID,
       t.InstrumentName,
       t.FullInstrumentID,
       t.SpecInstrumentID,
       t.PosiDirection,
       t.HedgeFlag,
       tradingCount,
       tradingFee,
       t.Profit,
       t.BuyCapital,
       t.SellCapital,
       IF(t.ReturnBase = 0, 0, t.Profit / t.ReturnBase) AS ReturnRatio,
       0                                                AS ContributionRatio
FROM (SELECT t.HistoryNo,
             t.ExchangeID,
             t.InstrumentID,
             t3.InstrumentName,
             t.FullInstrumentID,
             t.SpecInstrumentID,
             t.PosiDirection,
             t.HedgeFlag,
             IFNULL(t2.TradingCount, 0)                             AS TradingCount,
             IFNULL(t2.TradingAmount, 0)                            AS TradingAmount,
             IFNULL(t2.BuyCapital, 0)                               AS BuyCapital,
             IFNULL(t2.SellCapital, 0)                              AS SellCapital,
             IFNULL(t2.TradingProfit, 0)                            AS TradingProfit,
             IFNULL(t2.TradingFee, 0)                               AS TradingFee,
             IFNULL(t2.TradingProfit, 0) - IFNULL(t2.TradingFee, 0) AS Profit,
             CASE
                 WHEN t.PosiDirection = '2' THEN IFNULL(t2.BuyCapital, 0)
                 WHEN t.PosiDirection = '3' THEN -1 * IFNULL(t2.SellCapital, 0)
                 ELSE 0 END                                         AS ReturnBase
      FROM (SELECT DISTINCT t.HistoryNo,
                            t.ExchangeID,
                            t.InstrumentID,
                            t.FullInstrumentID,
                            t.SpecInstrumentID,
                            t.PosiDirection,
                            t.HedgeFlag
            FROM quant.t_Future_QuantPosition t
            WHERE t.HistoryNo = #{history_no}) t
               LEFT JOIN (SELECT t.HistoryNo,
                                 t.ExchangeID,
                                 t.InstrumentID,
                                 t.PosiDirection,
                                 t.HedgeFlag,
                                 SUM(tradingCount)  AS TradingCount,
                                 SUM(tradingAmount) AS TradingAmount,
                                 SUM(t.BuyCapital)  AS BuyCapital,
                                 SUM(t.SellCapital) AS SellCapital,
                                 SUM(tradingProfit) AS TradingProfit,
                                 SUM(tradingFee)    AS TradingFee
                          FROM (SELECT t.HistoryNo,
                                       t.ExchangeID,
                                       t.InstrumentID,
                                       CASE
                                           WHEN (t.Direction = '0' AND t.OffsetFlag = '0') OR
                                                (t.Direction = '1' and t.OffsetFlag != '0') THEN '2'
                                           WHEN (t.Direction = '1' AND t.OffsetFlag = '0') OR
                                                (t.Direction = '0' and t.OffsetFlag != '0') THEN '3'
                                           ELSE 0 END  AS PosiDirection,
                                       t.HedgeFlag,
                                       1               AS TradingCount,
                                       tradingAmount,
                                       CASE WHEN t.Direction = '0' THEN 1 WHEN t.Direction = '1' THEN 0 ELSE 0 END *
                                       t.TradingAmount AS BuyCapital,
                                       CASE WHEN t.Direction = '0' THEN 0 WHEN t.Direction = '1' THEN 1 ELSE 0 END *
                                       t.TradingAmount AS SellCapital,
                                       CASE WHEN t.Direction = '0' THEN -1 WHEN t.Direction = '1' THEN 1 ELSE 0 END *
                                       t.TradingAmount AS TradingProfit,
                                       tradingFee
                                FROM quant.t_Future_Quanttrade t
                                WHERE t.HistoryNo = #{history_no}) t
                          GROUP BY t.HistoryNo, t.ExchangeID, t.InstrumentID, t.PosiDirection, t.HedgeFlag) t2
                         ON (t.HistoryNo = t2.HistoryNo AND t.ExchangeID = t2.ExchangeID AND
                             t.InstrumentID = t2.InstrumentID AND t.PosiDirection = t2.PosiDirection AND
                             t.HedgeFlag = t2.HedgeFlag)
               LEFT JOIN(SELECT t.HistoryNo,
                                t.ExchangeID,
                                t.InstrumentID,
                                t.InstrumentName,
                                t.PosiDirection,
                                t.HedgeFlag
                         FROM quant.t_Future_QuantPosition t
                         WHERE t.HistoryNo = #{history_no}
                           AND tradingDay = (SELECT MAX(tp.TradingDay)
                                             FROM quant.t_Future_QuantPosition tp
                                             WHERE tp.HistoryNo = #{history_no})) t3
                        ON (t.HistoryNo = t3.HistoryNo AND t.ExchangeID = t3.ExchangeID AND
                            t.InstrumentID = t3.InstrumentID AND t.PosiDirection = t3.PosiDirection AND
                            t.HedgeFlag = t3.HedgeFlag)) t
```

```sql
INSERT INTO quant.t_Future_QuantProfit(HistoryNo, ExchangeID, InstrumentID, InstrumentName, FullInstrumentID,
                                       SpecInstrumentID, PosiDirection, HedgeFlag, ContributionRatio)
SELECT t.HistoryNo,
       t.ExchangeID,
       t.InstrumentID,
       t.InstrumentName,
       t.FullInstrumentID,
       t.SpecInstrumentID,
       t.PosiDirection,
       HedgeFlag,
       CASE
           WHEN t.Profit > 0 AND t1.TotalGain > 0 THEN t.Profit / t1.TotalGain
           WHEN t.Profit < 0 AND t1.TotalLose < 0 THEN t.Profit / t1.TotalLose
           ELSE 0 END AS ContributionRatio
FROM quant.t_Future_QuantProfit t,
     (SELECT t.HistoryNo,
             SUM(IF(t.Profit > 0, t.Profit, 0)) AS TotalGain,
             SUM(IF(t.Profit < 0, t.Profit, 0)) AS TotalLose
      FROM quant.t_Future_QuantProfit t
      WHERE t.HistoryNo = #{history_no}
      GROUP BY t.HistoryNo) t1
WHERE t.HistoryNo = #{history_no}
  AND t.HistoryNo = t1.HistoryNo ON DUPLICATE KEY
UPDATE ContributionRatio =
VALUES (ContributionRatio)
```

# 客户回测资产收益 t_clientquanttestprofit

```sql
create table quant.t_ClientQuantTestProfit
(
        HistoryNo    bigInt(10)   not null COMMENT '回测历史序列号'
        ,TradingDay     varchar(8) binary  not null COMMENT '交易日'
        ,TradingTime     varchar(8) binary  not null COMMENT '交易时间'
        ,LastAsset    decimal(19,3)   not null COMMENT '期初资金'
        ,Asset    decimal(19,3)   not null COMMENT '期末资金'
        ,DayProfit    decimal(19,3)   not null COMMENT '当日盈亏'
        ,DayBuyCapital    decimal(19,3)   not null COMMENT '当日买入'
        ,DaySellCapital    decimal(19,3)   not null COMMENT '当日卖出'
        ,TotalProfit    decimal(19,3)   not null COMMENT '累计收益'
        ,TotalProfitRatio    decimal(14,8)   not null COMMENT '累计收益率'
          ,PRIMARY KEY (HistoryNo,TradingDay,TradingTime)
) COMMENT='客户回测资产收益';
```

```sql
SELECT HistoryNo,
       TradingDay,
       '15:00:00'       AS TradingTime,
       PreAsset         AS LastAsset,
       TotalAsset       AS Asset,
       TodayProfit      AS DayProfit,
       TodayBuyCapital  AS DayBuyCapital,
       TodaySellCapital AS DaySellCapital,
       Profit           AS TotalProfit,
       ProfitRatio      AS TotalProfitRatio
FROM quant.t_future_quantasset
WHERE HistoryNo = #{history_no}
```

# 回测基准收益 t_quanttestbenchmarkprofit

```sql
CREATE TABLE `t_quanttestbenchmarkprofit`
(
    `HistoryNo`          bigint(10) NOT NULL COMMENT '回测历史序列号',
    `BenchmarkStockID`   varchar(10) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '基准代码',
    `TradingDay`         varchar(8) CHARACTER SET utf8 COLLATE utf8_bin  NOT NULL COMMENT '交易日',
    `TradingTime`        varchar(8) CHARACTER SET utf8 COLLATE utf8_bin  NOT NULL COMMENT '交易时间',
    `BenchmarkStockName` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL COMMENT '基准名称',
    `LastClosingPrice`   decimal(20, 6)                                  NOT NULL,
    `ClosingPrice`       decimal(20, 6)                                  NOT NULL,
    `TotalProfit`        decimal(12, 3)                                  NOT NULL COMMENT '累计收益',
    `TotalProfitRatio`   decimal(14, 8)                                  NOT NULL COMMENT '累计收益率',
    PRIMARY KEY (`HistoryNo`, `BenchmarkStockID`, `TradingDay`, `TradingTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回测基准收益';
```

```sql
SELECT t1.HistoryNo,
       CONCAT(CASE
                  WHEN t2.ExchangeID = '1' THEN 'sh'
                  WHEN t2.ExchangeID = '2' THEN 'sz'
                  WHEN t2.ExchangeID = '4' THEN 'bj'
                  ELSE '' END, t2.SecurityID)                                  AS BenchmarkStockID,
       t2.SecurityName                                                         AS BenchmarkStockName,
       t2.TradingDay,
       t2.TradingTime,
       IF(t2.LastClosingPrice = 0, t2.ClosingPrice, t2.LastClosingPrice)       AS LastClosingPrice,
       t2.ClosingPrice,
       ROUND(t2.ClosingPrice - t3.LastClosingPrice, 4)                         AS TotalProfit,
       ROUND((t2.ClosingPrice - t3.LastClosingPrice) / t3.LastClosingPrice, 6) AS TotalProfitRatio
FROM quant.t_future_quantasset t1,
     quant.t_quantmarketdata t2,
     (SELECT t.ExchangeID,
             t.SecurityID,
             IF(t.LastClosingPrice = 0, t.ClosingPrice, t.LastClosingPrice) AS LastClosingPrice
      FROM quant.t_quantmarketdata t,
           (SELECT t.ExchangeID, t.SecurityID, MIN(TradingDay) AS MinTradingDay
            FROM quant.t_quantmarketdata t
            WHERE t.FullSecurityID IN (${bench_ids})
            GROUP BY t.ExchangeID, t.SecurityID) t1,
           (SELECT MIN(TradingDay) AS MinQuantTradingDay
            FROM quant.t_future_quantasset
            WHERE HistoryNo = #{history_no}) t2
      WHERE t.ExchangeID = t1.ExchangeID
        AND t.SecurityID = t1.SecurityID
        AND ((t.TradingDay = t1.MinTradingDay AND t1.MinTradingDay > t2.MinQuantTradingDay) OR
             (t.TradingDay = t2.MinQuantTradingDay AND t1.MinTradingDay <= t2.MinQuantTradingDay))) t3
WHERE t1.HistoryNo = #{history_no}
  AND t1.TradingDay = t2.TradingDay
  AND t2.ExchangeID = t3.ExchangeID
  AND t2.SecurityID = t3.SecurityID
  AND t2.FullSecurityID IN (${bench_ids})
```

# 回测历史 t_quanttesthistory

```sql
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
```

```sql
SELECT DISTINCT SecurityCategoryType
FROM quant.t_simtestsubmd
WHERE HistoryNo = #{history_no}
```

```sql
SELECT t.InitAsset,
       t.TotalAsset,
       (SELECT COUNT(1) FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) AS TestTradeDays
FROM quant.t_future_quantasset t
WHERE t.HistoryNo = #{history_no}
ORDER BY t.TradingDay DESC LIMIT 1
```