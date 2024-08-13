# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-03-23 13:41:54
LastEditTime : 2022-02-11 15:39:40
LastEditors  : yi.mt
Description  : 
'''

import os
import re
import rapidjson

from nxpy.rsh.easy_hosts import EasyHostsUtils


class EasyConfig:
    @staticmethod
    def load(file_path, encoding="UTF-8"):
        with open(file_path, encoding=encoding) as f:
            config = rapidjson.load(f)
            return config

    @staticmethod
    def get(context, property_path):
        property_items = property_path.split(".")
        config_value = context
        for item in property_items:
            config_value = config_value.get(item)

        return config_value


class EasyConfigUtils:
    __param_pattern = re.compile(r"@([\.a-zA-Z0-9_]+)@")
    __refer_pattern = re.compile(r"&([\.a-zA-Z0-9_]+)&")

    @staticmethod
    def easy_load(home, shares, files, addons={}):
        context = {}
        config = {}

        config_home = home
        if config_home is None:
            default_home = os.getcwd()
            config_home = os.path.join(os.environ.get("NXPY_HOME", default_home), "configuration")

        if config_home is not None and shares is not None:
            for share_name in shares:
                if share_name.find(":") == -1:
                    config_file = os.path.join(config_home, os.environ.get("NXPY_ENV"), share_name + ".json")
                    context.update({share_name: EasyConfig.load(config_file)})
                else:
                    share_name_items = share_name.split(":", 1)
                    config_file = os.path.join(config_home, os.environ.get("NXPY_ENV"), share_name_items[1] + ".json")
                    context.update({share_name_items[0]: EasyConfig.load(config_file)})

        if files is not None:
            for config_file in files:
                if config_file is not None:
                    # 判断config_file是否根目录开始
                    if not config_file.startswith(os.getcwd()[0:3]):
                        config_file = os.path.join(config_home, os.environ.get("NXPY_ENV"), config_file)
                    if os.path.exists(config_file):
                        config.update(EasyConfig.load(config_file))
                    else:
                        print("config file [%s] not find ".format(config_file))

        if addons is not None:
            config.update(addons)

        return context, config

    @staticmethod
    def easy_parse(raw_value, kwargs):
        parsed_value = raw_value
        if parsed_value:
            params = EasyConfigUtils.__param_pattern.findall(parsed_value)
            for param in params:
                param_name = param[0] if isinstance(param, list) else param
                param_value = kwargs.get(param_name)
                if param_value:
                    parsed_value = parsed_value.replace(f"@{param_name}@", str(param_value))
            refers = EasyConfigUtils.__refer_pattern.findall(parsed_value)
            for refer in refers:
                refer_name = refer[0] if isinstance(refer, list) else refer
                refer_items = refer_name.split(".", 1)
                refer_region = refer_items[0]
                refer_property = refer_items[1]
                refer_value = None
                if refer_region == "hosts":
                    hosts_items = refer_property.split(".", 1)
                    host_id = hosts_items[0]
                    prop_name = hosts_items[1]
                    refer_value = EasyHostsUtils.get_host(host_id).get(prop_name)
                if refer_value:
                    parsed_value = parsed_value.replace(f"&{refer_name}&", str(refer_value))

        return parsed_value
