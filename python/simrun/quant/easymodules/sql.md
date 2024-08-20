```sql
SELECT t1.HistoryNo, CONCAT(CASE WHEN t2.ExchangeID = '1' THEN 'sh' WHEN t2.ExchangeID = '2' THEN 'sz' WHEN t2.ExchangeID = '4' THEN 'bj' ELSE '' END, t2.SecurityID) AS BenchmarkStockID, t2.SecurityName AS BenchmarkStockName, t2.TradingDay, t2.TradingTime, IF(t2.LastClosingPrice = 0, t2.ClosingPrice, t2.LastClosingPrice) AS LastClosingPrice, t2.ClosingPrice, ROUND(t2.ClosingPrice - t3.LastClosingPrice, 4) AS TotalProfit, ROUND((t2.ClosingPrice - t3.LastClosingPrice) / t3.LastClosingPrice, 6) AS TotalProfitRatio
                    FROM quant.t_future_quantasset t1, quant.t_quantmarketdata t2, 
                        (SELECT t.ExchangeID, t.SecurityID, IF(t.LastClosingPrice = 0, t.ClosingPrice, t.LastClosingPrice) AS LastClosingPrice
                            FROM quant.t_quantmarketdata t, (SELECT t.ExchangeID, t.SecurityID, MIN(TradingDay) AS MinTradingDay FROM quant.t_quantmarketdata t WHERE t.FullSecurityID IN (${bench_ids}) GROUP BY t.ExchangeID, t.SecurityID) t1, (SELECT MIN(TradingDay) AS MinQuantTradingDay FROM quant.t_future_quantasset WHERE HistoryNo = #{history_no}) t2
                            WHERE t.ExchangeID = t1.ExchangeID AND t.SecurityID = t1.SecurityID AND ((t.TradingDay = t1.MinTradingDay AND t1.MinTradingDay > t2.MinQuantTradingDay) OR (t.TradingDay = t2.MinQuantTradingDay AND t1.MinTradingDay <= t2.MinQuantTradingDay))) t3
                    WHERE t1.HistoryNo = #{history_no} AND t1.TradingDay = t2.TradingDay AND t2.ExchangeID = t3.ExchangeID AND t2.SecurityID = t3.SecurityID AND t2.FullSecurityID IN (${bench_ids})
```

