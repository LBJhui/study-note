# _*_ coding: utf-8 _*_
# @Time: 2024/4/19 10:05
# @Author: LBJ辉
# @File: datasource
# @Project: nxops-01
from abc import abstractmethod

import rapidjson
from dbutils.pooled_db import PooledDB
from nxpy.db.constants import DBTYPE_MYSQL, DBTYPE_MSSQL, DBTYPE_POSTGRESQL, DBTYPE_ORACLE, DATASOURCE_CONFIG_NAME


class DBOperator:
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

        self.pool = PooledDB(self.driver, **settings)
        self.pools.update({self.pid: self})

    @classmethod
    def get_datasource(cls, pid):
        return cls.pools.get(pid, None)


class DataSourceUtils:
    @staticmethod
    def load_datasources(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (source_id, source_config) in config.items():
                DataSource(source_id, source_config.get("type"), source_config.get("settings"),
                           source_config.get("driver", None))

    @staticmethod
    def get_datasource(*args, **kwargs):
        datasource_id = kwargs.get(DATASOURCE_CONFIG_NAME)
        return DataSource.get_datasource(datasource_id)
