# -*- coding: UTF-8 -*-
# cython: language_level=3EasyDBExecutorUtils

'''
@Author       : yi.mt
@Date         : 2020-06-10 17:42:30
@LastEditTime : 2020-08-11 17:41:10
@LastEditors  : yi.mt
@Description  : 
'''

import os
import re
import uuid
import platform
import importlib
import rapidjson

from abc import ABC, abstractmethod

from nxpy.context import AppRuntime

from nxpy.os.path import PathUtils
from nxpy.log.logger import LoggerUtils

from nxpy.exception.exceptions import DbStatementNotFoundException, DbStatementNotAllowedException

from nxpy.db.datasource import DataSourceUtils

from nxpy.security.realm import SecurityRealm, Securable

from nxpy.db.constants import DBTYPE_MYSQL, DBTYPE_MSSQL, DBTYPE_POSTGRESQL, DBTYPE_ORACLE, EXECUTOR_CONFIG_NAME

app_runtime_executor = "executor"


def init_app_runtime_executor(paras, batch_paras, dboper, assembler, default_return, results, export, feedback):
    return {"success": True, "return": default_return, "go": None, "dboper": dboper, "assembler": assembler, "paras": paras, "batch_paras": batch_paras, "results": results, "error": {}, "export": export, "feedback": feedback}


def with_executor_runtime(key, default_return):
    def wrapper(func):
        def do_with_executor_runtime(self, *args, **kwargs):
            paras = kwargs.get("paras", {})
            batch_paras = kwargs.get("batch_paras", None)
            dboper = kwargs.get("dboper", None)
            if len(args) >= 2:
                paras = args[1]
                if len(args) >= 3:
                    batch_paras = args[2]
                    if len(args) >= 4:
                        dboper = args[3]

            dboper = dboper if dboper else self.get_datasource()
            assembler = EasyDBAssemblerUtils.get_assembler(dboper)

            old_runtime = AppRuntime.get_value(key)
            
            results = []
            export = {}
            feedback = {}
            if old_runtime:
                results = old_runtime.get("results", results)
                export = old_runtime.get("export", export)
                feedback = old_runtime.get("feedback", feedback)

            AppRuntime.set_value(key, init_app_runtime_executor(paras=paras, batch_paras=batch_paras, dboper=dboper, assembler=assembler, default_return=default_return, results=results, export=export, feedback=feedback))
            try:
                result = func(self, *args, **kwargs)
                return result
            finally:
                if paras:
                    paras.update(feedback)
                AppRuntime.del_value(key)
                if old_runtime:
                    AppRuntime.set_value(key, old_runtime)
        return do_with_executor_runtime
    return wrapper


sql_pattern = re.compile(r"(\$\{[\[\]\.a-zA-Z0-9_]+\})|(#\{[\[\]\.a-zA-Z0-9_]+\})")
if_cases_pattern = re.compile(r"<if\s+.+</if>")
if_items_pattern = re.compile(r"(<if\s+test=\")(.+)(\"\s*>)(.+)(</if>)")


def replace_has_expr(matched):
    var_name = str(matched.group('var_name'))
    return f"'{var_name}' in dir()"


def parse_has_expr(expr):
    a = re.compile(r"has\((?P<var_name>[^\)]+)\)")
    return re.sub(r"has\((?P<var_name>[^\)]+)\)", replace_has_expr, expr)


def eval_when_expr(expr, locals, *args, **kwargs):
    session = AppRuntime.get_value("session")
    realm = AppRuntime.get_value("realm")
    return eval(expr, {"session": session, "realm": realm}, locals)


def compile_dynamic_code(code, *args, **kwargs):
    exec_env = globals().copy()
    exec(code, exec_env)
    return exec_env


def exec_dynamic_code(env, action, runtime, *args, **kwargs):
    env[f"do_{action}"](runtime=runtime, *args, **kwargs)


def default_statement_loops(runtime):
    yield 0


class EasyDBRow():
    def __init__(self, meta, data):
        super().__init__()
        self.data = data
        self.dict = None
        if meta:
            self.dict = {column_name: idx for idx, column_name in enumerate(meta.get("columns", []))}

        self.size = len(self.data) if self.data else 0

        self.start_index = 0
        self.end_index = self.size

    def __len__(self):
        return self.size

    def __getitem__(self, key = 0):
        index = key
        if isinstance(key, str):
            index = self.dict[key]

        return self.data[index]
        
    def __setitem__(self, key, value):
        index = key
        if isinstance(key, str):
            index = self.dict[key]
            
        self.data[index] = value
    
    def __delitem__(self, key):
        index = key
        if isinstance(key, str):
            index = self.dict[key]
        
        if index and index < self.size:
            del self.data[index]
            self.size -= 1

    def __iter__(self):
        return self

    def __reversed__(self):
        while self.end_index > 0:
            self.end_index -= 1
            yield self[self.end_index]

    def __next__(self):
        if self.start_index >= self.size:
            raise StopIteration
 
        elem = self.data[self.start_index]
        self.start_index += 1
        return elem

class EasyDBResult():
    def __init__(self, meta, data):
        super().__init__()
        self.meta = meta
        self.data = data
        self._data = None

        if self.data:
            self._data = [EasyDBRow(meta, row) for row in self.data]

        self.size = len(self.data) if self.data else 0

        self.start_index = 0
        self.end_index = self.size

    @staticmethod
    def load(meta, data):
        if isinstance(data, list):
            return EasyDBResult(meta, data)
        return data

    def get_columns(self):
        return self.meta.get("columns", None) if self.meta else None

    def __len__(self):
        return self.size

    def __getitem__(self, index = 0):
        return self._data[index]
        
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __delitem__(self, index):
        if index and index < self.size:
            del self._data[index]
            del self.data[index]
            self.size -= 1

    def __iter__(self):
        return self

    def __reversed__(self):
        while self.end_index > 0:
            self.end_index -= 1
            yield self[self.end_index]

    def __next__(self):
        if self.start_index >= self.size:
            raise StopIteration
 
        elem = self.data[self.start_index]
        self.start_index += 1
        return elem

    def get_data(self):
        return self.data


class EasyDBStatement(Securable):
    def __init__(self, id, ware_id, executor_id, module, stmt, realm=None, parent=None):
        self.id = id
        self.ware_id = ware_id
        self.executor_id = executor_id
        self.module = module
        self.config = stmt
        self.parent = parent
        self.statement = None
        self.statemethod = None
        self.meta = None
        self.preloads = []
        self.runtimes = []
        self.cases_if = []

        self.refer_id = None
        self.refer_statement = None
        self.refer_executor = None

        if isinstance(stmt, list):
            self.statement = []
            for idx, sub_stmt in enumerate(stmt):
                sub_statement = EasyDBStatement(f"{id}.{idx}", ware_id, self.executor_id, self.module, sub_stmt, realm, parent=self)
                self.statement.append(sub_statement)
        else:
            self._set_statement(stmt)

        super().__init__(f"{executor_id}.{ware_id}.{id}")

        if not self.parent:
            self.bind_rules(realm=realm)

    def __getattribute__(self, name):
        if name in ["statement", "preloads", "runtimes", "cases_if"]:
            if self.refer_statement:
                return self.refer_statement.__getattribute__(name)
        return super().__getattribute__(name)

    def bind_rules(self, *args, **kwargs):
        realm = kwargs.get("realm")
        if realm:
            self.realm = SecurityRealm(auth_id=realm.get("auth_id", None), auth_level=realm.get("auth_level", None), auth_token=realm.get("auth_token", None), roles=realm.get("roles", None))

            rules = realm.get("rules", None)
            if rules and self.id in rules:
                self.realm.update(**rules.get(self.id))
        super().bind_rules(*args, **kwargs)

    def _set_statement(self, stmt):
        if isinstance(stmt, dict):
            self._set_statement_from_dict(stmt)
        elif isinstance(stmt, tuple):
            if len(stmt) >= 2:
                self._set_statement_from_dict({"sql": stmt[0], "meta": stmt[1]})
            else:
                self._set_statement_from_str(stmt[0])
        else:
            self._set_statement_from_str(stmt)

    def _set_statement_from_dict(self, stmt):
        if self.parent and "id" in stmt:
            parent_id = self.parent.id
            self_id = stmt.get("id")
            self.id = f"{parent_id}.{self_id}"

        self.meta = stmt.get("meta", None)
        if self.meta:
            columns = self.meta.get("columns", None)
            fields = self.meta.get("fields", None)
            if not columns and fields:
                self.meta["columns"] = fields

        d_stmt = stmt.get("sql", None)
        if d_stmt:
            if isinstance(d_stmt, list):
                self.statement = []
                for idx, sub_stmt in enumerate(d_stmt):
                    sub_id = (self.id + "." + sub_stmt.get("id")) if isinstance(sub_stmt, dict) and "id" in sub_stmt else f"{self.id}.{idx}"
                    sub_statement = EasyDBStatement(sub_id, self.ware_id, self.executor_id, self.module, sub_stmt, parent=self)
                    self.statement.append(sub_statement)
            elif isinstance(d_stmt, str):
                self._set_statement_from_str(d_stmt)
            else:
                self.statemethod = d_stmt

    def _set_statement_from_str(self, stmt_sql):
        if stmt_sql[0] == "@":
            self.refer_id = stmt_sql[1:]
            return

        self.statement = stmt_sql

        raw_paras = sql_pattern.findall(self.statement)
        for idx, raw_para in enumerate(raw_paras):
            if raw_para[0]:
                self._push_preload_parameter({"name": raw_para[0][2:-1], "expr": raw_para[0]})
            else:
                raw_para_expr = raw_para[1]
                new_raw_para_expr = f"#{idx}{raw_para_expr[1:]}"
                self.statement = self.statement.replace(raw_para_expr, new_raw_para_expr, 1)
                self._push_runtime_parameter({"name": raw_para_expr[2:-1], "expr": new_raw_para_expr})

        raw_cases_if = if_cases_pattern.findall(self.statement)
        for raw_case_if in raw_cases_if:
            raw_case_items_if = if_items_pattern.findall(raw_case_if)
            if len(raw_case_items_if) == 1 and len(raw_case_items_if[0]) == 5:
                self.cases_if.append({"holder": raw_case_if, "when": parse_has_expr(raw_case_items_if[0][1]), "then": raw_case_items_if[0][3]})

    def _push_preload_parameter(self, parameter):
        self.preloads.append(parameter)

    def _push_runtime_parameter(self, parameter):
        self.runtimes.append(parameter)


class EasyDBTransaction():
    def __init__(self, datasource, executor):
        super().__init__()

        self.executor = executor
        self.transaction = datasource.get_transaction()

    def begin(self):
        self.transaction.begin()

    def commit(self):
        self.transaction.commit()

    def rollback(self):
        self.transaction.rollback()

    def close(self):
        self.transaction.close()

    def execute(self, stmt_id, paras, batch_paras=None):
        return self.executor.execute(stmt_id, paras, batch_paras, dboper=self.transaction)

    def executemany(self, stmt_id, paras, batch_paras=None):
        return self.executor.executemany(stmt_id, paras, batch_paras, dboper=self.transaction)

    def queryone(self, stmt_id, paras):
        return self.executor.queryone(stmt_id, paras, dboper=self.transaction)

    def querylist(self, stmt_id, paras):
        return self.executor.querylist(stmt_id, paras, dboper=self.transaction)

    def roll_querylist(self, stmt_id, paras, roll_size=5000):
        for error, result in self.executor.roll_querylist(stmt_id, paras, dboper=self.transaction, roll_size=roll_size):
            yield error, result


class EasyDBAssembler():
    def __init__(self):
        super().__init__()

        self.default_total_sql_template = """SELECT COUNT(1) FROM (@sql@) t"""
        self.default_page_sql_template = """@sql@ LIMIT @begin@, @size@"""

    def make_statement(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        paras = runtime.get("paras", None)
        sql = stmt.statemethod(stmt, paras) if stmt.statemethod else stmt.statement
        return (sql, paras)

    def make_total_statement(self, sql, stmt, *args, **kwargs):
        total_sql = self.default_total_sql_template.replace("@sql@", sql)
        return total_sql

    def make_page_statement(self, sql, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        pager = runtime.get("current").get("pager")
        page_sql_template = self.default_page_sql_template
        if stmt.meta and "page_template" in stmt.meta:
            page_sql_template = stmt.meta.get("page_template")
        page_sql = page_sql_template.replace("@sql@", sql).replace("@begin@", str(pager.get("begin"))).replace("@size@", str(pager.get("size")))
        return page_sql

    def parse_expr_value(self, expr, *args, **kwargs):
        session = AppRuntime.get_value("session")
        realm = AppRuntime.get_value("realm")

        try:
            value = ("{" + expr + "}").format(session=session, realm=realm, *args, **kwargs)
            return value if value != "None" else None
        except KeyError as e:
            LoggerUtils.debug(f"variable [{expr}] is not found")
            return None


class EasyDBAssembler_Mysql(EasyDBAssembler):
    def __init__(self):
        super().__init__()

    def make_statement(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        paras = runtime.get("paras", None)
        batch_paras = runtime.get("batch_paras", None)
        
        sql = stmt.statemethod(stmt, paras) if stmt.statemethod else stmt.statement
        parameters = []

        if sql:
            paras = paras if paras and isinstance(paras, dict) else {}
            if stmt.cases_if:
                for case_if in stmt.cases_if:
                    if_exec_result = eval_when_expr(case_if.get("when"), paras)
                    if if_exec_result:
                        sql = sql.replace(case_if.get("holder"), case_if.get("then"))
                    else:
                        sql = sql.replace(case_if.get("holder"), "")

            for p_para in stmt.preloads:
                if p_para.get("expr") in sql:
                    sql = sql.replace(p_para.get("expr"), self.parse_expr_value(p_para.get("name"), **paras))
                
            if stmt.meta and stmt.meta.get("many", False) and batch_paras:
                origin_sql = sql
                sql_compiled = False
                for sub_raw_paras in batch_paras:
                    parse_paras = dict(paras, **sub_raw_paras) if paras else sub_raw_paras
                    sub_paras = []
                    for r_para in stmt.runtimes:
                        if r_para.get("expr") in origin_sql:
                            if not sql_compiled:
                                sql = sql.replace(r_para.get("expr"), "%s")
                            sub_paras.append(self.parse_expr_value(r_para.get("name"), **parse_paras))
                    sql_compiled = True
                    parameters.append(tuple(sub_paras))
            else:
                for r_para in stmt.runtimes:
                    if r_para.get("expr") in sql:
                        sql = sql.replace(r_para.get("expr"), "%s")
                        parameters.append(self.parse_expr_value(r_para.get("name"), **paras))
                parameters = tuple(parameters)

        LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] = [{sql}]")

        return sql, parameters


class EasyDBAssembler_Pgsql(EasyDBAssembler_Mysql):
    def __init__(self):
        super().__init__()


class EasyDBAssembler_Mssql(EasyDBAssembler_Mysql):
    def __init__(self):
        super().__init__()


class EasyDBAssembler_Oracle(EasyDBAssembler_Mysql):
    def __init__(self):
        super().__init__()
        
        self.default_page_sql_template = """SELECT ttdata.* FROM(SELECT tdata.*, ROWNUM AS rowno FROM(@sql@) tdata WHERE ROWNUM <= @end@) ttdata WHERE ttdata.rowno > @begin@"""

    def make_statement(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        paras = runtime.get("paras", None)
        batch_paras = runtime.get("batch_paras", None)
        
        sql = stmt.statemethod(stmt, paras) if stmt.statemethod else stmt.statement
        parameters = []

        if sql:
            paras = paras if paras and isinstance(paras, dict) else {}
            if stmt.cases_if:
                for case_if in stmt.cases_if:
                    if_exec_result = eval_when_expr(case_if.get("when"), paras)
                    if if_exec_result:
                        sql = sql.replace(case_if.get("holder"), case_if.get("then"))
                    else:
                        sql = sql.replace(case_if.get("holder"), "")

            for p_para in stmt.preloads:
                if p_para.get("expr") in sql:
                    sql = sql.replace(p_para.get("expr"), self.parse_expr_value(p_para.get("name"), **paras))
            
            param_idx = 0
            if stmt.meta and stmt.meta.get("many", False) and batch_paras:
                origin_sql = sql
                sql_compiled = False
                for sub_raw_paras in batch_paras:
                    parse_paras = dict(paras, **sub_raw_paras) if paras else sub_raw_paras
                    sub_paras = []
                    for r_para in stmt.runtimes:
                        if r_para.get("expr") in origin_sql:
                            if not sql_compiled:
                                param_idx += 1
                                sql = sql.replace(r_para.get("expr"), f":{param_idx}")
                            sub_paras.append(self.parse_expr_value(r_para.get("name"), **parse_paras))
                    sql_compiled = True
                    parameters.append(sub_paras)
            else:
                for r_para in stmt.runtimes:
                    if r_para.get("expr") in sql:
                        param_idx += 1
                        sql = sql.replace(r_para.get("expr"), f":{param_idx}")
                        parameters.append(self.parse_expr_value(r_para.get("name"), **paras))

        LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] = [{sql}]")

        return sql, parameters

    def make_page_statement(self, sql, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        pager = runtime.get("current").get("pager")
        end = pager.get("begin") + pager.get("size")
        page_sql_template = self.default_page_sql_template
        if stmt.meta and "page_template" in stmt.meta:
            page_sql_template = stmt.meta.get("page_template")
        page_sql = page_sql_template.replace("@sql@", sql).replace("@begin@", str(pager.get("begin"))).replace("@end@", str(end))
        return page_sql


class EasyDBAssemblerUtils():
    runtimes = {"default": EasyDBAssembler(), DBTYPE_MYSQL: EasyDBAssembler_Mysql(), DBTYPE_MSSQL: EasyDBAssembler_Mssql(), DBTYPE_POSTGRESQL: EasyDBAssembler_Pgsql(), DBTYPE_ORACLE: EasyDBAssembler_Oracle()}

    @classmethod
    def get_assembler(cls, dboper):
        return cls.runtimes.get(dboper.dbtype, cls.runtimes.get("default"))


class EasyDBExecutor():

    executors = {}

    def __init__(self, eid, *args, **kwargs):
        super().__init__()
        
        self.lib_ware_suffix = ".so"
        if platform.system() == "Windows":
            self.lib_ware_suffix = ".pyd"
        self.lib_ware_suffix_rpos = -1 * len(self.lib_ware_suffix)

        self.eid = eid
        self.datasource_id = kwargs.get("datasource", None)
        self._datasource = None
        self.package = kwargs.get("package", None)
        self.home = kwargs.get("home", None)
        self.recursive = kwargs.get("recursive", True)
        self.fixes = kwargs.get("fixes", None)
        self._wares = kwargs.get("wares", None)

        if self.datasource_id:
            self._datasource = DataSourceUtils.get_datasource(datasource_id=self.datasource_id)

        if self.home:
            self.home = [(PathUtils.get_real_path(item), None) for item in self.home] if isinstance(self.home, list) else [PathUtils.get_real_path(self.home)]
        elif self.package:
            self.home = [(importlib.import_module(item).__path__[0], item) for item in self.package] if isinstance(self.package, list) else [(importlib.import_module(self.package).__path__[0], self.package)]
        
        self.wares = {}

        if self.home:
            for (ware_home, package_name) in self.home:
                for root, dirs, files in os.walk(ware_home):
                    if not self.recursive and root != ware_home:
                        continue
                    for file_name in files:
                        if file_name[-3:] == ".py" or file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
                            self._load_ware(file_name, ware_home=ware_home, package_name=package_name, is_lib=True if file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix else False, file_path=None if root == ware_home else os.path.join(root, file_name))

        if self.fixes:
            self.fixes = [PathUtils.get_real_path(item) for item in self.fixes] if isinstance(self.fixes, list) else PathUtils.get_real_path(self.fixes)
            fix_homes = self.fixes if isinstance(self.fixes, list) else [self.fixes]
            for fix_home in fix_homes: 
                for root, dirs, files in os.walk(fix_home):
                    for file_name in files:
                        if file_name[-3:] == ".py" or file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
                            self._load_ware(file_name, ware_home=fix_home, package_name=None, is_lib=True if file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix else False, is_fix=True)

        self.executors.update({self.eid: self})

    @classmethod
    def get_executor(cls, eid):
        return cls.executors.get(eid, None)

    def get_datasource(self):
        if self.datasource_id and not self._datasource:
            self._datasource = DataSourceUtils.get_datasource(datasource_id=self.datasource_id)
        return self._datasource

    def get_transaction(self, datasource=None):
        transaction = EasyDBTransaction(datasource if datasource else self.get_datasource(), self)
        return transaction

    def find_statement(self, stmt_id, check_accessable=True):
        [ware_id, rstmt_id] = stmt_id.split(".", 1) # 只分割一次
        ware = self.wares.get(ware_id, None)
        if ware:
            stmt = ware.get(rstmt_id, None)
            if stmt:
                if not check_accessable or stmt.is_accessable():
                    self._fix_statement(stmt, check_accessable=False)
                    return stmt
                else:
                    raise DbStatementNotAllowedException(stmt_id)
        raise DbStatementNotFoundException(stmt_id)

    def _fix_statement(self, stmt, check_accessable=False):
        if stmt.refer_id and not stmt.refer_statement:
            executor = self
            refer_stmt_id = stmt.refer_id
            if stmt.refer_id[0] == "@":
                [executor_id, refer_stmt_id] = refer_stmt_id[1:].split(".", 1)
                executor = EasyDBExecutor.get_executor(executor_id)
            stmt.refer_executor = executor
            stmt.refer_statement = executor.find_statement(refer_stmt_id, check_accessable=check_accessable)
            if stmt.refer_statement and stmt.refer_statement.meta:
                stmt.meta = dict(stmt.refer_statement.meta, **stmt.meta) if stmt.meta else stmt.refer_statement.meta
            
        if stmt.meta and "prework" in stmt.meta:
            prework = stmt.meta.get("prework")
            if isinstance(prework, str):
                if prework[0] == "@":
                    stmt.meta["prework_method"] = stmt.module.__dict__[prework[1:]]
                else:
                    stmt.meta["prework_action"] = compile_dynamic_code(prework)
            else:
                stmt.meta["prework_method"] = prework
        if stmt.meta and "callback" in stmt.meta:
            callback = stmt.meta.get("callback")
            if isinstance(callback, str):
                if callback[0] == "@":
                    stmt.meta["callback_method"] = stmt.module.__dict__[callback[1:]]
                else:
                    stmt.meta["callback_action"] = compile_dynamic_code(callback)
            else:
                stmt.meta["callback_method"] = callback

    def pandas_query(self, stmt_id, paras, *args, **kwargs):
        stmt = self.find_statement(stmt_id)
        
        dboper = self.get_datasource()
        assembler = EasyDBAssemblerUtils.get_assembler(dboper)

        results = []
        export = {}
        feedback = {}

        AppRuntime.set_value(app_runtime_executor, init_app_runtime_executor(paras=paras, batch_paras=None, dboper=dboper, assembler=assembler, default_return=False, results=results, export=export, feedback=feedback))
            
        result = self._pandas_query(stmt, *args, **kwargs)

        AppRuntime.del_value(app_runtime_executor)

        return result

    @with_executor_runtime(app_runtime_executor, True)
    def queryone(self, stmt_id, paras, dboper=None, *args, **kwargs):
        stmt = self.find_statement(stmt_id)
        
        error, result = self._simple_execute(self._queryone, stmt, *args, **kwargs)
        if not error:
            result = result[0]
        
        return error, result

    def _queryone(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        sql, parameters = runtime.get("assembler").make_statement(stmt)

        error = None
        result = None

        dboper = runtime.get("dboper")
        try:
            result = [dboper.queryone(sql, parameters)]
        except Exception as e:
            LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] execute error: [{str(e)}]")
            error = stmt.meta.get("error") if stmt.meta and "error" in stmt.meta else {"code": -1, "msg": str(e), "cause": e}

        return error, result

    @with_executor_runtime(app_runtime_executor, True)
    def querylist(self, stmt_id, paras, dboper=None, *args, **kwargs):
        stmt = self.find_statement(stmt_id)
        
        return self._simple_execute(self._querylist, stmt, *args, **kwargs)

    def roll_querylist(self, stmt_id, paras, roll_size=5000, dboper=None, *args, **kwargs,):
        stmt = self.find_statement(stmt_id)
        
        dboper = dboper if dboper else self.get_datasource()
        assembler = EasyDBAssemblerUtils.get_assembler(dboper)

        results = []
        export = {}
        feedback = {}

        AppRuntime.set_value(app_runtime_executor, init_app_runtime_executor(paras=paras, batch_paras=None, dboper=dboper, assembler=assembler, default_return=True, results=results, export=export, feedback=feedback))
            
        for error, result in self._roll_querylist(stmt, roll_size, *args, **kwargs):
            yield error, result

        if paras:
            paras.update(feedback)
        AppRuntime.del_value(app_runtime_executor)

    def _querylist(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        assembler = runtime.get("assembler")
        sql, parameters = assembler.make_statement(stmt)

        error = None
        result = None

        dboper = runtime.get("dboper")
        try:
            if "pager" in runtime.get("current"):
                total_sql = assembler.make_total_statement(sql, stmt)
                total_count = dboper.queryone(total_sql, parameters)[0]
                runtime.get("current").get("pager").update({"total": total_count})
                
                sql = assembler.make_page_statement(sql, stmt)

            result = dboper.querylist(sql, parameters)
        except Exception as e:
            LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] execute error: [{str(e)}]")
            error = stmt.meta.get("error") if stmt.meta and "error" in stmt.meta else {"code": -1, "msg": str(e), "cause": e}

        return error, result

    def _pandas_query(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        assembler = runtime.get("assembler")
        sql, parameters = assembler.make_statement(stmt)
        
        dboper = runtime.get("dboper")
        try:
            import pandas
            result = pandas.read_sql_query(sql, dboper.connect(), params=parameters)
            return None, result
        except Exception as e:
            LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] execute error: [{str(e)}]")
            error = {"code": -1, "msg": str(e), "cause": e}
            return error, None
        
    def _roll_querylist(self, stmt, roll_size, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        assembler = runtime.get("assembler")
        sql, parameters = assembler.make_statement(stmt)

        error = None
        result = None

        dboper = runtime.get("dboper")
        try:
            meta = stmt.meta
            rolled_idx = 0
            for result in dboper.roll_querylist(sql, parameters, roll_size):
                error = runtime.get("error")
                result = result.get_data() if isinstance(result, EasyDBResult) else result
                if meta and ("result_id" in meta or "fields" in meta or "notes" in meta):
                    result = {"data": result}
                    if "result_id" in meta:
                        result.update({"id": meta.get("result_id")})
                    if "fields" in meta:
                        result.update({"fields": meta.get("fields")})
                    if "notes" in meta:
                        result.update({"notes": meta.get("notes")})
                rolled_idx += 1
                yield error, [result]
            if rolled_idx == 0:
                result = []
                if meta and ("result_id" in meta or "fields" in meta or "notes" in meta):
                    result = {"data": result}
                    if "result_id" in meta:
                        result.update({"id": meta.get("result_id")})
                    if "fields" in meta:
                        result.update({"fields": meta.get("fields")})
                    if "notes" in meta:
                        result.update({"notes": meta.get("notes")})
                yield error, [result]
        except Exception as e:
            LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] execute error: [{str(e)}]")
            error = stmt.meta.get("error") if stmt.meta and "error" in stmt.meta else {"code": -1, "msg": str(e), "cause": e}
            yield error, result

    @with_executor_runtime(app_runtime_executor, False)
    def execute(self, stmt_id, paras, batch_paras=None, dboper=None, *args, **kwargs):
        stmt = self.find_statement(stmt_id)
        if stmt.meta and stmt.meta.get("virtual", False):
            action_method = stmt.meta.get("action")
            runtime = AppRuntime.get_value(app_runtime_executor)
            return action_method(stmt, runtime, *args, **kwargs)
        else:
            return self._simple_execute(self._execute, stmt, *args, **kwargs)

    def _execute(self, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        sql, parameters = runtime.get("assembler").make_statement(stmt)

        error = None
        result = None

        dboper = runtime.get("dboper")
        try:
            if stmt.meta and stmt.meta.get("many", False):
                result = dboper.executemany(sql, parameters)
            else:
                result = dboper.execute(sql, parameters)
        except Exception as e:
            LoggerUtils.debug(f"sql [{stmt.ware_id}.{stmt.id}] execute error: [{str(e)}]")
            error = stmt.meta.get("error") if stmt.meta and "error" in stmt.meta else {"code": -1, "msg": str(e), "cause": e}

        return error, result

    @with_executor_runtime(app_runtime_executor, False)
    def executemany(self, stmt_id, paras, batch_paras=None, dboper=None, *args, **kwargs):
        stmt = self.find_statement(stmt_id)

        return self._simple_execute(self._execute, stmt, *args, **kwargs)

    def _simple_execute(self, func, stmt, *args, **kwargs):
        runtime = AppRuntime.get_value(app_runtime_executor)
        results = runtime.get("results")
        if isinstance(stmt.statement, list):
            do_while = True
            while do_while:
                do_while = False
                sub_idx = 0
                while sub_idx < len(stmt.statement):
                    sub_stmt = stmt.statement[sub_idx]
                    sub_idx += 1
                    go = runtime.get("go", None)
                    if go and go != sub_stmt.id:
                        continue
                    runtime["go"] = None

                    self._fix_statement(sub_stmt)
                    if self._before_execute(sub_stmt):
                        loops = sub_stmt.meta.get("loops", default_statement_loops) if sub_stmt.meta else default_statement_loops
                        for loop_idx in loops(runtime):
                            error, result = func(stmt=sub_stmt)
                            if not sub_stmt.meta:
                                if runtime.get("return"):
                                    if "pager" in runtime.get("current"):
                                        result = {"data": result, "pager": runtime.get("current").get("pager")}
                                    results.append(result)
                                if error:
                                    return error, results
                            else:
                                runtime["result"] = EasyDBResult.load(sub_stmt.meta, result)
                                if error:
                                    runtime["error"] = error
                                    runtime["exception"] = error
                                    runtime["go"] = "exit"
                                    break
                        if self._after_execute(stmt=sub_stmt):
                            runtime["success"] = True
                        else:
                            if not runtime.get("success") and not runtime.get("error"):
                                runtime["error"] = sub_stmt.meta.get("error", None)
                            break

                    go = runtime.get("go", None)
                    if go and go == "next":
                        runtime["go"] = None
                    elif go and go == "exit":
                        break
                    elif go and go == ":loop":
                        sub_idx -= 1
                        runtime["go"] = None
                    elif go and go[0] == "<":
                        runtime.update({"go": go[1:]})
                        do_while = True
                        break
        else:
            self._fix_statement(stmt)
            if self._before_execute(stmt):
                loops = stmt.meta.get("loops", default_statement_loops) if stmt.meta else default_statement_loops
                for loop_idx in loops(runtime):
                    error, result = func(stmt=stmt)
                    if not stmt.meta:
                        if runtime.get("return"):
                            if "pager" in runtime.get("current"):
                                result = {"data": result, "pager": runtime.get("current").get("pager")}
                            results.append(result)
                        if error:
                            return error, results
                    else:
                        runtime["result"] = EasyDBResult.load(stmt.meta, result)
                        if error:
                            runtime["error"] = error
                            runtime["exception"] = error
                if self._after_execute(stmt):
                    runtime["success"] = True
                else:
                    if not runtime.get("success") and not runtime.get("error") and stmt.meta.get("error", None):
                        runtime["error"] = error

        return runtime.get("error"), results

    def _before_execute(self, stmt):
        runtime = AppRuntime.get_value(app_runtime_executor)

        runtime["current"] = {}
        paras = runtime.get("paras", {})
        if paras and "pager" in paras:
            pager = paras.get("pager")
            page_no = pager.get("no") - 1
            page_size = pager.get("size")
            template_pager = dict(pager, begin=page_no * page_size, end=(page_no + 1) * page_size)
            runtime["current"].update({"pager": template_pager})

        if not stmt.meta:
            return True

        prework_method = stmt.meta.get("prework_method", None)
        if prework_method:
            prework_method(runtime=runtime)
        else:
            prework_action = stmt.meta.get("prework_action", None) if stmt.meta else None
            if prework_action:
                exec_dynamic_code(prework_action, "prework", runtime)

        export = runtime.get("export", None)
        if export:
            paras = runtime.get("paras", {})
            paras = dict(paras, **export)
            runtime["paras"] = paras

        go_expr = runtime.get("go", None)
        go_expr = go_expr if go_expr else "current"
        if go_expr == "exit":
            return False
        elif go_expr[0] == "@":
            go_stmt_id = go_expr[1:]
            error, result = self.execute(stmt_id=go_stmt_id, paras=runtime.get("paras"), batch_paras=runtime.get("batch_paras"), dboper=runtime.get("dboper"))
            if error:
                runtime["error"] = error
                return False
            else:
                runtime["go"] = None
                return True
        elif go_expr != "current":
            next_stmt_id = None if go_expr == "next" else go_expr
            return False
        return True

    def _after_execute(self, stmt):
        runtime = AppRuntime.get_value(app_runtime_executor)
        if not stmt.meta:
            return True

        meta = stmt.meta
        callback_method = stmt.meta.get("callback_method", None)
        if callback_method:
            callback_method(runtime=runtime)
        else:
            callback_action = meta.get("callback_action", None)
            if callback_action:
                exec_dynamic_code(callback_action, "callback", runtime)

        export = runtime.get("export", None)
        if export:
            paras = runtime.get("paras", {})
            paras = dict(paras, **export)
            runtime["paras"] = paras

        is_return = meta.get("return", runtime.get("return"))
        if is_return:
            result = runtime.get("result")
            result = result.get_data() if isinstance(result, EasyDBResult) else result
            if "result_id" in meta or "fields" in meta or "notes" in meta or "pager" in runtime.get("current") or runtime.get("error"):
                result = {"data": result}
                if "result_id" in meta:
                    result.update({"id": meta.get("result_id")})
                if "fields" in meta:
                    result.update({"fields": meta.get("fields")})
                if "notes" in meta:
                    result.update({"notes": meta.get("notes")})
                if "pager" in runtime.get("current"):
                    result.update({"pager": runtime.get("current").get("pager")})
                if runtime.get("error"):
                    result.update({"error": meta.get("error")})
            runtime.get("results").append(result)

        go_expr = runtime.get("go", None)
        go_expr = go_expr if go_expr else "next"
        if go_expr == "exit":
            return False
        elif go_expr[0] == "@":
            go_stmt_id = go_expr[1:]
            error, result = self.execute(stmt_id=go_stmt_id, paras=runtime.get("paras"), batch_paras=runtime.get("batch_paras"), dboper=runtime.get("dboper"))
            if error:
                runtime["error"] = error
                return False
            else:
                runtime["go"] = None
                return True
        return True

    def _import_ware_from_file(self, ware_id, ware_name, ware_home, package_name, is_fix=False, file_path=None):
        if not is_fix and ware_home:
            module_ware_id = ware_id
            if file_path:
                module_ware_id = file_path.replace(ware_home, "").replace(".py", "").replace(self.lib_ware_suffix, "").replace(os.path.sep, ".")
                module_ware_id = module_ware_id[1:] if module_ware_id[0] == "." else module_ware_id
            module = importlib.import_module((package_name + ".{}").format(module_ware_id))
            return module, module.alias if "alias" in module.__dict__ else ware_id, module.ware, module.realm if "realm" in module.__dict__ else None
        else:
            module_name = str(uuid.uuid4()) + "-" + ware_id
            module_location = file_path if file_path else os.path.join(ware_home, ware_name)
            module_spec = importlib.util.spec_from_file_location(module_name, location=module_location)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            return module, module.alias if "alias" in module.__dict__ else ware_id, module.ware, module.realm

    def _load_ware(self, ware_name, ware_home, package_name, is_lib=False, is_fix=False, file_path=None):
        ware_id = ware_name
        if ware_name[-3:] == ".py":
            ware_id = ware_id[:-3]
        elif ware_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
            ware_id = ware_id[:self.lib_ware_suffix_rpos]
        else:
            ware_name += self.lib_ware_suffix if is_lib else ".py"

        if self._wares and ware_id not in self._wares:
            return

        module, n_ware_id, raw_ware, raw_realm = self._import_ware_from_file(ware_id, ware_name, ware_home, package_name, is_fix=is_fix, file_path=file_path)
        well_ware = self.wares.get(n_ware_id, {})
        for stmt_id, stmt in raw_ware.items():
            easy_stmt = EasyDBStatement(stmt_id, ware_id, self.eid, module, stmt, raw_realm)
            well_ware.update({stmt_id: easy_stmt})

        self.wares.update({ware_id: well_ware, n_ware_id: well_ware})


class EasyDBExecutorUtils():
    @staticmethod
    def load_executors(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (executor_id, executor_config) in config.items():
                EasyDBExecutor(executor_id, **executor_config)

    @staticmethod
    def get_executor(*args, **kwargs):
        executor_id = kwargs.get(EXECUTOR_CONFIG_NAME)
        return EasyDBExecutor.get_executor(executor_id)
