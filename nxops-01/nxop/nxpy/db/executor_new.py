# _*_ coding: utf-8 _*_
# @Time: 2024/4/25 9:48
# @Author: LBJ辉
# @File: executor_new
# @Project: nxops-01
import importlib
import os
import platform
from abc import abstractmethod

import rapidjson
from dbutils.pooled_db import PooledDB
from nxpy.os.path import PathUtils

DBTYPE_MYSQL = "mysql"
DBTYPE_MSSQL = "mssql"
DBTYPE_POSTGRESQL = "pgsql"
DBTYPE_ORACLE = "oracle"
DATASOURCE_CONFIG_NAME = "datasource_id"
EXECUTOR_CONFIG_NAME = "executor_id"


class EasyDBExecutorUtils:
    # 加载 executor.json 配置文件
    @staticmethod
    def load_executors(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (execuotr_id, execuotr_config) in config.items():
                EasyDBExecutor(execuotr_id, **execuotr_config)


class EasyDBExecutor:
    executors = {}

    def __init__(self, eid, **kwargs):
        super().__init__()
        self.lib_ware_suffix = ".so"  # 配置文件后缀名
        if platform.system() == "Windows":
            self.lib_ware_suffix = ".pyd"
        self.lib_ware_suffix_rpos = -1 * len(self.lib_ware_suffix)

        self.eid = eid  # task
        self.datasource_id = kwargs.get("datasource", None)  # simrun
        self._datasource = None
        self.package = kwargs.get("package", None)  # nxpy.task.easymodules
        self.home = kwargs.get("home", None)
        self._wares = kwargs.get("_wares", None)

        if self.datasource_id:
            self._datasource = DataSourceUtils.get_datasource(datasource_id=self.datasource_id)

        if self.home:
            self.home = [(PathUtils.get_real_path(item), None) for item in self.home] if isinstance(self.home,
                                                                                                    list) else [
                PathUtils.get_real_path(self.home)]
        elif self.package:
            self.home = [(importlib.import_module(item).__path__[0], item) for item in self.package] if isinstance(
                self.package, list) else [(importlib.import_module(self.package).__path__[0], self.package)]

        # [('D:\\Desktop\\note-docsify\\nxops-01\\nxop\\nxpy\\task\\easymodules', 'nxpy.task.easymodules')]

        self.wares = {}

        if self.home:
            for (ware_home, package_name) in self.home:
                for root, dirs, files in os.walk(ware_home):
                    # root D:\Desktop\note-docsify\nxops-01\nxop\nxpy\task\easymodules
                    if root != ware_home:
                        continue
                    for file_name in files:
                        # task_process.py
                        if file_name[-3:] == ".py" or file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
                            self._load_ware(file_name, ware_home=ware_home, package_name=package_name,
                                            is_lib=True if file_name[
                                                           self.lib_ware_suffix_rpos:] == self.lib_ware_suffix else False,
                                            file_path=None if root == ware_home else os.path.join(root, file_name))

    def _import_ware_from_file(self, ware_id, ware_name, ware_home, package_name, is_fix=False, file_path=None):
        return

    # 加载 easymodules 文件夹下文件的 ware
    def _load_ware(self, ware_name, ware_home, package_name, is_lib=False, is_fix=False, file_path=None):
        ware_id = ware_name
        # 去掉文件名后缀
        if ware_name[-3:] == ".py":
            ware_id = ware_id[:-3]  # task_process
        elif ware_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
            ware_id = ware_id[:self.lib_ware_suffix_rpos]
        else:
            ware_name += self.lib_ware_suffix if is_lib else ".py"

        if self._wares and ware_id not in self._wares:
            return

        module, n_ware_id, raw_ware, raw_realm = self._import_ware_from_file(ware_id, ware_name, ware_home,
                                                                             package_name, is_fix=is_fix,
                                                                             file_path=file_path)


class DataSourceUtils:
    @staticmethod
    def get_datasource(**kwargs):
        datasource_id = kwargs.get(DATASOURCE_CONFIG_NAME)
        return DataSource.get_datasource(datasource_id)


class DBOperator:
    def __init__(self):
        super().__init__()
        self.dbtype = 0  # 数据库类型

    @abstractmethod
    def query(self, sql, parameters):
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

    def __init__(self, pid, dbtype, settings, driver=None):
        super().__init__()
        self.pid = pid
        self.dbtype = dbtype
        self.settings = settings
        self.driver = driver
        if not self.driver:
            if self.dbtype == DBTYPE_MYSQL:
                import mysql.connector
                self.driver = mysql.connector
            elif self.dbtype == DBTYPE_MSSQL:
                import pymssql
                self.driver = pymssql
            elif self.dbtype == DBTYPE_POSTGRESQL:
                import psycopg2
                self.driver = psycopg2
            elif self.dbtype == DBTYPE_ORACLE:
                import cx_Oracle
                self.driver = cx_Oracle

        self.pool = PooledDB(self.driver, **self.settings)

        self.pools.update({self.pid: self})

    @classmethod
    def get_datasource(cls, pid):
        return cls.pools.get(pid, None)
