# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-15 11:45:31
LastEditTime : 2020-08-19 11:32:59
LastEditors  : yi.mt
@Description  : 
'''

import rapidjson

from nxpy.context import AppContext

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options


class EasyCacheUtils():
    cache_settings = {}
    cache_manager = None

    @classmethod
    def load_settings(cls, config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            cls.cache_settings = rapidjson.load(cf)

        cls.cache_manager = CacheManager(**cls.cache_settings)

    @classmethod
    def get_cache(cls, *args, **kwargs):
        if not cls.cache_manager:
            return None

        i_kwargs = dict(cls.cache_settings, **kwargs)
        return cls.cache_manager.get_cache(*args, **i_kwargs)


if __name__ == "__main__":
    EasyCacheUtils.load_settings(AppContext.get_config_path("cache.json"))
    cache = EasyCacheUtils.get_cache("cache1")
    cache.set_value("test", "9999")
    print(cache.get_value("test"))
