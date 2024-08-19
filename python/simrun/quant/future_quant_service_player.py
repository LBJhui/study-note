# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 14:32
# @Author: LBJ辉
# @File: future_quant_service_player
# @Project: python
import datetime
import os
import shutil
import threading
import time
from urllib.parse import quote

import click
import pandas
import rapidjson
from sqlalchemy import create_engine

from nxpy.config.easy_config import EasyConfigUtils
from nxpy.context import AppContext
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutorUtils, EasyDBExecutor
from nxpy.log.logger import LoggerUtils
from nxpy.os.path import PathUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.service.service_player import ServicePlayer


def print_object(obj):
    for key, value in vars(obj).items():
        print(f"{key} = {value}")


class QuantServicePlayer_Future(ServicePlayer):
    def __init__(self, options={}, config=None):
        super().__init__(options=options, config=config)  # 根据config路径，内容赋值给 options
        self.condition = threading.Condition()
        """
        options = {
            'service_id': 'quant_clearer', 
            'clear_executor_id': 'simrun', 
            'executor_id': 'simrun', 
            'web_host': 'quant_web', 
            'quant_home': './media/yimt/e/temp/futurequant/out', 
            'web_home': './media/yimt/e/temp/futurequant/web', 
            'remote_quant_mid_home': './media/yimt/e/temp/futurequant/mid', 
            'remote_web_result_home': '${HOME}/simtrade_upload/quant', 
            'temp_home': './media/yimt/e/temp/futurequant/temp', 
            'backup_home': './media/yimt/e/temp/futurequant/backup', 
            'bench_ids': "'000001.SH', '000016.SH', '000300.SH', '000905.SH', '399006.SZ'"
        }
        config = ./config/simrun\quant\future_service_quant.json
        matters = []
        service_id = quant_clearer
        condition = <Condition(<unlocked _thread.RLock object owner=0 count=0 at 0x000002393BB85780>, 0)>
        """

    def get_history_no(self, options):
        executor = EasyDBExecutorUtils.get_executor(**options)
        error, exec_result = executor.execute("QuantDataClear.get_history_no", paras=options)

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
            clear_executor.execute("QuantDataClear.clean_future_simtest_data", paras=options)  # 清空数据控中 history_no 相关数据

            mysql_config = clear_executor.get_datasource().settings
            mysql_url = f"mysql+mysqlconnector://%s:%s@%s:%s/quant?charset=utf8" % (mysql_config["user"], quote(mysql_config["password"]), mysql_config["host"], str(mysql_config.get("port", 3306)))
            mysql_engine = create_engine(mysql_url, execution_options={"autocommit": False})

            with mysql_engine.connect() as connection:
                with connection.begin():
                    simtest_info_file = os.path.join(data_home, "SimTestInfo.csv")  # 回测概要信息文件
                    if os.path.exists(simtest_info_file):
                        simtest_info_data = pandas.read_csv(simtest_info_file, encoding=file_encoding, dtype="object")
                        simtest_info_data["QuantID"] = options.get("quant_id")
                        simtest_info_data["HistoryNo"] = history_no
                        simtest_info_data["UserID"] = simtest_info_data["InvestorID"]
                        simtest_info_data["MDFrequency"] = "Ticker"
                        simtest_info_data.to_sql(name="t_Future_SimTestInfo", con=connection, if_exists='append', index=False, chunksize=10000)

                    init_position_file = os.path.join(data_home, "SimTestInitalPosition.csv")  # 初始持仓文件
                    if os.path.exists(init_position_file):
                        init_position_data = pandas.read_csv(init_position_file, encoding=file_encoding, dtype="object")
                        init_position_data["HistoryNo"] = history_no
                        init_position_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        init_position_data.to_sql(name="t_Future_SimTestInitPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_trade_file = os.path.join(data_home, "SimTestFutureTrade.csv")  # 期货成交明细文件
                    if os.path.exists(spot_trade_file):
                        spot_trade_data = pandas.read_csv(spot_trade_file, encoding=file_encoding, dtype="object")
                        spot_trade_data["HistoryNo"] = history_no
                        spot_trade_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_trade_data.to_sql(name="t_Future_SimTestTrade", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_order_file = os.path.join(data_home, "SimTestFutureOrder.csv")  # 期货报单明细文件
                    if os.path.exists(spot_order_file):
                        spot_order_data = pandas.read_csv(spot_order_file, encoding=file_encoding, dtype="object")
                        spot_order_data["HistoryNo"] = history_no
                        spot_order_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_order_data.to_sql(name="t_Future_SimTestOrder", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_position_file = os.path.join(data_home, "SimTestFuturePosition.csv")  # 期货综合持仓文件
                    if os.path.exists(spot_position_file):
                        spot_position_data = pandas.read_csv(spot_position_file, encoding=file_encoding, dtype="object")
                        spot_position_data["HistoryNo"] = history_no
                        spot_position_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_position_data.to_sql(name="t_Future_SimTestPosition", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_position_detail_file = os.path.join(data_home, "SimTestFuturePositionDetail.csv")  # 期货持仓明细文件
                    if os.path.exists(spot_position_detail_file):
                        spot_position_detail_data = pandas.read_csv(spot_position_detail_file, encoding=file_encoding, dtype="object")
                        spot_position_detail_data["HistoryNo"] = history_no
                        spot_position_detail_data.rename(columns={"VolumeMutiple": "VolumeMultiple"}, inplace=True)
                        spot_position_detail_data.to_sql(name="t_Future_SimTestPositionDetail", con=connection, if_exists='append', index=False, chunksize=10000)

                    sub_md_file = os.path.join(data_home, "SimTestSubMD.csv")  # 行情订阅明细文件
                    if os.path.exists(sub_md_file):
                        sub_md_data = pandas.read_csv(sub_md_file, encoding=file_encoding, dtype="object")
                        sub_md_data["HistoryNo"] = history_no
                        if "VolumeMultiple" in sub_md_data.columns:
                            sub_md_data.drop("VolumeMultiple", axis=1, inplace=True)
                        if "VolumeMutiple" in sub_md_data.columns:
                            sub_md_data.drop("VolumeMutiple", axis=1, inplace=True)
                        sub_md_data.to_sql(name="t_Future_SimTestSubMD", con=connection, if_exists='append', index=False, chunksize=10000)

                    spot_asset_file = os.path.join(data_home, "SimTestTradingAccount.csv")  # 资金账户明细文件
                    if os.path.exists(spot_asset_file):
                        spot_asset_data = pandas.read_csv(spot_asset_file, encoding=file_encoding, dtype="object")
                        spot_asset_data["HistoryNo"] = history_no
                        spot_asset_data.to_sql(name="t_Future_SimTestTradingAccount", con=connection, if_exists='append', index=False, chunksize=10000)
        except Exception as e:
            self.error(f"dump[{history_no}] failed: error: [{e}]")
            return False
        return True

    def deal_quant_data(self, options):
        history_no = options.get('history_no')
        if not history_no:
            self.error('none history_no')
            return False

        self.info(f"deal[{history_no}] begin")

        try:
            executor = EasyDBExecutorUtils.get_executor(**options)

            clear_executor_id = options.get("clear_executor_id")
            clear_executor = EasyDBExecutor.get_executor(clear_executor_id)

            parameters = {"history_no": history_no}

            error, exec_result = clear_executor.execute("QuantDataClear.deal_future_quant_data", paras=parameters)
            ##############################################
        except Exception as e:
            self.error(f"deal[{history_no}] failed: error: [{e}]")
            return False

        self.info(f"deal[{history_no}] finished")
        return True

    def clear_quant(self, options):
        result = self.dump_quant_data(options)

        if result:
            result = self.deal_quant_data(options)
        #
        # if result:
        #     result = self.fit_web_quant(options)

        return result

    def start(self):
        pid = os.getpid()
        quant_home = self.options.get("quant_home")  # ./media/yimt/e/temp/futurequant/out
        quant_home = PathUtils.get_real_path(quant_home)  # ./media/yimt/e/temp/futurequant/out
        backup_home = self.options.get("backup_home")  # ./media/yimt/e/temp/futurequant/backup
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

                        # SimTestInfo.csv（回测概要信息文件）
                        test_info_file_path = os.path.join(test_home, 'SimTestInfo.csv')  # /media/yimt/e/temp/futurequant/out\00030675\20211120225021\SimTestInfo.csv
                        test_info_prc_file_path = os.path.join(test_home, '.prc')  # ./media/yimt/e/temp/futurequant/out\00030675\20211120225021\.prc

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
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding, dtype='object')
                            except Exception as e:
                                file_encoding = 'GB18030'
                                test_info_data = pandas.read_csv(test_info_file_path, encoding=file_encoding, dtype='object')
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
    # _context = {'base_home': '.', 'config_home': './config/simrun', 'env_id': 'quant'}
    LoggerUtils.load_loggers(AppContext.get_config_path("loggers.json"))
    # wande是每天从万得库拿行情用的，simrun就是业务数据库，mem是内存数据库，为了提升性能，生产的各种数据处理是在memsql执行的，最后把结果落到mysql
    EasyDBExecutorUtils.load_executors(AppContext.get_config_path("dbexecutors.json"))
    DataSourceUtils.load_datasources(AppContext.get_config_path("datasources.json"))
    EasyHostsUtils.load_hosts(AppContext.get_config_path("hosts.json"))

    service_config_path = AppContext.get_config_path(config)

    service_player = QuantServicePlayer_Future(config=service_config_path)
    service_player.start()


if __name__ == '__main__':
    start()
