# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-11 09:31:03
LastEditTime : 2022-07-08 14:49:02
LastEditors  : yi.mt
@Description  : 
'''

from abc import ABC, abstractmethod

from nxpy.log.logger import LoggerUtils
from nxpy.monitor.easy_tracer import EasyTracer


class TaskWorker():
    def __init__(self):
        super().__init__()
        self.worker_id = None

    def export(self, kwargs, newargs):
        export_args = kwargs.get("__export__", {})
        export_args.update(newargs)
        kwargs.update({"__export__": export_args})

    def report(self, module, title, content, kwargs):
        monitors = kwargs.get("task_processes").monitors
        for monitor in monitors:
            monitor.report(module, title, content)

    def info(self, content):
        msg = content
        if self.worker_id:
            msg = f"{self.worker_id} {content}"
        
        LoggerUtils.info(msg)

    def error(self, content):
        msg = content
        if self.worker_id:
            msg = f"{self.worker_id} {content}"
        
        LoggerUtils.error(msg)

    def warning(self, content):
        msg = content
        if self.worker_id:
            msg = f"{self.worker_id} {content}"
        
        LoggerUtils.warning(msg)

    def debug(self, content):
        msg = content
        if self.worker_id:
            msg = f"{self.worker_id} {content}"
        
        LoggerUtils.debug(msg)

    def log(self, content):
        msg = content
        if self.worker_id:
            msg = f"{self.worker_id} {content}"
        
        LoggerUtils.log(msg)

    def deal(self, kwargs):
        return self.do_deal(kwargs)

    def do_deal(self, kwargs):
        return True


class TaskWorker_Stage(TaskWorker):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return TaskWorker

    def deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        task_processes = kwargs.get("task_processes")

        self.worker_id = f"{task_processes.id} [{stage_id}]"

        self.info("beginning")

        if not task_processes.check_pre_stage(kwargs):
            task_processes.halt()
            return False

        if task_processes.check_stage(kwargs):
            self.info("finished: [result=done]")
            return True

        if not task_processes.begin_stage(kwargs):
            return False

        result = self.init_procedures(kwargs)
        if result:
            result = self.do_deal(kwargs)

        new_kwargs = kwargs
        new_kwargs.update(kwargs.get("__export__", {}))

        if result:
            task_processes.finish_stage(new_kwargs)
        else:
            task_processes.fail_stage(new_kwargs)

        self.info(f"finished: [result={result}]")

        return result

    def init_procedures(self, kwargs):
        return True


class TaskWorker_Procedure(TaskWorker):
    def __init__(self):
        super().__init__()

    def deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")

        task_processes = kwargs.get("task_processes")

        self.worker_id = f"{task_processes.id} [{stage_id}:{procedure_id}]"

        self.info("beginning")

        if not task_processes.check_pre_procedure(kwargs):
            return False

        if task_processes.check_procedure(kwargs):
            self.info("finished: [result=done]")
            return True

        if not task_processes.begin_procedure(kwargs):
            return False

        result = self.do_deal(kwargs)

        new_kwargs = kwargs
        new_kwargs.update(kwargs.get("__export__", {}))
        
        if result:
            task_processes.finish_procedure(new_kwargs)
        else:
            task_processes.fail_procedure(new_kwargs)

        self.info(f"finished: [result={result}]")

        return result


def get_procedure_worker():
    return TaskWorker_Procedure()


def get_stage_worker():
    return TaskWorker_Stage()
