# _*_ coding: utf-8 _*_
# @Time: 2024/8/5 16:27
# @Author: LBJ辉
# @File: future_quant_service_player
# @Project: nxops-quant
# 期货
import datetime
import os
import shutil
import sqlite3
import threading
import time
from urllib.parse import quote

import click
import pandas
import rapidjson
from nxpy.config.easy_config import EasyConfigUtils
from nxpy.context import AppContext
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutor, EasyDBExecutorUtils
from nxpy.log.logger import LoggerUtils
from nxpy.os.path import PathUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.rsh.easy_rsh import EasyRSH
from nxpy.service.service_player import ServicePlayer
from pandas.io import sql as pandas_sql
from sqlalchemy import create_engine


def print_object(obj):
    for key, value in vars(obj).items():
        print(f"{key} = {value}")


class QuantServicePlayer_Future(ServicePlayer):
    def __init__(self, options={}, config=None):
        super().__init__(options=options, config=config)
        self.condition = threading.Condition()

    def get_history_no(self, options):
        excutor = EasyDBExecutorUtils.get_executor(**options)

        error, exec_result = excutor.execute("QuantDataClear.get_history_no", paras=options)
        if error:
            self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
            return None
        return exec_result[0][0][0]

    def dump_quant_data(self, options):
        history_no = options.get('history_no')
        if not history_no:
            self.error('none history_no')
            return False

        data_home = options.get('data_home')
        data_home = PathUtils.get_real_path(EasyConfigUtils.easy_parse(data_home, options))

        file_encoding = options.get('file_encoding')

        try:
            clear_executor_id = options.get('clear_executor_id')
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)
            clear_executor.execute("QuantDataClear.clean_future_simtest_data", paras=options)

            mysql_config = clear_executor.get_datasource().settings
            mysql_url = f"mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (
                mysql_config["user"], quote(mysql_config["password"]), mysql_config["host"],
                str(mysql_config.get("port", 3306)))
            mysql_engine = create_engine(mysql_url, execution_options={"autocommit": False})

            with mysql_engine.connect() as connection:
                with connection.begin():
                    simtest_info_file = os.path.join(data_home, "SimTestInfo.csv")
                    if os.path.exists(simtest_info_file):
                        simtest_info_data = pandas.read_csv(simtest_info_file, encoding=file_encoding, dtype="object")
                        simtest_info_data["QuantID"] = options.get("quant_id")
                        simtest_info_data["HistoryNo"] = history_no
                        simtest_info_data["UserID"] = simtest_info_data["InvestorID"]
                        simtest_info_data["MDFrequency"] = "Ticker"
                        simtest_info_data.to_sql(name="t_Future_SimTestInfo", con=connection, if_exists='append',
                                                 index=False, chunksize=10000)

                    init_position_file = os.path.join(data_home, "SimTestInitalPosition.csv")
                    if os.path.exists(init_position_file):
                        init_position_data = pandas.read_csv(init_position_file, encoding=file_encoding, dtype="object")
                        init_position_data["HistoryNo"] = history_no
                        init_position_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        init_position_data.to_sql(name="t_Future_SimTestInitPosition", con=connection,
                                                  if_exists='append', index=False, chunksize=10000)

                    spot_trade_file = os.path.join(data_home, "SimTestFutureTrade.csv")
                    if os.path.exists(spot_trade_file):
                        spot_trade_data = pandas.read_csv(spot_trade_file, encoding=file_encoding, dtype="object")
                        spot_trade_data["HistoryNo"] = history_no
                        spot_trade_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_trade_data.to_sql(name="t_Future_SimTestTrade", con=connection, if_exists='append',index=False, chunksize=10000)

                    spot_order_file = os.path.join(data_home, "SimTestFutureOrder.csv")
                    if os.path.exists(spot_order_file):
                        spot_order_data = pandas.read_csv(spot_order_file, encoding=file_encoding, dtype="object")
                        spot_order_data["HistoryNo"] = history_no
                        spot_order_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_order_data.to_sql(name="t_Future_SimTestOrder", con=connection, if_exists='append',index=False, chunksize=10000)

                    spot_position_file = os.path.join(data_home, "SimTestFuturePosition.csv")
                    if os.path.exists(spot_position_file):
                        spot_position_data = pandas.read_csv(spot_position_file, encoding=file_encoding, dtype="object")
                        spot_position_data["HistoryNo"] = history_no
                        spot_position_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_position_data.to_sql(name="t_Future_SimTestPosition", con=connection, if_exists='append',
                                                  index=False, chunksize=10000)

                    spot_position_detail_file = os.path.join(data_home, "SimTestFuturePositionDetail.csv")
                    if os.path.exists(spot_position_detail_file):
                        spot_position_detail_data = pandas.read_csv(spot_position_detail_file, encoding=file_encoding,dtype="object")
                        spot_position_detail_data["HistoryNo"] = history_no
                        spot_position_detail_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_position_detail_data.to_sql(name="t_Future_SimTestPositionDetail", con=connection,if_exists='append', index=False, chunksize=10000)

                    sub_md_file = os.path.join(data_home, "SimTestSubMD.csv")
                    if os.path.exists(sub_md_file):
                        sub_md_data = pandas.read_csv(sub_md_file, encoding=file_encoding, dtype="object")
                        sub_md_data["HistoryNo"] = history_no
                        if "VolumeMultiple" in sub_md_data.columns:
                            sub_md_data.drop("VolumeMultiple", axis=1, inplace=True)
                        if "VolumeMutiple" in sub_md_data.columns:
                            sub_md_data.drop("VolumeMutiple", axis=1, inplace=True)
                        sub_md_data.to_sql(name="t_Future_SimTestSubMD", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_asset_file = os.path.join(data_home, "SimTestTradingAccount.csv")
                    if os.path.exists(spot_asset_file):
                        spot_asset_data = pandas.read_csv(spot_asset_file, encoding=file_encoding, dtype="object")
                        spot_asset_data["HistoryNo"] = history_no
                        spot_asset_data.to_sql(name="t_Future_SimTestTradingAccount", con=connection,
                                               if_exists='append', index=False, chunksize=10000)
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

            error, exec_result = clear_executor.execute("QuantDataClear.deal_future_quant_data", paras=parameters)
            if error:
                self.error(f"deal[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False
            else:
                mysql_config = executor.get_datasource().settings
                mysql_url = "mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (mysql_config["user"], quote(mysql_config["password"]), mysql_config["host"], str(mysql_config.get("port", 3306)))
                mysql_engine = create_engine(mysql_url, pool_pre_ping=True, pool_recycle=600, execution_options={"autocommit": False})

                with mysql_engine.connect() as connection:
                    with connection.begin():
                        error, test_profit_data = clear_executor.pandas_query("QuantDataClear.get_future_quant_test_profit", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_future_quant_test_profit error: [code={error['code']}, msg={error['msg']}]")
                            return False
                        test_profit_data.to_sql(name="t_ClientQuantTestProfit", con=connection, if_exists='append', index=False, chunksize=10000)

                        error, bench_profit_data = clear_executor.pandas_query("QuantDataClear.get_future_quant_bench_profit", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_future_quant_bench_profit error: [code={error['code']}, msg={error['msg']}]")
                            return False
                        bench_profit_data.to_sql(name="t_QuantTestBenchmarkProfit", con=connection, if_exists='append', index=False, chunksize=10000)

                        error, test_info_data = clear_executor.pandas_query("QuantDataClear.get_future_quant_test_info", options)
                        if error:
                            self.error(f"deal[{history_no}] failed: get_future_quant_test_info error: [code={error['code']}, msg={error['msg']}]")
                            return False

                error, quant_market = clear_executor.querylist("QuantDataClear.get_quant_test_market", paras=options)
                if error:
                    self.error(f"deal[{history_no}] failed: get_quant_test_market error: [code={error['code']}, msg={error['msg']}]")
                    return False

                batch_paras = []
                if quant_market and len(quant_market) > 0 and quant_market[0] and len(quant_market[0]) > 0:
                    batch_paras = [{"quant_market": row[0]} for row in quant_market[0]]

                error, quant_history = clear_executor.queryone("QuantDataClear.get_future_quant_test_history", paras=options)
                if error:
                    self.error(f"deal[{history_no}] failed: get_future_quant_test_history error: [code={error['code']}, msg={error['msg']}]")
                    return False

                init_asset = 0
                total_asset = 0
                test_trade_days = 0
                if quant_history and len(quant_history) > 0 and quant_history[0] and len(quant_history[0]) > 0:
                    init_asset = quant_history[0][0]
                    total_asset = quant_history[0][1]
                    test_trade_days = quant_history[0][2]

                error, exec_result = executor.execute("QuantDataClear.save_future_quant_history", paras=dict(options, test_data_status="0", test_data_file_status="0", init_asset=init_asset, total_asset=total_asset, test_trade_days=test_trade_days), batch_paras=batch_paras)
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
            error, quant_orders = clear_executor.pandas_query("QuantDataClear.get_future_quant_orders", parameters)
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

            future_quant_orders_groups = quant_orders.groupby("InstrumentID")
            for group_instrument_id, future_quant_orders in future_quant_orders_groups:
                future_quant_orders = future_quant_orders.sort_values(["TradingDay", "OrderSysID"])
                order_file_name = f"order_{group_instrument_id}.csv"
                order_file_path = os.path.join(history_home, order_file_name)
                future_quant_orders.to_csv(order_file_path, index=False, chunksize=10000)

            error, quant_trades = clear_executor.pandas_query("QuantDataClear.get_future_quant_trades", parameters)
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

            future_quant_trades_groups = quant_trades.groupby("InstrumentID")
            for group_instrument_id, future_quant_trades in future_quant_trades_groups:
                future_quant_trades = future_quant_trades.sort_values(["TradingDay", "TradeID"])
                trade_file_name = f"trade_{group_instrument_id}.csv"
                trade_file_path = os.path.join(history_home, trade_file_name)
                future_quant_trades.to_csv(trade_file_path, index=False, chunksize=10000)

            error, quant_assets = clear_executor.pandas_query("QuantDataClear.get_future_quant_assets", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            asset_file_path = os.path.join(history_home, "ammout.csv")
            quant_assets.to_csv(asset_file_path, index=False, chunksize=10000)

            error, quant_positions = clear_executor.pandas_query("QuantDataClear.get_future_quant_positions", parameters)
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

            error, quant_profits = clear_executor.pandas_query("QuantDataClear.get_future_quant_profits", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            profit_file_path = os.path.join(history_home, "profit.csv")
            quant_profits.to_csv(profit_file_path, index=False, chunksize=10000)

            error, quant_summary = clear_executor.pandas_query("QuantDataClear.get_future_quant_month_summary", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            summary_file_path = os.path.join(history_home, "month_summary.csv")
            quant_summary.to_csv(summary_file_path, index=False, chunksize=10000)

            error, quant_benches = clear_executor.pandas_query("QuantDataClear.get_future_quant_benches", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            bench_file_path = os.path.join(history_home, "comb_bench.csv")
            quant_benches.to_csv(bench_file_path, index=False, chunksize=10000)

            error, quant_submds = clear_executor.pandas_query("QuantDataClear.get_future_quant_submds", parameters)
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

            sql = """CREATE TABLE position(TradingDay int,InstrumentID text,InstrumentName text,PosiDirection text,HedgeFlag text,Position int,SettlementPrice real,TotalPosCost real,OpenPosCost real,Margin real,TradingFee real,Profit real,YdPosition int,TodayProfit real, TodayBuyCapital real, TodaySellCapital real, BuyCapital real, SellCapital real, ReturnRatio real, ContributionRatio real,LastSettlementPrice real)"""
            sqlite_cursor.execute(sql)
            sql = """CREATE UNIQUE INDEX IDX_Position_TradingDay_InstrumentID_PosiDirection_HedgeFlag ON position(TradingDay ASC,InstrumentID ASC, PosiDirection ASC, HedgeFlag ASC)"""
            sqlite_cursor.execute(sql)
            sql = """CREATE TABLE dkmd(TradingDay int,InstrumentID text,LastClosingPrice real,OpeningPrice real,ClosingPrice real,TopPrice real,FloorPrice real,TradingVolume int,TradingAmount real,LongOpenPosCost real,ShortOpenPosCost real,LongYdPosition int,ShortYdPosition int)"""
            sqlite_cursor.execute(sql)
            sql = "CREATE UNIQUE INDEX IDX_dkmd_TradingDay_InstrumentID ON dkmd(TradingDay ASC,InstrumentID ASC)"
            sqlite_cursor.execute(sql)

            sqlite_cursor.close()

            error, quant_db_positions = clear_executor.pandas_query("QuantDataClear.get_future_quant_db_positions", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            pandas_sql.to_sql(quant_db_positions, name='position', con=sqlite_conn, if_exists='append', index=False, chunksize=10000)

            error, quant_instruments = clear_executor.querylist("QuantDataClear.get_quant_sub_instruments", parameters)
            if error:
                self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                return False

            if quant_instruments and quant_instruments[0]:
                i_parameters = parameters.copy()
                for exchange_id, instrument_id in quant_instruments[0]:
                    i_parameters.update({"exchange_id": exchange_id, "instrument_id": instrument_id})
                    error, quant_dkmds = clear_executor.pandas_query("QuantDataClear.get_quant_future_dkmds", i_parameters)
                    if error:
                        self.error(f"fit[{history_no}] failed: [code={error['code']}, msg={error['msg']}]")
                        return False

                    if len(quant_dkmds):
                        full_instrument_id = quant_dkmds['InstrumentID'].values[0]
                        dkmd_file_name = f"dk_{full_instrument_id}.csv"
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
                print(1)
                web_host_id = options.get("web_host")
                print(web_host_id)
                web_host_config = EasyHostsUtils.get_host(web_host_id)
                print(web_host_config)
                web_host_ssh = EasyRSH(use_sftp=False)
                web_host_ssh.connect_s(web_host_config)

                remote_quant_mid_home = options.get("remote_quant_mid_home")
                remote_web_result_home = options.get("remote_web_result_home")
                print(remote_web_result_home)
                move_command = f"mv -f {remote_quant_mid_home}/{history_no} {remote_web_result_home}"

                web_host_ssh.execute(move_command)

                web_host_ssh.disconnect()
            except Exception as e:
                self.error(f"fit[{history_no}] failed: execute[{move_command}] error: {e}")
                return False

        except Exception as e:
            print(2)
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

            clear_executor.execute("QuantDataClear.clean_future_simtest_data", paras=options)
            clear_executor.execute("QuantDataClear.clean_future_quant_data", paras=options)
        except Exception as e:
            self.error(f"clean[{history_no}] failed: error[{e}]")

        self.info(f"clean[{history_no}] finished")

    def start(self):
        """
        options = {
            'service_id': 'quant_clearer',
            'clear_executor_id': 'simrun',
            'executor_id': 'simrun',
            'web_host': 'quant_web',
            'quant_home': '/media/yimt/e/temp/futurequant/out',
            'web_home': '/media/yimt/e/temp/futurequant/web',
            'remote_quant_mid_home': '/media/yimt/e/temp/futurequant/mid',
            'remote_web_result_home': '${HOME}/simtrade_upload/quant',
            'temp_home': '/media/yimt/e/temp/futurequant/temp',
            'backup_home': '/media/yimt/e/temp/futurequant/backup',
            'bench_ids': "'000001.SH', '000016.SH', '000300.SH', '000905.SH', '399006.SZ'"
        }
        config = ./config/simrun\quant\future_service_quant.json
        matters = []
        service_id = quant_clearer
        condition = <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x000001597B9E8B40>, 0)>
        """

        # 获取当前进程的PID
        pid = os.getpid()
        quant_home = self.options.get("quant_home")
        quant_home = PathUtils.get_real_path(quant_home)
        backup_home = self.options.get("backup_home")
        if backup_home:
            backup_home = PathUtils.get_real_path(backup_home)

        while True:
            time.sleep(3)
            try:
                # os.listdir 用于列出指定目录下的所有文件和目录名，并将它们以列表（list）的形式返回。
                # 如果不指定目录，则默认列出当前工作目录下的所有文件和目录。
                '''
                目录结构
                quant_home
                    user_id
                        quant_id
                            csv
                '''
                # quant_home: 源数据目录
                for investor_dir in os.listdir(quant_home):
                    investor_home = os.path.join(quant_home, investor_dir)
                    if os.path.isfile(investor_home):
                        continue
                    for test_dir in os.listdir(investor_home):
                        quant_id = test_dir
                        test_home = os.path.join(investor_home, test_dir)
                        if os.path.isfile(test_home):
                            continue

                        test_info_file_path = os.path.join(test_home, 'SimTestInfo.csv')
                        # ./media/yimt/e/temp/futurequant/out\user_id\quant_id\SimTestInfo.csv
                        test_info_prc_file_path = os.path.join(test_home, '.prc')

                        if not os.path.exists(test_info_file_path):
                            continue

                        prc_info = None
                        if os.path.exists(test_info_prc_file_path):
                            """
                            在多线程编程中，可以使用 with 语句来自动管理锁的获取与释放。
                            import threading
                            lock = threading.Lock()
                            with lock:  
                                # 临界区代码
                                print("Critical section")
                            # 锁在这里自动释放
                            """
                            with self.condition:
                                with open(test_info_prc_file_path) as prc_file:
                                    prc_info = rapidjson.load(prc_file)
                                self.condition.notify()
                            if prc_info:
                                prc_status = prc_info.get('status')
                                if prc_status == 'cleared':
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
                                elif prc_status == 'clearing' and pid == prc_info.get('pid'):
                                    continue

                        file_encoding = 'UTF-8'
                        test_completed = False
                        try:
                            try:
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding,
                                                                 dtype='object')
                            except Exception as e:
                                file_encoding = 'GB18030'
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding,
                                                                 dtype='object')
                            test_end_time = test_info_data.iloc[0]['TestEndTime']
                            if not isinstance(test_end_time, float) and len(test_end_time) == 14:
                                test_completed = True
                        except Exception as e:
                            self.error(e)

                        if not test_completed:
                            continue

                        history_no = self.get_history_no(self.options)
                        options = self.options.copy()

                        prc_info = {"history_no": history_no, "quant_id": quant_id, "pid": pid,
                                    "file_encoding": file_encoding, "file_path": test_info_prc_file_path,
                                    "status": "clearing",
                                    "begin_time": datetime.datetime.now().strftime("%Y%m%d %H:%M:%S.%f"),
                                    "old_prc_info": prc_info}
                        options.update({"history_no": history_no, "quant_id": quant_id, "data_home": test_home,
                                        "file_encoding": file_encoding, "prc_info": prc_info})

                        with open(test_info_prc_file_path, mode="w", encoding="UTF-8") as f:
                            f.write(rapidjson.dumps(prc_info))

                        self.info(f"deal [{history_no}]->[{test_home}]")

                        self.clear_quant(options)
            except Exception as e:
                self.error(e)


@click.command()
@click.option('--env', required=True)
@click.option('--config', required=True)
@click.option('--run_id', required=False, default=1)
def start(env, config, run_id):
    AppContext.load("./config/simrun_context.json", env)

    # 日志
    # AppContext.get_config_path("loggers.json"): ./config/simrun\quant\loggers.json
    LoggerUtils.load_loggers(AppContext.get_config_path("loggers.json"))

    # 数据库相关
    # wande是每天从万得库拿行情用的，simrun就是业务数据库，mem是内存数据库，为了提升性能，生产的各种数据处理是在memsql执行的，最后把结果落到mysql
    EasyDBExecutorUtils.load_executors(AppContext.get_config_path("dbexecutors.json"))
    DataSourceUtils.load_datasources(AppContext.get_config_path("datasources.json"))
    EasyHostsUtils.load_hosts(AppContext.get_config_path("hosts.json"))

    service_config_path = AppContext.get_config_path(config)

    service_player = QuantServicePlayer_Future(config=service_config_path)
    service_player.start()


if __name__ == "__main__":
    start()
