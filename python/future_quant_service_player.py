# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 14:32
# @Author: LBJ辉
# @File: future_quant_service_player
# @Project: python

import click
from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.context import AppContext
from nxpy.log.logger import LoggerUtils


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


if __name__ == '__main__':
    start()
