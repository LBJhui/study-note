# _*_ coding: utf-8 _*_
# @Time: 2024/4/18 9:55
# @Author: LBJ辉
# @File: context
# @Project: nxops-01
import threading

import rapidjson
from nxpy.os.path import PathUtils

import os


class AppContext():
    BASE_HOME = "base_home"
    CONFIG_HOME = "config_home"
    ENV_ID = "env_id"
    _context = {BASE_HOME: ".", CONFIG_HOME: "./config", ENV_ID: None}

    @classmethod
    def load(cls, context_file, env_id=None):
        if context_file:
            context_file_path = PathUtils.get_real_path(context_file)
            with open(context_file_path, encoding="UTF-8") as df:
                context = rapidjson.load(df)
                cls._context.update(context)
            if env_id:
                cls._context.update({cls.ENV_ID: env_id})

    # 获取 _context 属性值
    @classmethod
    def get(cls, key, default_value=None):
        return cls._context.get(key, default_value)

    # 根据 env_id，拼接路径
    @staticmethod
    def get_config_path(file_path):
        env_id = AppContext.get(AppContext.ENV_ID, None)
        if env_id:
            return os.path.join(PathUtils.get_real_path(AppContext.get(AppContext.CONFIG_HOME)), env_id, file_path)
        return os.path.join(PathUtils.get_real_path(AppContext.get(AppContext.CONFIG_HOME)), file_path)


APP_RUNTIME_LOCAL = threading.local()


class AppRuntime():
    @staticmethod
    def get_value(key):
        if hasattr(APP_RUNTIME_LOCAL, "runtime"):
            return APP_RUNTIME_LOCAL.runtime.get(key, None)
        return None

    @staticmethod
    def set_value(key, value):
        if not hasattr(APP_RUNTIME_LOCAL, "runtime"):
            APP_RUNTIME_LOCAL.runtime = {}
        APP_RUNTIME_LOCAL.runtime.update({key: value})

    @staticmethod
    def del_value(key):
        if hasattr(APP_RUNTIME_LOCAL, "runtime"):
            APP_RUNTIME_LOCAL.runtime.pop(key, None)
