# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 14:42
# @Author: LBJ辉
# @File: context
# @Project: python
import os

import rapidjson  # pip install python-rapidjson

from nxpy.os.path import PathUtils


class AppContext:
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

    @classmethod
    def get(cls, key, default_value=None):
        return cls._context.get(key, default_value)

    def get_config_path(file_path):
        env_id = AppContext.get(AppContext.ENV_ID, None)
        if env_id:
            return os.path.join(PathUtils.get_real_path(AppContext.get(AppContext.CONFIG_HOME)), env_id, file_path)
        return os.path.join(PathUtils.get_real_path(AppContext.get(AppContext.CONFIG_HOME)), file_path)
