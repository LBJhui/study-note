# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2021-08-30 14:42:51
LastEditTime : 2022-08-11 18:24:51
LastEditors  : yi.mt
Description  : 
'''

import os
import delegator

from nxpy.context import AppContext

from nxpy.os.path import PathUtils

from nxpy.config.easy_config import EasyConfigUtils

from nxpy.task.task_worker import TaskWorker_Stage, TaskWorker_Procedure
            
class ShellWorker_Procedure(TaskWorker_Procedure):
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


    def callback_command(self, shell, shell_config, command_config, kwargs):
        if shell:
            out, err = shell.out, shell.err

            if err:
                os.sys.stderr.write("\033[1;31m%s\033[0m" % err)
                need_report = shell_config.get("need_report", False)
                if need_report:
                    task_processes = kwargs.get("task_processes")
                    self.report(f"{task_processes.id}", f"{self.worker_id}执行信息", f"[{command_config}][err][{err}]", kwargs)

            if out:
                os.sys.stderr.write("\033[1;32m%s\033[0m" % out)

                if isinstance(command_config, dict) and command_config.get("out_parameter_name", None):
                    line_separator = command_config.get("line_separator", ";")
                    out_parameter_name = command_config.get("out_parameter_name")
                    out_parameter_value = str(out).replace("\r","").replace("\n", line_separator)
                    kwargs.update({out_parameter_name: out_parameter_value})
                    self.export(kwargs, {out_parameter_name: out_parameter_value})
                    
                need_report = shell_config.get("need_report", False)
                if need_report:
                    task_processes = kwargs.get("task_processes")
                    self.report(f"{task_processes.id}", f"{self.worker_id}执行信息", f"[{command_config}][out][{out}]", kwargs)

    def do_deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")

        result = True
        shell_config = kwargs.get("shell")
        commands = shell_config.get("commands")
        for command_config in commands:
            command = self.prepare_command(shell_config, command_config, kwargs)
            if command:
                try:
                    shell = delegator.run(command)
                    self.callback_command(shell, shell_config, command_config, kwargs)
                except Exception as e:
                    self.error(f"failed: [{e}]")
                    kwargs.update({"procedureRemark": str(e)})
                    result = False
                    break

        return result


class ShellWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return ShellWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        serial = stage_config.get("serial", True)
        
        all_executed = True
        shells = stage_config.get("shells")
        for shell_config in shells:
            shell_id = shell_config.get("id")

            sheller = self._default_procedure_worker_class(kwargs)()
            
            parameters = kwargs.copy()
            parameters.update({"procedureID": shell_id, "shell": shell_config})
            if not sheller.deal(parameters):
                all_executed = False
                if serial:
                    break
            self.export(kwargs, parameters.get("__export__", {}))

        return all_executed

    def init_procedures(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        shells = stage_config.get("shells")
        process_paras = dict(kwargs, procedures=[[shell_config.get("id"), shell_config.get("title", shell_config.get("id"))] for shell_config in shells])

        result = task_processes.init_procedures(process_paras)
        return result


def get_procedure_worker():
    return ShellWorker_Procedure()


def get_stage_worker():
    return ShellWorker_Stage()