# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 14:32
# @Author: LBJ辉
# @File: future_quant_service_player
# @Project: python
import datetime
import os
import threading
import time

import click
import pandas
import rapidjson

from nxpy.context import AppContext
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutorUtils
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

    def start(self):
        pid = os.getpid()
        quant_home = self.options.get("quant_home")  # ./media/yimt/e/temp/futurequant/out
        quant_home = PathUtils.get_real_path(quant_home)  # ./media/yimt/e/temp/futurequant/out
        backup_home = self.options.get("backup_home")  # ./media/yimt/e/temp/futurequant/backup
        if backup_home:
            backup_home = PathUtils.get_real_path(backup_home)

        while True:
            time.sleep(3)

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
            for invester_dir in os.listdir(quant_home):
                investor_home = os.path.join(quant_home, invester_dir)
                if os.path.isfile(investor_home):
                    continue
                for test_dir in os.listdir(investor_home):
                    quant_id = test_dir
                    test_home = os.path.join(investor_home, test_dir)
                    if os.path.isfile(test_home):
                        continue

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
                            print(prc_info)
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
