# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:00
# @Author: LBJ辉
# @File: quant_data_clear
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
    "get_manual_quants": {
        "sql": """SELECT t.SequenceNo FROM quant.t_quanttestmanual t 
                    WHERE t.testdatastatus = '0' AND NOT EXISTS (SELECT HistoryNo FROM quant.t_simtestinfo WHERE ManualID = t.SequenceNo)
                    ORDER BY t.SequenceNo"""
    },
    "set_manual_quant_clearing": {
        "sql": """UPDATE quant.t_quanttestmanual t SET t.HistoryNo = #{history_no}, t.testdatastatus = #{manual_data_status} WHERE t.SequenceNo = #{manual_id}"""
    },
    "get_manual_quant_info": {
        "sql": """SELECT SequenceNo, TestInvestorID, TestUserID, StrategyName, TestDate, TestTime, TestTradeDateBegin, TestTradeDateEnd, TestTradeDays, TestKind, InitAsset, TradeFilePath, PosFilePath
                    FROM quant.t_quanttestmanual t 
                    WHERE t.SequenceNo = #{manual_id} AND t.testdatastatus = #{manual_data_status}"""
    },
    "clean_future_quant_data": [
        {
            "sql": """DELETE FROM quant.t_Future_QuantAsset WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_QuantDebt WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_QuantOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_QuantPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_QuantProfit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_Future_QuantTrade WHERE HistoryNo = #{history_no}"""
        }
    ],
    "clean_quant_data": [
        {
            "sql": """DELETE FROM quant.t_QuantAsset WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_QuantDebt WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_QuantOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_QuantPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_QuantProfit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_QuantTrade WHERE HistoryNo = #{history_no}"""
        }
    ],
    "clean_simtest_data": [
        {
            "sql": """DELETE FROM quant.t_SimTestInfo WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestInitPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSubMD WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSpotTradeDetail WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSpotOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSpotPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSpotResult WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSPTradeDetail WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSPOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSPPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestSPResult WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditTradeDetail WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditResult WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditDebt WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditRepayment WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditTransfer WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditSurplusPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_SimTestCreditFundTransferDetailEx WHERE HistoryNo = #{history_no}"""
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
    "get_manual_quant_rights": {
        "sql": """SELECT t.RecordDate, t.ExchangeID, t.SecurityID, SUM(t.DividendRate) AS DividendRate, SUM(t.ProfitRate) AS ProfitRate, SUM(t.IssueRate) AS IssueRate, SUM(t.IssuePrice) AS IssuePrice, MIN(t.DividendDate) AS DividendDate, MIN(t.NewStockMarketDate) AS NewStockMarketDate
                        FROM (SELECT t1.RecordDate, t1.ExchangeID, t1.SecurityID, t1.AfterRate AS DividendRate, t1.BonusRate + t1.TransferRate AS ProfitRate, 0 AS IssueRate, 0 AS IssuePrice, t1.DividendDate, t1.NewStockMarketDate
                                FROM quant.t_quantdividend t1, (SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no}) t2
                                WHERE t1.RecordDate >= #{test_trade_date_begin} AND t1.RecordDate < #{test_trade_date_end} AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                                UNION
                                SELECT t1.RecordDate, t1.ExchangeID, t1.SecurityID, 0 AS DividendRate, 0 AS ProfitRate, t1.IssueRate, t1.IssuePrice, t1.DividendDate, t1.NewStockMarketDate
                                FROM quant.t_quantrightissue t1, (SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no}) t2
                                WHERE t1.RecordDate >= #{test_trade_date_begin} AND t1.RecordDate < #{test_trade_date_end} AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID AND t1.NewStockMarketDate IS NOT NULL) t
                        GROUP BY t.RecordDate, t.ExchangeID, t.SecurityID
                        ORDER BY t.RecordDate"""
    },
    "get_manual_quant_positions": {
        "sql": """SELECT HistoryNo, TradingDay, ExchangeID, SecurityID, Volume, ClosePrice, TotalPosCost, TotalSecurityValue, CommissionFee, TotalGain, OpenPosPrice, TradingVolume, RecordVolume, DividendRate, ProfitRate, IssueRate, IssuePrice, ProfitVolume, IssueVolume
                        FROM quant.t_simtestspotposition
                        WHERE historyno = #{history_no} ORDER BY HistoryNo, ExchangeID, TradingDay, SecurityID"""
    },
    "clean_manual_quant_positions": {
        "sql": """DELETE FROM quant.t_SimTestSpotPosition WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_sub_instruments": {
        "sql": """SELECT DISTINCT ExchangeID, InstrumentID FROM quant.t_future_simtestsubmd WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_sub_securities": {
        "sql": """SELECT DISTINCT ExchangeID, SecurityID FROM quant.t_simtestsubmd WHERE HistoryNo = #{history_no}"""
    },
    "get_manual_quant_trades": {
        "sql": """SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t.TradeID, t.Direction, t.Volume, t.TradePrice, t.TradeAmount, t.CommissionFee
                        FROM (SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0001' AS TradeID, '1' AS Direction, 0 AS Volume, t.DividendRate AS TradePrice, t.RecordVolume * t.DividendRate AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.DividendRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0002' AS TradeID, '0' AS Direction, t.ProfitVolume AS Volume, 0 AS TradePrice, 0 AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.ProfitRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0003' AS TradeID, '0' AS Direction, t.IssueVolume AS Volume, t.IssuePrice AS TradePrice, t.IssueVolume * t.IssuePrice AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.IssueRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t.TradeID, t.Direction, t.Volume, t.TradePrice, t.Volume * t.TradePrice AS TradeAmount, t.CommissionFee
                            FROM quant.t_simtestspottradedetail t
                            WHERE t.HistoryNo = #{history_no}) t
                        ORDER BY t.HistoryNo, t.ExchangeID, t.SecurityID, t.TradingDay, t.TradeID"""
    },
    "deal_manual_quant_data": [
        {
            "sql": """INSERT INTO quant.t_simtestinfo(HistoryNo, UserID, QuantID, TestID, MDFrequency, InitalAmount, InitalOptionAmount, InitalCreditAmount, TestBeginDate, TestBeginTime, TestEndDate, TestEndTime, MDBeginDate, MDBeginTime, MDEndDate, MDEndTime, ManualID)
                        SELECT #{history_no} AS HistoryNo, #{test_investor_id} AS UserID, CONCAT(#{test_investor_id}, '-', #{manual_id}) AS QuantID, #{strategy_name} AS TestID, 'Second' AS MDFrequency, #{init_asset} AS InitalAmount, 0 AS InitalOptionAmount, 0 AS InitalCreditAmount, 
                                DATE_FORMAT(NOW(), '%Y%m%d') AS TestBeginDate, DATE_FORMAT(NOW(), '%H:%i:%S') AS TestBeginTime, DATE_FORMAT(NOW(), '%Y%m%d') AS TestEndDate, DATE_FORMAT(NOW(), '%H:%i:%S') AS TestEndTime, #{test_trade_date_begin} AS MDBeginDate, '09:30:00' AS MDBeginTime, #{test_trade_date_end} AS MDEndDate, '15:00:00' AS MDEndTime, #{manual_id} AS ManualID
                        FROM DUAL"""
        },
        {
            "sql": """DELETE FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no} AND t.Volume = 0"""
        },
        {
            "sql": """INSERT INTO quant.t_simtestspottradedetail(HistoryNo, TradingDay, TradeID, TradeDay, TradeTime, ExchangeID, SecurityID, Direction, Volume, TradePrice, TotalPosCost, CommissionFee, OrderLocalID, OrderSysID)
                        SELECT t1.HistoryNo, t1.TradingDay, t1.TradeID, t1.TradeDay, t1.TradeTime, t1.ExchangeID, t1.SecurityID, t1.Direction, t1.Volume, t1.TradePrice, IF(t1.Direction = '0', t1.Volume * t1.TradePrice, 0) + t1.Volume / t2.OrderVolume * t2.CommissionFee AS TotalPosCost, t1.Volume / t2.OrderVolume * t2.CommissionFee AS CommissionFee, t1.OrderLocalID, t1.OrderSysID
                        FROM quant.t_simtestspottradedetail t1,
                            (SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, t1.OrderSysID, SUM(t1.Volume) AS OrderVolume, GREATEST(#{min_commission_fee}, SUM(t1.Volume * t1.TradePrice) * #{commission_rate}) + SUM(t1.Volume * t1.TradePrice) * (IF(t1.ExchangeID = '1', #{transfer_rate}, 0) + IF(t1.Direction = '1', #{stamp_tax}, 0)) AS CommissionFee 
                            FROM quant.t_simtestspottradedetail t1
                            WHERE t1.HistoryNo = #{history_no}
                            GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, t1.OrderSysID) t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID AND t1.OrderSysID = t2.OrderSysID
                        ON DUPLICATE KEY UPDATE TotalPosCost = VALUES(TotalPosCost), CommissionFee = VALUES(CommissionFee)"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_securities(runtime)
            },
            "sql": """SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestinitposition t WHERE t.HistoryNo = #{history_no} AND t.SecurityKind = 's' ORDER BY t.ExchangeID, t.SecurityID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_simtestspotposition(HistoryNo, TradingDay, ExchangeID, SecurityID, Volume, ClosePrice, TotalPosCost, TotalSecurityValue, CommissionFee, TotalGain, OpenPosPrice, TradingVolume)
                        SELECT t1.HistoryNo, t2.TradingDay, t1.ExchangeID, t1.SecurityID, t1.Volume, t3.ClosingPrice AS ClosePrice, t1.TotalPosCost, t1.Volume * t3.ClosingPrice AS TotalSecurityValue, 0 AS CommissionFee, t1.Volume * t3.ClosingPrice - t1.TotalPosCost AS TotalGain, t1.TotalPosCost / t1.Volume AS OpenPosPrice, t1.Volume AS TradingVolume
                        FROM quant.t_simtestinitposition t1,
                            (SELECT DISTINCT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t2,
                            quant.t_quantmarketdata t3
                        WHERE t1.HistoryNo = #{history_no} AND t1.ExchangeID = #{exchange_id} AND t1.SecurityID = #{security_id} AND t1.ExchangeID = t3.ExchangeID AND t1.SecurityID = t3.SecurityID AND t2.TradingDay = t3.TradingDay"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_securities(runtime)
            },
            "sql": """SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no} AND NOT EXISTS (SELECT 1 FROM quant.t_simtestinitposition t1 WHERE t1.HistoryNo = #{history_no} AND t1.SecurityKind = 's' AND t1.ExchangeID = t.ExchangeID AND t1.SecurityID = t.SecurityID) ORDER BY t.ExchangeID, t.SecurityID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_simtestspotposition(HistoryNo, TradingDay, ExchangeID, SecurityID, Volume, ClosePrice, TotalPosCost, TotalSecurityValue, CommissionFee, TotalGain, OpenPosPrice)
                        SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) AS Volume, t2.ClosingPrice AS ClosePrice, SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume * t1.TradePrice) AS TotalPosCost, 
                                SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) * t2.ClosingPrice AS TotalSecurityValue, SUM(t1.CommissionFee) AS CommissionFee, SUM((IF(t1.Direction = '0', -1, 1) * t1.Volume * t1.TradePrice) - t1.CommissionFee) + SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) * t2.ClosingPrice AS TotalGain, 0 AS OpenPosPrice
                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestspottradedetail t2
                                WHERE t2.HistoryNo = #{history_no} AND t2.ExchangeID = #{exchange_id} AND t2.SecurityID = #{security_id} AND t1.TradingDay >= t2.TradingDay) t1, quant.t_quantmarketdata t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID"""
        },
        {
            "sql": """INSERT INTO quant.t_simtestspotposition(HistoryNo, TradingDay, ExchangeID, SecurityID, Volume, ClosePrice, TotalPosCost, TotalSecurityValue, CommissionFee, TotalGain, OpenPosPrice)
                        SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) AS Volume, t2.ClosingPrice AS ClosePrice, SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume * t1.TradePrice) AS TotalPosCost, 
                                SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) * t2.ClosingPrice AS TotalSecurityValue, SUM(t1.CommissionFee) AS CommissionFee, SUM((IF(t1.Direction = '0', -1, 1) * t1.Volume * t1.TradePrice) - t1.CommissionFee) + SUM(IF(t1.Direction = '0', 1, -1) * t1.Volume) * t2.ClosingPrice AS TotalGain, 0 AS OpenPosPrice
                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestspottradedetail t2, quant.t_simtestinitposition t3
                                WHERE t2.HistoryNo = #{history_no} AND t2.HistoryNo = t3.HistoryNo AND t2.ExchangeID = t3.ExchangeID AND t2.SecurityID = t3.SecurityID AND t3.SecurityKind = 's' AND t1.TradingDay >= t2.TradingDay) t1, quant.t_quantmarketdata t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID
                        ON DUPLICATE KEY UPDATE quant.t_simtestspotposition.Volume = quant.t_simtestspotposition.Volume + VALUES(Volume), 
                                    quant.t_simtestspotposition.TotalPosCost = quant.t_simtestspotposition.TotalPosCost + VALUES(TotalPosCost), 
                                    quant.t_simtestspotposition.TotalSecurityValue = quant.t_simtestspotposition.TotalSecurityValue + VALUES(TotalSecurityValue), 
                                    CommissionFee = VALUES(CommissionFee), quant.t_simtestspotposition.TotalGain = quant.t_simtestspotposition.TotalGain + VALUES(TotalGain)"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_rights(runtime)
            },
            "sql": """SELECT t.RecordDate, t.ExchangeID, t.SecurityID, SUM(t.DividendRate) AS DividendRate, SUM(t.ProfitRate) AS ProfitRate, SUM(t.IssueRate) AS IssueRate, SUM(t.IssuePrice) AS IssuePrice, MIN(t.DividendDate) AS DividendDate, MIN(t.NewStockMarketDate) AS NewStockMarketDate
                        FROM (SELECT t1.RecordDate, t1.ExchangeID, t1.SecurityID, t1.AfterRate AS DividendRate, t1.BonusRate + t1.TransferRate AS ProfitRate, 0 AS IssueRate, 0 AS IssuePrice, t1.DividendDate, t1.NewStockMarketDate
                                FROM quant.t_quantdividend t1, (SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no}) t2
                                WHERE t1.RecordDate >= #{test_trade_date_begin} AND t1.RecordDate < #{test_trade_date_end} AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                                UNION
                                SELECT t1.RecordDate, t1.ExchangeID, t1.SecurityID, 0 AS DividendRate, 0 AS ProfitRate, t1.IssueRate, t1.IssuePrice, t1.DividendDate, t1.NewStockMarketDate
                                FROM quant.t_quantrightissue t1, (SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspottradedetail t WHERE t.HistoryNo = #{history_no}) t2
                                WHERE t1.RecordDate >= #{test_trade_date_begin} AND t1.RecordDate < #{test_trade_date_end} AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID AND t1.NewStockMarketDate IS NOT NULL) t
                        GROUP BY t.RecordDate, t.ExchangeID, t.SecurityID
                        ORDER BY t.RecordDate"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """UPDATE quant.t_simtestspotposition t, (SELECT t.Volume FROM quant.t_simtestspotposition t WHERE t.HistoryNo = #{history_no} AND t.TradingDay = #{record_date} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}) t1
                        SET t.RecordVolume = t1.Volume, 
                            t.Volume = t.Volume + ROUND(t1.Volume * #{profit_rate}) + ROUND(t1.Volume * #{issue_rate}),
                            t.TotalPosCost = t.TotalPosCost + ROUND(t1.Volume * #{issue_rate}) * #{issue_price},
                            t.TotalSecurityValue = t.TotalSecurityValue + (ROUND(t1.Volume * #{profit_rate}) + ROUND(t1.Volume * #{issue_rate})) * t.ClosePrice,
                            t.TotalGain = t.TotalGain + (ROUND(t1.Volume * #{profit_rate}) + ROUND(t1.Volume * #{issue_rate})) * t.ClosePrice - ROUND(t1.Volume * #{issue_rate}) * #{issue_price},
                            t.DividendRate = IF(t.TradingDay = #{dividend_date}, #{dividend_rate}, 0),
                            t.ProfitRate = IF(t.TradingDay = #{dividend_date}, #{profit_rate}, 0),
                            t.IssueRate = IF(t.TradingDay = #{dividend_date}, #{issue_rate}, 0),
                            t.IssuePrice = IF(t.TradingDay = #{dividend_date}, #{issue_price}, 0),
                            t.ProfitVolume = IF(t.TradingDay = #{dividend_date}, ROUND(t1.Volume * #{profit_rate}), 0),
                            t.IssueVolume = IF(t.TradingDay = #{dividend_date}, ROUND(t1.Volume * #{issue_rate}), 0)
                        WHERE t.HistoryNo = #{history_no} AND t.TradingDay >= #{dividend_date} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_trades(runtime)
            },
            "sql": """SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t.TradeID, t.Direction, t.Volume, t.TradePrice, t.TradeAmount, t.CommissionFee
                        FROM (SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0001' AS TradeID, '1' AS Direction, 0 AS Volume, t.DividendRate AS TradePrice, t.RecordVolume * t.DividendRate AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.DividendRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0002' AS TradeID, '0' AS Direction, t.ProfitVolume AS Volume, 0 AS TradePrice, 0 AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.ProfitRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, '0003' AS TradeID, '0' AS Direction, t.IssueVolume AS Volume, t.IssuePrice AS TradePrice, t.IssueVolume * t.IssuePrice AS TradeAmount, 0 AS CommissionFee
                            FROM quant.t_simtestspotposition t
                            WHERE t.HistoryNo = #{history_no} AND t.RecordVolume > 0 AND t.IssueRate > 0
                            UNION
                            SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t.TradeID, t.Direction, t.Volume, t.TradePrice, t.Volume * t.TradePrice AS TradeAmount, t.CommissionFee
                            FROM quant.t_simtestspottradedetail t
                            WHERE t.HistoryNo = #{history_no}) t
                        ORDER BY t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t.TradeID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """UPDATE quant.t_simtestspotposition t
                        SET t.OpenPosPrice = (CASE WHEN t.Volume = 0 THEN 0 WHEN t.TradingVolume + IF(#{direction} = '0', 1, -1) * #{volume} = 0 THEN 0 WHEN #{direction} = '0' AND t.TradingVolume + #{volume} != 0 THEN (t.TradingVolume * t.OpenPosPrice + #{trade_amount} + #{commission_fee}) / (t.TradingVolume + #{volume}) ELSE t.OpenPosPrice END),
                            t.TradingVolume = t.TradingVolume + IF(#{direction} = '0', 1, -1) * #{volume}
                        WHERE t.HistoryNo = #{history_no} AND t.TradingDay >= #{trading_day} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}"""
        },
        {
            "sql": """INSERT INTO quant.t_simtestspotresult(HistoryNo, TradingDay, PreAmount, PreSecurityValue, Amount, SecurityValue)
                        SELECT #{history_no} AS HistoryNo, t1.TradingDay, t1.InitalAmount AS PreAmount, IFNULL(t2.PreSecurityValue, 0) AS PreSecurityValue, t1.InitalAmount, 0 AS SecurityValue
                        FROM (SELECT DISTINCT ti.InitalAmount, tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1,
                            (SELECT SUM(t1.Volume * t2.LastClosingPrice) AS PreSecurityValue FROM quant.t_simtestinitposition t1, quant.t_quantmarketdata t2 WHERE t1.HistoryNo = #{history_no} AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID AND t2.TradingDay = (SELECT MIN(tm.TradingDay) AS FirstTradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate)) t2"""
        },
        {
            "sql": """UPDATE quant.t_simtestspotresult t,
                        (SELECT t1.HistoryNo, t1.TradingDay, t1.SecurityValue, t1.ProfitValue + t2.TradeAmount AS AmountChange
                            FROM (SELECT t.HistoryNo, t.TradingDay, SUM(t.TotalSecurityValue) AS SecurityValue, SUM(t.RecordVolume * t.DividendRate - t.IssueVolume * t.IssuePrice) AS ProfitValue
                                FROM quant.t_simtestspotposition t
                                WHERE t.HistoryNo = #{history_no}
                                GROUP BY t.HistoryNo, t.TradingDay) t1,
                                (SELECT t1.HistoryNo, t1.TradingDay, SUM(IF(t1.Direction = '0', -1, 1) * t1.Volume * t1.TradePrice) - SUM(t1.CommissionFee) AS TradeAmount
                                FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                        FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestspottradedetail t2
                                        WHERE t2.HistoryNo = #{history_no} AND t1.TradingDay >= t2.TradingDay) t1
                                GROUP BY t1.HistoryNo, t1.TradingDay) t2
                            WHERE t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.Tradingday) t1
                        SET t.Amount = t.Amount + t1.AmountChange, t.SecurityValue = t1.SecurityValue
                        WHERE t.HistoryNo = t1.HistoryNo AND t.TradingDay = t1.TradingDay"""
        },
        {
            "sql": """UPDATE quant.t_simtestspotresult t,
                        (SELECT t2.HistoryNo, t1.TradingDay, t2.Amount, t2.SecurityValue
                            FROM (SELECT tm.TradingDay, tm.LastTradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1,
                                quant.t_simtestspotresult t2
                            WHERE t2.HistoryNo = #{history_no} AND t1.LastTradingDay = t2.TradingDay) t1
                        SET t.PreAmount = t1.Amount, t.PreSecurityValue = t1.SecurityValue
                        WHERE t.HistoryNo = t1.HistoryNo AND t.TradingDay = t1.TradingDay"""
        },
        {
            "sql": """INSERT INTO quant.t_simtestsubmd(HistoryNo, TradingDay, ExchangeID, SecurityID, ExchSecurityID, SecurityCategoryType)
                        SELECT #{history_no} AS HistoryNo, t1.TradingDay, t2.ExchangeID, t2.SecurityID, NULL AS ExchSecurityID, 's' AS SecurityCategoryType
                        FROM (SELECT DISTINCT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1,
                            (SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspotposition t WHERE t.HistoryNo = #{history_no}) t2"""
        },
        {
            "sql": """INSERT INTO quant.t_simtestinfo(HistoryNo, UserID, QuantID, TestID, MDFrequency, InitalAmount, InitalOptionAmount, InitalCreditAmount, TestBeginDate, TestBeginTime, TestEndDate, TestEndTime, MDBeginDate, MDBeginTime, MDEndDate, MDEndTime, ManualID)
                        SELECT #{history_no} AS HistoryNo, #{test_investor_id} AS UserID, CONCAT(#{test_investor_id}, '-', #{manual_id}) AS QuantID, #{strategy_name} AS TestID, 'Second' AS MDFrequency, #{init_asset} AS InitalAmount, 0 AS InitalOptionAmount, 0 AS InitalCreditAmount, 
                                DATE_FORMAT(NOW(), '%Y%m%d') AS TestBeginDate, DATE_FORMAT(NOW(), '%H:%i:%S') AS TestBeginTime, DATE_FORMAT(NOW(), '%Y%m%d') AS TestEndDate, DATE_FORMAT(NOW(), '%H:%i:%S') AS TestEndTime, #{test_trade_date_begin} AS MDBeginDate, '09:30:00' AS MDBeginTime, #{test_trade_date_end} AS MDEndDate, '15:00:00' AS MDEndTime, #{manual_id} AS ManualID
                        FROM DUAL
                        ON DUPLICATE KEY UPDATE TestEndDate = VALUES(TestEndDate), TestEndTime = VALUES(TestEndTime)"""
        }
    ],
    "deal_future_quant_data": [
        ## save_future_quant_order 回测报单信息
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
    "deal_quant_data": [
        ## save_quant_order
        {
            "sql": """DELETE FROM quant.t_QuantOrder WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantOrder(HistoryNo,TradingDay,ExchangeID,SecurityID,SecurityName,FullSecurityID,SpecSecurityID,SecurityKind,Direction,OffsetFlag,SimOrderType,LimitPrice,Volume,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,Turnover)
                        SELECT #{history_no} AS HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 's' AS SecurityKind, t.Direction,IF(t.Direction = '0', '0', '1') AS OffsetFlag, t.SimOrderType, t.LimitPrice, t.Volume, t.OrderLocalID, t.OrderSysID, t.OrderStatus, t.VolumeTraded, t.InsertTime,0 AS InsertMillisec, t.CancelTime, t.Turnover
                        FROM quant.t_SimTestSpotOrder t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantOrder(HistoryNo,TradingDay,ExchangeID,SecurityID,SecurityName,FullSecurityID,SpecSecurityID,SecurityKind,Direction,OffsetFlag,SimOrderType,LimitPrice,Volume,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,Turnover)
                        SELECT #{history_no} AS HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '-', t.ExchSecurityID) AS SpecSecurityID, 'o' AS SecurityKind, t.Direction, t.OffsetFlag, t.SimOrderType, t.LimitPrice, t.Volume, t.OrderLocalID, t.OrderSysID, t.OrderStatus, t.VolumeTraded, t.InsertTime, t.InsertMillisec, t.CancelTime, 0 AS Turnover
                        FROM quant.t_SimTestSpOrder t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantOrder(HistoryNo,TradingDay,ExchangeID,SecurityID,SecurityName,FullSecurityID,SpecSecurityID,SecurityKind,Direction,OffsetFlag,SimOrderType,LimitPrice,Volume,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,Turnover)
                        SELECT #{history_no} AS HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 'r' AS SecurityKind, t.Direction,CASE WHEN t.Direction IN ('0', 'i', 'l') THEN '0' WHEN t.Direction IN ('1', 'j', 'k') THEN '1' ELSE '' END AS OffsetFlag, t.SimOrderType, t.LimitPrice, t.Volume, t.OrderLocalID, t.OrderSysID, t.OrderStatus, t.VolumeTraded, t.InsertTime,0 AS InsertMillisec, t.CancelTime, t.Turnover
                        FROM quant.t_SimTestCreditOrder t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        ## save_quant_trade
        {
            "sql": """DELETE FROM quant.t_QuantTrade WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantTrade(HistoryNo, TradingDay, TradeID, TradeDate, TradeTime, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, Direction, OffsetFlag, Price, Volume, VolumeMultiple, OrderLocalID, OrderSysID, TradingAmount, TotalPosCost, TradingFee, BeforeTradeTodayAmount, AfterTradeTodayAmount)
                        SELECT t.HistoryNo, t.TradingDay, t.TradeID, t.TradeDay AS TradeDate, t.TradeTime, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 's' AS SecurityKind, t.Direction, IF(t.Direction = '0', '0', '1') AS OffsetFlag, t.TradePrice AS Price, t.Volume, 1 AS VolumeMultiple, t.OrderLocalID, t.OrderSysID, t.TradePrice * t.Volume AS TradingAmount, t.TotalPosCost, t.CommissionFee AS TradingFee, 0 AS BeforeTradeTodayAmount, 0 AS AfterTradeTodayAmount
                        FROM quant.t_simtestspottradedetail t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantTrade(HistoryNo, TradingDay, TradeID, TradeDate, TradeTime, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, Direction, OffsetFlag, Price, Volume, VolumeMultiple, OrderLocalID, OrderSysID, TradingAmount, TotalPosCost, TradingFee, BeforeTradeTodayAmount, AfterTradeTodayAmount)
                        SELECT t.HistoryNo, t.TradingDay, t.TradeID, t.TradeDay AS TradeDate, t.TradeTime, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '-', t.ExchSecurityID) AS SpecSecurityID, 'o' AS SecurityKind, t.Direction, t.OffsetFlag, t.TradePrice AS Price, t.Volume, t.VolumeMultiple, t.OrderLocalID, t.OrderSysID, t.TradePrice * t.Volume * t.VolumeMultiple AS TradingAmount, t.TotalPosCost, t.CommissionFee AS TradingFee, t.BeforeTradeTodayAmount, t.AfterTradeTodayAmount
                        FROM quant.t_simtestsptradedetail t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantTrade(HistoryNo, TradingDay, TradeID, TradeDate, TradeTime, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, Direction, OffsetFlag, Price, Volume, VolumeMultiple, OrderLocalID, OrderSysID, TradingAmount, TotalPosCost, TradingFee, BeforeTradeTodayAmount, AfterTradeTodayAmount)
                        SELECT t.HistoryNo, t.TradingDay, t.TradeID, t.TradeDay AS TradeDate, t.TradeTime, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 's' AS SecurityKind, t.Direction, CASE WHEN t.Direction IN ('0', 'i', 'l') THEN '0' WHEN t.Direction IN ('1', 'j', 'k') THEN '1' ELSE '' END AS OffsetFlag, t.TradePrice AS Price, t.Volume, 1 AS VolumeMultiple, t.OrderLocalID, t.OrderSysID, t.TradePrice * t.Volume AS TradingAmount, t.TotalPosCost, t.CommissionFee AS TradingFee, 0 AS BeforeTradeTodayAmount, 0 AS AfterTradeTodayAmount
                        FROM quant.t_simtestcredittradedetail t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        },
        ## save_quant_asset
        {
            "sql": """DELETE FROM quant.t_QuantAsset WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantAsset(HistoryNo, TradingDay, InitAmount, InitMargin, InitSecurityValue, InitAsset, PreAmount, PreMargin, PreSecurityValue, PreAsset, Amount, Margin, SecurityValue, TodayBuyCapital, TodaySellCapital, TodayProfit, Profit, TotalAsset, ProfitRatio, MaxTodayLongAmount, MaxTodayShortAmount, s_InitAmount, s_InitMargin, s_InitSecurityValue, s_PreAmount, s_PreMargin, s_PreSecurityValue, s_Amount, s_Margin, s_SecurityValue, s_TodayProfit, s_Profit, s_TotalAsset, o_InitAmount, o_InitMargin, o_InitSecurityValue, o_PreAmount, o_PreMargin, o_PreSecurityValue, o_Amount, o_Margin, o_SecurityValue, o_TodayProfit, o_Profit, o_TotalAsset, r_InitAmount, r_InitMargin, r_InitSecurityValue, r_PreAmount, r_PreMargin, r_PreSecurityValue, r_Amount, r_Margin, r_SecurityValue, r_TodayProfit, r_Profit, r_TotalAsset, PreCollateralValueWithoutCreditBuy, CollateralValueWithoutCreditBuy, CreditBuyAmount, CreditBuyInterestFee, CreditBuyProfit, CreditSellAmount, CreditSellInterestFee, CreditSellProfit, TotalNetAsset, PreCreditBuySecurityValue, CreditBuySecurityValue, PreCreditSellSecurityValue, CreditSellSecurityValue)
                        SELECT t.HistoryNo, t.TradingDay, SUM(t.InitAmount) AS InitAmount, SUM(t.InitMargin) AS InitMargin, SUM(t.InitSecurityValue) AS InitSecurityValue, SUM(t.InitAsset) AS InitAsset, SUM(t.PreAmount) AS PreAmount, SUM(t.PreMargin) AS PreMargin, SUM(t.PreSecurityValue) AS PreSecurityValue, SUM(t.PreAsset) AS PreAsset, SUM(t.Amount) AS Amount, SUM(t.Margin) AS Margin, SUM(t.SecurityValue) AS SecurityValue, SUM(IFNULL(tt.TodayBuyCapital, 0)) AS TodayBuyCapital, SUM(IFNULL(tt.TodaySellCapital, 0)) AS TodaySellCapital, SUM(t.TodayProfit) AS TodayProfit, SUM(t.Profit) AS Profit, SUM(t.TotalAsset) AS TotalAsset, IF(SUM(t.InitAsset) = 0, 0, SUM(t.Profit) / SUM(t.InitAsset)) AS ProfitRatio, SUM(t.MaxTodayLongAmount) AS MaxTodayLongAmount, SUM(t.MaxTodayShortAmount) AS MaxTodayShortAmount, SUM(t.s_InitAmount) AS s_InitAmount, SUM(t.s_InitMargin) AS s_InitMargin, SUM(t.s_InitSecurityValue) AS s_InitSecurityValue, SUM(t.s_PreAmount) AS s_PreAmount, SUM(t.s_PreMargin) AS s_PreMargin, SUM(t.s_PreSecurityValue) AS s_PreSecurityValue, SUM(t.s_Amount) AS s_Amount, SUM(t.s_Margin) AS s_Margin, SUM(t.s_SecurityValue) AS s_SecurityValue, SUM(t.s_TodayProfit) AS s_TodayProfit, SUM(t.s_Profit) AS s_Profit, SUM(t.s_TotalAsset) AS s_TotalAsset, SUM(t.o_InitAmount) AS o_InitAmount, SUM(t.o_InitMargin) AS o_InitMargin, SUM(t.o_InitSecurityValue) AS o_InitSecurityValue, SUM(t.o_PreAmount) AS o_PreAmount, SUM(t.o_PreMargin) AS o_PreMargin, SUM(t.o_PreSecurityValue) AS o_PreSecurityValue, SUM(t.o_Amount) AS o_Amount, SUM(t.o_Margin) AS o_Margin, SUM(t.o_SecurityValue) AS o_SecurityValue, SUM(t.o_TodayProfit) AS o_TodayProfit, SUM(t.o_Profit) AS o_Profit, SUM(t.o_TotalAsset) AS o_TotalAsset, SUM(t.r_InitAmount) AS r_InitAmount, SUM(t.r_InitMargin) AS r_InitMargin, SUM(t.r_InitSecurityValue) AS r_InitSecurityValue, SUM(t.r_PreAmount) AS r_PreAmount, SUM(t.r_PreMargin) AS r_PreMargin, SUM(t.r_PreSecurityValue) AS r_PreSecurityValue, SUM(t.r_Amount) AS r_Amount, SUM(t.r_Margin) AS r_Margin, SUM(t.r_SecurityValue) AS r_SecurityValue, SUM(t.r_TodayProfit) AS r_TodayProfit, SUM(t.r_Profit) AS r_Profit, SUM(t.r_TotalAsset) AS r_TotalAsset, SUM(t.PreCollateralValueWithoutCreditBuy) AS PreCollateralValueWithoutCreditBuy, SUM(t.CollateralValueWithoutCreditBuy) AS CollateralValueWithoutCreditBuy, SUM(t.CreditBuyAmount) AS CreditBuyAmount, SUM(t.CreditBuyInterestFee) AS CreditBuyInterestFee, SUM(t.CreditBuyProfit) AS CreditBuyProfit, SUM(t.CreditSellAmount) AS CreditSellAmount, SUM(t.CreditSellInterestFee) AS CreditSellInterestFee, SUM(t.CreditSellProfit) AS CreditSellProfit, SUM(t.TotalNetAsset) AS TotalNetAsset, SUM(t.PreCreditBuySecurityValue) AS PreCreditBuySecurityValue, SUM(t.CreditBuySecurityValue) AS CreditBuySecurityValue, SUM(t.PreCreditSellSecurityValue) AS PreCreditSellSecurityValue, SUM(t.CreditSellSecurityValue) AS CreditSellSecurityValue
                        FROM(
                            SELECT t.HistoryNo, t.TradingDay, SUM(t.InitAmount) AS InitAmount, SUM(t.InitMargin) AS InitMargin, SUM(t.InitSecurityValue) AS InitSecurityValue, SUM(t.InitAsset) AS InitAsset, SUM(t.PreAmount) AS PreAmount, SUM(t.PreMargin) AS PreMargin, SUM(t.PreSecurityValue) AS PreSecurityValue, SUM(t.PreAsset) AS PreAsset, SUM(t.Amount) AS Amount, SUM(t.Margin) AS Margin, SUM(t.SecurityValue) AS SecurityValue, SUM(t.TodayProfit) AS TodayProfit, SUM(t.Profit) AS Profit, SUM(t.TotalAsset) AS TotalAsset, SUM(t.MaxTodayLongAmount) AS MaxTodayLongAmount, SUM(t.MaxTodayShortAmount) AS MaxTodayShortAmount, SUM(t.s_InitAmount) AS s_InitAmount, SUM(t.s_InitMargin) AS s_InitMargin, SUM(t.s_InitSecurityValue) AS s_InitSecurityValue, SUM(t.s_PreAmount) AS s_PreAmount, SUM(t.s_PreMargin) AS s_PreMargin, SUM(t.s_PreSecurityValue) AS s_PreSecurityValue, SUM(t.s_Amount) AS s_Amount, SUM(t.s_Margin) AS s_Margin, SUM(t.s_SecurityValue) AS s_SecurityValue, SUM(t.s_TodayProfit) AS s_TodayProfit, SUM(t.s_Profit) AS s_Profit, SUM(t.s_TotalAsset) AS s_TotalAsset, SUM(t.o_InitAmount) AS o_InitAmount, SUM(t.o_InitMargin) AS o_InitMargin, SUM(t.o_InitSecurityValue) AS o_InitSecurityValue, SUM(t.o_PreAmount) AS o_PreAmount, SUM(t.o_PreMargin) AS o_PreMargin, SUM(t.o_PreSecurityValue) AS o_PreSecurityValue, SUM(t.o_Amount) AS o_Amount, SUM(t.o_Margin) AS o_Margin, SUM(t.o_SecurityValue) AS o_SecurityValue, SUM(t.o_TodayProfit) AS o_TodayProfit, SUM(t.o_Profit) AS o_Profit, SUM(t.o_TotalAsset) AS o_TotalAsset, SUM(t.r_InitAmount) AS r_InitAmount, SUM(t.r_InitMargin) AS r_InitMargin, SUM(t.r_InitSecurityValue) AS r_InitSecurityValue, SUM(t.r_PreAmount) AS r_PreAmount, SUM(t.r_PreMargin) AS r_PreMargin, SUM(t.r_PreSecurityValue) AS r_PreSecurityValue, SUM(t.r_Amount) AS r_Amount, SUM(t.r_Margin) AS r_Margin, SUM(t.r_SecurityValue) AS r_SecurityValue, SUM(t.r_TodayProfit) AS r_TodayProfit, SUM(t.r_Profit) AS r_Profit, SUM(t.r_TotalAsset) AS r_TotalAsset, SUM(t.PreCollateralValueWithoutCreditBuy) AS PreCollateralValueWithoutCreditBuy, SUM(t.CollateralValueWithoutCreditBuy) AS CollateralValueWithoutCreditBuy, SUM(t.CreditBuyAmount) AS CreditBuyAmount, SUM(t.CreditBuyInterestFee) AS CreditBuyInterestFee, SUM(t.CreditBuyProfit) AS CreditBuyProfit, SUM(t.CreditSellAmount) AS CreditSellAmount, SUM(t.CreditSellInterestFee) AS CreditSellInterestFee, SUM(t.CreditSellProfit) AS CreditSellProfit, SUM(t.TotalNetAsset) AS TotalNetAsset, SUM(t.PreCreditBuySecurityValue) AS PreCreditBuySecurityValue, SUM(t.CreditBuySecurityValue) AS CreditBuySecurityValue, SUM(t.PreCreditSellSecurityValue) AS PreCreditSellSecurityValue, SUM(t.CreditSellSecurityValue) AS CreditSellSecurityValue
                            FROM (SELECT t.HistoryNo, t.TradingDay, t4.InitAmount, t4.InitMargin, t4.InitSecurityValue, t4.InitAmount + t4.InitMargin + t4.InitSecurityValue AS InitAsset, t.PreAmount, 0 AS PreMargin, t.PreSecurityValue, t.PreAmount + t.PreSecurityValue AS PreAsset, t.Amount, 0 AS Margin, t.SecurityValue, t.Amount + t.SecurityValue - t.PreAmount - t.PreSecurityValue AS TodayProfit, t.Amount + t.SecurityValue - t4.InitAmount - t4.InitSecurityValue AS Profit, t.Amount + t.SecurityValue AS TotalAsset, 0 AS MaxTodayLongAmount, 0 AS MaxTodayShortAmount, t4.InitAmount As s_InitAmount, t4.InitMargin AS s_InitMargin, t4.InitSecurityValue AS s_InitSecurityValue, t.PreAmount AS s_PreAmount, 0 AS s_PreMargin, t.PreSecurityValue AS s_PreSecurityValue, t.Amount AS s_Amount, 0 AS s_Margin, t.SecurityValue AS s_SecurityValue, t.Amount + t.SecurityValue - t.PreAmount - t.PreSecurityValue AS s_TodayProfit, t.Amount + t.SecurityValue - t4.InitAmount - t4.InitSecurityValue AS s_Profit, t.Amount + t.SecurityValue AS s_TotalAsset, 0 AS o_InitAmount, 0 AS o_InitMargin, 0 AS o_InitSecurityValue, 0 AS o_PreAmount, 0 AS o_PreMargin, 0 AS o_PreSecurityValue, 0 AS o_Amount, 0 AS o_Margin, 0 AS o_SecurityValue, 0 AS o_TodayProfit, 0 AS o_Profit, 0 AS o_TotalAsset, 0 AS r_InitAmount, 0 AS r_InitMargin, 0 AS r_InitSecurityValue, 0 AS r_PreAmount, 0 AS r_PreMargin, 0 AS r_PreSecurityValue, 0 AS r_Amount, 0 AS r_Margin, 0 AS r_SecurityValue, 0 AS r_TodayProfit, 0 AS r_Profit, 0 AS r_TotalAsset, 0 AS PreCollateralValueWithoutCreditBuy, 0 AS CollateralValueWithoutCreditBuy, 0 AS CreditBuyAmount, 0 AS CreditBuyInterestFee, 0 AS CreditBuyProfit, 0 AS CreditSellAmount, 0 AS CreditSellInterestFee, 0 AS CreditSellProfit, 0 AS TotalNetAsset, 0 AS PreCreditBuySecurityValue, 0 AS CreditBuySecurityValue, 0 AS PreCreditSellSecurityValue, 0 AS CreditSellSecurityValue
                                FROM quant.t_simtestspotresult t
                                JOIN quant.t_quantmarketdata t3 ON (t3.ExchangeID = '1' AND t3.SecurityID = '000001' AND t.TradingDay = t3.TradingDay)
                                JOIN (SELECT t.TradingDay, t.PreAmount AS InitAmount, 0 AS InitMargin, t.PreSecurityValue AS InitSecurityValue FROM quant.t_simtestspotresult t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay Limit 1) t4
                                WHERE t.HistoryNo = #{history_no}
                                UNION
                                SELECT t.HistoryNo, t.TradingDay, t4.InitAmount, t4.InitMargin, t4.InitSecurityValue, t4.InitAmount + t4.InitMargin + t4.InitSecurityValue AS InitAsset, t.PreAmount, t.PreMargin, t.PreSecurityValue, t.PreAmount + t.PreMargin + t.PreSecurityValue AS PreAsset, t.Amount, t.Margin, t.SecurityValue, t.Amount + t.Margin + t.SecurityValue - t.PreAmount - t.PreMargin - t.PreSecurityValue AS TodayProfit, t.Amount + t.Margin + t.SecurityValue - t4.InitAmount - t4.InitMargin - t4.InitSecurityValue AS Profit, t.Amount + t.Margin + t.SecurityValue AS TotalAsset, t.MaxTodayLongAmount, t.MaxTodayShortAmount, 0 AS s_InitAmount, 0 AS s_InitMargin, 0 AS s_InitSecurityValue, 0 AS s_PreAmount, 0 AS s_PreMargin, 0 AS s_PreSecurityValue, 0 AS s_Amount, 0 AS s_Margin, 0 AS s_SecurityValue, 0 AS s_TodayProfit, 0 AS s_Profit, 0 AS s_TotalAsset, t4.InitAmount AS o_InitAmount, t4.InitMargin AS o_InitMargin, t4.InitSecurityValue As o_InitSecurityValue, t.PreAmount AS o_PreAmount, t.PreMargin AS o_PreMargin, t.PreSecurityValue AS o_PreSecurityValue, t.Amount AS o_Amount, t.Margin AS o_Margin, t.SecurityValue AS o_SecurityValue, t.Amount + t.SecurityValue - t.PreAmount - t.PreSecurityValue AS o_TodayProfit, t.Amount + t.SecurityValue - t4.InitAmount - t4.InitSecurityValue AS o_Profit, t.Amount + t.SecurityValue AS o_TotalAsset, 0 As r_InitAmount, 0 AS r_InitMargin, 0 AS r_InitSecurityValue, 0 AS r_PreAmount, 0 AS r_PreMargin, 0 AS r_PreSecurityValue, 0 AS r_Amount, 0 AS r_Margin, 0 AS r_SecurityValue, 0 AS r_TodayProfit, 0 AS r_Profit, 0 AS r_TotalAsset, 0 AS PreCollateralValueWithoutCreditBuy, 0 AS CollateralValueWithoutCreditBuy, 0 AS CreditBuyAmount, 0 AS CreditBuyInterestFee, 0 AS CreditBuyProfit, 0 AS CreditSellAmount, 0 AS CreditSellInterestFee, 0 AS CreditSellProfit, 0 AS TotalNetAsset, 0 AS PreCreditBuySecurityValue, 0 AS CreditBuySecurityValue, 0 AS PreCreditSellSecurityValue, 0 AS CreditSellSecurityValue
                                FROM quant.t_simtestspresult t
                                JOIN quant.t_quantmarketdata t3 ON (t3.ExchangeID = '1' AND t3.SecurityID = '000001' AND t.TradingDay = t3.TradingDay)
                                JOIN (SELECT t.TradingDay, t.PreAmount AS InitAmount, t.PreMargin AS InitMargin, t.PreSecurityValue AS InitSecurityValue FROM quant.t_simtestspresult t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay Limit 1) t4
                                WHERE t.HistoryNo = #{history_no}
                                UNION
                                SELECT t.HistoryNo, t.TradingDay, t4.InitAmount, t4.InitMargin, t4.InitSecurityValue, t4.InitAmount + t4.InitMargin + t4.InitSecurityValue AS InitAsset, t.PreAmount, 0 AS PreMargin, t.PreSecurityValue, t.PreAmount + t.PreSecurityValue AS PreAsset, t.Amount, 0 AS Margin, t.SecurityValue, t.Amount + t.SecurityValue - t.PreAmount - t.PreSecurityValue AS TodayProfit, t.Amount + t.SecurityValue - t4.InitAmount - t4.InitSecurityValue AS Profit, t.Amount + t.SecurityValue AS TotalAsset, 0 AS MaxTodayLongAmount, 0 AS MaxTodayShortAmount, 0 AS s_InitAmount, 0 AS s_InitMargin, 0 AS s_InitSecurityValue, 0 AS s_PreAmount, 0 AS s_PreMargin, 0 AS s_PreSecurityValue, 0 AS s_Amount, 0 AS s_Margin, 0 AS s_SecurityValue, 0 AS s_TodayProfit, 0 AS s_Profit, 0 AS s_TotalAsset, 0 As o_InitAmount, 0 AS o_InitMargin, 0 AS o_InitSecurityValue, 0 AS o_PreAmount, 0 AS o_PreMargin, 0 AS o_PreSecurityValue, 0 AS o_Amount, 0 AS o_Margin, 0 AS o_SecurityValue, 0 AS o_TodayProfit, 0 AS o_Profit, 0 AS o_TotalAsset, t4.InitAmount AS r_InitAmount, t4.InitMargin AS r_InitMargin, t4.InitSecurityValue As r_InitSecurityValue, t.PreAmount AS r_PreAmount, 0 AS r_PreMargin, t.PreSecurityValue AS r_PreSecurityValue, t.Amount AS r_Amount, 0 AS r_Margin, t.SecurityValue AS r_SecurityValue, t.Amount + t.SecurityValue - t.PreAmount - t.PreSecurityValue AS r_TodayProfit, t.Amount + t.SecurityValue - t4.InitAmount - t4.InitSecurityValue AS r_Profit, t.Amount + t.SecurityValue AS r_TotalAsset, t.PreCollateralValueWithoutCreditBuy, t.CollateralValueWithoutCreditBuy, t.CreditBuyAmount, t.CreditBuyInterestFee, t.CreditBuyProfit, t.CreditSellAmount, t.CreditSellInterestFee, t.CreditSellProfit, t.TotalNetAsset, t.PreCreditBuySecurityValue, t.CreditBuySecurityValue, t.PreCreditSellSecurityValue, t.CreditSellSecurityValue
                                FROM quant.t_simtestcreditresult t
                                JOIN quant.t_quantmarketdata t3 ON (t3.ExchangeID = '1' AND t3.SecurityID = '000001' AND t.TradingDay = t3.TradingDay)
                                JOIN (SELECT t.TradingDay, t.PreAmount AS InitAmount, 0 AS InitMargin, t.PreSecurityValue AS InitSecurityValue FROM quant.t_simtestcreditresult t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay Limit 1) t4
                                WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNo, t.TradingDay) t
                        LEFT JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(IFNULL(IF((t.SecurityKind = 'o' AND ((t.Direction = '0' AND t.OffsetFlag = '0') OR (t.Direction = '1' AND t.OffsetFlag = '1'))) OR (t.SecurityKind != 'o' AND t.Direction = '0'), t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodayBuyCapital, SUM(IFNULL(IF((t.SecurityKind = 'o' AND ((t.Direction = '0' AND t.OffsetFlag = '1') OR (t.Direction = '1' AND t.OffsetFlag = '0')) OR (t.SecurityKind != '0' AND t.Direction = '1')), t.Price * t.Volume * t.VolumeMultiple, 0), 0)) AS TodaySellCapital FROM quant.t_QuantTrade t WHERE t.HistoryNo = #{history_no} GROUP BY t.HistoryNo, t.TradingDay) tt ON (t.HistoryNo = tt.HistoryNo AND t.TradingDay = tt.TradingDay)
                        GROUP BY t.HistoryNo, t.TradingDay"""
        },
        ## save_quant_position
        {
            "sql": """DELETE FROM quant.t_QuantPosition WHERE HistoryNo = #{history_no}"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_securities(runtime)
            },
            "sql": """SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspotposition t WHERE t.HistoryNo = #{history_no} ORDER BY t.ExchangeID, t.SecurityID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_QuantPosition(HistoryNo, TradingDay, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, OptionsType, PosiDirection, FirstDate, LastDate, StrikeDate, ExpireDate, Volume, PreVolume, ClosingPrice, SettlementPrice, PreSettlementPrice, UnderlyingClosePrice, UnderlyingPreClosePrice, StrikePrice, TradingAmount, TotalPosCost, OpenPosCost, PreOpenPosCost, HoldingValue, TradingFee, Profit, TodayProfit, Margin, TodayBuyCapital, TodaySellCapital, BuyCapital, SellCapital, InitTotalPosCost, InitHoldingValue, InitTodayAmount, MaxTodayAmount, FinalTodayAmount, TotalOpenPosCost, CreditBuyPos, CreditBuyAmount, CreditBuyInterestFee, CreditSellPos, CreditSellAmount, CreditSellInterestFee, CollateralOutPos, CollateralInPos, ReturnRatio, ContributionRatio)
                         SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t3.SecurityName AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 's' AS SecurityKind, '' AS OptionsType, '2' AS PosiDirection, NULL AS FirstDate, NULL AS LastDate, NULL AS StrikeDate, NULL AS ExpireDate, t.Volume, IFNULL(t4.Volume, IFNULL(t1.Volume, 0)) AS PreVolume, t.ClosePrice AS ClosingPrice, t.ClosePrice AS SettlementPrice, t3.LastClosingPrice AS PreSettlementPrice, 0 AS UnderlyingClosePrice, 0 AS UnderlyingPreClosePrice, 0 AS StrikePrice, 0 AS TradingAmount, t.TotalPosCost, t.OpenPosPrice AS OpenPosCost, IFNULL(t4.OpenPosPrice, 0) AS PreOpenPosCost, t.TotalSecurityValue AS HoldingValue, t.CommissionFee AS TradingFee, t.TotalGain AS Profit, t.TotalGain - IFNULL(t4.TotalGain, 0) AS TodayProfit, 0 AS Margin, IFNULL(t5.TodayBuyCapital, 0) AS TodayBuyCapital, IFNULL(t5.TodaySellCapital, 0) AS TodaySellCapital, IFNULL(t5.BuyCapital, 0) AS BuyCapital, IFNULL(t5.SellCapital, 0) AS SellCapital, IFNULL(t1.TotalPosCost, 0) AS InitTotalPosCost, IFNULL(t1.SecurityValue, 0) AS InitHoldingValue, 0 AS InitTodayAmount, 0 AS MaxTodayAmount, 0 AS FinalTodayAmount, 0 AS TotalOpenPosCost, 0 AS CreditBuyPos, 0 AS CreditBuyAmount, 0 AS CreditBuyInterestFee, 0 AS CreditSellPos, 0 AS CreditSellAmount, 0 AS CreditSellInterestFee, 0 AS CollateralOutPos, 0 AS CollateralInPos, IF(IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0) = 0 , 0, t.TotalGain / (IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0))) AS ReturnRatio, IF(t6.AbsProfit = 0, 0, t.TotalGain / t6.AbsProfit) AS ContributionRatio
                            FROM quant.t_simtestspotposition t
                            LEFT JOIN quant.t_simtestinitposition t1 ON (t.HistoryNo = t1.HistoryNo AND t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND t1.SecurityKind = 's')
                            JOIN quant.t_simtestinfo t2 ON (t.HistoryNo = t2.HistoryNo)
                            JOIN quant.t_quantmarketdata t3 ON (t.TradingDay = t3.TradingDay AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t3.SecurityID)
                            LEFT JOIN quant.t_simtestspotposition t4 ON (t.HistoryNo = t4.HistoryNo AND t3.LastTradingDay = t4.Tradingday AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t4.SecurityID)
                            LEFT JOIN (SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '0', 1, 0) * t1.Volume * t1.TradePrice) AS TodayBuyCapital, SUM(IF(t1.Direction = '0', 1, 0) * t1.Volume * t1.TradePrice) AS BuyCapital, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '1', 1, 0) * t1.Volume * t1.TradePrice) AS TodaySellCapital, SUM(IF(t1.Direction = '1', 1, 0) * t1.Volume * t1.TradePrice) AS SellCapital
                                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                                FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestspottradedetail t2
                                                WHERE t2.HistoryNo = #{history_no} AND t1.TradingDay >= t2.TradingDay) t1, quant.t_quantmarketdata t2
                                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID) t5 ON (t.HistoryNo = t5.HistoryNo AND t.TradingDay = t5.TradingDay AND t.ExchangeID = t5.ExchangeID AND t.SecurityID = t5.SecurityID)
                            JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(ABS(t.Profit)) AS AbsProfit FROM (SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpotPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestCreditPosition t WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNO, t.TradingDay) t6 ON (t.HistoryNo = t6.HistoryNo AND t.TradingDay = t6.TradingDay)
                            WHERE t.HistoryNo = #{history_no} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_securities(runtime)
            },
            "sql": """SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestspposition t WHERE t.HistoryNo = #{history_no} ORDER BY t.ExchangeID, t.SecurityID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_QuantPosition(HistoryNo, TradingDay, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, OptionsType, PosiDirection, FirstDate, LastDate, StrikeDate, ExpireDate, Volume, PreVolume, ClosingPrice, SettlementPrice, PreSettlementPrice, UnderlyingClosePrice, UnderlyingPreClosePrice, StrikePrice, TradingAmount, TotalPosCost, OpenPosCost, PreOpenPosCost, HoldingValue, TradingFee, Profit, TodayProfit, Margin, TodayBuyCapital, TodaySellCapital, BuyCapital, SellCapital, InitTotalPosCost, InitHoldingValue, InitTodayAmount, MaxTodayAmount, FinalTodayAmount, TotalOpenPosCost, CreditBuyPos, CreditBuyAmount, CreditBuyInterestFee, CreditSellPos, CreditSellAmount, CreditSellInterestFee, CollateralOutPos, CollateralInPos, ReturnRatio, ContributionRatio)
                        SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t3.SecurityName AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '-', t.ExchSecurityID) AS SpecSecurityID, 'o' AS SecurityKind, t.OptionsType, t.PosiDirection, t.FirstDate, t.LastDate, t.StrikeDate, t.ExpireDate, t.Volume, IFNULL(t4.Volume, IFNULL(t1.Volume, 0)) AS PreVolume, t.ClosePrice AS ClosingPrice, t.SettlementPrice, t.PreSettlementPrice, t.UnderlyingClosePrice, t.UnderlyingPreClosePrice, t.StrikePrice, 0 AS TradingAmount, t.TotalPosCost, t.OpenPosPrice AS OpenPosCost, IFNULL(t4.OpenPosPrice, 0) AS PreOpenPosCost, t.TotalSecurityValue AS HoldingValue, t.CommissionFee AS TradingFee, t.TotalGain AS Profit, t.TodayProfit, t.Margin, IFNULL(t5.TodayBuyCapital, 0) AS TodayBuyCapital, IFNULL(t5.TodaySellCapital, 0) AS TodaySellCapital, IFNULL(t5.BuyCapital, 0) AS BuyCapital, IFNULL(t5.SellCapital, 0) AS SellCapital, IFNULL(t1.TotalPosCost, 0) AS InitTotalPosCost, IFNULL(t1.SecurityValue, 0) AS InitHoldingValue, t.InitTodayAmount, t.MaxTodayAmount, t.FinalTodayAmount, t.OpenPosPrice * t.Volume * t.VolumeMultiple AS TotalOpenPosCost, 0 AS CreditBuyPos, 0 AS CreditBuyAmount, 0 AS CreditBuyInterestFee, 0 AS CreditSellPos, 0 AS CreditSellAmount, 0 AS CreditSellInterestFee, 0 AS CollateralOutPos, 0 AS CollateralInPos, CASE WHEN t.PosiDirection = '2' THEN IF(IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0) = 0 , 0, t.TotalGain / (IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0))) WHEN t.PosiDirection = '3' THEN IF(ABS(IFNULL(t1.SecurityValue, 0) - IFNULL(t5.SellCapital, 0)) = 0 , 0, t.TotalGain / ABS(IFNULL(t1.SecurityValue, 0) - IFNULL(t5.SellCapital, 0))) ELSE 0 END AS ReturnRatio, IF(t6.AbsProfit = 0, 0, t.TotalGain / t6.AbsProfit) AS ContributionRatio
                        FROM quant.t_simtestspposition t
                        LEFT JOIN quant.t_simtestinitposition t1 ON (t.HistoryNo = t1.HistoryNo AND t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND t1.SecurityKind = 'o')
                        JOIN quant.t_simtestinfo t2 ON (t.HistoryNo = t2.HistoryNo)
                        JOIN quant.t_quantmarketdata t3 ON (t.ExchangeID = t3.ExchangeID AND t.SecurityID = t3.SecurityID AND t.TradingDay = t3.TradingDay)
                        LEFT JOIN quant.t_simtestspposition t4 ON (t.HistoryNo = t4.HistoryNo AND t3.LastTradingDay = t4.Tradingday AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t4.SecurityID)
                        LEFT JOIN (SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IFNULL(IF((t1.Direction = '0' AND t1.OffsetFlag = '0') OR (t1.Direction = '1' AND t1.OffsetFlag = '1'), t1.TradePrice * t1.Volume * t1.VolumeMultiple, 0), 0)) AS TodayBuyCapital, SUM(IFNULL(IF((t1.Direction = '0' AND t1.OffsetFlag = '0') OR (t1.Direction = '1' AND t1.OffsetFlag = '1'), t1.TradePrice * t1.Volume * t1.VolumeMultiple, 0), 0)) AS BuyCapital, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IFNULL(IF((t1.Direction = '0' AND t1.OffsetFlag = '1') OR (t1.Direction = '1' AND t1.OffsetFlag = '0'), t1.TradePrice * t1.Volume * t1.VolumeMultiple, 0), 0)) AS TodaySellCapital, SUM(IFNULL(IF((t1.Direction = '0' AND t1.OffsetFlag = '1') OR (t1.Direction = '1' AND t1.OffsetFlag = '0'), t1.TradePrice * t1.Volume * t1.VolumeMultiple, 0), 0)) AS SellCapital
                                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.OffsetFlag, t2.VolumeMultiple, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                                FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestsptradedetail t2
                                                WHERE t2.HistoryNo = #{history_no} AND t1.TradingDay >= t2.TradingDay) t1, quant.t_quantmarketdata t2
                                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID) t5 ON (t.HistoryNo = t5.HistoryNo AND t.TradingDay = t5.TradingDay AND t.ExchangeID = t5.ExchangeID AND t.SecurityID = t5.SecurityID)
                        JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(ABS(t.Profit)) AS AbsProfit FROM (SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpotPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestCreditPosition t WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNO, t.TradingDay) t6 ON (t.HistoryNo = t6.HistoryNo AND t.TradingDay = t6.TradingDay)
                        WHERE t.HistoryNo = #{history_no} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}"""
        },
        {
            "meta": {
                "callback": lambda runtime: do_callback_get_securities(runtime)
            },
            "sql": """SELECT DISTINCT t.ExchangeID, t.SecurityID FROM quant.t_simtestcreditposition t WHERE t.HistoryNo = #{history_no} ORDER BY t.ExchangeID, t.SecurityID"""
        },
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_QuantPosition(HistoryNo, TradingDay, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, OptionsType, PosiDirection, FirstDate, LastDate, StrikeDate, ExpireDate, Volume, PreVolume, ClosingPrice, SettlementPrice, PreSettlementPrice, UnderlyingClosePrice, UnderlyingPreClosePrice, StrikePrice, TradingAmount, TotalPosCost, OpenPosCost, PreOpenPosCost, HoldingValue, TradingFee, Profit, TodayProfit, Margin, TodayBuyCapital, TodaySellCapital, BuyCapital, SellCapital, InitTotalPosCost, InitHoldingValue, InitTodayAmount, MaxTodayAmount, FinalTodayAmount, TotalOpenPosCost, CreditBuyPos, CreditBuyAmount, CreditBuyInterestFee, CreditSellPos, CreditSellAmount, CreditSellInterestFee, CollateralOutPos, CollateralInPos, ReturnRatio, ContributionRatio)
                        SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, t3.SecurityName AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, 's' AS SecurityKind, '' AS OptionsType, '2' AS PosiDirection, NULL AS FirstDate, NULL AS LastDate, NULL AS StrikeDate, NULL AS ExpireDate, t.Volume, IFNULL(t4.Volume, IFNULL(t1.Volume, 0)) AS PreVolume, t.ClosePrice AS ClosingPrice, t.ClosePrice AS SettlementPrice, t3.LastClosingPrice AS PreSettlementPrice, 0 AS UnderlyingClosePrice, 0 AS UnderlyingPreClosePrice, 0 AS StrikePrice, 0 AS TradingAmount, t.TotalPosCost, t.OpenPosPrice AS OpenPosCost, IFNULL(t4.OpenPosPrice, 0) AS PreOpenPosCost, t.TotalSecurityValue AS HoldingValue, t.CommissionFee AS TradingFee, t.TotalGain AS Profit, t.TotalGain - IFNULL(t4.TotalGain, 0) AS TodayProfit, 0 AS Margin, IFNULL(t5.TodayBuyCapital, 0) AS TodayBuyCapital, IFNULL(t5.TodaySellCapital, 0) AS TodaySellCapital, IFNULL(t5.BuyCapital, 0) AS BuyCapital, IFNULL(t5.SellCapital, 0) AS SellCapital, IFNULL(t1.TotalPosCost, 0) AS InitTotalPosCost, IFNULL(t1.SecurityValue, 0) AS InitHoldingValue, 0 AS InitTodayAmount, 0 AS MaxTodayAmount, 0 AS FinalTodayAmount, t.OpenPosCost AS TotalOpenPosCost, t.CreditBuyPos, t.CreditBuyAmount, t.CreditBuyInterestFee, t.CreditSellPos, t.CreditSellAmount, t.CreditSellInterestFee, t.CollateralOutPos, t.CollateralInPos, IF(IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0) = 0 , 0, t.TotalGain / (IFNULL(t1.SecurityValue, 0) + IFNULL(t5.BuyCapital, 0))) AS ReturnRatio, IF(t6.AbsProfit = 0, 0, t.TotalGain / t6.AbsProfit) AS ContributionRatio
                            FROM quant.t_simtestcreditposition t
                            LEFT JOIN quant.t_simtestinitposition t1 ON (t.HistoryNo = t1.HistoryNo AND t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND t1.SecurityKind = 'r')
                            JOIN quant.t_simtestinfo t2 ON (t.HistoryNo = t2.HistoryNo)
                            JOIN quant.t_quantmarketdata t3 ON (t.TradingDay = t3.TradingDay AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t3.SecurityID)
                            LEFT JOIN quant.t_simtestcreditposition t4 ON (t.HistoryNo = t4.HistoryNo AND t3.LastTradingDay = t4.Tradingday AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t4.SecurityID)
                            LEFT JOIN (SELECT t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '0' OR t1.Direction = 'i' OR t1.Direction = 'l', 1, 0) * t1.Volume * t1.TradePrice) AS TodayBuyCapital, SUM(IF(t1.Direction = '0' OR t1.Direction = 'i' OR t1.Direction = 'l', 1, 0) * t1.Volume * t1.TradePrice) AS BuyCapital, SUM(IF(t1.TradingDay = t1.TradeDay, 1, 0) * IF(t1.Direction = '1' OR t1.Direction = 'j' OR t1.Direction = 'k', 1, 0) * t1.Volume * t1.TradePrice) AS TodaySellCapital, SUM(IF(t1.Direction = '1' OR t1.Direction = 'j' OR t1.Direction = 'k', 1, 0) * t1.Volume * t1.TradePrice) AS SellCapital
                                        FROM (SELECT t2.HistoryNo, t1.TradingDay, t2.TradeID, t2.TradeDay, t2.TradeTime, t2.ExchangeID, t2.SecurityID, t2.Direction, t2.Volume, t2.TradePrice, t2.TotalPosCost, t2.CommissionFee, t2.OrderLocalID, t2.OrderSysID
                                                FROM (SELECT tm.TradingDay FROM quant.t_simtestinfo ti, quant.t_quantmarketdata tm WHERE ti.HistoryNo = #{history_no} AND tm.ExchangeID = '1' AND tm.SecurityID = '000001' AND tm.Tradingday >= ti.MDBeginDate AND tm.TradingDay <= ti.MDEndDate) t1, quant.t_simtestcredittradedetail t2
                                                WHERE t2.HistoryNo = #{history_no} AND t1.TradingDay >= t2.TradingDay) t1, quant.t_quantmarketdata t2
                                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID
                                        GROUP BY t1.HistoryNo, t1.TradingDay, t1.ExchangeID, t1.SecurityID) t5 ON (t.HistoryNo = t5.HistoryNo AND t.TradingDay = t5.TradingDay AND t.ExchangeID = t5.ExchangeID AND t.SecurityID = t5.SecurityID)
                            JOIN (SELECT t.HistoryNo, t.TradingDay, SUM(ABS(t.Profit)) AS AbsProfit FROM (SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpotPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestSpPosition t WHERE t.HistoryNo = #{history_no} UNION ALL SELECT t.HistoryNo, t.TradingDay, t.TotalGain AS Profit FROM quant.t_SimTestCreditPosition t WHERE t.HistoryNo = #{history_no}) t GROUP BY t.HistoryNO, t.TradingDay) t6 ON (t.HistoryNo = t6.HistoryNo AND t.TradingDay = t6.TradingDay)
                            WHERE t.HistoryNo = #{history_no} AND t.ExchangeID = #{exchange_id} AND t.SecurityID = #{security_id}"""
        },
        ## save_quant_profit
        {
            "sql": """DELETE FROM quant.t_QuantProfit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantProfit(HistoryNo, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, PosiDirection, InitHoldingValue, FinalHoldingValue, TradingCount, TradingFee, Profit, BuyCapital, SellCapital, ReturnRatio, ContributionRatio)
                        SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityName, t.FullSecurityID, t.SpecSecurityID, t.SecurityKind, t.PosiDirection, t.InitHoldingValue, t.FinalHoldingValue, t.TradingCount, t.TradingFee, t.Profit, t.BuyCapital, t.SellCapital, IF(t.ReturnBase = 0, 0, t.Profit / t.ReturnBase) AS ReturnRatio, 0 AS ContributionRatio
                        FROM(
                            SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t3.SecurityName, t.FullSecurityID, t.SpecSecurityID, t.SecurityKind, t.PosiDirection, IFNULL(t3.InitHoldingValue, 0) AS InitHoldingValue, IFNULL(t3.FinalHoldingValue, 0) AS FinalHoldingValue, IFNULL(t2.TradingCount, 0) AS TradingCount, IFNULL(t2.TradingAmount, 0) AS TradingAmount, IFNULL(t2.BuyCapital, 0) AS BuyCapital, IFNULL(t2.SellCapital, 0) AS SellCapital, IFNULL(t2.TradingProfit, 0) AS TradingProfit, IFNULL(t2.TradingFee, 0) AS TradingFee, IFNULL(t3.FinalHoldingValue, 0) - IFNULL(t3.InitHoldingValue, 0) + IFNULL(t2.TradingProfit, 0) - IFNULL(t2.TradingFee, 0) AS Profit, CASE WHEN t.PosiDirection = '2' THEN IFNULL(t3.InitHoldingValue, 0) + IFNULL(t2.BuyCapital, 0) WHEN t.PosiDirection = '3' THEN IFNULL(t3.InitHoldingValue, 0) - IFNULL(t2.SellCapital, 0) ELSE 0 END AS ReturnBase
                            FROM
                                (SELECT DISTINCT t.HistoryNo, t.ExchangeID, t.SecurityID, t.FullSecurityID, t.SpecSecurityID, t.SecurityKind, t.PosiDirection
                                FROM quant.t_QuantPosition t
                                WHERE t.HistoryNo = #{history_no}) t
                                LEFT JOIN (SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityKind, t.PosiDirection, SUM(t.TradingCount) AS TradingCount, SUM(T.TradingAmount) AS TradingAmount, SUM(t.BuyCapital) AS BuyCapital, SUM(t.SellCapital) AS SellCapital, SUM(t.TradingProfit) AS TradingProfit, SUM(t.TradingFee) AS TradingFee
                                FROM
                                (SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityKind, IF(t.SecurityKind = 'o' AND ((t.Direction = '0' AND t.OffsetFlag = '1') OR (t.Direction = '1' AND t.OffsetFlag = '0')), '3', '2') AS PosiDirection, 1 AS TradingCount, t.TradingAmount, CASE WHEN t.Direction in ('0', 'i', 'l') THEN 1 WHEN t.Direction in ('1', 'j', 'k') THEN 0 ELSE 0 END * t.TradingAmount AS BuyCapital, CASE WHEN t.Direction in ('0', 'i', 'l') THEN 0 WHEN t.Direction in ('1', 'j', 'k') THEN 1 ELSE 0 END * t.TradingAmount AS SellCapital, CASE WHEN t.Direction in ('0', 'i', 'l') THEN -1 WHEN t.Direction in ('1', 'j', 'k') THEN 1 ELSE 0 END * t.TradingAmount AS TradingProfit, t.TradingFee
                                FROM quant.t_quanttrade t
                                WHERE t.HistoryNo = #{history_no}) t
                                GROUP BY t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityKind, t.PosiDirection) t2 ON (t.HistoryNo = t2.HistoryNo AND t.ExchangeID = t2.ExchangeID AND t.SecurityID = t2.SecurityID AND t.SecurityKind = t2.SecurityKind AND t.PosiDirection = t2.PosiDirection)
                                LEFT JOIN(SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityName, t.SecurityKind, t.PosiDirection, t.InitHoldingValue, t.HoldingValue AS FinalHoldingValue
                                FROM quant.t_QuantPosition t
                                WHERE t.HistoryNo = #{history_no} AND t.TradingDay = (SELECT MAX(tp.TradingDay) FROM quant.t_QuantPosition tp WHERE tp.HistoryNo = #{history_no})) t3 ON (t.HistoryNo = t3.HistoryNo AND t.ExchangeID = t3.ExchangeID AND t.SecurityID = t3.SecurityID AND t.SecurityKind = t3.SecurityKind AND t.PosiDirection = t3.PosiDirection)) t"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantProfit(HistoryNo, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, SecurityKind, PosiDirection, ContributionRatio)
                        SELECT t.HistoryNo, t.ExchangeID, t.SecurityID, t.SecurityName, t.FullSecurityID, t.SpecSecurityID, t.SecurityKind, t.PosiDirection, CASE WHEN t.Profit > 0 AND t1.TotalGain > 0 THEN t.Profit / t1.TotalGain WHEN t.Profit < 0 AND t1.TotalLose < 0 THEN t.Profit / t1.TotalLose ELSE 0 END AS ContributionRatio
                        FROM quant.t_QuantProfit t,
                            (SELECT t.HistoryNo, SUM(IF(t.Profit > 0, t.Profit, 0)) AS TotalGain, SUM(IF(t.Profit < 0, t.Profit, 0)) AS TotalLose
                            FROM quant.t_QuantProfit t
                            WHERE t.HistoryNo = #{history_no}
                            GROUP BY t.HistoryNo) t1
                        WHERE t.HistoryNo = #{history_no} AND t.HistoryNo = t1.HistoryNo
                        ON DUPLICATE KEY UPDATE ContributionRatio = VALUES(ContributionRatio)"""
        },
        ## save_quant_debt
        {
            "sql": """DELETE FROM quant.t_QuantDebt WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """INSERT INTO quant.t_QuantDebt(HistoryNo, TradingDay, ExchangeID, SecurityID, SecurityName, FullSecurityID, SpecSecurityID, CreditDebtID, CreditDebtType, CreditDebtStatus, OpenDate, OpenTime, ExpireDate, Volume, Amount, UnpaidVolume, UnpaidAmount, UnpaidTradingFee, UnpaidInterestFee)
                        SELECT t.HistoryNo, t.TradingDay, t.ExchangeID, t.SecurityID, IFNULL(t1.SecurityName, '') AS SecurityName, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS FullSecurityID, CONCAT(t.SecurityID, '.', CASE WHEN t.ExchangeID = '1' THEN 'SH' WHEN t.ExchangeID = '2' THEN 'SZ' WHEN t.ExchangeID = '4' THEN 'BJ' ELSE 'NULL' END) AS SpecSecurityID, t.CreditDebtID, t.CreditDebtType, t.CreditDebtStatus, t.OpenDate, t.OpenTime, t.ExpireDate, t.Volume, t.Amount, t.UnpaidVolume, t.UnpaidAmount, t.UnpaidTradingFee, t.UnpaidInterestFee
                        FROM quant.t_SimTestCreditDebt t
                        LEFT JOIN quant.t_quantmarketdata t1 ON (t.TradingDay = t1.TradingDay And t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID)
                        WHERE t.HistoryNo = #{history_no}"""
        }
    ],
    "clean_future_quant_history": [
        {
            "sql": """DELETE FROM quant.t_clientquanttestprofit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_quanttestbenchmarkprofit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_future_simtestinfo WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_quanttesthistory WHERE HistoryNo = #{history_no}"""
        }
    ],
    "clean_quant_history": [
        {
            "sql": """DELETE FROM quant.t_clientquanttestprofit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_quanttestbenchmarkprofit WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_simtestinfo WHERE HistoryNo = #{history_no}"""
        },
        {
            "sql": """DELETE FROM quant.t_quanttesthistory WHERE HistoryNo = #{history_no}"""
        }
    ],
    # 回测盈亏信息
    "get_future_quant_test_profit": {
        "sql": """SELECT HistoryNo, TradingDay, '15:00:00' AS TradingTime, PreAsset AS LastAsset, TotalAsset AS Asset, TodayProfit AS DayProfit, TodayBuyCapital AS DayBuyCapital, TodaySellCapital AS DaySellCapital, Profit AS TotalProfit, ProfitRatio AS TotalProfitRatio
                    FROM quant.t_future_quantasset
                    WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_test_profit": {
        "sql": """SELECT HistoryNo, TradingDay, '15:00:00' AS TradingTime, PreAsset AS LastAsset, TotalAsset AS Asset, TodayProfit AS DayProfit, TodayBuyCapital AS DayBuyCapital, TodaySellCapital AS DaySellCapital, Profit AS TotalProfit, ProfitRatio AS TotalProfitRatio
                    FROM quant.t_quantasset
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
    "get_quant_bench_profit": {
        "sql": """SELECT t1.HistoryNo, CONCAT(CASE WHEN t2.ExchangeID = '1' THEN 'sh' WHEN t2.ExchangeID = '2' THEN 'sz' WHEN t2.ExchangeID = '4' THEN 'bj' ELSE '' END, t2.SecurityID) AS BenchmarkStockID, t2.SecurityName AS BenchmarkStockName, t2.TradingDay, t2.TradingTime, IF(t2.LastClosingPrice = 0, t2.ClosingPrice, t2.LastClosingPrice) AS LastClosingPrice, t2.ClosingPrice, ROUND(t2.ClosingPrice - t3.LastClosingPrice, 4) AS TotalProfit, ROUND((t2.ClosingPrice - t3.LastClosingPrice) / t3.LastClosingPrice, 6) AS TotalProfitRatio
                    FROM quant.t_quantasset t1, quant.t_quantmarketdata t2, 
                        (SELECT t.ExchangeID, t.SecurityID, IF(t.LastClosingPrice = 0, t.ClosingPrice, t.LastClosingPrice) AS LastClosingPrice
                            FROM quant.t_quantmarketdata t, (SELECT t.ExchangeID, t.SecurityID, MIN(TradingDay) AS MinTradingDay FROM quant.t_quantmarketdata t WHERE t.FullSecurityID IN (${bench_ids}) GROUP BY t.ExchangeID, t.SecurityID) t1, (SELECT MIN(TradingDay) AS MinQuantTradingDay FROM quant.t_quantasset WHERE HistoryNo = #{history_no}) t2
                            WHERE t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND ((t.TradingDay = t1.MinTradingDay AND t1.MinTradingDay > t2.MinQuantTradingDay) OR (t.TradingDay = t2.MinQuantTradingDay AND t1.MinTradingDay <= t2.MinQuantTradingDay))) t3
                    WHERE t1.HistoryNo = #{history_no} AND t1.TradingDay = t2.TradingDay AND t2.ExchangeID = t3.ExchangeID AND t2.SecurityID = t3.SecurityID AND t2.FullSecurityID IN (${bench_ids})"""
    },
    "get_future_quant_test_info": {
        "sql": """SELECT HistoryNo, BrokerID, UserID, InvestorID, QuantID, TestID, TestName, MDFrequency, InitalAmount, TestBeginTime, TestEndTime, ActualMDBeginDate, ActualMDEndDate, SetMDBeginDate, SetMDEndDate, ManualID
                    FROM quant.t_future_simtestinfo
                    WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_test_info": {
        "sql": """SELECT HistoryNo, UserID, QuantID, TestID, MDFrequency, InitalAmount, InitalOptionAmount, InitalCreditAmount, TestBeginDate, TestBeginTime, TestEndDate, TestEndTime, MDBeginDate, MDBeginTime, MDEndDate, MDEndTime, ManualID
                    FROM quant.t_simtestinfo
                    WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_test_market": {
        "sql": """SELECT DISTINCT SecurityCategoryType FROM quant.t_simtestsubmd WHERE HistoryNo = #{history_no}"""
    },
    "get_future_quant_test_history": {
        "sql": """SELECT t.InitAsset, t.TotalAsset, (SELECT COUNT(1) FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) AS TestTradeDays FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay DESC LIMIT 1"""
    },
    "get_quant_test_history": {
        "sql": """SELECT t.InitAsset, t.TotalAsset, (SELECT COUNT(1) FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) AS TestTradeDays FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no} ORDER BY t.TradingDay DESC LIMIT 1"""
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
    "save_quant_history": [
        {
            "meta": {
                "many": True,
                "prework": lambda runtime: do_prework_check_batch_paras(runtime)
            },
            "sql": """INSERT INTO quant.t_quanttestmarket(HistoryNo, Market) VALUES(#{history_no}, #{quant_market})"""
        },
        {
            "sql": """INSERT INTO quant.t_quanttesthistory(HistoryNo, TestID, TestInvestorID, TestUserID, StrategyName, TestDate, TestTime, TestTradeDateBegin, TestTradeDateEnd, TestTradeDays, TestKind, InitAsset, Asset, TestDataStatus, TestDataFileStatus, TestRunTime)
                            SELECT t.HistoryNo, t.QuantID AS TestID, t.UserID AS TestInvestorID, t2.UserID AS TestUserID, t.TestID AS StrategyName, t.TestBeginDate AS TestDate, t.TestBeginTime AS TestTime, t.MDBeginDate AS TestTradeDateBegin, t.MDEndDate AS TestTradeDateEnd, #{test_trade_days} AS TestTradeDays, IF(t.MDFrequency = 'Minute', '2', IF(t.MDFrequency = 'Second', '3', '1')) AS TestKind, #{init_asset} AS InitAsset, #{total_asset} AS Asset, #{test_data_status} AS TestDataStatus, #{test_data_file_status} AS TestDataFileStatus, 1000 * TIMESTAMPDIFF(SECOND, CONCAT(SUBSTR(t.TestBeginDate, 1, 4), '-', SUBSTR(t.TestBeginDate, 5, 2), '-', SUBSTR(t.TestBeginDate, 7, 2), ' ', t.TestBeginTime), CONCAT(SUBSTR(t.TestEndDate, 1, 4), '-', SUBSTR(t.TestEndDate, 5, 2), '-', SUBSTR(t.TestEndDate, 7, 2), ' ', t.TestEndTime)) AS TestRunTime
                            FROM quant.t_simtestinfo t, siminfo.t_investor t1, simtrade.t_user t2
                            WHERE t.HistoryNo = #{history_no} AND t.UserID = t1.InvestorID AND t1.OpenId = t2.Mobile LIMIT 1
                            ON DUPLICATE KEY UPDATE TestDataFileStatus = VALUES(TestDataFileStatus)"""
        }
    ],
    "get_future_quant_orders": {
        "sql": """SELECT TradingDay,FullInstrumentID AS InstrumentID,InstrumentName,Direction,OffsetFlag,HedgeFlag,SimOrderType,OrderPriceType,VolumeCondition,TimeCondition,ROUND(LimitPrice, 4) AS LimitPrice,Volume,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,ROUND(Turnover, 6) AS Turnover
                    FROM quant.t_future_quantorder
                    WHERE HistoryNo = #{history_no}
                    ORDER BY TradingDay, OrderLocalID, OrderSysID"""
    },
    "get_quant_orders": {
        "sql": """SELECT TradingDay,FullSecurityID AS StockID,SecurityName AS StockName,SecurityKind,Direction,OffsetFlag,SimOrderType,ROUND(LimitPrice, 4) AS LimitPrice,Volume,OrderLocalID,OrderSysID,OrderStatus,VolumeTraded,InsertTime,InsertMillisec,CancelTime,ROUND(Turnover, 6) AS Turnover
                    FROM quant.t_quantorder
                    WHERE HistoryNo = #{history_no} 
                    ORDER BY TradingDay, OrderLocalID, OrderSysID"""
    },
    "get_future_quant_trades": {
        "sql": """SELECT TradingDay,TradeID,OrderLocalID,OrderSysID,TradeDate,TradeTime,FullInstrumentID AS InstrumentID,InstrumentName,Direction,OffsetFlag,HedgeFlag,Volume,ROUND(Price, 4) AS Price, ROUND(TradingAmount, 2) AS TradingAmount, ROUND(TotalPosCost, 2) AS TotalPosCost, ROUND(TradingFee, 2) AS TradingFee, ROUND(BeforeTradeTodayAmount, 4) AS BeforeTradeTodayAmount, ROUND(AfterTradeTodayAmount, 4) AS AfterTradeTodayAmount
                    FROM quant.t_future_quanttrade
                    WHERE HistoryNo = #{history_no} 
                    ORDER BY TradingDay, TradeID, OrderLocalID, OrderSysID"""
    },
    "get_quant_trades": {
        "sql": """SELECT TradingDay,TradeID,OrderLocalID,OrderSysID,TradeDate,TradeTime,FullSecurityID AS StockID,SecurityName AS StockName,SecurityKind,Direction,OffsetFlag,Volume,ROUND(Price, 4) AS Price, ROUND(TradingAmount, 2) AS TradingAmount, ROUND(TotalPosCost, 2) AS TotalPosCost, ROUND(TradingFee, 2) AS TradingFee, ROUND(BeforeTradeTodayAmount, 4) AS BeforeTradeTodayAmount, ROUND(AfterTradeTodayAmount, 4) AS AfterTradeTodayAmount
                    FROM quant.t_quanttrade
                    WHERE HistoryNo = #{history_no} 
                    ORDER BY TradingDay, TradeID, OrderLocalID, OrderSysID"""
    },
    "get_future_quant_assets": {
        "sql": """SELECT TradingDay,PreAmount,PreMargin,PreAsset,Amount,Margin,TotalAsset, MaxTodayLongAmount, MaxTodayShortAmount
                    FROM quant.t_future_quantasset
                    WHERE HistoryNo = #{history_no} 
                    ORDER BY TradingDay"""
    },
    "get_quant_assets": {
        "sql": """SELECT TradingDay,PreAmount,PreMargin,PreSecurityValue,Amount,Margin,SecurityValue, MaxTodayLongAmount, MaxTodayShortAmount, s_PreAmount,s_PreMargin,s_PreSecurityValue,s_Amount,s_Margin,s_SecurityValue, o_PreAmount,o_PreMargin,o_PreSecurityValue,o_Amount,o_Margin,o_SecurityValue,r_PreAmount,r_PreMargin,r_PreSecurityValue,r_Amount,r_Margin,r_SecurityValue,PreCollateralValueWithoutCreditBuy,CollateralValueWithoutCreditBuy,CreditBuyAmount,CreditBuyInterestFee,CreditBuyProfit,CreditSellAmount,CreditSellInterestFee,CreditSellProfit,TotalNetAsset AS TotalNetAssert,PreCreditBuySecurityValue,CreditBuySecurityValue,PreCreditSellSecurityValue,CreditSellSecurityValue
                    FROM quant.t_quantasset
                    WHERE HistoryNo = #{history_no}
                    ORDER BY TradingDay"""
    },
    "get_future_quant_month_summary": {
        "sql": """SELECT t.TradeMonth, ROUND(t1.PreAsset, 2) AS LastAsset, ROUND(t2.TotalAsset, 2) AS Asset, ROUND(t.BuyTradingAmount, 2) AS BuyTradingAmount, ROUND(t.SellTradingAmount, 2) AS SellTradingAmount, t3.Volume
                    FROM (SELECT HistoryNo, SUBSTR(TradingDay, 1, 6) AS TradeMonth, MIN(TradingDay) AS FirstTradingDay, MAX(TradingDay) AS LastTradingDay, SUM(TodayBuyCapital) AS BuyTradingAmount, SUM(TodaySellCapital) AS SellTradingAmount
                            FROM quant.t_future_quantasset
                            WHERE HistoryNo = #{history_no}
                            GROUP BY HistoryNo, SUBSTR(TradingDay, 1, 6))t, quant.t_future_quantasset t1, quant.t_future_quantasset t2,
                        (SELECT HistoryNo, SUBSTR(TradingDay, 1, 6) AS TradeMonth, COUNT(1) AS Volume FROM quant.t_future_quanttrade WHERE historyno = #{history_no}) t3
                    WHERE t.HistoryNo = t1.HistoryNo AND t.HistoryNo = t2.HistoryNo AND t.FirstTradingDay = t1.TradingDay AND t.LastTradingDay = t2.TradingDay
                        AND t.HistoryNo = t3.HistoryNo AND t.TradeMonth = t3.TradeMonth
                    ORDER BY t.TradeMonth"""
    },
    "get_quant_month_summary": {
        "sql": """SELECT t.TradeMonth, ROUND(t1.PreAsset, 2) AS LastAsset, ROUND(t2.TotalAsset, 2) AS Asset, ROUND(t.BuyTradingAmount, 2) AS BuyTradingAmount, ROUND(t.SellTradingAmount, 2) AS SellTradingAmount, t3.Volume
                    FROM (SELECT HistoryNo, SUBSTR(TradingDay, 1, 6) AS TradeMonth, MIN(TradingDay) AS FirstTradingDay, MAX(TradingDay) AS LastTradingDay, SUM(TodayBuyCapital) AS BuyTradingAmount, SUM(TodaySellCapital) AS SellTradingAmount
                            FROM quant.t_quantasset
                            WHERE HistoryNo = #{history_no}
                            GROUP BY HistoryNo, SUBSTR(TradingDay, 1, 6))t, quant.t_quantasset t1, quant.t_quantasset t2,
                        (SELECT HistoryNo, SUBSTR(TradingDay, 1, 6) AS TradeMonth, COUNT(1) AS Volume FROM quant.t_quanttrade WHERE historyno = #{history_no}) t3
                    WHERE t.HistoryNo = t1.HistoryNo AND t.HistoryNo = t2.HistoryNo AND t.FirstTradingDay = t1.TradingDay AND t.LastTradingDay = t2.TradingDay
                        AND t.HistoryNo = t3.HistoryNo AND t.TradeMonth = t3.TradeMonth
                    ORDER BY t.TradeMonth"""
    },
    "get_future_quant_positions": {
        "sql": """SELECT TradingDay,FullInstrumentID AS InstrumentID,InstrumentName,PosiDirection,HedgeFlag,Position,ROUND(SettlementPrice, 4) AS SettlementPrice,ROUND(PositionCost, 2) AS TotalPosCost,ROUND(OpenCost, 2) AS OpenPosCost,ROUND(UseMargin, 2) AS Margin,ROUND(Commission, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,YdPosition,ROUND(TodayProfit, 2) AS TodayProfit,ROUND(TodayBuyCapital, 2) AS TodayBuyCapital,ROUND(TodaySellCapital, 2) AS TodaySellCapital,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(ReturnRatio, 4) AS ReturnRatio,ROUND(ContributionRatio, 4) AS ContributionRatio,ROUND(LastSettlementPrice, 2) AS LastSettlementPrice,ROUND(OpenCost, 2) AS TotalOpenPosCost
                    FROM quant.t_future_quantposition
                    WHERE historyno = #{history_no}
                    UNION
                    SELECT t1.TradingDay,'000000' AS InstrumentID,'000000' AS InstrumentName,'' AS PosiDirection,'' AS HedgeFlag,0 AS Position,ROUND(t2.TotalAsset, 2) AS SettlementPrice,ROUND(t2.Amount, 2) AS TotalPosCost,0 AS OpenPosCost,ROUND(t2.Margin, 2) AS Margin,0 AS TradingFee,ROUND(t2.Profit, 2) AS Profit,0 AS YdPosition,ROUND(t2.TodayProfit, 2) AS TodayProfit,0 AS TodayBuyCapital,0 AS TodaySellCapital,0 AS BuyCapital,0 AS SellCapital,0 AS ReturnRatio,0 AS ContributionRatio,0 AS LastSettlementPrice,0 AS TotalOpenPosCost
                        FROM quant.t_future_quantposition t1, quant.t_future_quantasset t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay
                ORDER BY TradingDay, InstrumentID DESC"""
    },
    "get_quant_positions": {
        "sql": """SELECT TradingDay,FullSecurityID AS StockID,SecurityName AS StockName,SecurityKind,PosiDirection,Volume,ROUND(ClosingPrice, 4) AS ClosingPrice,ROUND(SettlementPrice, 4) AS SettlementPrice,ROUND(UnderlyingClosePrice, 4) AS UnderlyingClosePrice,ROUND(StrikePrice, 4) AS StrikePrice,OptionsType,FirstDate,LastDate,StrikeDate,ExpireDate,ROUND(TotalPosCost, 2) AS TotalPosCost,ROUND(OpenPosCost, 2) AS OpenPosCost,ROUND(HoldingValue, 2) AS HoldingValue,ROUND(Margin, 2) AS Margin,ROUND(TradingFee, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,PreVolume,ROUND(PreOpenPosCost, 2) AS PreOpenPosCost,ROUND(TodayProfit, 2) AS TodayProfit,ROUND(TodayBuyCapital, 2) AS TodayBuyCapital,ROUND(TodaySellCapital, 2) AS TodaySellCapital,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(InitTotalPosCost, 2) AS InitTotalPosCost,ROUND(InitHoldingValue, 2) AS InitHoldingValue,ROUND(ReturnRatio, 4) AS ReturnRatio,ROUND(ContributionRatio, 4) AS ContributionRatio,ROUND(PreSettlementPrice, 2) AS PreSettlementPrice,ROUND(UnderlyingPreClosePrice, 2) AS UnderlyingPreClosePrice,ROUND(MaxTodayAmount, 2) AS MaxTodayAmount,ROUND(InitTodayAmount, 2) AS InitTodayAmount,ROUND(FinalTodayAmount, 2) AS FinalTodayAmount,ROUND(TotalOpenPosCost, 2) AS TotalOpenPosCost,CreditBuyPos,ROUND(CreditBuyAmount, 2) AS CreditBuyAmount,ROUND(CreditBuyInterestFee, 2) AS CreditBuyInterestFee,CreditSellPos,ROUND(CreditSellAmount, 2) AS CreditSellAmount,ROUND(CreditSellInterestFee, 2) AS CreditSellInterestFee,CollateralOutPos,CollateralInPos
                    FROM quant.t_quantposition
                    WHERE historyno = #{history_no}
                    ORDER BY TradingDay, FullSecurityID
                    UNION
                    SELECT t1.TradingDay,'000000' AS StockID,'000000' AS StockName,'s' AS SecurityKind,'' AS PosiDirection,0 AS Volume,ROUND(t2.s_TotalAsset, 2) AS ClosingPrice,ROUND(t2.s_SecurityValue, 2) AS SettlementPrice,0 AS UnderlyingClosePrice,0 AS StrikePrice,'' AS OptionsType,'' AS FirstDate,'' AS LastDate,'' AS StrikeDate,'' AS ExpireDate,ROUND(t2.s_Amount, 2) AS TotalPosCost,0 AS OpenPosCost,ROUND(t2.s_SecurityValue, 2) AS HoldingValue,ROUND(t2.s_Margin, 2) AS Margin,0 AS TradingFee,ROUND(t2.s_Profit, 2) AS Profit,0 AS PreVolume,0 AS PreOpenPosCost,ROUND(t2.s_TodayProfit, 2) AS TodayProfit,0 AS TodayBuyCapital,0 AS TodaySellCapital,0 AS BuyCapital,0 AS SellCapital,0 AS InitTotalPosCost,0 AS InitHoldingValue,0 AS ReturnRatio,0 AS ContributionRatio,0 AS PreSettlementPrice,0 AS UnderlyingPreClosePrice,0 AS MaxTodayAmount,0 AS InitTodayAmount,0 AS FinalTodayAmount,0 AS TotalOpenPosCost,0 AS CreditBuyPos,0 AS CreditBuyAmount,0 AS CreditBuyInterestFee,0 AS CreditSellPos,0 AS CreditSellAmount,0 AS CreditSellInterestFee,0 AS CollateralOutPos,0 AS CollateralInPos
                        FROM quant.t_quantposition t1, quant.t_quantasset t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.SecurityKind = 's' AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay
                    UNION
                    SELECT t1.TradingDay,'000000' AS StockID,'000000' AS StockName,'o' AS SecurityKind,'' AS PosiDirection,0 AS Volume,ROUND(t2.o_TotalAsset, 2) AS ClosingPrice,ROUND(t2.o_SecurityValue, 2) AS SettlementPrice,0 AS UnderlyingClosePrice,0 AS StrikePrice,'' AS OptionsType,'' AS FirstDate,'' AS LastDate,'' AS StrikeDate,'' AS ExpireDate,ROUND(t2.o_Amount, 2) AS TotalPosCost,0 AS OpenPosCost,ROUND(t2.o_SecurityValue, 2) AS HoldingValue,ROUND(t2.o_Margin, 2) AS Margin,0 AS TradingFee,ROUND(t2.o_Profit, 2) AS Profit,0 AS PreVolume,0 AS PreOpenPosCost,ROUND(t2.o_TodayProfit, 2) AS TodayProfit,0 AS TodayBuyCapital,0 AS TodaySellCapital,0 AS BuyCapital,0 AS SellCapital,0 AS InitTotalPosCost,0 AS InitHoldingValue,0 AS ReturnRatio,0 AS ContributionRatio,0 AS PreSettlementPrice,0 AS UnderlyingPreClosePrice,0 AS MaxTodayAmount,0 AS InitTodayAmount,0 AS FinalTodayAmount,0 AS TotalOpenPosCost,0 AS CreditBuyPos,0 AS CreditBuyAmount,0 AS CreditBuyInterestFee,0 AS CreditSellPos,0 AS CreditSellAmount,0 AS CreditSellInterestFee,0 AS CollateralOutPos,0 AS CollateralInPos
                        FROM quant.t_quantposition t1, quant.t_quantasset t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.SecurityKind = 'o' AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay
                    UNION
                    SELECT t1.TradingDay,'000000' AS StockID,'000000' AS StockName,'r' AS SecurityKind,'' AS PosiDirection,0 AS Volume,ROUND(t2.r_TotalAsset, 2) AS ClosingPrice,ROUND(t2.r_SecurityValue, 2) AS SettlementPrice,0 AS UnderlyingClosePrice,0 AS StrikePrice,'' AS OptionsType,'' AS FirstDate,'' AS LastDate,'' AS StrikeDate,'' AS ExpireDate,ROUND(t2.r_Amount, 2) AS TotalPosCost,0 AS OpenPosCost,ROUND(t2.r_SecurityValue, 2) AS HoldingValue,ROUND(t2.r_Margin, 2) AS Margin,0 AS TradingFee,ROUND(t2.r_Profit, 2) AS Profit,0 AS PreVolume,0 AS PreOpenPosCost,ROUND(t2.r_TodayProfit, 2) AS TodayProfit,0 AS TodayBuyCapital,0 AS TodaySellCapital,0 AS BuyCapital,0 AS SellCapital,0 AS InitTotalPosCost,0 AS InitHoldingValue,0 AS ReturnRatio,0 AS ContributionRatio,0 AS PreSettlementPrice,0 AS UnderlyingPreClosePrice,0 AS MaxTodayAmount,0 AS InitTodayAmount,0 AS FinalTodayAmount,0 AS TotalOpenPosCost,0 AS CreditBuyPos,0 AS CreditBuyAmount,0 AS CreditBuyInterestFee,0 AS CreditSellPos,0 AS CreditSellAmount,0 AS CreditSellInterestFee,0 AS CollateralOutPos,0 AS CollateralInPos
                        FROM quant.t_quantposition t1, quant.t_quantasset t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.SecurityKind = 'r' AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay
                    UNION
                    SELECT t1.TradingDay,'000000' AS StockID,'000000' AS StockName,'' AS SecurityKind,'' AS PosiDirection,0 AS Volume,ROUND(t2.TotalAsset, 2) AS ClosingPrice,ROUND(t2.SecurityValue, 2) AS SettlementPrice,0 AS UnderlyingClosePrice,0 AS StrikePrice,'' AS OptionsType,'' AS FirstDate,'' AS LastDate,'' AS StrikeDate,'' AS ExpireDate,ROUND(t2.Amount, 2) AS TotalPosCost,0 AS OpenPosCost,ROUND(t2.SecurityValue, 2) AS HoldingValue,ROUND(t2.Margin, 2) AS Margin,0 AS TradingFee,ROUND(t2.Profit, 2) AS Profit,0 AS PreVolume,0 AS PreOpenPosCost,ROUND(t2.TodayProfit, 2) AS TodayProfit,0 AS TodayBuyCapital,0 AS TodaySellCapital,0 AS BuyCapital,0 AS SellCapital,0 AS InitTotalPosCost,0 AS InitHoldingValue,0 AS ReturnRatio,0 AS ContributionRatio,0 AS PreSettlementPrice,0 AS UnderlyingPreClosePrice,0 AS MaxTodayAmount,0 AS InitTodayAmount,0 AS FinalTodayAmount,0 AS TotalOpenPosCost,0 AS CreditBuyPos,0 AS CreditBuyAmount,0 AS CreditBuyInterestFee,0 AS CreditSellPos,0 AS CreditSellAmount,0 AS CreditSellInterestFee,0 AS CollateralOutPos,0 AS CollateralInPos
                        FROM quant.t_quantposition t1, quant.t_quantasset t2
                        WHERE t1.HistoryNo = #{history_no} AND t1.HistoryNo = t2.HistoryNo AND t1.TradingDay = t2.TradingDay"""
    },
    "get_future_quant_profits": {
        "sql": """SELECT FullInstrumentID AS InstrumentID,InstrumentName,PosiDirection,TradingCount,ROUND(TradingFee, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(ContributionRatio, 4) AS ContributionRatio,ROUND(ReturnRatio, 4) AS ReturnRatio
                    FROM quant.t_future_quantprofit
                    WHERE HistoryNo = #{history_no} ORDER BY InstrumentID"""
    },
    "get_quant_profits": {
        "sql": """SELECT FullSecurityID AS StockID,SecurityName AS StockName,SecurityKind,PosiDirection,ROUND(InitHoldingValue, 2) AS InitHoldingValue,ROUND(FinalHoldingValue, 2) AS FinalHoldingValue,TradingCount,ROUND(TradingFee, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(ContributionRatio, 4) AS ContributionRatio,ROUND(ReturnRatio, 4) AS ReturnRatio
                    FROM quant.t_quantprofit 
                    WHERE HistoryNo = #{history_no} ORDER BY FullSecurityID"""
    },
    "get_quant_debts": {
        "sql": """SELECT TradingDay,CreditDebtID,CreditDebtType,CreditDebtStatus,ExchangeID,FullSecurityID AS StockID,SecurityName AS StockName,OpenDate,OpenTime,ExpireDate,Volume,Amount,UnpaidVolume,UnpaidAmount,UnpaidTradingFee,UnpaidInterestFee
                    FROM quant.t_quantdebt
                    WHERE HistoryNo = #{history_no} ORDER BY TradingDay, CreditDebtID"""
    },
    "get_quant_repayments": {
        "sql": """SELECT TradingDay,CreditRepayID,CreditDebtID,OrderSysID,ExchangeID,RepaidAmount,RepaidVolume,RepaidTradingFee,RepaidInterestFee
                    FROM quant.t_simtestcreditrepayment
                    WHERE HistoryNo = #{history_no} ORDER BY TradingDay, CreditRepayID, CreditDebtID"""
    },
    "get_quant_future_dkmds": {
        "sql": """SELECT t1.TradingDay, t1.FullInstrumentID AS InstrumentID, ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, t3.LongOpenPosCost, t3.ShortOpenPosCost, t3.LongYdPosition, t3.ShortYdPosition
                    FROM quant.t_future_quantmarketdata t1
                    JOIN quant.t_future_quantasset t2 ON (t2.HistoryNo = #{history_no} AND t1.TradingDay = t2.TradingDay)
                    LEFT JOIN (SELECT t3.HistoryNo, t3.TradingDay, t3.ExchangeID, t3.InstrumentID, t3.FullInstrumentID, SUM(ROUND(IF(t3.PosiDirection = '2', t3.OpenCost, 0), 2)) AS LongOpenPosCost, SUM(ROUND(IF(t3.PosiDirection = '3', t3.OpenCost, 0), 2)) AS ShortOpenPosCost, SUM(ROUND(IF(t3.PosiDirection = '2', t3.YdPosition, 0), 2)) AS LongYdPosition, SUM(ROUND(IF(t3.PosiDirection = '3', t3.YdPosition, 0), 2)) AS ShortYdPosition FROM quant.t_future_quantposition t3 WHERE t3.HistoryNo = #{history_no} GROUP BY t3.HistoryNo, t3.TradingDay, t3.ExchangeID, t3.InstrumentID, t3.FullInstrumentID) t3 ON (t3.HistoryNo = #{history_no} AND t1.TradingDay = t3.TradingDay AND t1.ExchangeID = t3.ExchangeID AND t1.InstrumentID = t3.InstrumentID)
                    WHERE t1.ExchangeID = #{exchange_id} AND t1.InstrumentID = #{instrument_id}
                    ORDER BY t1.TradingDay"""
    },
    "get_quant_security_dkmds": {
        "sql": """SELECT t1.TradingDay, t1.TradingTime, t1.FullSecurityID AS StockID, ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.AdjLastClosingPrice, 4) AS AdjLastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.AdjOpeningPrice, 4) AS AdjOpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.AdjClosingPrice, 4) AS AdjClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.AdjTopPrice, 4) AS AdjTopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, ROUND(t1.AdjFloorPrice, 4) AS AdjFloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, ROUND(IF(t3.PosiDirection = '2', t3.OpenPosCost, 0), 2) AS OpenPosCost, ROUND(IF(t3.PosiDirection = '3', t3.OpenPosCost, 0), 2) AS ShortOpenPosCost, ROUND(IF(t3.PosiDirection = '2', t3.OpenPosCost, 0), 2) AS LongOpenPosCost, IF(t3.PosiDirection = '2', t3.PreVolume, 0) AS PreVolume, IF(t3.PosiDirection = '3', t3.PreVolume, 0) AS ShortPreVolume, IF(t3.PosiDirection = '2', t3.PreVolume, 0) AS LongPreVolume
                    FROM quant.t_quantmarketdata t1
                    JOIN quant.t_quantasset t2 ON (t2.HistoryNo = #{history_no} AND t1.TradingDay = t2.TradingDay)
                    LEFT JOIN quant.t_quantposition t3 ON (t3.HistoryNo = #{history_no} AND t1.TradingDay = t3.TradingDay AND t1.ExchangeID = t3.ExchangeID AND t1.SecurityID = t3.SecurityID)
                    WHERE t1.ExchangeID = #{exchange_id} AND t1.SecurityID = #{security_id}
                    ORDER BY t1.TradingDay, t1.TradingTime"""
    },
    "get_future_quant_dkmds": {
        "sql": """SELECT t1.TradingDay, t1.FullInstrumentID AS InstrumentID, ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, ROUND(IF(t3.PosiDirection = '2', t3.OpenCost, 0), 2) AS LongOpenPosCost,  ROUND(IF(t3.PosiDirection = '3', t3.OpenCost, 0), 2) AS ShortOpenPosCost,IF(t3.PosiDirection = '2', t3.YdPosition, 0) AS LongYdPosition, IF(t3.PosiDirection = '3', t3.YdPosition, 0) AS ShortYdPosition
                    FROM quant.t_future_quantmarketdata t1
                    JOIN (SELECT DISTINCT t2.ExchangeID, t2.InstrumentID, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_future_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2 ON (t1.TradingDay >= t2.FirstTradingDay AND t1.TradingDay <= t2.LastTradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.InstrumentID = t2.InstrumentID)
                    LEFT JOIN quant.t_future_quantposition t3 ON (t3.HistoryNo = #{history_no} AND t1.TradingDay = t3.TradingDay AND t1.ExchangeID = t3.ExchangeID AND t1.InstrumentID = t3.InstrumentID)
                    ORDER BY t1.TradingDay"""
    },
    "get_quant_dkmds": {
        "sql": """SELECT t1.TradingDay, t1.TradingTime, t1.FullSecurityID AS StockID, ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.AdjLastClosingPrice, 4) AS AdjLastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.AdjOpeningPrice, 4) AS AdjOpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.AdjClosingPrice, 4) AS AdjClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.AdjTopPrice, 4) AS AdjTopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, ROUND(t1.AdjFloorPrice, 4) AS AdjFloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, ROUND(IF(t3.PosiDirection = '2', t3.OpenPosCost, 0), 2) AS OpenPosCost, ROUND(IF(t3.PosiDirection = '3', t3.OpenPosCost, 0), 2) AS ShortOpenPosCost, ROUND(IF(t3.PosiDirection = '2', t3.OpenPosCost, 0), 2) AS LongOpenPosCost, IF(t3.PosiDirection = '2', t3.PreVolume, 0) AS PreVolume, IF(t3.PosiDirection = '3', t3.PreVolume, 0) AS ShortPreVolume, IF(t3.PosiDirection = '2', t3.PreVolume, 0) AS LongPreVolume
                    FROM quant.t_quantmarketdata t1
                    JOIN (SELECT DISTINCT t2.ExchangeID, t2.SecurityID, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2 ON (t1.TradingDay >= t2.FirstTradingDay AND t1.TradingDay <= t2.LastTradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID)
                    LEFT JOIN quant.t_quantposition t3 ON (t3.HistoryNo = #{history_no} AND t1.TradingDay = t3.TradingDay AND t1.ExchangeID = t3.ExchangeID AND t1.SecurityID = t3.SecurityID)
                    ORDER BY t1.TradingDay, t1.TradingTime"""
    },
    "get_future_quant_benches": {
        "sql": """SELECT t1.TradingDay, t1.FullInstrumentID AS InstrumentID, ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.ClosingPrice - t1.OpeningPrice) / t1.OpeningPrice, (t4.OpeningPrice - t1.OpeningPrice) / t1.OpeningPrice), 6) AS DayProfitRatio, ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.ClosingPrice - t5.OpeningPrice) / t5.OpeningPrice, (t4.OpeningPrice - t5.OpeningPrice) / t5.OpeningPrice), 6) AS ProfitRatio
                    FROM (SELECT t1.TradingDay, t1.ExchangeID, t1.InstrumentID, t1.FullInstrumentID, t2.FirstTradingDay, t2.LastTradingDay, t1.OpeningPrice, t1.ClosingPrice FROM quant.t_future_quantmarketdata t1, (SELECT t2.TradingDay, t2.ExchangeID, t2.InstrumentID, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_future_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.InstrumentID = t2.InstrumentID) t1
                    JOIN quant.t_future_quantmarketdata t4 ON (t1.TradingDay = t4.LastTradingDay AND t1.ExchangeID = t4.ExchangeID AND t1.InstrumentID = t4.InstrumentID)
                    JOIN quant.t_future_quantmarketdata t5 ON (t1.FirstTradingDay = t5.TradingDay AND t1.ExchangeID = t5.ExchangeID AND t1.InstrumentID = t5.InstrumentID)
                    ORDER BY t1.TradingDay, t1.InstrumentID"""
    },
    "get_quant_benches": {
        "sql": """SELECT t1.TradingDay, t1.FullSecurityID AS StockID, ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.AdjClosingPrice - t1.AdjOpeningPrice) / t1.AdjOpeningPrice, (t4.AdjOpeningPrice - t1.AdjOpeningPrice) / t1.AdjOpeningPrice), 6) AS DayProfitRatio, ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.AdjClosingPrice - t5.AdjOpeningPrice) / t5.AdjOpeningPrice, (t4.AdjOpeningPrice - t5.AdjOpeningPrice) / t5.AdjOpeningPrice), 6) AS ProfitRatio
                    FROM (SELECT t1.TradingDay, t1.ExchangeID, t1.SecurityID, t1.FullSecurityID, t2.FirstTradingDay, t2.LastTradingDay, t1.AdjOpeningPrice, t1.AdjClosingPrice FROM quant.t_quantmarketdata t1, (SELECT t2.TradingDay, t2.ExchangeID, t2.SecurityID, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID) t1
                    JOIN quant.t_quantmarketdata t4 ON (t1.TradingDay = t4.LastTradingDay AND t1.ExchangeID = t4.ExchangeID AND t1.SecurityID = t4.SecurityID)
                    JOIN quant.t_quantmarketdata t5 ON (t1.FirstTradingDay = t5.TradingDay AND t1.ExchangeID = t5.ExchangeID AND t1.SecurityID = t5.SecurityID)
                    ORDER BY t1.TradingDay, t1.FullSecurityID"""
    },
    "get_future_quant_submds": {
        "sql": """SELECT t1.TradingDay, t1.FullInstrumentID AS InstrumentID, t1.InstrumentName , ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.ClosingPrice - t1.OpeningPrice) / t1.OpeningPrice, (t4.OpeningPrice - t1.OpeningPrice) / t1.OpeningPrice), 6) AS DayProfitRatio
                    FROM (SELECT t1.TradingDay, t1.ExchangeID, t1.InstrumentID, t1.FullInstrumentID, t1.InstrumentName, t2.FirstTradingDay, t2.LastTradingDay, t1.LastClosingPrice, t1.ClosingPrice, t1.OpeningPrice, t1.TopPrice, t1.FloorPrice, t1.TradingVolume, t1.TradingAmount FROM quant.t_future_quantmarketdata t1, (SELECT t2.TradingDay, t2.ExchangeID, t2.InstrumentID, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_future_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_future_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.InstrumentID = t2.InstrumentID) t1
                    JOIN quant.t_future_quantmarketdata t4 ON (t1.TradingDay = t4.LastTradingDay AND t1.ExchangeID = t4.ExchangeID AND t1.InstrumentID = t4.InstrumentID)
                    ORDER BY t1.TradingDay, t1.FullInstrumentID"""
    },
    "get_quant_submds": {
        "sql": """SELECT t1.TradingDay, t1.FullSecurityID AS StockID, t1.SecurityName AS StockName, t1.SecurityCategoryType, t1.TradingTime, ROUND(t1.LastClosingPrice, 4) AS LastClosingPrice, ROUND(t1.AdjLastClosingPrice, 4) AS AdjLastClosingPrice, ROUND(t1.OpeningPrice, 4) AS OpeningPrice, ROUND(t1.AdjOpeningPrice, 4) AS AdjOpeningPrice, ROUND(t1.ClosingPrice, 4) AS ClosingPrice, ROUND(t1.AdjClosingPrice, 4) AS AdjClosingPrice, ROUND(t1.TopPrice, 4) AS TopPrice, ROUND(t1.AdjTopPrice, 4) AS AdjTopPrice, ROUND(t1.FloorPrice, 4) AS FloorPrice, ROUND(t1.AdjFloorPrice, 4) AS AdjFloorPrice, t1.TradingVolume, ROUND(t1.TradingAmount, 2) AS TradingAmount, ROUND(t4.AdjOpeningPrice, 4) AS NextAdjOpeningPrice,ROUND(IF(t1.TradingDay = t1.LastTradingDay, (t1.AdjClosingPrice - t1.AdjOpeningPrice) / t1.AdjOpeningPrice, (t4.AdjOpeningPrice - t1.AdjOpeningPrice) / t1.AdjOpeningPrice), 6) AS DayProfitRatio
                    FROM (SELECT t1.TradingDay, t1.TradingTime, t1.ExchangeID, t1.SecurityID, t1.FullSecurityID, t1.SecurityName, t2.SecurityCategoryType, t2.FirstTradingDay, t2.LastTradingDay, t1.LastClosingPrice, t1.AdjLastClosingPrice, t1.OpeningPrice, t1.AdjOpeningPrice, t1.ClosingPrice, t1.AdjClosingPrice, t1.TopPrice, t1.AdjTopPrice, t1.FloorPrice, t1.AdjFloorPrice, t1.TradingVolume, t1.TradingAmount FROM quant.t_quantmarketdata t1, (SELECT t2.TradingDay, t2.ExchangeID, t2.SecurityID, t2.SecurityCategoryType, t3.FirstTradingDay, t4.LastTradingDay FROM quant.t_simtestsubmd t2, (SELECT MIN(t.TradingDay) AS FirstTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t3, (SELECT MAX(t.TradingDay) AS LastTradingDay FROM quant.t_quantasset t WHERE t.HistoryNo = #{history_no}) t4 WHERE t2.HistoryNo = #{history_no}) t2
                        WHERE t1.TradingDay = t2.TradingDay AND t1.ExchangeID = t2.ExchangeID AND t1.SecurityID = t2.SecurityID) t1
                    JOIN quant.t_quantmarketdata t4 ON (t1.TradingDay = t4.LastTradingDay AND t1.ExchangeID = t4.ExchangeID AND t1.SecurityID = t4.SecurityID)
                    ORDER BY t1.TradingDay, t1.FullSecurityID"""
    },
    "get_future_quant_db_positions": {
        "sql": """SELECT TradingDay,FullInstrumentID AS InstrumentID,InstrumentName,PosiDirection,HedgeFlag,Position,ROUND(SettlementPrice, 4) AS SettlementPrice,ROUND(PositionCost, 2) AS TotalPosCost,ROUND(OpenCost, 2) AS OpenPosCost,ROUND(UseMargin, 2) AS Margin,ROUND(Commission, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,YdPosition,ROUND(TodayProfit, 2) AS TodayProfit,ROUND(TodayBuyCapital, 2) AS TodayBuyCapital,ROUND(TodaySellCapital, 2) AS TodaySellCapital,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(ReturnRatio, 6) AS ReturnRatio,ROUND(ContributionRatio, 6) AS ContributionRatio,ROUND(LastSettlementPrice, 4) AS LastSettlementPrice
                    FROM quant.t_future_quantposition
                    WHERE HistoryNo = #{history_no}"""
    },
    "get_quant_db_positions": {
        "sql": """SELECT TradingDay,FullSecurityID AS StockID,SecurityName AS StockName,SecurityKind,PosiDirection,Volume,ROUND(ClosingPrice, 4) AS ClosingPrice,ROUND(SettlementPrice, 4) AS SettlementPrice,ROUND(UnderlyingClosePrice, 4) AS UnderlyingClosePrice,ROUND(StrikePrice, 4) AS StrikePrice,OptionsType,FirstDate,LastDate,StrikeDate,ExpireDate,ROUND(TotalPosCost, 2) AS TotalPosCost,ROUND(OpenPosCost, 2) AS OpenPosCost,ROUND(HoldingValue, 2) AS HoldingValue,ROUND(TradingFee, 2) AS TradingFee,ROUND(Profit, 2) AS Profit,PreVolume,ROUND(PreOpenPosCost, 2) AS PreOpenPosCost,ROUND(TodayProfit, 2) AS TodayProfit,ROUND(TodayBuyCapital, 2) AS TodayBuyCapital,ROUND(TodaySellCapital, 2) AS TodaySellCapital,ROUND(BuyCapital, 2) AS BuyCapital,ROUND(SellCapital, 2) AS SellCapital,ROUND(InitTotalPosCost, 2) AS InitTotalPosCost,ROUND(InitHoldingValue, 2) AS InitHoldingValue,ROUND(ReturnRatio, 6) AS ReturnRatio,ROUND(ContributionRatio, 6) AS ContributionRatio,ROUND(PreSettlementPrice, 4) AS PreSettlementPrice, ROUND(UnderlyingPreClosePrice, 4) AS UnderlyingPreClosePrice, ROUND(MaxTodayAmount, 2) AS MaxTodayAmount, ROUND(InitTodayAmount, 2) AS InitTodayAmount,ROUND(FinalTodayAmount, 2) AS FinalTodayAmount,ROUND(TotalOpenPosCost, 2) AS TotalOpenPosCost,CreditBuyPos,ROUND(CreditBuyAmount, 2) AS CreditBuyAmount,ROUND(CreditBuyInterestFee, 2) AS CreditBuyInterestFee,CreditSellPos,ROUND(CreditSellAmount, 2) AS CreditSellAmount,ROUND(CreditSellInterestFee, 2) AS CreditSellInterestFee,CollateralOutPos,CollateralInPos
                    FROM quant.t_quantposition
                    WHERE HistoryNo = #{history_no}"""
    }
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


def do_callback_get_rights(runtime, *args, **kwargs):
    result = runtime["result"]

    if result:
        batch_paras = []
        for row in result:
            record_date = row[0]
            exchange_id = row[1]
            security_id = row[2]
            dividend_rate = float(row[3])
            profit_rate = float(row[4])
            issue_rate = float(row[5])
            issue_price = float(row[6])
            dividend_date = row[7]
            newstock_market_data = row[8]

            batch_paras.append({"record_date": record_date, "exchange_id": exchange_id, "security_id": security_id,
                                "dividend_rate": dividend_rate, "profit_rate": profit_rate,
                                "issue_rate": issue_rate, "issue_price": issue_price, "dividend_date": dividend_date,
                                "newstock_market_data": newstock_market_data})

        runtime["batch_paras"] = batch_paras


def do_callback_get_securities(runtime, *args, **kwargs):
    result = runtime["result"]

    if result:
        batch_paras = []
        for row in result:
            exchange_id = row[0]
            security_id = row[1]

            batch_paras.append({"exchange_id": exchange_id, "security_id": security_id})

        runtime["batch_paras"] = batch_paras


def do_prework_check_batch_paras(runtime, *args, **kwargs):
    batch_paras = runtime["batch_paras"]
    if not batch_paras or len(batch_paras) == 0:
        runtime["go"] = "next"


def do_callback_get_trades(runtime, *args, **kwargs):
    result = runtime["result"]

    if result:
        batch_paras = []
        for row in result:
            history_no = row[0]
            trading_day = row[1]
            exchange_id = row[2]
            security_id = row[3]
            trade_id = row[4]
            direction = row[5]
            volume = int(row[6])
            trade_price = float(row[7])
            trade_amount = float(row[8])
            commission_fee = float(row[9])

            batch_paras.append({"history_no": history_no, "trading_day": trading_day, "exchange_id": exchange_id,
                                "security_id": security_id,
                                "trade_id": trade_id, "direction": direction, "volume": volume,
                                "trade_price": trade_price, "trade_amount": trade_amount,
                                "commission_fee": commission_fee})
        runtime["batch_paras"] = batch_paras
