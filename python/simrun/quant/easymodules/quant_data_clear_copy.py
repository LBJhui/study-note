# _*_ coding: utf-8 _*_
# @Time: 2024/8/22 13:40
# @Author: LBJ辉
# @File: quant_data_clear_copy
# @Project: python
alias = "QuantDataClear"

realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "get_history_no": [
        {
            "meta": {
                "return": True,
                "callback": lambda runtime: do_update_history_no(runtime)
            },
            "sql": """SELECT CurrValue FROM quant.t_Counter WHERE CounterID = 't_QuantTestHistory' FOR UPDATE"""
        },
        {
            "sql": """UPDATE quant.t_Counter SET CurrValue = #{new_history_no} WHERE CounterID = 't_QuantTestHistory'"""
        }
    ],
    "clean_future_simtest_data": [
        {
            "sql": """DELETE FROM quant.t_Future_SimTestInfo WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestInitPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestTrade WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestPositionDetail WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestSubMD WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_SimTestTradingAccount WHERE HistoryNo = #{history_no}"""
        }
    ],
    "deal_future_quant_data": [
        # save_future_quant_order 回测报单信息
        {

            "sql": """DELETE FROM quant.t_Future_QuantOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantOrder(HistoryNo,TradingDay,ExchangeID,InstrumentID,InstrumentName,FullInstrumentID,SpecInstrumentID,Direction,OffsetFlag,HedgeFlag,OrderPriceType,TimeCondition,VolumeCondition,ContingentCondition,SimOrderType,LimitPrice,Volume,VolumeMultiple,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,Turnover)
                        SELECT #{history_no} AS HistoryNo, t.TradingDay, t.ExchangeID, t.InstrumentID, IFNULL(t1.InstrumentName, '') AS InstrumentName, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS FullInstrumentID, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS SpecInstrumentID, t.Direction, t.OffsetFlag, t.HedgeFlag, t.OrderPriceType, t.TimeCondition, t.VolumeCondition, t.ContingentCondition, NULL AS SimOrderType, t.LimitPrice, t.VolumeTotalOriginal AS Volume, t.VolumeMultiple, t.OrderLocalID, t.OrderSysID, t.OrderStatus, t.VolumeTraded, t.InsertTime,0 AS InsertMillisec, t.CancelTime, t.TradeAmount AS Turnover
                        FROM quant.t_Future_SimTestOrder t
                        LEFT JOIN quant.t_future_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.InstrumentID = t1.InstrumentID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        ## save_future_quant_trade 回测成交信息
        {
            "sql": """DELETE FROM quant.t_Future_QuantTrade WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantTrade(HistoryNo, TradingDay, TradeID, TradeDate, TradeTime, ExchangeID, InstrumentID, InstrumentName, FullInstrumentID, SpecInstrumentID, Direction, OffsetFlag, HedgeFlag, Price, Volume, VolumeMultiple, OrderLocalID, OrderSysID, TradingAmount, TotalPosCost, TradingFee, BeforeTradeTodayAmount, AfterTradeTodayAmount)
                        SELECT t.HistoryNo, t.TradingDay, t.TradeID, t.TradeDate, t.TradeTime, t.ExchangeID, t.InstrumentID, IFNULL(t1.InstrumentName, '') AS InstrumentName, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS FullInstrumentID, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS SpecInstrumentID, t.Direction, t.OffsetFlag, t.HedgeFlag, t.Price, t.Volume, t.VolumeMultiple, t.OrderLocalID, t.OrderSysID, t.Price * t.Volume * t.VolumeMultiple AS TradingAmount, t.Price * t.Volume * t.VolumeMultiple + t.Commission AS TotalPosCost, t.Commission AS TradingFee, 0 AS BeforeTradeTodayAmount, 0 AS AfterTradeTodayAmount
                        FROM quant.t_Future_SimTestTrade t
                        LEFT JOIN quant.t_future_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.InstrumentID = t1.InstrumentID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        ## save_future_quant_asset 回测资产信息
        {
            "sql": """DELETE FROM quant.t_Future_QuantAsset WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantAsset(HistoryNo, TradingDay, InitAmount, InitMargin, InitAsset, PreAmount, PreMargin, PreAsset, Amount, Margin, TodayBuyCapital, TodaySellCapital, TodayProfit, Profit, TotalAsset, ProfitRatio, MaxTodayLongAmount, MaxTodayShortAmount)
                        SELECT t.HistoryNo, t.TradingDay, SUM(t.InitAmount) AS InitAmount, SUM(t.InitMargin) AS InitMargin, SUM(t.InitAsset) AS InitAsset, SUM(t.PreAmount) AS PreAmount, SUM(t.PreMargin) AS PreMargin, SUM(t.PreAsset) AS PreAsset, SUM(t.Amount) AS Amount, SUM(t.Margin) AS Margin, SUM(IFNULL(tt.TodayBuyCapital, 0)) AS TodayBuyCapital, SUM(IFNULL(tt.TodaySellCapital, 0)) AS TodaySellCapital, SUM(t.TodayProfit) AS TodayProfit, SUM(t.Profit) AS Profit, SUM(t.TotalAsset) AS TotalAsset, IF(SUM(t.InitAsset) = 0, 0, SUM(t.Profit) / SUM(t.InitAsset)) AS ProfitRatio, SUM(t.MaxTodayLongAmount) AS MaxTodayLongAmount, SUM(t.MaxTodayShortAmount) AS MaxTodayShortAmount
                        FROM(
                            SELECT t.HistoryNo, t.TradingDay, SUM(t.InitAmount) AS InitAmount, SUM(t.InitMargin) AS InitMargin, SUM(t.InitAsset) AS InitAsset, SUM(t.PreAmount) AS PreAmount, SUM(t.PreMargin) AS PreMargin, SUM(t.PreAsset) AS PreAsset, SUM(t.Amount) AS Amount, SUM(t.Margin) AS Margin, SUM(t.TodayProfit) AS TodayProfit, SUM(t.Profit) AS Profit, SUM(t.TotalAsset) AS TotalAsset, SUM(t.MaxTodayLongAmount) AS MaxTodayLongAmount, SUM(t.MaxTodayShortAmount) AS MaxTodayShortAmount
                            FROM (SELECT t.HistoryNo, t.TradingDay, t4.InitAmount, t4.InitMargin, t4.InitAmount AS InitAsset, t.PreBalance AS PreAmount, 0 AS PreMargin, t.PreBalance AS PreAsset, t.Balance AS Amount, t.CurrMargin AS Margin, t.Balance - t.PreBalance AS TodayProfit, t.Balance - t4.InitAmount AS Profit, t.Balance AS TotalAsset, 0 AS MaxTodayLongAmount, 0 AS MaxTodayShortAmount
                                FROM quant.t_Future_SimTestTradingAccount t
                                JOIN (SELECT DISTINCT TradingDay FROM quant.t_future_quantmarketdata WHERE ExchangeID = 'SHFE') t3 ON (t.TradingDay = t3.TradingDay)
                                JOIN (SELECT t.TradingDay, t.PreBalance AS InitAmount, t.PreMargin AS InitMargin FROM quant.t_Future_SimTestTradingAccount t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay Limit 1) t4
                                WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNo, t.TradingDay) t
                        LEFT JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(IFNULL(IF((t.Direction = '0' AND t.OffsetFlag = '0') OR (t.Direction = '1' AND t.OffsetFlag = '1'), t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodayBuyCapital, SUM(IFNULL(IF((t.Direction = '0' AND t.OffsetFlag = '1') OR (t.Direction = '1' AND t.OffsetFlag = '0'), t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodaySellCapital FROM quant.t_Future_QuantTrade t WHERE t.HistoryNo = #{history_no} GROUP BY t.HistoryNo, t.TradingDay) tt ON (t.HistoryNo = tt.HistoryNo AND t.TradingDay = tt.TradingDay)
                        GROUP BY t.HistoryNo, t.TradingDay"""
        },
        ## save_future_quant_position 回测持仓信息
        {
            "sql": """DELETE FROM quant.t_Future_QuantPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantPosition(HistoryNo,TradingDay,ExchangeID,InstrumentID,InstrumentName,FullInstrumentID,SpecInstrumentID,PosiDirection,HedgeFlag,PositionDate,Position,YdPosition,OpenVolume,CloseVolume,VolumeMultiple,OpenAmount,CloseAmount,PositionCost,PreMargin,UseMargin,ExchangeMargin,Commission,CloseProfit,PositionProfit,SettlementPrice,LastSettlementPrice,OpenCost,CloseProfitByDate,CloseProfitByTrade,TodayPosition,MarginRateByMoney,MarginRateByVolume,Profit,TodayProfit,TodayBuyCapital,TodaySellCapital,BuyCapital,SellCapital,ReturnRatio,ContributionRatio)
                        SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.InstrumentID, t3.InstrumentName AS InstrumentName, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS FullInstrumentID, CONCAT(t.InstrumentID, '.', t.ExchangeID) AS SpecInstrumentID, t.PosiDirection, t.HedgeFlag, t.PositionDate, t.Position, t.YdPosition, t.OpenVolume, t.CloseVolume, t.VolumeMultiple, t.OpenAmount, t.CloseAmount, t.PositionCost,
                            t.PreMargin, t.UseMargin, t.ExchangeMargin, t.Commission, t.CloseProfit, t.PositionProfit, t.SettlementPrice, t3.LastSettlementPrice, t.OpenCost, t.CloseProfitByDate, t.CloseProfitByTrade, t.TodayPosition, t.MarginRateByMoney, t.MarginRateByVolume, t.CloseProfit + t.PositionProfit AS Profit, t.CloseProfit + t.PositionProfit - IFNULL(t4.CloseProfit, 0) - IFNULL(t4.PositionProfit, 0) AS TodayProfit, IFNULL(t5.TodayBuyCapital, 0) AS TodayBuyCapital, IFNULL(t5.TodaySellCapital, 0) AS TodaySellCapital, IFNULL(t5.BuyCapital, 0) AS BuyCapital, IFNULL(t5.SellCapital, 0) AS SellCapital, IF(IFNULL(t5.BuyCapital, 0) = 0 , 0, (t.CloseProfit + t.PositionProfit) / t5.BuyCapital) AS ReturnRatio, IF(t6.AbsProfit = 0, 0, (t.CloseProfit + t.PositionProfit) / t6.AbsProfit) AS ContributionRatio
                            FROM quant.t_future_simtestposition t
                            JOIN quant.t_future_simtestinfo t2 ON (t.HistoryNo = t2.HistoryNo)
                            JOIN quant.t_future_quantmarketdata t3 ON (t.TradingDay = t3.TradingDay AND t.ExchangeID = t3.ExchangeID AND t.InstrumentID = t3.InstrumentID)
                            LEFT JOIN quant.t_future_simtestposition t4 ON (t.HistoryNo = t4.HistoryNo AND t3.LastTradingDay = t4.Tradingday AND t.ExchangeID = t3.ExchangeID AND t.InstrumentID = t4.InstrumentID AND t.PosiDirection = t4.PosiDirection AND t.HedgeFlag = t4.HedgeFlag)
                            LEFT JOIN (SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.InstrumentID, t1.HedgeFlag, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '0', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS TodayBuyCapital, SUM(IF(t1.Direction = '0', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS BuyCapital, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '1', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS TodaySellCapital, SUM(IF(t1.Direction = '1', 1, 0) * t1.Volume * t1.Price * t1.VolumeMultiple) AS SellCapital
                                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradingDay AS TradeDay, t2.TradeDate, t2.TradeTime, t2.ExchangeID, t2.InstrumentID, t2.Direction, t2.HedgeFlag, t2.Volume, t2.VolumeMultiple, t2.Price, t2.Commission, t2.OrderLocalID, t2.OrderSysID
                                                FROM (SELECT tm.TradingDay FROM quant.t_future_simtestinfo ti, quant.t_future_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = 'SHFE' AND tm.Tradingday >= ti.SetMDBeginDate AND tm.TradingDay <= ti.SetMDEndDate) t1, quant.t_future_simtesttrade t2
                                                WHERE t2.HistoryNo = #{history_no} AND t1.TradingDay >= t2.TradingDay) t1, quant.t_future_quantmarketdata t2
                                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.InstrumentID = t2.InstrumentID
                                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.InstrumentID, t1.HedgeFlag) t5 ON (t.HistoryNo = t5.HistoryNo AND t.TradingDay = t5.TradingDay AND t.ExchangeID = t5.ExchangeID AND t.InstrumentID = t5.InstrumentID AND t.HedgeFlag = t5.HedgeFlag)
                            JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(ABS(t.Profit)) AS AbsProfit FROM (SELECT t.HistoryNo, t.TradingDay, t.CloseProfit + t.PositionProfit AS Profit FROM quant.t_future_simtestposition t WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNO, t.TradingDay) t6 ON (t.HistoryNo = t6.HistoryNo AND t.TradingDay = t6.TradingDay)
                            WHERE t.HistoryNo = #{history_no}"""
        },
        ## save_future_quant_profit 期货回测盈亏信息
        {
            "sql": """DELETE FROM quant.t_Future_QuantProfit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantProfit(HistoryNo, ExchangeID, InstrumentID, InstrumentName, FullInstrumentID, SpecInstrumentID, PosiDirection, HedgeFlag, TradingCount, TradingFee, Profit, BuyCapital, SellCapital, ReturnRatio, ContributionRatio)
                        SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, t.InstrumentName, t.FullInstrumentID, t.SpecInstrumentID, t.PosiDirection, t.HedgeFlag, tradingCount, tradingFee, t.Profit, t.BuyCapital, t.SellCapital, IF(t.ReturnBase = 0, 0, t.Profit / t.ReturnBase) AS ReturnRatio, 0 AS ContributionRatio
                        FROM(
                            SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, t3.InstrumentName, t.FullInstrumentID, t.SpecInstrumentID, t.PosiDirection, t.HedgeFlag, IFNULL(t2.TradingCount, 0) AS TradingCount, IFNULL(t2.TradingAmount, 0) AS TradingAmount, IFNULL(t2.BuyCapital, 0) AS BuyCapital, IFNULL(t2.SellCapital, 0) AS SellCapital, IFNULL(t2.TradingProfit, 0) AS TradingProfit, IFNULL(t2.TradingFee, 0) AS TradingFee, IFNULL(t2.TradingProfit, 0) - IFNULL(t2.TradingFee, 0) AS Profit, CASE WHEN t.PosiDirection = '2' THEN IFNULL(t2.BuyCapital, 0) WHEN t.PosiDirection = '3' THEN -1 * IFNULL(t2.SellCapital, 0) ELSE 0 END AS ReturnBase
                            FROM
                                (SELECT DISTINCT t.HistoryNo, t.ExchangeID, t.InstrumentID, t.FullInstrumentID, t.SpecInstrumentID, t.PosiDirection, t.HedgeFlag
                                FROM quant.t_Future_QuantPosition t
                                WHERE t.HistoryNo = #{history_no}) t
                                LEFT JOIN (SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, t.PosiDirection, t.HedgeFlag, SUM(tradingCount) AS TradingCount, SUM(tradingAmount) AS TradingAmount, SUM(t.BuyCapital) AS BuyCapital, SUM(t.SellCapital) AS SellCapital, SUM(tradingProfit) AS TradingProfit, SUM(tradingFee) AS TradingFee
                                FROM
                                (SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, CASE WHEN (t.Direction = '0' AND t.OffsetFlag = '0') OR (t.Direction = '1' and t.OffsetFlag != '0') THEN '2' WHEN (t.Direction = '1' AND t.OffsetFlag = '0') OR (t.Direction = '0' and t.OffsetFlag != '0')  THEN '3' ELSE 0 END AS PosiDirection, t.HedgeFlag, 1 AS TradingCount, tradingAmount, CASE WHEN t.Direction = '0' THEN 1 WHEN t.Direction = '1' THEN 0 ELSE 0 END * t.TradingAmount AS BuyCapital, CASE WHEN t.Direction = '0' THEN 0 WHEN t.Direction = '1' THEN 1 ELSE 0 END * t.TradingAmount AS SellCapital, CASE WHEN t.Direction = '0' THEN -1 WHEN t.Direction = '1' THEN 1 ELSE 0 END * t.TradingAmount AS TradingProfit, tradingFee
                                FROM quant.t_Future_Quanttrade t
                                WHERE t.HistoryNo = #{history_no}) t
                                GROUP BY t.HistoryNo, t.ExchangeID, t.InstrumentID, t.PosiDirection, t.HedgeFlag) t2 ON (t.HistoryNo = t2.HistoryNo AND t.ExchangeID = t2.ExchangeID AND t.InstrumentID = t2.InstrumentID AND t.PosiDirection = t2.PosiDirection AND t.HedgeFlag = t2.HedgeFlag)
                                LEFT JOIN(SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, t.InstrumentName, t.PosiDirection, t.HedgeFlag
                                FROM quant.t_Future_QuantPosition t
                                WHERE t.HistoryNo = #{history_no} AND tradingDay = (SELECT MAX(tp.TradingDay) FROM quant.t_Future_QuantPosition tp WHERE tp.HistoryNo = #{history_no})) t3 ON (t.HistoryNo = t3.HistoryNo AND t.ExchangeID = t3.ExchangeID AND t.InstrumentID = t3.InstrumentID AND t.PosiDirection = t3.PosiDirection AND t.HedgeFlag = t3.HedgeFlag)) t"""
        },
        {
            "sql": """INSERT INTO quant.t_Future_QuantProfit(HistoryNo, ExchangeID, InstrumentID, InstrumentName, FullInstrumentID, SpecInstrumentID, PosiDirection, HedgeFlag, ContributionRatio)
                        SELECT t.HistoryNo, t.ExchangeID, t.InstrumentID, t.InstrumentName, t.FullInstrumentID, t.SpecInstrumentID, t.PosiDirection, HedgeFlag, CASE WHEN t.Profit > 0 AND t1.TotalGain > 0 THEN t.Profit / t1.TotalGain WHEN t.Profit < 0 AND t1.TotalLose < 0 THEN t.Profit / t1.TotalLose ELSE 0 END AS ContributionRatio
                        FROM quant.t_Future_QuantProfit t,
                            (SELECT t.HistoryNo, SUM(IF(t.Profit > 0, t.Profit, 0)) AS TotalGain, SUM(IF(t.Profit < 0, t.Profit, 0)) AS TotalLose
                            FROM quant.t_Future_QuantProfit t
                            WHERE t.HistoryNo = #{history_no}
                            GROUP BY t.HistoryNo) t1
                        WHERE t.HistoryNo = #{history_no} AND t.HistoryNo = t1.HistoryNo
                        ON DUPLICATE KEY UPDATE ContributionRatio = VALUES(ContributionRatio)"""
        }
    ],
    "get_future_quant_test_profit": {
        "sql": """SELECT HistoryNo, TradingDay, '15:00:00' AS TradingTime, PreAsset AS LastAsset, TotalAsset AS Asset, TodayProfit AS DayProfit, TodayBuyCapital AS DayBuyCapital, TodaySellCapital AS DaySellCapital, Profit AS TotalProfit, ProfitRatio AS TotalProfitRatio
                FROM quant.t_future_quantasset
                WHERE HistoryNo = #{history_no}"""
    },
    # 回测基准行情信息
    "get_future_quant_bench_profit": {
        "sql": """SELECT t1.HistoryNo, CONCAT(CASE WHEN t2.ExchangeID = '1' THEN 'sh' WHEN t2.ExchangeID = '2' THEN 'sz' WHEN t2.ExchangeID = '4' THEN 'bj' ELSE '' END, t2.SecurityID) AS BenchmarkStockID, t2.SecurityName AS BenchmarkStockName, t2.TradingDay, t2.TradingTime, IF(t2.LastClosingPrice = 0, t2.ClosingPrice, t2.LastClosingPrice) AS LastClosingPrice, t2.ClosingPrice, ROUND(t2.ClosingPrice - t3.LastClosingPrice, 4) AS TotalProfit, ROUND((t2.ClosingPrice - t3.LastClosingPrice) / t3.LastClosingPrice, 6) AS TotalProfitRatio
                FROM quant.t_future_quantasset t1, quant.t_quantmarketdata t2, 
                    (SELECT t.ExchangeID, t.SecurityID, IF(t.LastClosingPrice = 0, t.ClosingPrice, t.LastClosingPrice) AS LastClosingPrice
                        FROM quant.t_quantmarketdata t, (SELECT t.ExchangeID, t.SecurityID, MIN(TradingDay) AS MinTradingDay FROM quant.t_quantmarketdata t WHERE t.FullSecurityID IN (${bench_ids}) GROUP BY t.ExchangeID, t.SecurityID) t1, (SELECT MIN(TradingDay) AS MinQuantTradingDay FROM quant.t_future_quantasset WHERE HistoryNo = #{history_no}) t2
                        WHERE t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND ((t.TradingDay = t1.MinTradingDay AND t1.MinTradingDay > t2.MinQuantTradingDay) OR (t.TradingDay = t2.MinQuantTradingDay AND t1.MinTradingDay <= t2.MinQuantTradingDay))) t3
                WHERE t1.HistoryNo = #{history_no} AND t1.TradingDay = t2.TradingDay AND t2.ExchangeID = t3.ExchangeID AND t2.SecurityID = t3.SecurityID AND t2.FullSecurityID IN (${bench_ids})"""
    },
    "get_quant_test_market": {
        "sql": """SELECT DISTINCT SecurityCategoryType FROM quant.t_simtestsubmd WHERE HistoryNo = #{history_no}"""
    },
    "get_future_quant_test_history": {
        "sql": """SELECT t.InitAsset, t.TotalAsset, (SELECT COUNT(1) FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) AS TestTradeDays FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay DESC LIMIT 1"""
    },
    "save_future_quant_history": [
        {
            "sql": """INSERT INTO quant.t_quanttesthistory(HistoryNo, TestID, TestInvestorID, TestUserID, StrategyName, TestDate, TestTime, TestTradeDateBegin, TestTradeDateEnd, TestTradeDays, TestKind, InitAsset, Asset, TestDataStatus, TestDataFileStatus, TestRunTime)
                        SELECT t.HistoryNo, t.QuantID AS TestID, t.UserID AS TestInvestorID, t2.UserID AS TestUserID, t.TestID AS StrategyName, substr(t.TestBeginTime, 1, 8) AS TestDate, CONCAT(substr(t.TestBeginTime, 9, 2), ':', substr(t.TestBeginTime, 11, 2), ':', substr(t.TestBeginTime, 13, 2)) AS TestTime, t.SetMDBeginDate AS TestTradeDateBegin, t.SetMDEndDate AS TestTradeDateEnd, #{test_trade_days} AS TestTradeDays, '1' AS TestKind, #{init_asset} AS InitAsset, #{total_asset} AS Asset, #{test_data_status} AS TestDataStatus, #{test_data_file_status} AS TestDataFileStatus, 1000 * TIMESTAMPDIFF(SECOND, t.TestBeginTime, t.TestEndTime) AS TestRunTime
                        FROM quant.t_future_simtestinfo t, siminfo.t_investor t1, simtrade.t_user t2
                        WHERE t.HistoryNo = #{history_no} AND t.UserID = t1.InvestorID AND t1.OpenId = t2.Mobile LIMIT 1
                        ON DUPLICATE KEY UPDATE TestDataFileStatus = VALUES(TestDataFileStatus)"""
        }
    ],
}


def do_update_history_no(runtime, *args, **kwargs):
    error = runtime["error"]
    result = runtime["result"]
    if not error:
        history_no = int(result[0][0])
        new_history_no = history_no + 1
        runtime["export"] = {"new_history_no": new_history_no}
    else:
        runtime["go"] = "exit"
