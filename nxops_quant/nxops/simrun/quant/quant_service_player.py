# _*_ coding: utf-8 _*_
# @Time: 2024/8/12 14:49
# @Author: LBJ辉
# @File: quant_service_player
# @Project: nxops_quant
import datetime
import os
import shutil
import sqlite3
import threading
import time
import warnings

import click
import pandas
import rapidjson

warnings.filterwarnings("ignore")
from pandas.io import sql as pandas_sql
from sqlalchemy import create_engine

from nxpy.context import AppContext
from nxpy.log.logger import LoggerUtils
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutor, EasyDBExecutorUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.rsh.easy_rsh import EasyRSH
from nxpy.os.path import PathUtils
from nxpy.config.easy_config import EasyConfigUtils
from nxpy.service.service_player import ServicePlayer


class QuantServicePlayer(ServicePlayer):
    def __init__(self, options={}, config=None):
        super().__init__(options=options, config=config)

        self.condition = threading.Condition()

    def get_history_no(self, options):
        executor = EasyDBExecutorUtils.get_executor(**options)

        error, exec_result = executor.execute("QuantDataClear.get_history_no", paras=options)
        if error:
            self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
            return None

        return exec_result[0][0][0]

    def dump_quant_data(self, options):
        history_no = options.get("history_no")
        if not history_no:
            self.error("none history_no")
            return False

        data_home = options.get("data_home")
        data_home = PathUtils.get_real_path(EasyConfigUtils.easy_parse(data_home, options))

        file_encoding = options.get("file_encoding")

        try:
            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            clear_executor.execute("QuantDataClear.clean_simtest_data", paras=options)

            mysql_config = clear_executor.get_datasource().settings
            mysql_url = "mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (mysql_config["user"], mysql_config["password"], mysql_config["host"], str(mysql_config.get("port", 3306)))
            mysql_engine = create_engine(mysql_url, execution_options={"autocommit": False})

            with mysql_engine.connect() as connection:
                with connection.begin():
                    simtest_info_file = os.path.join(data_home, "TestInfo.csv")
                    if os.path.exists(simtest_info_file):
                        simtest_info_data = pandas.read_csv(simtest_info_file, encoding=file_encoding, dtype="object")
                        simtest_info_data["QuantID"] = options.get("quant_id")
                        simtest_info_data["HistoryNo"] = history_no
                        simtest_info_data.to_sql(name="t_SimTestInfo", con=connection, if_exists='append', index=False, chunksize=10000)

                    init_position_file = os.path.join(data_home, "SimTestInitPosition.csv")
                    if os.path.exists(init_position_file):
                        init_position_data = pandas.read_csv(init_position_file, encoding=file_encoding, dtype="object")
                        init_position_data["HistoryNo"] = history_no
                        init_position_data.to_sql(name="t_SimTestInitPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_trade_detail_file = os.path.join(data_home, "SimTestTradeDetail.csv")
                    if os.path.exists(spot_trade_detail_file):
                        spot_trade_detail_data = pandas.read_csv(spot_trade_detail_file, encoding=file_encoding, dtype="object")
                        spot_trade_detail_data["HistoryNo"] = history_no
                        spot_trade_detail_data.to_sql(name="t_SimTestSpotTradeDetail", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_order_file = os.path.join(data_home, "SimTestOrder.csv")
                    if os.path.exists(spot_order_file):
                        spot_order_data = pandas.read_csv(spot_order_file, encoding=file_encoding, dtype="object")
                        spot_order_data["HistoryNo"] = history_no
                        spot_order_data.to_sql(name="t_SimTestSpotOrder", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_position_file = os.path.join(data_home, "SimTestPosition.csv")
                    if os.path.exists(spot_position_file):
                        spot_position_data = pandas.read_csv(spot_position_file, encoding=file_encoding, dtype="object")
                        spot_position_data["HistoryNo"] = history_no
                        spot_position_data.to_sql(name="t_SimTestSpotPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_asset_file = os.path.join(data_home, "SimTestResult.csv")
                    if os.path.exists(spot_asset_file):
                        spot_asset_data = pandas.read_csv(spot_asset_file, encoding=file_encoding, dtype="object")
                        spot_asset_data["HistoryNo"] = history_no
                        spot_asset_data.to_sql(name="t_SimTestSpotResult", con=connection, if_exists='append', index=False, chunksize=10000)

                    sub_md_file = os.path.join(data_home, "SimSubMD.csv")
                    if os.path.exists(sub_md_file):
                        sub_md_data = pandas.read_csv(sub_md_file, encoding=file_encoding, dtype="object")
                        sub_md_data["HistoryNo"] = history_no
                        sub_md_data.to_sql(name="t_SimTestSubMD", con=connection, if_exists='append', index=False, chunksize=10000)

                    sp_trade_detail_file = os.path.join(data_home, "SimTestSPSSETradeDetail.csv")
                    if os.path.exists(sp_trade_detail_file):
                        sp_trade_detail_data = pandas.read_csv(sp_trade_detail_file, encoding=file_encoding, dtype="object")
                        sp_trade_detail_data["HistoryNo"] = history_no
                        sp_trade_detail_data.to_sql(name="t_SimTestSPTradeDetail", con=connection, if_exists='append', index=False, chunksize=10000)

                    sp_order_file = os.path.join(data_home, "SimTestSPSSEOrder.csv")
                    if os.path.exists(sp_order_file):
                        sp_order_data = pandas.read_csv(sp_order_file, encoding=file_encoding, dtype="object")
                        sp_order_data["HistoryNo"] = history_no
                        sp_order_data.to_sql(name="t_SimTestSPOrder", con=connection, if_exists='append', index=False, chunksize=10000)

                    sp_position_file = os.path.join(data_home, "SimTestSPSSEPosition.csv")
                    if os.path.exists(sp_position_file):
                        sp_position_data = pandas.read_csv(sp_position_file, encoding=file_encoding, dtype="object")
                        sp_position_data["HistoryNo"] = history_no
                        sp_position_data.to_sql(name="t_SimTestSPPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    sp_asset_file = os.path.join(data_home, "SimTestSPResult.csv")
                    if os.path.exists(sp_asset_file):
                        sp_asset_data = pandas.read_csv(sp_asset_file, encoding=file_encoding, dtype="object")
                        sp_asset_data["HistoryNo"] = history_no
                        sp_asset_data.to_sql(name="t_SimTestSPResult", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_trade_detail_file = os.path.join(data_home, "SimTestCreditTradeDetail.csv")
                    if os.path.exists(credit_trade_detail_file):
                        credit_trade_detail_data = pandas.read_csv(credit_trade_detail_file, encoding=file_encoding, dtype="object")
                        credit_trade_detail_data["HistoryNo"] = history_no
                        credit_trade_detail_data.to_sql(name="t_SimTestCreditTradeDetail", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_order_file = os.path.join(data_home, "SimTestCreditOrder.csv")
                    if os.path.exists(credit_order_file):
                        credit_order_data = pandas.read_csv(credit_order_file, encoding=file_encoding, dtype="object")
                        credit_order_data["HistoryNo"] = history_no
                        credit_order_data.to_sql(name="t_SimTestCreditOrder", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_position_file = os.path.join(data_home, "SimTestCreditPosition.csv")
                    if os.path.exists(credit_position_file):
                        credit_position_data = pandas.read_csv(credit_position_file, encoding=file_encoding, dtype="object")
                        credit_position_data["HistoryNo"] = history_no
                        credit_position_data.to_sql(name="t_SimTestCreditPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_asset_file = os.path.join(data_home, "SimTestCreditResult.csv")
                    if os.path.exists(credit_asset_file):
                        credit_asset_data = pandas.read_csv(credit_asset_file, encoding=file_encoding, dtype="object")
                        credit_asset_data["HistoryNo"] = history_no
                        credit_asset_data.rename(columns={"TotalNetAssert": "TotalNetAsset"}, inplace=True)
                        credit_asset_data.to_sql(name="t_SimTestCreditResult", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_debt_file = os.path.join(data_home, "SimTestCreditDebt.csv")
                    if os.path.exists(credit_debt_file):
                        credit_debt_data = pandas.read_csv(credit_debt_file, encoding=file_encoding, dtype="object")
                        credit_debt_data["HistoryNo"] = history_no
                        credit_debt_data.to_sql(name="t_SimTestCreditDebt", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_repayment_file = os.path.join(data_home, "SimTestCreditRepayment.csv")
                    if os.path.exists(credit_repayment_file):
                        credit_repayment_data = pandas.read_csv(credit_repayment_file, encoding=file_encoding, dtype="object")
                        credit_repayment_data["HistoryNo"] = history_no
                        credit_repayment_data.to_sql(name="t_SimTestCreditRepayment", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_transfer_file = os.path.join(data_home, "SimTestCreditTransfer.csv")
                    if os.path.exists(credit_transfer_file):
                        credit_transfer_data = pandas.read_csv(credit_transfer_file, encoding=file_encoding, dtype="object")
                        credit_transfer_data["HistoryNo"] = history_no
                        credit_transfer_data.to_sql(name="t_SimTestCreditTransfer", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_surplus_file = os.path.join(data_home, "SimTestCreditSurplusPosition.csv")
                    if os.path.exists(credit_surplus_file):
                        credit_surplus_data = pandas.read_csv(credit_surplus_file, encoding=file_encoding, dtype="object")
                        credit_surplus_data["HistoryNo"] = history_no
                        credit_surplus_data.to_sql(name="t_SimTestCreditSurplusPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    credit_fund_transfer_file = os.path.join(data_home, "SimTestCreditFundTransferDetailEx.csv")
                    if os.path.exists(credit_fund_transfer_file):
                        credit_fund_transfer_data = pandas.read_csv(credit_fund_transfer_file, encoding=file_encoding, dtype="object")
                        credit_fund_transfer_data["HistoryNo"] = history_no
                        credit_fund_transfer_data.to_sql(name="t_SimTestCreditFundTransferDetailEx", con=connection, if_exists='append', index=False, chunksize=10000)
        except Exception as e:
            self.error(f"dump[{history_no}] failed: error: [{e}]")
            return False

        return True

    def deal_quant_data(self, options):
        history_no = options.get("history_no")
        if not history_no:
            self.error("failed: none history_no")
            return False

        self.info(f"deal[{history_no}] begin")

        try:
            executor = EasyDBExecutorUtils.get_executor(**options)

            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            parameters = {"history_no": history_no}

            error, exec_result = clear_executor.execute("QuantDataClear.deal_quant_data", paras=parameters)
            if error:
                self.error(f"deal[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False
            else:
                mysql_config = executor.get_datasource().settings
                mysql_url = "mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (mysql_config["user"], mysql_config["password"], mysql_config["host"], str(mysql_config.get("port", 3306)))
                mysql_engine = create_engine(mysql_url, pool_pre_ping=True, pool_recycle=600, execution_options={"autocommit": False})

                with mysql_engine.connect() as connection:
                    with connection.begin():
                        error, test_profit_data = clear_executor.pandas_query("QuantDataClear.get_quant_test_profit", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_quant_test_profit error: [code={error['code']}, msg={error['msg']}]")
                            return False
                        test_profit_data.to_sql(name="t_ClientQuantTestProfit", con=connection, if_exists='append', index=False, chunksize=10000)

                        error, bench_profit_data = clear_executor.pandas_query("QuantDataClear.get_quant_bench_profit", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_quant_bench_profit error: [code={error['code']}, msg={error['msg']}]")
                            return False
                        bench_profit_data.to_sql(name="t_QuantTestBenchmarkProfit", con=connection, if_exists='append', index=False, chunksize=10000)

                        error, test_info_data = clear_executor.pandas_query("QuantDataClear.get_quant_test_info", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_quant_test_info error: [code={error['code']}, msg={error['msg']}]")
                            return False
                        test_info_data.to_sql(name="t_SimTestInfo", con=connection, if_exists='append', index=False, chunksize=10000)

                error, quant_market = clear_executor.querylist("QuantDataClear.get_quant_test_market", paras=options)
                if error:
                    self.error(f"deal[{history_no}] failed: get_quant_test_market error: [code={error['code']}, msg={error['msg']}]")
                    return False

                batch_paras = []
                if quant_market and len(quant_market) > 0 and quant_market[0] and len(quant_market[0]) > 0:
                    batch_paras = [{"quant_market": row[0]} for row in quant_market[0]]

                error, quant_history = clear_executor.queryone("QuantDataClear.get_quant_test_history", paras=options)
                if error:
                    self.error(f"deal[{history_no}] failed: get_quant_test_history error: [code={error['code']}, msg={error['msg']}]")
                    return False

                init_asset = 0
                total_asset = 0
                test_trade_days = 0
                if quant_history and len(quant_history) > 0 and quant_history[0] and len(quant_history[0]) > 0:
                    init_asset = quant_history[0][0]
                    total_asset = quant_history[0][1]
                    test_trade_days = quant_history[0][2]

                error, exec_result = executor.execute("QuantDataClear.save_quant_history", paras=dict(options, test_data_status="0", test_data_file_status="0", init_asset=init_asset, total_asset=total_asset, test_trade_days=test_trade_days), batch_paras=batch_paras)
                if error:
                    self.error(f"deal[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                    return False
        except Exception as e:
            self.error(f"deal[{history_no}] failed: error: [{e}]")
            return False

        self.info(f"deal[{history_no}] finished")
        return True

    def fit_web_quant(self, options):
        history_no = options.get("history_no")
        if not history_no:
            self.error("none history_no")
            return False

        self.info(f"fit[{history_no}] begin")

        web_home = options.get("web_home")
        web_home = PathUtils.get_real_path(web_home)

        temp_home = options.get("temp_home")
        temp_home = PathUtils.get_real_path(temp_home)

        history_home = os.path.join(temp_home, f"{history_no}")
        if not os.path.exists(history_home):
            os.makedirs(history_home)

        try:
            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            parameters = {"history_no": history_no}
            error, quant_orders = clear_executor.pandas_query("QuantDataClear.get_quant_orders", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            day_quant_orders_groups = quant_orders.groupby("TradingDay")
            order_list_file_path = os.path.join(history_home, "order.txt")
            with open(order_list_file_path, "w") as order_list_file:
                for group_trading_day, day_quant_orders in day_quant_orders_groups:
                    day_quant_orders = day_quant_orders.sort_values("OrderSysID")
                    order_file_name = f"order_{group_trading_day}.csv"
                    order_file_path = os.path.join(history_home, order_file_name)
                    order_list_file.write(f"{order_file_name}\n")
                    day_quant_orders.to_csv(order_file_path, index=False, chunksize=10000)

            security_quant_orders_groups = quant_orders.groupby("StockID")
            for group_security_id, security_quant_orders in security_quant_orders_groups:
                security_quant_orders = security_quant_orders.sort_values(["TradingDay", "OrderSysID"])
                order_file_name = f"order_{group_security_id}.csv"
                order_file_path = os.path.join(history_home, order_file_name)
                security_quant_orders.to_csv(order_file_path, index=False, chunksize=10000)

            error, quant_trades = clear_executor.pandas_query("QuantDataClear.get_quant_trades", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            day_quant_trades_groups = quant_trades.groupby("TradingDay")
            trade_list_file_path = os.path.join(history_home, "trade.txt")
            with open(trade_list_file_path, "w") as trade_list_file:
                for group_trading_day, day_quant_trades in day_quant_trades_groups:
                    day_quant_trades = day_quant_trades.sort_values("TradeID")
                    trade_file_name = f"trade_{group_trading_day}.csv"
                    trade_file_path = os.path.join(history_home, trade_file_name)
                    trade_list_file.write(f"{trade_file_name}\n")
                    day_quant_trades.to_csv(trade_file_path, index=False, chunksize=10000)

            security_quant_trades_groups = quant_trades.groupby("StockID")
            for group_security_id, security_quant_trades in security_quant_trades_groups:
                security_quant_trades = security_quant_trades.sort_values(["TradingDay", "TradeID"])
                trade_file_name = f"trade_{group_security_id}.csv"
                trade_file_path = os.path.join(history_home, trade_file_name)
                security_quant_trades.to_csv(trade_file_path, index=False, chunksize=10000)

            error, quant_assets = clear_executor.pandas_query("QuantDataClear.get_quant_assets", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            asset_file_path = os.path.join(history_home, "ammout.csv")
            quant_assets.to_csv(asset_file_path, index=False, chunksize=10000)

            error, quant_positions = clear_executor.pandas_query("QuantDataClear.get_quant_positions", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            day_quant_positions_groups = quant_positions.groupby("TradingDay")
            position_list_file_path = os.path.join(history_home, "position.txt")
            with open(position_list_file_path, "w") as position_list_file:
                for group_trading_day, day_quant_positions in day_quant_positions_groups:
                    position_file_name = f"position_{group_trading_day}.csv"
                    position_file_path = os.path.join(history_home, position_file_name)
                    position_list_file.write(f"{position_file_name}\n")
                    day_quant_positions.to_csv(position_file_path, index=False, chunksize=10000)

            error, quant_profits = clear_executor.pandas_query("QuantDataClear.get_quant_profits", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            profit_file_path = os.path.join(history_home, "profit.csv")
            quant_profits.to_csv(profit_file_path, index=False, chunksize=10000)

            error, quant_summary = clear_executor.pandas_query("QuantDataClear.get_quant_month_summary", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            summary_file_path = os.path.join(history_home, "month_summary.csv")
            quant_summary.to_csv(summary_file_path, index=False, chunksize=10000)

            error, quant_debts = clear_executor.pandas_query("QuantDataClear.get_quant_debts", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            day_quant_debts_groups = quant_debts.groupby("TradingDay")
            debt_list_file_path = os.path.join(history_home, "debt.txt")
            with open(debt_list_file_path, "w") as debt_list_file:
                for group_trading_day, day_quant_debts in day_quant_debts_groups:
                    debt_file_name = f"debt_{group_trading_day}.csv"
                    debt_file_path = os.path.join(history_home, debt_file_name)
                    debt_list_file.write(f"{debt_file_name}\n")
                    day_quant_debts.to_csv(debt_file_path, index=False, chunksize=10000)

            error, quant_repayments = clear_executor.pandas_query("QuantDataClear.get_quant_repayments", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            day_quant_repayments_groups = quant_repayments.groupby("TradingDay")
            repayment_list_file_path = os.path.join(history_home, "repayment.txt")
            with open(repayment_list_file_path, "w") as repayment_list_file:
                for group_trading_day, day_quant_repayments in day_quant_repayments_groups:
                    repayment_file_name = f"repayment_{group_trading_day}.csv"
                    repayment_file_path = os.path.join(history_home, repayment_file_name)
                    repayment_list_file.write(f"{repayment_file_name}\n")
                    day_quant_repayments.to_csv(repayment_file_path, index=False, chunksize=10000)

            error, quant_benches = clear_executor.pandas_query("QuantDataClear.get_quant_benches", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            bench_file_path = os.path.join(history_home, "comb_bench.csv")
            quant_benches.to_csv(bench_file_path, index=False, chunksize=10000)

            error, quant_submds = clear_executor.pandas_query("QuantDataClear.get_quant_submds", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            submd_file_path = os.path.join(history_home, "sub_md_data.csv")
            quant_submds.to_csv(submd_file_path, index=False, chunksize=10000)

            history_db_file_path = os.path.join(history_home, f"{history_no}.db")
            if os.path.exists(history_db_file_path):
                os.remove(history_db_file_path)

            sqlite_conn = sqlite3.connect(history_db_file_path)
            sqlite_conn.text_factory = str
            sqlite_cursor = sqlite_conn.cursor()

            sql = """CREATE TABLE position(TradingDay int,StockID text,StockName text,SecurityKind text, PosiDirection text,Volume int,ClosingPrice real,SettlementPrice real,UnderlyingClosePrice real,StrikePrice real,OptionsType text,FirstDate text,LastDate text,StrikeDate text,ExpireDate text,TotalPosCost real,OpenPosCost real,HoldingValue real,Margin real,TradingFee real,Profit real,PreVolume int,PreOpenPosCost real,TodayProfit real, TodayBuyCapital real, TodaySellCapital real, BuyCapital real, SellCapital real, InitTotalPosCost real, InitHoldingValue real, ReturnRatio real, ContributionRatio real,PreSettlementPrice real, UnderlyingPreClosePrice real, MaxTodayAmount real, InitTodayAmount real, FinalTodayAmount real, TotalOpenPosCost real, CreditBuyPos int,CreditBuyAmount real,CreditBuyInterestFee real, CreditSellPos int, CreditSellAmount real,CreditSellInterestFee real,CollateralOutPos int,CollateralInPos int)"""
            sqlite_cursor.execute(sql)
            sql = """CREATE UNIQUE INDEX IDX_Position_TradingDay_StockID_SecurityKind_PosiDirection ON position(TradingDay ASC,StockID ASC, SecurityKind ASC, PosiDirection ASC)"""
            sqlite_cursor.execute(sql)
            sql = """CREATE TABLE dkmd(TradingDay int,TradingTime text,StockID text,LastClosingPrice real,AdjLastClosingPrice real,OpeningPrice real,AdjOpeningPrice real,ClosingPrice real,AdjClosingPrice real,TopPrice real,AdjTopPrice real,FloorPrice real,AdjFloorPrice real,TradingVolume int,TradingAmount real,OpenPosCost real,ShortOpenPosCost real,LongOpenPosCost real,PreVolume int,ShortPreVolume int,LongPreVolume int)"""
            sqlite_cursor.execute(sql)
            sql = "CREATE UNIQUE INDEX IDX_dkmd_TradingDay_TradingTime_StockID ON dkmd(TradingDay ASC,TradingTime ASC,StockID ASC)";
            sqlite_cursor.execute(sql)

            sqlite_cursor.close()

            error, quant_db_positions = clear_executor.pandas_query("QuantDataClear.get_quant_db_positions", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            pandas_sql.to_sql(quant_db_positions, name='position', con=sqlite_conn, if_exists='append', index=False, chunksize=10000)

            error, quant_securities = clear_executor.querylist("QuantDataClear.get_quant_sub_securities", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            if quant_securities and quant_securities[0]:
                i_parameters = parameters.copy()
                for exchange_id, security_id in quant_securities[0]:
                    i_parameters.update({"exchange_id": exchange_id, "security_id": security_id})
                    error, quant_dkmds = clear_executor.pandas_query("QuantDataClear.get_quant_security_dkmds", i_parameters)
                    if error:
                        self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                        return False

                    if len(quant_dkmds):
                        full_security_id = quant_dkmds['StockID'].values[0]
                        dkmd_file_name = f"dk_{full_security_id}.csv"
                        dkmd_file_path = os.path.join(history_home, dkmd_file_name)
                        quant_dkmds.to_csv(dkmd_file_path, index=False, chunksize=10000)

                        pandas_sql.to_sql(quant_dkmds, name='dkmd', con=sqlite_conn, if_exists='append', index=False, chunksize=10000)

            sqlite_conn.close()

            web_history_home = os.path.join(web_home, f"{history_no}")
            try:
                if os.path.exists(web_history_home):
                    shutil.rmtree(web_history_home)
                shutil.move(history_home, web_history_home)
            except Exception as e:
                self.error(f"fit[{history_no}] failed: move[{history_home}->{web_history_home}] error: {e}")
                return False

            try:
                web_host_id = options.get("web_host")
                web_host_config = EasyHostsUtils.get_host(web_host_id)

                web_host_ssh = EasyRSH(use_sftp=False)
                web_host_ssh.connect_s(web_host_config)

                remote_quant_mid_home = options.get("remote_quant_mid_home")
                remote_web_result_home = options.get("remote_web_result_home")
                move_command = f"mv -f {remote_quant_mid_home}/{history_no} {remote_web_result_home}"

                web_host_ssh.execute(move_command)

                web_host_ssh.disconnect()
            except Exception as e:
                self.error(f"fit[{history_no}] failed: execute[{move_command}] error: {e}")
                return False

        except Exception as e:
            self.error(f"fit[{history_no}] failed: error[{e}]")
            return False

        self.info(f"fit[{history_no}] finished")
        return True

    def clear_quant(self, options):
        result = self.dump_quant_data(options)

        if result:
            result = self.deal_quant_data(options)

        if result:
            result = self.fit_web_quant(options)

        return result

    def after_clear_quant(self, options):
        history_no = options.get("history_no")
        if not history_no:
            self.error("none history_no")
        self.info(f"clean[{history_no}] begin")

        prc_info = options.get("prc_info")
        if prc_info:
            test_info_prc_file_path = prc_info.get("file_path")
            prc_info.update({"status": "cleared", "end_time": datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f")})

            with self.condition:
                with open(test_info_prc_file_path, mode="w", encoding="UTF-8") as f:
                    f.write(rapidjson.dumps(prc_info))
                self.condition.notify()

        try:
            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            clear_executor.execute("QuantDataClear.clean_simtest_data", paras=options)
            clear_executor.execute("QuantDataClear.clean_quant_data", paras=options)
        except Exception as e:
            self.error(f"clean[{history_no}] failed: error[{e}]")

        self.info(f"clean[{history_no}] finished")

    def start(self):
        pid = os.getpid()

        quant_home = self.options.get("quant_home")
        quant_home = PathUtils.get_real_path(quant_home)

        backup_home = self.options.get("backup_home")
        if backup_home:
            backup_home = PathUtils.get_real_path(backup_home)

        fair_count = self.options.get("fair_count", 1)
        blacklist = self.options.get("blacklist", [])

        while True:
            time.sleep(0.1)
            try:
                for investor_dir in os.listdir(quant_home):
                    if investor_dir in blacklist:
                        continue
                    investor_home = os.path.join(quant_home, investor_dir)
                    if os.path.isfile(investor_home):
                        continue

                    processing_count = 0
                    for test_dir in os.listdir(investor_home):
                        if processing_count >= fair_count:
                            break

                        quant_id = test_dir
                        test_home = os.path.join(investor_home, test_dir)
                        if os.path.isfile(test_home):
                            continue

                        test_info_file_path = os.path.join(test_home, "TestInfo.csv")
                        test_info_prc_file_path = os.path.join(test_home, ".prc")

                        if not os.path.exists(test_info_file_path):
                            continue

                        prc_info = None
                        if os.path.exists(test_info_prc_file_path):
                            with self.condition:
                                with open(test_info_prc_file_path) as prc_file:
                                    prc_info = rapidjson.load(prc_file)
                                self.condition.notify()
                            if prc_info:
                                prc_status = prc_info.get("status")
                                if prc_status == "cleared":
                                    if backup_home:
                                        if os.path.exists(test_home):
                                            backup_dir = os.path.join(backup_home, investor_dir)
                                            if not os.path.exists(backup_dir):
                                                os.makedirs(backup_dir)
                                            backup_path = os.path.join(backup_dir, test_dir)
                                            try:
                                                shutil.move(test_home, backup_path)
                                            except Exception as e:
                                                self.error(f"failed: move[{test_home}->{backup_path}] error: {e}")
                                    continue
                                elif prc_status == "clearing" and pid == prc_info.get("pid"):
                                    continue

                        file_encoding = "UTF-8"
                        test_completed = False
                        try:
                            try:
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding, dtype="object")
                            except Exception as e:
                                file_encoding = "GB18030"
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding, dtype="object")
                            test_end_date = test_info_data.iloc[0]["TestEndDate"]
                            test_end_time = test_info_data.iloc[0]["TestEndTime"]
                            if not isinstance(test_end_date, float) and not isinstance(test_end_time, float) and len(test_end_date) == 8 and len(test_end_time) == 8:
                                test_completed = True
                        except Exception as e:
                            self.error(f"failed: load[{test_info_file_path}] error: {e}")

                        if not test_completed:
                            continue

                        processing_count += 1
                        history_no = self.get_history_no(self.options)
                        options = self.options.copy()

                        prc_info = {"history_no": history_no, "quant_id": quant_id, "pid": pid, "file_encoding": file_encoding, "file_path": test_info_prc_file_path, "status": "clearing", "begin_time": datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f"), "old_prc_info": prc_info}
                        options.update({"history_no": history_no, "quant_id": quant_id, "data_home": test_home, "file_encoding": file_encoding, "prc_info": prc_info})

                        with open(test_info_prc_file_path, mode="w", encoding="UTF-8") as f:
                            f.write(rapidjson.dumps(prc_info))

                        self.info(f"deal [{history_no}]->[{test_home}]")

                        # self.fork_matter(id=history_no, target=self.clear_quant, options=options, callback=self.after_clear_quant)
                        self.clear_quant(options)
                        self.after_clear_quant(options)

            except Exception as e:
                self.error(e)

@click.command()
@click.option('--env', required=True)
@click.option('--config', required=True)
@click.option('--run_id', required=False, default=1)
def start(env, config, run_id):
    AppContext.load("./config/simrun_context.json", env)

    LoggerUtils.load_loggers(AppContext.get_config_path("loggers.json"))
    EasyDBExecutorUtils.load_executors(AppContext.get_config_path("dbexecutors.json"))
    DataSourceUtils.load_datasources(AppContext.get_config_path("datasources.json"))
    EasyHostsUtils.load_hosts(AppContext.get_config_path("hosts.json"))

    service_config_path = AppContext.get_config_path(config)

    service_player = QuantServicePlayer(config=service_config_path)
    service_player.start()

if __name__ == "__main__":
    start()
