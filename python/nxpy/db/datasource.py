# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 15:56
# @Author: LBJ辉
# @File: datasource
# @Project: python
from abc import abstractmethod

from nxpy.db.constants import DATASOURCE_CONFIG_NAME


class DBOperator():
    def __init__(self):
        super().__init__()
        self.dbtype = 0

    @abstractmethod
    def queryone(self, sql, parameters):
        pass

    @abstractmethod
    def querylist(self, sql, parameters):
        pass

    @abstractmethod
    def execute(self, sql, parameters):
        pass

    @abstractmethod
    def executemany(self, sql, parameters):
        pass


class DataSource(DBOperator):
    pools = {}

    def __init__(self, pid, dbtype, settings, drive=None):
        super().__init__()

    @classmethod
    def get_datasource(cls, pid):
        return cls.pools.get(pid, None)


class DataSourceUtils:
    @staticmethod
    def get_datasource(*args, **kwargs):
        datasource_id = kwargs.get(DATASOURCE_CONFIG_NAME)
        return DataSource.get_datasource(datasource_id)
