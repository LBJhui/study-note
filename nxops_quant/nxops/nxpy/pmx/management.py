# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-07-15 16:04:48
@LastEditTime : 2020-07-16 15:57:15
@LastEditors  : yi.mt
@Description  : 
'''

from abc import ABC, abstractmethod


class Managable():
    @abstractmethod
    def on_manage(self, *args, **kwargs):
        return True


class Manager():
    @abstractmethod
    def manage(self, *args, **kwargs):
        return True


class ManagementGateway():
    managables = {}

    @classmethod
    def register_manager(cls, manager_id, manager):
        cls.managables.update({manager_id: manager})

    @classmethod
    def get_manager(cls, manager_id):
        return cls.managables.get(manager_id, None)
