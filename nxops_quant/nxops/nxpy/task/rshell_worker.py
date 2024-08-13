# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-06-28 11:18:59
LastEditTime : 2022-08-11 18:22:31
LastEditors  : yi.mt
Description  : 
'''

import os
import time

from nxpy.context import AppContext

from nxpy.os.path import PathUtils

from nxpy.rsh.easy_rsh import EasyRSH, EasyRSHUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.config.easy_config import EasyConfigUtils

from nxpy.task.task_worker import TaskWorker_Stage, TaskWorker_Procedure

from nxpy.task.task_processes import EasyTaskThread
            
class RshellWorker_Procedure(TaskWorker_Procedure):
    def __init__(self):
        super().__init__()

    def prepare_command(self, shell, command, kwargs):
        cmd_string = command
        if isinstance(command, list):
            cmd_string = command[0]
        elif isinstance(command, dict):
            cmd_string = command.get("cmd")

        cmd_string = EasyConfigUtils.easy_parse(cmd_string, kwargs)

        return cmd_string

    def callback_command(self, remote_shell, shell_config, command_config, kwargs):
        if remote_shell:
            stdin, stdout, stderr = remote_shell

            err_lines = stderr.readlines()
            if err_lines:
                os.sys.stderr.write("\033[1;31m%s\033[0m" % "".join(err_lines))
                need_report = shell_config.get("need_report", False)
                if need_report:
                    task_processes = kwargs.get("task_processes")
                    self.report(f"{task_processes.id}", f"{self.worker_id}执行信息", f"[{command_config}][err][{err_lines}]", kwargs)

            out_lines = stdout.readlines()
            if out_lines:
                os.sys.stderr.write("\033[1;32m%s\033[0m" % "".join(out_lines))

                if isinstance(command_config, dict) and command_config.get("out_parameter_name", None):
                    line_separator = command_config.get("line_separator", ";")
                    out_parameter_name = command_config.get("out_parameter_name")
                    out_parameter_value = line_separator.join(out_lines)
                    kwargs.update({out_parameter_name: out_parameter_value})
                    self.export(kwargs, {out_parameter_name: out_parameter_value})

                need_report = shell_config.get("need_report", False)
                if need_report:
                    task_processes = kwargs.get("task_processes")
                    self.report(f"{task_processes.id}", f"{self.worker_id}执行信息", f"[{command_config}][out][{out_lines}]", kwargs)

    def do_deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")
        rsh = kwargs.get("rsh")

        result = True
        shell_config = kwargs.get("shell")
        commands = shell_config.get("commands")
        for command_config in commands:
            remote_command = self.prepare_command(shell_config, command_config, kwargs)
            if remote_command:
                try:
                    remote_shell = rsh.execute(remote_command)
                    self.callback_command(remote_shell, shell_config, command_config, kwargs)
                except Exception as e:
                    self.error(f"failed: [{e}]")
                    kwargs.update({"procedureRemark": str(e)})
                    result = False
                    break

        return result


class RshellWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return RshellWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        serial = stage_config.get("serial", True)
        
        all_executed = True
        shells = stage_config.get("shells")
        deal_threads = []
        failed_rshells = []
        for shell_config in shells:
            shell_id = shell_config.get("id")
            if serial:
                if not self.deal_rshell(shell_config, kwargs):
                    all_executed = False
                    failed_rshells.append(shell_id)
                    break
            else:
                deal_thread = EasyTaskThread(id=shell_id, target=self.deal_rshell, args=(shell_config, kwargs))
                deal_threads.append(deal_thread)
                deal_thread.start()
        
        if not serial:
            while True:
                all_finished = True
                for deal_thread in deal_threads:
                    if deal_thread.is_alive():
                        all_finished = False
                if all_finished:
                    for deal_thread in deal_threads:
                        if deal_thread.get_result() == False:
                            all_executed = False
                            failed_rshells.append(deal_thread.id)
                    break
                else:
                    time.sleep(1)

        if not all_executed:
            self.error(f"failed: {failed_rshells}")
            self.report(f"{task_processes.id}", f"{task_processes.id}运行状态", f"[{self.worker_id}]执行失败: {failed_rshells}")

        return all_executed

    def init_procedures(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        shells = stage_config.get("shells")
        process_paras = dict(kwargs, procedures=[[shell_config.get("id"), shell_config.get("title", shell_config.get("id"))] for shell_config in shells])

        result = task_processes.init_procedures(process_paras)
        return result

    def deal_rshell(self, shell_config, kwargs):
        shell_id = shell_config.get("id")
        host_id = shell_config.get("host")
        remote_host_config = EasyHostsUtils.get_host(host_id)

        rsh = EasyRSH()
        rsh.connect_s(remote_host_config)

        sheller = self._default_procedure_worker_class(kwargs)()
        
        parameters = kwargs.copy()
        parameters.update({"rsh": rsh, "procedureID": shell_id, "shell": shell_config})
        
        result = sheller.deal(parameters)

        self.export(kwargs, parameters.get("__export__", {}))

        return result


def get_procedure_worker():
    return RshellWorker_Procedure()


def get_stage_worker():
    return RshellWorker_Stage()