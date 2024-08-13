# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-24 09:47:01
LastEditTime : 2022-07-20 15:33:23
LastEditors  : yi.mt
@Description  : 
'''
import time
import importlib
import rapidjson

import threading

import traceback

from nxpy.context import AppContext

from nxpy.log.logger import LoggerUtils

from nxpy.config.easy_config import EasyConfigUtils

from nxpy.db.executor import EasyDBExecutorUtils

from nxpy.monitor.easy_monitor import EasyMonitorUtils
from nxpy.monitor.easy_tracer import EasyTracerUtils


class EasyTaskThread(threading.Thread):
    def __init__(self, id, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.id = id
        self.result = False
    
    def run(self):
        try:
            if self._target:
                self.result = self._target(*self._args, **self._kwargs)
            else:
                self.result = None
        finally:
            del self._target, self._args, self._kwargs

    def get_result(self):
        return self.result


class TaskProcesses():
    STAGE_STATUS_INITIAL = 0
    STAGE_STATUS_SUCCESS = 1
    STAGE_STATUS_FAILED = -1
    STAGE_STATUS_WORKING = 2
    STAGE_STATUS_SKIPED = 3

    PROCEDURE_STATUS_INITIAL = 0
    PROCEDURE_STATUS_SUCCESS = 1
    PROCEDURE_STATUS_FAILED = -1
    PROCEDURE_STATUS_WORKING = 2
    PROCEDURE_STATUS_SKIPED = 3

    def __init__(self, processes, options):
        super().__init__()

        self.running = False
        self.options = options

        task_id = self.options.get("taskID")
        run_id = self.options.get("runID")

        self.id = f"{task_id}:{run_id}"

        self.processes_config = {}

        processes_config_path = AppContext.get_config_path(processes)
        with open(processes_config_path, encoding="UTF-8") as pf:
            self.processes_config = rapidjson.load(pf)

        self._set_monitors()

        self.task_config = self.processes_config.get("task", {})

        self.executor = EasyDBExecutorUtils.get_executor(executor_id=options.get("executor_id"))
        if not self.executor:
            self.executor = EasyDBExecutorUtils.get_executor(executor_id=self.task_config.get("executor_id"))

    def _get_executor(self, kwargs):
        if self.executor:
            return self.executor
        return EasyDBExecutorUtils.get_executor(executor_id=kwargs.get("executor_id"))

    def _set_monitors(self):
        self.monitors = []
        self.tracers = []
        monitors_config = self.processes_config.get("monitors")
        if monitors_config:
            for monitor_config in monitors_config:
                if monitor_config.get("is_tracer", False):
                    tracer = EasyTracerUtils.create_tracer(monitor_config)
                    if tracer:
                        self.monitors.append(tracer)
                        self.tracers.append(tracer)
                else:
                    monitor = EasyMonitorUtils.create_monitor(monitor_config)
                    if monitor:
                        self.monitors.append(monitor)

    def _trace_report(self):
        if self.tracers:
            for tracer in self.tracers:
                try:
                    tracer.commit(self.options)
                except Exception as e:
                    LoggerUtils.error(f"{self.id} [trace_report] failed: [{e}]")

    def startup(self):
        self.running = True
        parameters = self.options.copy()
        
        LoggerUtils.info(f"{self.id} beginning")
        self.report(f"{self.id}", f"{self.id}运行状态", "开始执行")

        parameters.update({"task_processes": self})

        if not self.init_stages("depends", parameters):
            self.report(f"{self.id}", f"{self.id}运行状态", "执行失败: init_stages[depends]")
            self._trace_report()
            return

        for stage_id in self.processes_config.get("depends", []):
            if not self.running:
                break
            if not self.deal_stage(stage_id, parameters):
                LoggerUtils.error(f"{self.id} failed: {stage_id}")
                self.report(f"{self.id}", f"{self.id}运行状态", f"执行失败: {stage_id}")
                self._trace_report()
                return

        if not self.init_stages("stages", parameters):
            self.report(f"{self.id}", f"{self.id}运行状态", "执行失败: init_stages[stages]")
            self._trace_report()
            return

        for stage_id in self.processes_config.get("stages"):
            if not self.running:
                break
            if isinstance(stage_id, list):
                stage_ids = stage_id
                deal_threads = []
                for stage_id in stage_ids:
                    deal_thread = EasyTaskThread(id=stage_id, target=self.deal_stage, args=(stage_id, parameters))
                    deal_threads.append(deal_thread)
                    deal_thread.start()
                all_success = True
                failed_stages = []
                while True:
                    all_finished = True
                    for deal_thread in deal_threads:
                        if deal_thread.is_alive():
                            all_finished = False
                    if all_finished:
                        for deal_thread in deal_threads:
                            if deal_thread.get_result() == False:
                                all_success = False
                                failed_stages.append(deal_thread.id)
                        break
                    else:
                        time.sleep(1)
                if not all_success:
                    LoggerUtils.error(f"{self.id} failed: {failed_stages}")
                    self.report(f"{self.id}", f"{self.id}运行状态", f"执行失败: {failed_stages}")
                    break
            else:
                if not self.deal_stage(stage_id, parameters):
                    LoggerUtils.error(f"{self.id} failed: {stage_id}")
                    self.report(f"{self.id}", f"{self.id}运行状态", f"执行失败: {stage_id}")
                    self._trace_report()
                    return

        LoggerUtils.info(f"{self.id} finished")
        self.report(f"{self.id}", f"{self.id}运行状态", "执行结束")
        self._trace_report()

    def halt(self):
        self.running = False

    def report(self, module, title, content):
        silent = self.task_config.get("silent", False)
        if not silent:
            for monitor in self.monitors:
                monitor.report(module, title, content)

    def deal_stage(self, stage_id, parameters):
        stage_config = self.processes_config.get(stage_id, None)

        result = False
        if stage_config:
            delay_seconds = stage_config.get("delay", 0)
            if delay_seconds > 0:
                time.sleep(delay_seconds)
            retry_config = stage_config.get("retry", None)

            need_report = stage_config.get("need_report", False)
            if need_report:
                self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] 开始")

            deal_parameters = {}
            deal_times = 0
            while True:
                deal_times += 1
                stage_name = stage_config.get("name", stage_id)
                deal_parameters.update({"stageID": stage_id, "stageName": stage_name})
                deal_parameters.update(self.processes_config.get("parameters", {}))
                deal_parameters.update(self.processes_config.get(stage_id).get("parameters", {}))
                deal_parameters.update(parameters)

                stage_tag = self._gen_stage_tag(stage_id, stage_config, deal_parameters)
                deal_parameters.update({"stageTag": stage_tag})
                
                stage_worker = self.get_stage_worker(deal_parameters)
                try:
                    result = stage_worker.deal(deal_parameters)
                except Exception as e:
                    LoggerUtils.error(f"{self.id} [deal_stage] [{stage_id}] failed: [{e}]")
                    self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] failed: [{e}]")
                if retry_config and not result:
                    retry_max_times = retry_config.get("max_times", 3)
                    retry_interval = retry_config.get("interval", 60)
                    if retry_max_times > deal_times:
                        time.sleep(retry_interval)
                        deal_parameters = {}
                        LoggerUtils.info(f"{self.id} [deal_stage] [{stage_id}] retrying [{deal_times}]")
                        self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] retrying [{deal_times}]")
                        continue
                    
                break

            parameters.update(deal_parameters.get("__export__", {}))

            if need_report:
                self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] 结束[result={result}]")

            if not result:
                fail_ignore = stage_config.get("fail_ignore", False)
                if fail_ignore:
                    result = True
                    LoggerUtils.warning(f"{self.id} [deal_stage] [{stage_id}] fail-ignored")
                    self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] fail-ignored")
                else:
                    LoggerUtils.error(f"{self.id} [deal_stage] [{stage_id}] failed")
                    self.report(f"{self.id}", f"{self.id}运行状态", f"[deal_stage] [{stage_id}] failed")

        return result

    def get_stage(self, kwargs):
        stage_id = kwargs.get("stageID")
        return self.processes_config.get(stage_id, None)

    def check_stage(self, kwargs):
        stage_status = self._get_stage_status(kwargs)

        LoggerUtils.debug(f"{self.id} [check_stage] [{kwargs}] [status={stage_status}]")

        if stage_status == self.STAGE_STATUS_SUCCESS or stage_status == self.STAGE_STATUS_SKIPED:
            return True
        else:
            return False

    def check_pre_stage(self, kwargs):
        stage_id = kwargs.get("stageID")
        stage_config = self.processes_config.get(stage_id, None)
        if stage_config:
            pre_stages = stage_config.get("pre_stages")
            if pre_stages:
                all_pre_finished = True
                for pre_stage_id in pre_stages:
                    parameters = kwargs.copy()
                    parameters.update({"stageID": pre_stage_id})
                    stage_status = self._get_stage_status(parameters)
                    if not (stage_status == self.STAGE_STATUS_SUCCESS or stage_status == self.STAGE_STATUS_SKIPED):
                        all_pre_finished = False
                        LoggerUtils.error(f"{self.id} [check_pre_stage] [{stage_id}] failed: [{pre_stage_id} status={stage_status}]")
                        break
                return all_pre_finished
            else:
                return True
        LoggerUtils.error(f"{self.id} [check_pre_stage] [{stage_id}] failed: Not Found")
        return False

    def _get_stage_status(self, kwargs):
        executor = self._get_executor(kwargs)
        error, [stage_status] = executor.queryone("task_processes.get_task_stage_status", kwargs)
        if error:
            LoggerUtils.error(f"{self.id} [_get_stage_status] [{kwargs}] failed: [code={error['code']}, msg={error['msg']}]")
            return False
        return stage_status[0]

    def init_stages(self, category, kwargs):
        stages = self.processes_config.get(category, [])
        executor = self._get_executor(kwargs)

        LoggerUtils.info(f"{self.id} [init_{category}] beginning")
        try:
            batch_paras = []
            clean_paras = []
            for stage_id in stages:
                if isinstance(stage_id, list):
                    stage_ids = stage_id
                    for stage_id in stage_ids:
                        always = self.processes_config.get(stage_id).get("always", False)
                        para = self._gen_init_stage_parameters(stage_id, kwargs)
                        if para:
                            batch_paras.append(para)
                            if always:
                                clean_paras.append(para)
                else:
                    always = self.processes_config.get(stage_id).get("always", False)
                    para = self._gen_init_stage_parameters(stage_id, kwargs)
                    if para:
                        batch_paras.append(para)
                        if always:
                            clean_paras.append(para)

            if len(clean_paras) > 0:
                executor.executemany(stmt_id="task_processes.clean_task_stages", paras=None, batch_paras=clean_paras)
                executor.executemany(stmt_id="task_processes.clean_task_procedures", paras=None, batch_paras=clean_paras)
            if len(batch_paras) > 0:
                executor.executemany(stmt_id="task_processes.init_task_stages", paras=None, batch_paras=batch_paras)
        except Exception as e:
            traceback.print_exc(e)
            LoggerUtils.error(f"{self.id} [init_{category}] [{kwargs}] failed: [{e}]")
            return False

        LoggerUtils.info(f"{self.id} [init_{category}] finished")
        return True

    def _gen_init_stage_parameters(self, stage_id, kwargs):
        stage_config = self.processes_config.get(stage_id, None)
        if stage_config:
            stage_name = stage_config.get("name", stage_id)
            stage_tag = self._gen_stage_tag(stage_id, stage_config, kwargs)
            return dict(kwargs.copy(), stageID=stage_id, stageTag=stage_tag, stageName=stage_name, stageStatus=self.STAGE_STATUS_INITIAL)
        return None

    def _gen_stage_tag(self, stage_id, stage_config, kwargs):
        stage_tag = stage_config.get("tag", self.task_config.get("default_tag", stage_id))
        stage_tag = EasyConfigUtils.easy_parse(stage_tag, kwargs)
        return stage_tag

    def _update_stage_tag(self, kwargs):
        stage_tag = kwargs.get("stageTag", None)
        if stage_tag:
            stage_tag = EasyConfigUtils.easy_parse(stage_tag, kwargs)
            kwargs.update({"stageTag": stage_tag})

    def begin_stage(self, kwargs):
        LoggerUtils.debug(f"{self.id} [begin_stage] [{kwargs['stageID']}] beginning")

        paras = dict(kwargs, stageStatus=self.STAGE_STATUS_WORKING)
        result = self._mark_task_stage(paras)

        LoggerUtils.debug(f"{self.id} [begin_stage] [{kwargs['stageID']}] finished")

        return result

    def fail_stage(self, kwargs):
        LoggerUtils.debug(f"{self.id} [fail_stage] [{kwargs['stageID']}] beginning")

        paras = dict(kwargs, stageStatus=self.STAGE_STATUS_FAILED)
        result = self._mark_task_stage(paras)

        LoggerUtils.debug(f"{self.id} [fail_stage] [{kwargs['stageID']}] finished")
        return result

    def finish_stage(self, kwargs):
        LoggerUtils.debug(f"{self.id} [finish_stage] [{kwargs['stageID']}] beginning")

        paras = dict(kwargs, stageStatus=self.STAGE_STATUS_SUCCESS)
        result = self._mark_task_stage(paras)

        LoggerUtils.debug(f"{self.id} [finish_stage] [{kwargs['stageID']}] finished")
        return result

    def skip_stage(self, kwargs):
        LoggerUtils.debug(f"{self.id} [skip_stage] [{kwargs['stageID']}] beginning")

        paras = dict(kwargs, stageStatus=self.STAGE_STATUS_SKIPED)
        result = self._mark_task_stage(paras)

        LoggerUtils.debug(f"{self.id} [skip_stage] [{kwargs['stageID']}] finished")
        return result

    def _mark_task_stage(self, kwargs):
        self._update_stage_tag(kwargs)
        executor = self._get_executor(kwargs)
        try:
            error, [rowcount] = executor.execute(stmt_id="task_processes.mark_task_stage", paras=kwargs)
            if error:
                LoggerUtils.error(f"{self.id} [_mark_task_stage] [{kwargs}] failed: [code={error['code']}, msg={error['msg']}]")
                return False
            elif rowcount != 1:
                LoggerUtils.warning(f"{self.id} [_mark_task_stage] [{kwargs}] missed: [rowcount={rowcount}]")
                return False
        except Exception as e:
            LoggerUtils.error(f"{self.id} [_mark_task_stage] [{kwargs}] failed: [{e}]")
            return False
        return True

    def init_procedures(self, kwargs):
        procedures = kwargs.get("procedures")

        executor = self._get_executor(kwargs)

        LoggerUtils.info(f"{self.id} [init_procedures] [{kwargs['stageID']}] beginning")
        try:
            batch_paras = [dict(kwargs.copy(), procedureID=procedure_config[0] if isinstance(procedure_config, list) else procedure_config,
                            procedureName=procedure_config[1] if isinstance(procedure_config, list) else procedure_config, procedureStatus=self.PROCEDURE_STATUS_INITIAL) for procedure_config in procedures]
            executor.executemany(stmt_id="task_processes.init_task_procedures", paras=None, batch_paras=batch_paras)
        except Exception as e:
            LoggerUtils.error(f"{self.id} [init_procedures] [{kwargs}] failed: [{e}]")
            return False

        LoggerUtils.info(f"{self.id} [init_procedures] [{kwargs['stageID']}] finished")
        return True

    def check_procedure(self, kwargs):
        procedure_status = self._get_procedure_status(kwargs)

        LoggerUtils.debug(f"{self.id} [check_procedure] [{kwargs}] [status={procedure_status}]")

        if procedure_status == self.PROCEDURE_STATUS_SUCCESS or procedure_status == self.PROCEDURE_STATUS_SKIPED:
            return True
        else:
            return False

    def check_pre_procedure(self, kwargs):
        return True

    def get_pre_procedure(self, kwargs):
        pass

    def _get_procedure_status(self, kwargs):
        executor = self._get_executor(kwargs)
        error, [procedure_status] = executor.queryone("task_processes.get_task_procedure_status", kwargs)
        if error:
            LoggerUtils.error(f"{self.id} [_get_procedure_status] [{kwargs}] failed: [code={error['code']}, msg={error['msg']}]")
        return procedure_status[0]

    def begin_procedure(self, kwargs):
        LoggerUtils.debug(f"{self.id} [begin_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] beginning")

        paras = dict(kwargs, procedureStatus=self.PROCEDURE_STATUS_WORKING)
        result = self._mark_task_procedure(paras)

        LoggerUtils.debug(f"{self.id} [begin_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] finished")
        return result

    def fail_procedure(self, kwargs):
        LoggerUtils.debug(f"{self.id} [fail_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] beginning")

        paras = dict(kwargs, procedureStatus=self.PROCEDURE_STATUS_FAILED)
        result = self._mark_task_procedure(paras)

        LoggerUtils.debug(f"{self.id} [fail_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] finished")
        return result

    def finish_procedure(self, kwargs):
        LoggerUtils.debug(f"{self.id} [finish_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] beginning")

        paras = dict(kwargs, procedureStatus=self.PROCEDURE_STATUS_SUCCESS)
        result = self._mark_task_procedure(paras)

        LoggerUtils.debug(f"{self.id} [finish_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] finished")
        return result

    def skip_procedure(self, kwargs):
        LoggerUtils.debug(f"{self.id} [skip_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] beginning")

        paras = dict(kwargs, procedureStatus=self.PROCEDURE_STATUS_SKIPED)
        result = self._mark_task_procedure(paras)

        LoggerUtils.debug(f"{self.id} [skip_procedure] [{kwargs['stageID']}:{kwargs['procedureID']}] finished")
        return result

    def _mark_task_procedure(self, kwargs):
        self._update_stage_tag(kwargs)
        executor = self._get_executor(kwargs)
        try:
            error, [rowcount] = executor.execute(stmt_id="task_processes.mark_task_procedure", paras=kwargs)
            if error:
                LoggerUtils.error(f"{self.id} [_mark_task_procedure] [{kwargs}] failed: [code={error['code']}, msg={error['msg']}]")
                return False
            elif rowcount != 1:
                LoggerUtils.error(f"{self.id} [_mark_task_procedure] [{kwargs}] failed: [rowcount={rowcount}]")
                return False
        except Exception as e:
            LoggerUtils.error(f"{self.id} [_mark_task_procedure] [{kwargs}] failed: [{e}]")
            return False
        return True

    def get_stage_worker(self, kwargs):
        stage_id = kwargs.get("stageID")
        stage_config = self.processes_config.get(stage_id, None)
        if stage_config:
            module_config = stage_config.get("module", None)
            if module_config:
                module = importlib.import_module(module_config)
                return module.get_stage_worker()
            else:
                import task.db_task_worker
                return task.db_task_worker.get_stage_worker()

    def get_procedure_worker(self, kwargs):
        stage_id = kwargs.get("stageID")
        stage_config = self.processes_config.get(stage_id, None)
        if stage_config:
            module_config = stage_config.get("module", None)
            if module_config:
                module = importlib.import_module(module_config)
                return module.get_procedure_worker()
            else:
                import task.db_task_worker
                return task.db_task_worker.get_procedure_worker()
