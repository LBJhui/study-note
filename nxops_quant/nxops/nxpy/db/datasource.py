# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-10 17:42:30
LastEditTime : 2022-01-12 15:18:48
LastEditors  : yi.mt
@Description  : 
'''

import rapidjson

from abc import ABC, abstractmethod

from dbutils.pooled_db import PooledDB

from nxpy.os.path import PathUtils

from nxpy.log.logger import LoggerUtils

from nxpy.db.constants import DBTYPE_MYSQL, DBTYPE_MSSQL, DBTYPE_POSTGRESQL, DBTYPE_ORACLE, DATASOURCE_CONFIG_NAME


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

    def connect(self):
        return self._connect()

    def get_transaction(self):
        transaction = DBTransaction(self)
        return transaction

    def _connect(self):
        if self.pool:
            return self.pool.connection()
        return None

    def execute(self, sql, parameters):
        conn = self._connect()
        try:
            conn.begin()

            cursor = conn.cursor()
            cursor.execute(sql, parameters)
            result = cursor.rowcount
            if cursor.with_rows:
                result = cursor.fetchall()
                result = [list(row) for row in result] if result else result

            conn.commit()
            cursor.close()
            
            return result
        except Exception as e:
            conn.rollback()
            LoggerUtils.error(e)
            raise e
        finally:
            conn.close()

    def executemany(self, sql, parameters):
        conn = self._connect()
        try:
            conn.begin()

            cursor = conn.cursor()
            cursor.executemany(sql, parameters)
            rowcount = cursor.rowcount

            conn.commit()
            cursor.close()
            
            return rowcount
        except Exception as e:
            conn.rollback()
            LoggerUtils.error(e)
            raise e
        finally:
            conn.close()

    def queryone(self, sql, parameters):
        conn = self._connect()
        try:
            cursor = conn.cursor()

            cursor.execute(sql, parameters)
            result = cursor.fetchone()
            cursor.close()

            if result:
                result = list(result)
            return result
        except Exception as e:
            LoggerUtils.error(e)
            raise e
        finally:
            if conn:
                conn.close()

    def querylist(self, sql, parameters):
        conn = self._connect()
        try:
            cursor = conn.cursor()

            cursor.execute(sql, parameters)
            result = cursor.fetchall()
            cursor.close()

            if result:
                result = [list(row) for row in result]
            return result
        except Exception as e:
            LoggerUtils.error(e)
            raise e
        finally:
            if conn:
                conn.close()

    def roll_querylist(self, sql, parameters, roll_size=5000):
        conn = self._connect()
        try:
            cursor = conn.cursor()

            cursor.execute(sql, parameters)
            while True:
                result = cursor.fetchmany(roll_size)
                if result:
                    result = [list(row) for row in result]
                    yield result
                else:
                    break
            cursor.close()
        except Exception as e:
            LoggerUtils.error(e)
            raise e
        finally:
            if conn:
                conn.close()


class DBTransaction(DBOperator):
    def __init__(self, dbpool):
        super().__init__()

        self.conn = dbpool.connect()
        self.dbtype = dbpool.dbtype

    def begin(self):
        self.conn.begin()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.conn.close()

    def execute(self, sql, parameters):
        cursor = self.conn.cursor()
        cursor.execute(sql, parameters)
        result = cursor.rowcount
        if cursor.with_rows:
            result = cursor.fetchall()
            result = [list(row) for row in result] if result else result
        cursor.close()
        return result

    def executemany(self, sql, parameters):
        cursor = self.conn.cursor()
        cursor.executemany(sql, parameters)
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount

    def queryone(self, sql, parameters):
        cursor = self.conn.cursor()

        cursor.execute(sql, parameters)
        result = cursor.fetchone()
        cursor.close()

        if result:
            result = list(result)
        return result

    def querylist(self, sql, parameters):
        cursor = self.conn.cursor()

        cursor.execute(sql, parameters)
        result = cursor.fetchall()
        cursor.close()

        if result:
            result = [list(row) for row in result]
        return result

    def roll_querylist(self, sql, parameters, roll_size=5000):
        cursor = self.conn.cursor()

        cursor.execute(sql, parameters)
        while True:
            result = cursor.fetchmany(roll_size)
            if result:
                result = [list(row) for row in result]
                yield result
            else:
                break
        cursor.close()


class DataSourceUtils():
    @staticmethod
    def load_datasources(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (source_id, source_config) in config.items():
                DataSource(source_id, source_config.get("type"), source_config.get("settings"), source_config.get("driver", None))

    @staticmethod
    def get_datasource(*args, **kwargs):
        datasource_id = kwargs.get(DATASOURCE_CONFIG_NAME)
        return DataSource.get_datasource(datasource_id)
