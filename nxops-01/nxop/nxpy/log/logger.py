# _*_ coding: utf-8 _*_
# @Time: 2024/4/18 10:42
# @Author: LBJ辉
# @File: logger
# @Project: nxops-01
import sys

import rapidjson
from loguru import logger


class LoggerUtils():
    @staticmethod
    def load_loggers(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)
            for (logger_id, logger_config) in config.items():
                if logger_id == "sys.stderr":
                    a = logger.add(sys.stderr, **logger_config)
                else:
                    b = logger.add(logger_id, **logger_config)
