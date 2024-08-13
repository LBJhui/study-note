# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-08-11 09:39:34
LastEditTime : 2023-02-20 17:01:09
LastEditors  : yi.mt
@Description  : 
'''

import os
import csv
import decimal
import rapidjson

import traceback

from nxpy.context import AppContext

from nxpy.os.path import PathUtils

from nxpy.config.easy_config import EasyConfigUtils

from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.task.task_worker import TaskWorker_Stage, TaskWorker_Procedure


class DbCsvWorker_Procedure(TaskWorker_Procedure):
    def __init__(self):
        super().__init__()

    def prepare_target_file(self, kwargs):
        return None

    def prepare_load_stmt(self, kwargs):
        return None

    def do_deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")
        roll_size = kwargs.get("rollSize", 0)

        data_file_path = self.prepare_target_file(kwargs)
        load_stmt_id = self.prepare_load_stmt(kwargs)

        result = True
        if data_file_path and load_stmt_id:
            executor = EasyDBExecutorUtils.get_executor(**kwargs)

            try:
                if roll_size == 0:
                    error, query_result = executor.querylist(load_stmt_id, kwargs)
                    if error:
                        self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
                        kwargs.update({"procedureRemark": f"{error['msg']}"})
                        result = False
                    else:
                        if query_result:
                            [data_result] = query_result
                            notes = data_result.get("notes", {})
                            write_mode = notes.get("mode", "w")
                            file_encoding = notes.get("encoding", "UTF-8")
                            use_header = notes.get("header", True)
                            use_quota = notes.get("quota", False)
                            with open(data_file_path, mode=write_mode, encoding=file_encoding, errors="surrogateescape") as df:
                                wt = csv.writer(df, quoting=csv.QUOTE_ALL if use_quota else csv.QUOTE_NONE)
                                if use_header:
                                    wt.writerow(data_result.get("fields"))
                                rows = [[format(field, '.6f') if isinstance(field, decimal.Decimal) else (format(field, 'd') if isinstance(field, int) else (str(field) if field else '')).replace("\r", "").replace("\n", "") for field in row] for row in data_result.get("data")]
                                wt.writerows(rows)
                else:
                    roll_index = 0
                    for error, query_result in executor.roll_querylist(load_stmt_id, kwargs, roll_size):
                        if error:
                            self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
                            kwargs.update({"procedureRemark": f"{error['msg']}"})
                            result = False
                            break
                        else:
                            if query_result:
                                [data_result] = query_result
                                notes = data_result.get("notes", {})
                                write_mode = notes.get("mode", "w")
                                file_encoding = notes.get("encoding", "UTF-8")
                                use_header = notes.get("header", True)
                                use_quota = notes.get("quota", False)
                                with open(data_file_path, mode=write_mode if roll_index == 0 else "a", encoding=file_encoding, errors="surrogateescape") as df:
                                    wt = csv.writer(df, quoting=csv.QUOTE_ALL if use_quota else csv.QUOTE_NONE)
                                    if roll_index == 0 and use_header:
                                        wt.writerow(data_result.get("fields"))
                                    roll_index += 1
                                    rows = [[format(field, '.6f') if isinstance(field, decimal.Decimal) else (format(field, 'd') if isinstance(field, int) else (str(field) if field else '')).replace("\r", "").replace("\n", "") for field in row] for row in data_result.get("data")]
                                    wt.writerows(rows)
            except Exception as e:
                self.error(f"failed: [{e}]")
                traceback.print_stack()
                kwargs.update({"procedureRemark": str(e)})
                result = False

        return result


class DbCsvWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return DbCsvWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        serial = stage_config.get("serial", True)

        data_files = stage_config.get("data_files")
        data_files_config_path = AppContext.get_config_path(data_files)

        all_loaded = True
        with open(data_files_config_path, encoding="UTF-8") as df:
            data_files_config = rapidjson.load(df)
            data_files_home = data_files_config.get("home")
            data_files_home = EasyConfigUtils.easy_parse(data_files_home, kwargs)
            data_files_home = PathUtils.get_real_path(data_files_home)

            parameters = kwargs.copy()
            loader = self._default_procedure_worker_class(kwargs)()
            for file_config in data_files_config.get("files"):
                file_name = file_config[0] if isinstance(file_config, list) else file_config
                parameters.update({"dataHome": data_files_home, "procedureID": file_name})
                if not loader.deal(parameters):
                    all_loaded = False
                    if serial:
                        break

        return all_loaded

    def init_procedures(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        data_files = stage_config.get("data_files")
        data_files_config_path = AppContext.get_config_path(data_files)
        with open(data_files_config_path, encoding="UTF-8") as df:
            data_files_config = rapidjson.load(df)
            data_file_configs = data_files_config.get("files")
            process_paras = dict(kwargs, procedures=[file_config for file_config in data_file_configs])

            result = task_processes.init_procedures(process_paras)
            return result


def get_procedure_worker():
    return DbCsvWorker_Procedure()


def get_stage_worker():
    return DbCsvWorker_Stage()