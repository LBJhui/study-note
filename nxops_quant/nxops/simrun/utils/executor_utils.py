# _*_ coding: utf-8 _*_
# @Time: 2024/8/6 11:04
# @Author: LBJ辉
# @File: executor_utils
# @Project: nxops_quant

def do_exit_callback_procedure(runtime, step, *args, **kwargs):
    if runtime["error"]:
        from nxpy.log.logger import LoggerUtils
        LoggerUtils.info(f"{step} failed")
        runtime["go"] = "exit"