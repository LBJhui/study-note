# _*_ coding: utf-8 _*_
# @Time: 2024/8/12 16:11
# @Author: LBJ辉
# @File: manual_quant_service_player
# @Project: nxops_quant
import os
import time
import warnings

import click
import pandas

warnings.filterwarnings("ignore")
from sqlalchemy import create_engine

from nxpy.context import AppContext
from nxpy.log.logger import LoggerUtils
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutor, EasyDBExecutorUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.os.path import PathUtils
from nxpy.config.easy_config import EasyConfigUtils
from simrun.quant.quant_service_player import QuantServicePlayer


def set_exchange_id(df):
    first_char = str(df["SecurityID"])[0:1]
    if first_char == "6":
        return "1"
    elif first_char == "0" or first_char == "3":
        return "2"
    elif first_char == "4" or first_char == "8":
        return "4"
    else:
        return "0"


class ManualQuantServicePlayer(QuantServicePlayer):
    def __init__(self, options={}, config=None):
        super().__init__(options=options, config=config)

    def get_history_no(self, options):
        executor = EasyDBExecutorUtils.get_executor(**options)

        error, exec_result = executor.execute("QuantDataClear.get_history_no", paras=options)
        if error:
            self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
            return None

        return exec_result[0][0][0]

    def deal_manual_quant_data(self, options):
        history_no = options.get("history_no")
        if not history_no:
            self.error("failed: none history_no")
            return False

        manual_id = options.get("manual_id")
        if not manual_id:
            self.error("deal[{history_no}] failed: none manual_id")
            return False

        self.info(f"deal[{manual_id}][{history_no}] begin")

        manual_home = options.get("manual_home")
        manual_home = PathUtils.get_real_path(EasyConfigUtils.easy_parse(manual_home, options))

        try:
            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            clear_executor.execute("QuantDataClear.clean_simtest_data", paras=options)

            executor = EasyDBExecutorUtils.get_executor(**options)

            error, manual_quant_info = executor.queryone("QuantDataClear.get_manual_quant_info", paras=options)
            if error:
                self.error(f"deal[{manual_id}][{history_no}] failed: get_manual_quant_info error: [code={error['code']}, msg={error['msg']}]")
                return False

            if len(manual_quant_info) == 0 or len(manual_quant_info[0]) == 0:
                self.error(f"deal[{manual_id}][{history_no}] failed: get_manual_quant_info error: none manual info")
                return False

            error, exec_result = executor.execute("QuantDataClear.clean_quant_history", paras=options)
            if error:
                self.error(f"deal[{manual_id}][{history_no}] failed: clean_quant_history error: [code={error['code']}, msg={error['msg']}]")
                return False

            row = manual_quant_info[0]
            quant_info = options.copy()
            quant_info.update({"manual_id": row[0], "test_data_status": "0", "test_data_file_status": "0", "test_investor_id": row[1], "test_user_id": row[2], "strategy_name": row[3], "test_date": row[4], "test_time": row[5],
                               "test_trade_date_begin": row[6], "test_trade_date_end": row[7], "test_trade_days": row[8], "test_kind": row[9], "init_asset": row[10],
                               "trade_file_path": row[11], "pos_file_path": row[12]})

            mysql_config = clear_executor.get_datasource().settings
            mysql_url = "mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (mysql_config["user"], mysql_config["password"], mysql_config["host"], str(mysql_config.get("port", 3306)))
            mysql_engine = create_engine(mysql_url, pool_pre_ping=True, pool_recycle=600, execution_options={"autocommit": False})

            with mysql_engine.connect() as connection:
                with connection.begin():
                    init_position_file = quant_info.get("pos_file_path")
                    if init_position_file:
                        init_position_file = init_position_file.replace("/quant/tradelist/", "")
                        init_position_file = os.path.join(manual_home, init_position_file)
                        if os.path.exists(init_position_file):
                            init_position_data = pandas.read_csv(init_position_file, dtype="object")
                            init_position_data["HistoryNo"] = history_no
                            init_position_data["ExchangeID"] = init_position_data.apply(lambda x: set_exchange_id(x), axis=1)
                            init_position_data["SecurityValue"] = 0
                            init_position_data["PosiDirection"] = "2"
                            init_position_data["SecurityKind"] = "s"
                            init_position_data["ExchSecurityID"] = None
                            init_position_data.to_sql(name="t_SimTestInitPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_trade_detail_file = quant_info.get("trade_file_path")
                    if not spot_trade_detail_file:
                        self.error(f"deal[{manual_id}][{history_no}] failed: trade file is none")
                        return False

                    spot_trade_detail_file = spot_trade_detail_file.replace("/quant/tradelist/", "")
                    spot_trade_detail_file = os.path.join(manual_home, spot_trade_detail_file)
                    if not os.path.exists(spot_trade_detail_file):
                        self.error(f"deal[{manual_id}][{history_no}] failed: trade file is not exist")
                        return False

                    spot_trade_detail_data = pandas.read_csv(spot_trade_detail_file, dtype="object")
                    spot_trade_detail_data["HistoryNo"] = history_no
                    spot_trade_detail_data["TradeDay"] = spot_trade_detail_data["TradingDay"]
                    spot_trade_detail_data["ExchangeID"] = spot_trade_detail_data.apply(lambda x: set_exchange_id(x), axis=1)
                    spot_trade_detail_data["TotalPosCost"] = 0
                    spot_trade_detail_data["CommissionFee"] = 0
                    spot_trade_detail_data["OrderLocalID"] = spot_trade_detail_data["OrderSysID"]
                    spot_trade_detail_data = spot_trade_detail_data[["HistoryNo", "TradingDay", "TradeID", "TradeDay", "TradeTime", "ExchangeID", "SecurityID", "Direction", "Volume", "TradePrice", "TotalPosCost", "CommissionFee", "OrderLocalID", "OrderSysID"]]
                    spot_trade_detail_data.to_sql(name="t_SimTestSpotTradeDetail", con=connection, if_exists='append', index=False, chunksize=10000)

            error, exec_result = clear_executor.execute("QuantDataClear.deal_manual_quant_data", paras=quant_info)
            if error:
                self.error(f"deal[{manual_id}][{history_no}] failed: deal_manual_quant_data error: [code={error['code']}, msg={error['msg']}]")
                return False

        except Exception as e:
            self.error(f"deal[{manual_id}][{history_no}] failed: deal_manual_quant_data error: {e}")
            return False

        self.info(f"deal[{manual_id}][{history_no}] finished")

        return True

    def clear_manual_quant(self, options):
        result = self.deal_manual_quant_data(options)

        if result:
            result = self.deal_quant_data(options)

        if result:
            result = self.fit_web_quant(options)

        if result:
            options.update({"manual_data_status": "1"})
        else:
            options.update({"manual_data_status": "2"})

        return result

    def after_clear_quant(self, options):
        history_no = options.get("history_no")
        manual_id = options.get("manual_id")

        self.info(f"closeout[{manual_id}][{history_no}] begin")

        try:
            executor = EasyDBExecutorUtils.get_executor(**options)
            error, exec_result = executor.execute("QuantDataClear.set_manual_quant_clearing", paras=options)
            if error:
                self.error(f"closeout[{manual_id}][{history_no}] failed: error: [code={error['code']}, msg={error['msg']}]")
                return False
        except Exception as e:
            self.error(f"closeout[{manual_id}][{history_no}] failed: error: {e}")

        self.info(f"closeout[{manual_id}][{history_no}] finished")

        super().after_clear_quant(options)
        return True

    def start(self):
        pid = os.getpid()
        executor = EasyDBExecutorUtils.get_executor(**self.options)
        while True:
            time.sleep(3)
            try:
                error, manual_quant_ids = executor.querylist("QuantDataClear.get_manual_quants", paras={})
                if error:
                    self.error(f"failed: get_manual_quants error: {error}")
                    continue

                if len(manual_quant_ids) > 0 and len(manual_quant_ids[0]) > 0:
                    for manual_id in manual_quant_ids[0][0]:
                        options = self.options.copy()

                        history_no = self.get_history_no(self.options)
                        options.update({"history_no": history_no, "manual_id": manual_id, "manual_data_status": "6"})

                        error, exec_result = executor.execute("QuantDataClear.set_manual_quant_clearing", paras=options)
                        if error:
                            self.error(f"failed: set_manual_quant_clearing error: {error}")
                            continue

                        # self.fork_matter(id=history_no, target=self.clear_manual_quant, options=options, callback=self.after_clear_quant)
                        self.clear_manual_quant(options)
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

    service_player = ManualQuantServicePlayer(config=service_config_path)
    service_player.start()


if __name__ == "__main__":
    start()
