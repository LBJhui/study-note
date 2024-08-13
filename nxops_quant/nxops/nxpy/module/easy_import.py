# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-27 15:59:54
@LastEditTime : 2020-07-27 16:01:30
@LastEditors  : yi.mt
@Description  : 
'''


import importlib


class EasyImportUtils():
    @staticmethod
    def import_module(module_name):
        module = importlib.import_module(module_name)
        return module

    @staticmethod
    def import_file(module_name, module_location):
        module_spec = importlib.util.spec_from_file_location(module_name, location=module_location)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        return module
    