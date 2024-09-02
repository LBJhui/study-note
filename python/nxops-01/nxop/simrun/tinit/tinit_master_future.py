# _*_ coding: utf-8 _*_
# @Time: 2024/4/17 11:15
# @Author: LBJ辉
# @File: tinit_master_future
# @Project: nxops-01
import time

import click
from nxpy.context import AppContext
from nxpy.db.datasource import DataSourceUtils
from nxpy.db.executor import EasyDBExecutorUtils
from nxpy.log.logger import LoggerUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.task.task_processes import TaskProcesses
from nxpy.task.task_worker import TaskWorker


class SimRun_TinitMaster(TaskWorker):
    def __init__(self):
        super().__init__()

    def deal(self, kwargs):
        task_id = f"{kwargs['env_id']}-tinit-future"
        current_time = time.strftime("%Y%m%d", time.localtime())
        run_id = f"{current_time}#{kwargs['run_id']}"
        options = dict(kwargs, taskID=task_id, runID=run_id)

        task_processes = TaskProcesses(processes="tinit/task_processes_future.json", options=options)
        task_processes.startup()


@click.command()
@click.option('--env', required=True)
@click.option('--run_id', required=False, default=1)
@click.option('--trading_day', required=False)
@click.option('--nature_day', required=False)
def start(env, run_id, trading_day, nature_day):
    # 配置 config 文件入口，并且传入 env 变量，之后可在 json 文件路径中拼接 env 变量
    AppContext.load("./config/simrun_context.json", env)
    # 加载 logger 插件
    LoggerUtils.load_loggers(AppContext.get_config_path("loggers.json"))
    # 加载数据库模块
    EasyDBExecutorUtils.load_executors(AppContext.get_config_path("dbexecutors.json"))
    # 连接数据库
    DataSourceUtils.load_datasources(AppContext.get_config_path("datasources.json"))
    EasyHostsUtils.load_hosts(AppContext.get_config_path("hosts.json"))

    SimRun_TinitMaster().deal(dict({}, env_id=env, run_id=run_id, trading_day=trading_day, nature_day=nature_day))


if __name__ == "__main__":
    start()
