# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-11 14:36:12
@LastEditTime : 2020-07-23 12:41:04
@LastEditors  : yi.mt
@Description  : 
'''

import os
import rapidjson
import threading

from nxpy.os.path import PathUtils

class AppContext():
    BASE_HOME = "base_home"
    CONFIG_HOME = "config_home"
    ENV_ID = "env_id"
    _context = {BASE_HOME: ".", CONFIG_HOME: "./config", ENV_ID: None}

    @classmethod
    def load(cls, context_file, env_id = None):
        if context_file:
            context_file_path = PathUtils.get_real_path(context_file)
            with open(context_file_path, encoding="UTF-8") as df:
                context = rapidjson.load(df)
                cls._context.update(context)
            if env_id:
                cls._context.update({cls.ENV_ID: env_id})

    @classmethod
    def get(cls, key, default_value=None):
        return cls._context.get(key, default_value)

    @classmethod
    def set(cls, key, value):
        cls._context.update({key: value})

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


def with_runtime(key, value):
    def wrapper(func):
        def do_with_runtime(self, *args, **kwargs):
            AppRuntime.set_value(key, value)
            result = func(self, *args, **kwargs)
            AppRuntime.del_value(key)
            return result
        return do_with_runtime
    return wrapper



if __name__ == "__main__":
    print(AppRuntime.get_value("a"))
    AppRuntime.set_value("a", 1)
    print(AppRuntime.get_value("a"))
    AppRuntime.set_value("a", 2)
    print(AppRuntime.get_value("a"))
    AppRuntime.del_value("b")
