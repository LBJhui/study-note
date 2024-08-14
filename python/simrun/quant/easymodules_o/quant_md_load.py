# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:02
# @Author: LBJ辉
# @File: quant_md_load
# @Project: python
# wande
alias = "QuantMdLoad"

realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "load_quant_md_ashare": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastClosingPrice, ROUND(NVL(t1.S_DQ_PRECLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, ROUND(NVL(t1.S_DQ_OPEN, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, ROUND(NVL(t1.S_DQ_CLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, ROUND(NVL(t1.S_DQ_HIGH, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, ROUND(NVL(t1.S_DQ_LOW, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS SettlementPrice, ROUND(NVL(t1.S_DQ_CLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastSettlementPrice, ROUND(NVL(t1.S_DQ_PRECLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjLastSettlementPrice,
                        NVL(t1.S_DQ_LIMIT, 0) AS UpperLimitPrice, NVL(t1.S_DQ_STOPPING, 0) AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 1000 AS TradingAmount, 
                        NVL(t1.S_DQ_ADJFACTOR, 1) AS AdjustFactor, #{last_trading_day} AS LastTradingDay,
                        t1.S_DQ_TRADESTATUSCODE AS TradeStatus
                    FROM sys_wind.ASHAREEODPRICES t1
                        JOIN sys_wind.ASHAREDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND t2.S_INFO_EXCHMARKET IN ('SSE', 'SZSE', 'BSE'))
                        LEFT JOIN (SELECT t.S_INFO_WINDCODE, t.S_DQ_ADJFACTOR FROM sys_wind.ASHAREEODPRICES t WHERE t.TRADE_DT = #{refer_day}) t3 ON (t1.S_INFO_WINDCODE = t3.S_INFO_WINDCODE)
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_md_ashare_old": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastClosingPrice, ROUND(NVL(t1.S_DQ_PRECLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, ROUND(NVL(t1.S_DQ_OPEN, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, ROUND(NVL(t1.S_DQ_CLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, ROUND(NVL(t1.S_DQ_HIGH, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, ROUND(NVL(t1.S_DQ_LOW, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS SettlementPrice, ROUND(NVL(t1.S_DQ_CLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastSettlementPrice, ROUND(NVL(t1.S_DQ_PRECLOSE, 0) * NVL(t1.S_DQ_ADJFACTOR, 1) / NVL(t3.S_DQ_ADJFACTOR, 1), 2) AS AdjLastSettlementPrice,
                        0 AS UpperLimitPrice, 0 AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 1000 AS TradingAmount, 
                        NVL(t1.S_DQ_ADJFACTOR, 1) AS AdjustFactor, #{last_trading_day} AS LastTradingDay,
                        t1.S_DQ_TRADESTATUSCODE AS TradeStatus
                    FROM sys_wind.ASHAREEODPRICES t1
                        JOIN sys_wind.ASHAREDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND t2.S_INFO_EXCHMARKET IN ('SSE', 'SZSE', 'BSE'))
                        LEFT JOIN (SELECT t.S_INFO_WINDCODE, t.S_DQ_ADJFACTOR FROM sys_wind.ASHAREEODPRICES t WHERE t.TRADE_DT = #{refer_day}) t3 ON (t1.S_INFO_WINDCODE = t3.S_INFO_WINDCODE)
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_md_cbond": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastClosingPrice, NVL(t1.S_DQ_PRECLOSE, 0) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, NVL(t1.S_DQ_OPEN, 0) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, NVL(t1.S_DQ_HIGH, 0) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, NVL(t1.S_DQ_LOW, 0) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS SettlementPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastSettlementPrice, NVL(t1.S_DQ_PRECLOSE, 0) AS AdjLastSettlementPrice,
                        0 AS UpperLimitPrice, 0 AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 1000 AS TradingAmount, 
                        1 AS AdjustFactor, #{last_trading_day} AS LastTradingDay,
                        CASE WHEN t1.S_DQ_TRADESTATUS = '停牌' THEN 0 WHEN t1.S_DQ_TRADESTATUS = 'N' THEN 1 
                            WHEN t1.S_DQ_TRADESTATUS = 'XD' THEN 2 WHEN t1.S_DQ_TRADESTATUS = 'XR' THEN 3 
                            WHEN t1.S_DQ_TRADESTATUS = 'DR' THEN 4 WHEN t1.S_DQ_TRADESTATUS = '交易' THEN -1 
                            WHEN t1.S_DQ_TRADESTATUS = '待核查' THEN -2 ELSE NULL END AS TradeStatus
                    FROM sys_wind.CBONDEODPRICES t1
                        JOIN sys_wind.CBONDDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND t2.S_INFO_EXCHMARKET IN ('SSE', 'SZSE', 'BSE'))
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_md_coption": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t3.S_DQ_CLOSE, NVL(t1.S_DQ_PRESETTLE, 0)) AS LastClosingPrice, NVL(t3.S_DQ_CLOSE, NVL(t1.S_DQ_PRESETTLE, 0)) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, NVL(t1.S_DQ_OPEN, 0) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, NVL(t1.S_DQ_HIGH, 0) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, NVL(t1.S_DQ_LOW, 0) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_SETTLE, 0) AS SettlementPrice, NVL(t1.S_DQ_SETTLE, 0) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRESETTLE, 0) AS LastSettlementPrice, NVL(t1.S_DQ_PRESETTLE, 0) AS AdjLastSettlementPrice,
                        0 AS UpperLimitPrice, 0 AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 10000 AS TradingAmount, 
                        1 AS AdjustFactor, #{last_trading_day} AS LastTradingDay, '-1' AS TradeStatus
                    FROM sys_wind.CHINAOPTIONEODPRICES t1
                        JOIN sys_wind.CHINAOPTIONDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND t2.S_INFO_EXCHANGE_NAME IN ('SSE', 'SZSE', 'BSE'))
                        LEFT JOIN (SELECT t.S_INFO_WINDCODE, t.S_DQ_CLOSE FROM sys_wind.CHINAOPTIONEODPRICES t WHERE t.TRADE_DT = #{last_trading_day}) t3 ON (t1.S_INFO_WINDCODE = t3.S_INFO_WINDCODE)
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_md_coption_old": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t3.S_DQ_CLOSE, NVL(t1.S_DQ_PRESETTLE, 0)) AS LastClosingPrice, NVL(t3.S_DQ_CLOSE, NVL(t1.S_DQ_PRESETTLE, 0)) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, NVL(t1.S_DQ_OPEN, 0) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, NVL(t1.S_DQ_HIGH, 0) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, NVL(t1.S_DQ_LOW, 0) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_SETTLE, 0) AS SettlementPrice, NVL(t1.S_DQ_SETTLE, 0) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRESETTLE, 0) AS LastSettlementPrice, NVL(t1.S_DQ_PRESETTLE, 0) AS AdjLastSettlementPrice,
                        0 AS UpperLimitPrice, 0 AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 10000 AS TradingAmount, 
                        1 AS AdjustFactor, #{last_trading_day} AS LastTradingDay, '-1' AS TradeStatus
                    FROM sys_wind.CHINAOPTIONEODPRICES t1
                        JOIN sys_wind.CHINAOPTIONDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND SUBSTR(t2.S_INFO_WINDCODE, LENGTH(t2.S_INFO_WINDCODE) - 2, 3) IN ('.SH', '.SZ', '.BJ'))
                        LEFT JOIN (SELECT t.S_INFO_WINDCODE, t.S_DQ_CLOSE FROM sys_wind.CHINAOPTIONEODPRICES t WHERE t.TRADE_DT = #{last_trading_day}) t3 ON (t1.S_INFO_WINDCODE = t3.S_INFO_WINDCODE)
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_md_aindex": {
        "sql": """SELECT DISTINCT t1.TRADE_DT AS TradingDay,
                        '15:00:00' AS TradingTime,
                        CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID, t2.S_INFO_NAME AS SecurityName,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastClosingPrice, NVL(t1.S_DQ_PRECLOSE, 0) AS AdjLastClosingPrice, 
                        NVL(t1.S_DQ_OPEN, 0) AS OpeningPrice, NVL(t1.S_DQ_OPEN, 0) AS AdjOpeningPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS ClosingPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjClosingPrice, 
                        NVL(t1.S_DQ_HIGH, 0) AS TopPrice, NVL(t1.S_DQ_HIGH, 0) AS AdjTopPrice, 
                        NVL(t1.S_DQ_LOW, 0) AS FloorPrice, NVL(t1.S_DQ_LOW, 0) AS AdjFloorPrice, 
                        NVL(t1.S_DQ_CLOSE, 0) AS SettlementPrice, NVL(t1.S_DQ_CLOSE, 0) AS AdjSettlementPrice,
                        NVL(t1.S_DQ_PRECLOSE, 0) AS LastSettlementPrice, NVL(t1.S_DQ_PRECLOSE, 0) AS AdjLastSettlementPrice,
                        0 AS UpperLimitPrice, 0 AS LowerLimitPrice, 
                        NVL(t1.S_DQ_VOLUME, 0) AS TradingVolume, NVL(t1.S_DQ_AMOUNT, 0) * 1000 AS TradingAmount, 
                        1 AS AdjustFactor, #{last_trading_day} AS LastTradingDay, '-1' AS TradeStatus
                    FROM sys_wind.AINDEXEODPRICES t1
                        JOIN sys_wind.AINDEXDESCRIPTION t2 ON (t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE AND t2.S_INFO_EXCHMARKET IN ('SSE', 'SZSE', 'BSE'))
                    WHERE t1.TRADE_DT = #{trading_day}"""
    },
    "load_quant_dividend": {
        "sql": """SELECT DISTINCT t1.EQY_RECORD_DT AS RecordDate, CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID,
                        SUM(NVL(t2.CASH_DVD_PER_SH_PRE_TAX, NVL(t1.CASH_DVD_PER_SH_PRE_TAX, 0))) AS BeforeRate, SUM(NVL(t2.CASH_DVD_PER_SH_AFTER_TAX, NVL(t1.CASH_DVD_PER_SH_AFTER_TAX, 0))) AS AfterRate,
                        SUM(NVL(t2.S_DIV_BONUSRATE, NVL(t1.S_DIV_BONUSRATE, 0))) AS BonusRate, SUM(NVL(t2.S_DIV_CONVERSEDRATE, NVL(t1.S_DIV_CONVERSEDRATE, 0))) AS TransferRate,
                        MIN(NVL(t2.EX_DT, t1.EX_DT)) AS DividendDate, MIN(NVL(t2.LISTING_DT_OF_DVD_SHR, t1.LISTING_DT_OF_DVD_SHR)) AS NewStockMarketDate
                    FROM sys_wind.AShareDividend t1
                         LEFT JOIN (SELECT t.* FROM sys_wind.AShareDividend t WHERE t.EQY_RECORD_DT = #{trading_day} AND t.IS_CHANGED = '1') t2 ON (t1.EQY_RECORD_DT = t2.EQY_RECORD_DT AND t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE)
                    WHERE t1.EQY_RECORD_DT = #{trading_day} and t1.S_DIV_PROGRESS = '3' AND (t1.S_DIV_OBJECT = '普通股股东' OR t1.S_DIV_OBJECT = '' OR t1.S_DIV_OBJECT IS NULL)
                    GROUP BY t1.EQY_RECORD_DT, t1.S_INFO_WINDCODE"""
    },
    "load_quant_dividend_all": {
        "sql": """SELECT DISTINCT t1.EQY_RECORD_DT AS RecordDate, CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID,
                        t1.S_INFO_WINDCODE AS FullSecurityID,
                        SUM(NVL(t2.CASH_DVD_PER_SH_PRE_TAX, NVL(t1.CASH_DVD_PER_SH_PRE_TAX, 0))) AS BeforeRate, SUM(NVL(t2.CASH_DVD_PER_SH_AFTER_TAX, NVL(t1.CASH_DVD_PER_SH_AFTER_TAX, 0))) AS AfterRate,
                        SUM(NVL(t2.S_DIV_BONUSRATE, NVL(t1.S_DIV_BONUSRATE, 0))) AS BonusRate, SUM(NVL(t2.S_DIV_CONVERSEDRATE, NVL(t1.S_DIV_CONVERSEDRATE, 0))) AS TransferRate,
                        MIN(NVL(t2.EX_DT, t1.EX_DT)) AS DividendDate, MIN(NVL(t2.LISTING_DT_OF_DVD_SHR, t1.LISTING_DT_OF_DVD_SHR)) AS NewStockMarketDate
                    FROM sys_wind.AShareDividend t1
                         LEFT JOIN (SELECT t.* FROM sys_wind.AShareDividend t WHERE t.EQY_RECORD_DT >= #{refer_day} AND t.IS_CHANGED = '1') t2 ON (t1.EQY_RECORD_DT = t2.EQY_RECORD_DT AND t1.S_INFO_WINDCODE = t2.S_INFO_WINDCODE)
                    WHERE t1.EQY_RECORD_DT >= #{refer_day} and t1.S_DIV_PROGRESS = '3' AND (t1.S_DIV_OBJECT = '普通股股东' OR t1.S_DIV_OBJECT = '' OR t1.S_DIV_OBJECT IS NULL)
                    GROUP BY t1.EQY_RECORD_DT, t1.S_INFO_WINDCODE"""
    },
    "load_quant_rightissue": {
        "sql": """SELECT DISTINCT t1.S_RIGHTSISSUE_REGDATESHAREB AS RecordDate, CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID, t1.S_INFO_WINDCODE AS FullSecurityID, 
                        t1.S_RIGHTSISSUE_PRICE AS IssuePrice, t1.S_RIGHTSISSUE_RATIO AS IssueRate,
                        t1.S_RIGHTSISSUE_EXDIVIDENDDATE AS DividendDate, t1.S_RIGHTSISSUE_LISTEDDATE AS NewStockMarketDate
                    FROM sys_wind.AShareRightIssue t1
                    WHERE t1.S_RIGHTSISSUE_REGDATESHAREB = #{trading_day} AND t1.S_RIGHTSISSUE_PROGRESS = '3'"""
    },
    "load_quant_rightissue_all": {
        "sql": """SELECT DISTINCT t1.S_RIGHTSISSUE_REGDATESHAREB AS RecordDate, CASE WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SH' THEN '1' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.SZ' THEN '2' 
                            WHEN SUBSTR(t1.S_INFO_WINDCODE, LENGTH(t1.S_INFO_WINDCODE) - 2, 3) = '.BJ' THEN '4' 
                            ELSE '' END AS ExchangeID,
                        REPLACE(REPLACE(REPLACE(t1.S_INFO_WINDCODE, '.SH', ''), '.SZ', ''), '.BJ', '') AS SecurityID, t1.S_INFO_WINDCODE AS FullSecurityID, 
                        t1.S_RIGHTSISSUE_PRICE AS IssuePrice, t1.S_RIGHTSISSUE_RATIO AS IssueRate,
                        t1.S_RIGHTSISSUE_EXDIVIDENDDATE AS DividendDate, t1.S_RIGHTSISSUE_LISTEDDATE AS NewStockMarketDate
                    FROM sys_wind.AShareRightIssue t1
                    WHERE t1.S_RIGHTSISSUE_REGDATESHAREB >= #{refer_day} AND t1.S_RIGHTSISSUE_PROGRESS = '3'"""
    },
    "load_quant_md_future": {
        "sql": """SELECT DISTINCT t1.trade_dt AS TradingDay, t2.s_info_exchmarket AS ExchangeID, t2.s_info_code AS InstrumentID, t2.s_info_windcode AS FullInstrumentID, t2.s_info_name AS InstrumentName, '0' AS LastClosingPrice, 
                            NVL(t1.s_dq_open, 0) AS OpeningPrice, NVL(t1.s_dq_close, 0) AS ClosingPrice, NVL(t1.s_dq_high, 0) AS TopPrice, NVL(t1.s_dq_low, 0) AS FloorPrice, NVL(t1.s_dq_settle, 0) AS SettlementPrice, 
                            NVL(t1.s_dq_presettle, 0) AS LastSettlementPrice, '0' AS UpperLimitPrice, '0' AS LowerLimitPrice, NVL(t1.s_dq_volume, 0) AS TradingVolume, NVL(t1.s_dq_amount, 0) AS TradingAmount, #{last_trading_day} AS LastTradingDay
                        FROM CCommodityFuturesEODPrices t1, CFuturesDescription t2
                        WHERE t1.trade_dt > #{trading_day}
                        and t1.s_info_windcode = t2.s_info_windcode
                        and t2.fs_info_type = '1'
                        and t2.s_info_exchmarket in ('SHFE', 'INE', 'DCE', 'CZCE', 'GFEX')
                        UNION
                        SELECT DISTINCT t1.trade_dt AS TradingDay, t2.s_info_exchmarket AS ExchangeID, t2.s_info_code AS InstrumentID, t2.s_info_windcode AS FullInstrumentID, t2.s_info_name AS InstrumentName, '0' AS LastClosingPrice, 
                            NVL(t1.s_dq_open, 0) AS OpeningPrice, NVL(t1.s_dq_close, 0) AS ClosingPrice, NVL(t1.s_dq_high, 0) AS TopPrice, NVL(t1.s_dq_low, 0) AS FloorPrice, NVL(t1.s_dq_settle, 0) AS SettlementPrice, 
                            NVL(t1.s_dq_presettle, 0) AS LastSettlementPrice, '0' AS UpperLimitPrice, '0' AS LowerLimitPrice, NVL(t1.s_dq_volume, 0) AS TradingVolume, NVL(t1.s_dq_amount, 0) AS TradingAmount, #{last_trading_day} AS LastTradingDay
                        FROM CIndexFuturesEODPrices t1, CFuturesDescription t2
                        WHERE t1.trade_dt > #{trading_day}
                        and t1.s_info_windcode = t2.s_info_windcode
                        and t2.fs_info_type = '1'
                        and t2.s_info_exchmarket = 'CFFEX'"""
    }
}
