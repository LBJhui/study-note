# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:10
# @Author: LBJ辉
# @File: tradingday_apis
# @Project: python
alias = "TradingDayApis"

realm = {
    "roles": {},
    "rules": {
    }
}

ware = {
    "get_TradingDayOfTradeSystem": """SELECT t1.tradingday, t1.lasttradingday FROM siminfo.t_tradesystemtradingday t1 
                                                WHERE t1.tradesystemid = #{systemId} limit 1""",
    "get_TradingDayOfBrokerSystem": """SELECT t1.tradingday, t1.lasttradingday FROM siminfo.t_tradesystemtradingday t1, siminfo.t_tradesystembrokersystem t2 
                                                WHERE t1.TradeSystemID = t2.TradeSystemID and t2.BrokerSystemID = #{systemId} limit 1""",
    "get_TradingDayOfSettlementGroup": """SELECT t1.tradingday, t1.lasttradingday FROM siminfo.t_tradesystemtradingday t1, siminfo.t_tradesystemsettlementgroup t2 
                                                WHERE t1.TradeSystemID = t2.TradeSystemID and t2.SettlementGroupID = #{settlementGroupId}} limit 1""",
    "get_NextDayOfDay": """SELECT DAY FROM siminfo.t_TradingCalendar t WHERE t.day > #{tradingDay} ORDER BY DAY LIMIT 1""",
    "get_NextTradingDayOfDay": """SELECT DAY FROM siminfo.t_TradingCalendar t WHERE t.day > #{tradingDay} AND t.tra = '1' ORDER BY DAY LIMIT 1""",
    "get_LastDayOfDay": """SELECT DAY FROM siminfo.t_TradingCalendar t WHERE t.day < #{tradingDay} ORDER BY DAY DESC LIMIT 1""",
    "get_LastTradingDayOfDay": """SELECT DAY FROM siminfo.t_TradingCalendar t WHERE t.day < #{tradingDay} AND t.tra = '1' ORDER BY DAY DESC LIMIT 1""",
    "get_RealTradingDayOfTradeSystem": """SELECT DAY FROM siminfo.t_tradingcalendar 
                                            WHERE day <= (SELECT IF(LatestRealTradingDay is NULL OR LatestRealTradingDay > TradingDay, TradingDay, LatestRealTradingDay) FROM siminfo.t_tradesystemtradingday WHERE TradeSystemID = #{systemId} LIMIT 1) 
                                                AND Tra = 1 ORDER BY DAY DESC LIMIT 1""",
    "get_RealTradingDayOfBrokerSystem": """SELECT DAY FROM siminfo.t_tradingcalendar 
                                            WHERE day <= (SELECT IF(t1.LatestRealTradingDay is NULL OR t1.LatestRealTradingDay > t1.TradingDay, t1.TradingDay, t1.LatestRealTradingDay) FROM siminfo.t_tradesystemtradingday t1, siminfo.t_tradesystembrokersystem t2 WHERE t1.TradeSystemID = t2.TradeSystemID AND t2.BrokerSystemID = #{systemId} LIMIT 1) 
                                                AND Tra = 1 ORDER BY DAY DESC LIMIT 1""",
    "get_RealTradingDayOfBrokerSystem": """SELECT DAY FROM siminfo.t_tradingcalendar 
                                            WHERE day <= (SELECT IF(t1.LatestRealTradingDay is NULL OR t1.LatestRealTradingDay > t1.TradingDay, t1.TradingDay, t1.LatestRealTradingDay) FROM siminfo.t_tradesystemtradingday t1, siminfo.t_tradesystemsettlementgroup t2 WHERE t1.TradeSystemID = t2.TradeSystemID AND t2.SettlementGroupId = #{settlementGroupId} LIMIT 1) 
                                                AND Tra = 1 ORDER BY DAY DESC LIMIT 1""",
    "get_RealTradingDayOfDay": """SELECT DAY FROM siminfo.t_tradingcalendar WHERE day <= #{tradingDay} AND Tra = 1 ORDER BY DAY DESC LIMIT 1""",
    "get_TradeSystemStartParams": """SELECT StartDate, EarliestStarttime, TradingSegmentType FROM siminfo.t_TradeSystemStartParams WHERE TradingDay = #{tradingDay} AND TradeSystemId = #{systemId}"""
}
