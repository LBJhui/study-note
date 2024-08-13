# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-23 15:19:56
@LastEditTime : 2020-08-12 10:22:59
@LastEditors  : yi.mt
@Description  : 
'''

import os

from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.task.task_worker import TaskWorker_Stage, TaskWorker_Procedure


class DbTaskWorker_Procedure(TaskWorker_Procedure):
    def __init__(self):
        super().__init__()

    def do_deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")

        executor = EasyDBExecutorUtils.get_executor(**kwargs)

        result = True
        try:
            error, exec_result = executor.execute(procedure_id, kwargs)
            if error:
                self.error(f"failed: [code={error['code']}, msg={error['msg']}]")
                kwargs.update({"procedureRemark": f"{error['msg']}"})
                result = False
        except Exception as e:
            self.error(f"failed: [{e}]")
            kwargs.update({"procedureRemark": str(e)})
            result = False

        return result


class DbTaskWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return DbTaskWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        task_worker = self._default_procedure_worker_class(kwargs)()

        serial = stage_config.get("serial", True)
        procedures = stage_config.get("procedures", [])

        all_success = True
        parameters = kwargs.copy()
        for procedure_config in procedures:
            procedure_id = procedure_config[0] if isinstance(procedure_config, list) else procedure_config
            parameters.update({"procedureID": procedure_id})
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
    return DbTaskWorker_Procedure()


def get_stage_worker():
    return DbTaskWorker_Stage()