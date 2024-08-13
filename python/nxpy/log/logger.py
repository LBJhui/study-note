# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 15:25
# @Author: LBJ辉
# @File: logger
# @Project: python
import os
import sys

import rapidjson
from loguru import _Logger, _Core

if "RUNNING_IN_APPHUB" in os.environ and os.environ["RUNNING_IN_APPHUB"] == "true":
    logger = _Logger(_Core(), None, -1, False, False, False, False, True, [], {})
else:
    logger = _Logger(_Core(), None, 1, False, False, False, False, True, [], {})


class LoggerUtils:
    @staticmethod
    def load_loggers(config_file_path):
        with open(config_file_path, encoding='UTF-8') as cf:
            config = rapidjson.load(cf)
            for (logger_id, logger_config) in config.items():
                if "sys.stderr" == logger_id:
                    a = logger.add(sys.stderr, **logger_config)
                else:
                    b = logger.add(logger_id, **logger_config)

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
