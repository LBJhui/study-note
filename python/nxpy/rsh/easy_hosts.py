# _*_ coding: utf-8 _*_
# @Time: 2024/8/14 14:17
# @Author: LBJ辉
# @File: easy_hosts
# @Project: python
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
