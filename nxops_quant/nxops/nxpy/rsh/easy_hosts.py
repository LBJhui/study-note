# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-10-20 15:02:49
LastEditTime : 2020-10-20 15:03:18
LastEditors  : yi.mt
Description  : 
'''

import rapidjson

class EasyHostsUtils():
    hosts_settings = {}

    @classmethod
    def load_hosts(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.hosts_settings = rapidjson.load(cf)

    @classmethod
    def get_host(cls, host_id):
        return cls.hosts_settings.get(host_id)