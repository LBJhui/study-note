# _*_ coding: utf-8 _*_
# @Time: 2024/4/23 10:21
# @Author: LBJ辉
# @File: management
# @Project: nxops-01
from abc import abstractmethod


class Managable:
    @abstractmethod
    def on_manage(self, *args, **kwargs):
        return True


class Manager:
    @abstractmethod
    def manage(self, *args, **kwargs):
        return True


class ManagementGateway:
    managables = {}

    @classmethod
    def register_manager(cls, manager_id, manager):
        cls.managables.update({manager_id: manager})

    @classmethod
    def get_manager(cls, manager_id):
        return cls.managables.get(manager_id, None)
