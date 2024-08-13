# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-24 16:08:30
LastEditTime : 2024-03-25 11:44:30
LastEditors  : yi.mt
@Description  : 
'''

import os
import sys
import traceback
import rapidjson

from loguru import _Logger, _Core
if "RUNNING_IN_APPHUB" in os.environ and os.environ["RUNNING_IN_APPHUB"] == "true":
    logger = _Logger(_Core(), None, -1, False, False, False, False, True, [], {})
    # logger = _Logger(
    # core=_Core(),
    # exception=None,
    # depth=-1,
    # record=False,
    # lazy=False,
    # colors=False,
    # raw=False,
    # capture=True,
    # patchers=[],
    # extra={})
else:
    logger = _Logger(_Core(), None, 1, False, False, False, False, True, [], {})
    # logger = _Logger(
    # core=_Core(),
    # exception=None,
    # depth=1,
    # record=False,
    # lazy=False,
    # colors=False,
    # raw=False,
    # capture=True,
    # patchers=[],
    # extra={})

from nxpy.context import AppContext

def get_caller():
    caller_trace_stack = traceback.extract_stack(limit=3)[0]
    name = caller_trace_stack[0]
    line = caller_trace_stack[1]
    function = caller_trace_stack[2]

    return name, function, line


class LoggerUtils():
    @staticmethod
    def load_loggers(config_file_path):
        #使用默认logger时需删除
        #logger.remove(handler_id=None)
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)
            for (logger_id, logger_config) in config.items():
                if "sys.stderr" == logger_id:
                    a=logger.add(sys.stderr, **logger_config)
                else:
                    b=logger.add(logger_id, **logger_config)

    @staticmethod
    def trace(_Logger__message, *args, **kwargs):
        logger.trace(_Logger__message, *args, **kwargs)

    @staticmethod
    def debug(_Logger__message, *args, **kwargs):
        logger.debug(_Logger__message, *args, **kwargs)

    @staticmethod
    def info(_Logger__message, *args, **kwargs):
        logger.info(_Logger__message, *args, **kwargs)

    @staticmethod
    def success(_Logger__message, *args, **kwargs):
        logger.success(_Logger__message, *args, **kwargs)

    @staticmethod
    def warning(_Logger__message, *args, **kwargs):
        logger.warning(_Logger__message, *args, **kwargs)

    @staticmethod
    def error(_Logger__message, *args, **kwargs):
        logger.error(_Logger__message, *args, **kwargs)

    @staticmethod
    def critical(_Logger__message, *args, **kwargs):
        logger.critical(_Logger__message, *args, **kwargs)

    @staticmethod
    def exception(_Logger__message, *args, **kwargs):
        logger.exception(_Logger__message, *args, **kwargs)

    @staticmethod
    def log(_Logger__message, *args, **kwargs):
        logger.log(_Logger__message, *args, **kwargs)