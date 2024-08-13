# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-08-05 11:33:47
LastEditTime : 2021-08-05 11:33:48
LastEditors  : yi.mt
Description  : 
'''

import os
import rapidjson

from nxpy.task.task_worker import TaskWorker_Stage

from nxpy.task.db_task_worker import DbTaskWorker_Procedure

from nxpy.module.easy_import import EasyImportUtils

class MixTaskWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return DbTaskWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        serial = stage_config.get("serial", True)
        procedures = stage_config.get("procedures", [])

        all_success = True
        parameters = kwargs.copy()
        for procedure_config in procedures:
            procedure_id = procedure_config[0] if isinstance(procedure_config, list) else procedure_config
            procedure_module = procedure_config[1] if isinstance(procedure_config, list) else None
            parameters.update({"procedureID": procedure_id})
            if procedure_module:
                module = EasyImportUtils.import_module(procedure_module)
                task_worker = module.get_procedure_worker()
                if not task_worker or not task_worker.deal(parameters):
                    all_success = False
                    if serial:
                        break
            else:
                task_worker = self._default_procedure_worker_class(kwargs)()
                if not task_worker.deal(parameters):
                    all_success = False
                    if serial:
                        break

        return all_success

    def init_procedures(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        procedures = stage_config.get("procedures", [])
        process_paras = dict(kwargs, procedures=[procedure_config for procedure_config in procedures])

        result = task_processes.init_procedures(process_paras)
        return result


def get_procedure_worker():
    return None


def get_stage_worker():
    return MixTaskWorker_Stage()