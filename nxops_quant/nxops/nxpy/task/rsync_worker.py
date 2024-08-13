# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
Author       : yi.mt
Date         : 2020-10-20 14:27:24
LastEditTime : 2020-10-20 14:29:13
LastEditors  : yi.mt
Description  : 
'''

import os
import rapidjson

from nxpy.context import AppContext

from nxpy.os.path import PathUtils

from nxpy.rsh.easy_rsh import EasyRSH, EasyRSHUtils
from nxpy.rsh.easy_hosts import EasyHostsUtils
from nxpy.config.easy_config import EasyConfigUtils

from nxpy.task.task_worker import TaskWorker_Stage, TaskWorker_Procedure


class RsyncWorker_Procedure(TaskWorker_Procedure):
    def __init__(self):
        super().__init__()

    def do_deal(self, kwargs):
        stage_id = kwargs.get("stageID")
        procedure_id = kwargs.get("procedureID")

        rsh = kwargs.get("rsh")
        rsync_type = kwargs.get("type")
        source_file = kwargs.get("source_file", None)
        source_home = kwargs.get("source_home", None)
        target_file = kwargs.get("target_file", None)
        target_home = kwargs.get("target_home", None)

        result = True
        try:
            if rsync_type == "get":
                if source_file:
                    if target_file:
                        source_file = EasyConfigUtils.easy_parse(source_file, kwargs)
                        is_required = True
                        ignore_existed = False
                        if source_file[0] == "?":
                            is_required = False
                            source_file = source_file[1:]
                        if source_file[0] == "!":
                            ignore_existed = True
                            source_file = source_file[1:]
                            
                        source_file = rsh.remote_path(source_file)
                        target_file = PathUtils.get_real_path(target_file)
                        if is_required or rsh.remote_exists(source_file):
                            EasyRSHUtils.get_file_to_file(rsh, source_file, target_file, ignore_existed)
                    else:
                        source_files = source_file if isinstance(source_file, list) else [source_file]
                        for source_file in source_files:
                            source_file = EasyConfigUtils.easy_parse(source_file, kwargs)
                            is_required = True
                            ignore_existed = False
                            if source_file[0] == "?":
                                is_required = False
                                source_file = source_file[1:]
                            if source_file[0] == "!":
                                ignore_existed = True
                                source_file = source_file[1:]

                            rename_flag_pos = source_file.find("->")
                            target_name = None 
                            if rename_flag_pos > 0:
                                target_name = source_file[rename_flag_pos + 2:]
                                source_file = source_file[0:rename_flag_pos]

                            source_file = rsh.remote_path(source_file)
                            target_home = PathUtils.get_real_path(target_home)
                            if is_required or rsh.remote_exists(source_file):
                                EasyRSHUtils.get_file_to_dir(rsh, source_file, target_home, target_name, ignore_existed)
                else:
                    ignore_existed = False
                    if source_home[0] == "!":
                        ignore_existed = True
                        source_home = source_home[1:]
                    source_home = rsh.remote_path(source_home)
                    target_home = PathUtils.get_real_path(target_home)
                    EasyRSHUtils.get_dir(rsh, source_home, target_home, ignore_existed)
            else:
                if source_file:
                    if target_file:
                        source_file = EasyConfigUtils.easy_parse(source_file, kwargs)
                        is_required = True
                        ignore_existed = False
                        if source_file[0] == "?":
                            is_required = False
                            source_file = source_file[1:]
                        if source_file[0] == "!":
                            ignore_existed = True
                            source_file = source_file[1:]
                            
                        source_file = PathUtils.get_real_path(source_file)
                        target_file = rsh.remote_path(target_file)
                        if is_required or os.path.exists(source_file):
                            EasyRSHUtils.put_file_to_file(rsh, source_file, target_file, ignore_existed)
                    else:
                        source_files = source_file if isinstance(source_file, list) else [source_file]
                        for source_file in source_files:
                            source_file = EasyConfigUtils.easy_parse(source_file, kwargs)
                            is_required = True
                            ignore_existed = False
                            if source_file[0] == "?":
                                is_required = False
                                source_file = source_file[1:]
                            if source_file[0] == "!":
                                ignore_existed = True
                                source_file = source_file[1:]

                            rename_flag_pos = source_file.find("->")
                            target_name = None 
                            if rename_flag_pos > 0:
                                target_name = source_file[rename_flag_pos + 2:]
                                source_file = source_file[0:rename_flag_pos]
                            source_file = PathUtils.get_real_path(source_file)
                            target_home = rsh.remote_path(target_home)
                            if is_required or os.path.exists(source_file):
                                EasyRSHUtils.put_file_to_dir(rsh, source_file, target_home, target_name, ignore_existed)
                else:
                    ignore_existed = False
                    if source_home[0] == "!":
                        ignore_existed = True
                        source_home = source_home[1:]
                    source_home = PathUtils.get_real_path(source_home)
                    target_home = rsh.remote_path(target_home)
                    EasyRSHUtils.put_dir(rsh, source_home, target_home, ignore_existed)
        except Exception as e:
            self.error(f"failed: [{e}]")
            kwargs.update({"procedureRemark": str(e)})
            result = False

        return result


class RsyncWorker_Stage(TaskWorker_Stage):
    def __init__(self):
        super().__init__()

    def _default_procedure_worker_class(self, kwargs):
        return RsyncWorker_Procedure

    def do_deal(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)

        serial = stage_config.get("serial", True)
        rsyncs = stage_config.get("rsyncs")
        rsyncs_config_path = AppContext.get_config_path(rsyncs)

        all_loaded = True
        with open(rsyncs_config_path, encoding="UTF-8") as df:
            rsyncs_config = rapidjson.load(df)
            rsync_idx = 0
            for rsync_config in rsyncs_config:
                rsync_type = rsync_config.get("type")

                procedure_id = rsync_config.get("id", None)
                procedure_id = procedure_id if procedure_id else f"rsync_{rsync_idx}"
                rsync_idx += 1

                source_host = rsync_config.get("source_host", None)
                source_home = EasyConfigUtils.easy_parse(rsync_config.get("source_home", None), kwargs)
                source_file = rsync_config.get("source_file", None)

                target_host = rsync_config.get("target_host", None)
                target_home = EasyConfigUtils.easy_parse(rsync_config.get("target_home", None), kwargs)
                target_file = EasyConfigUtils.easy_parse(rsync_config.get("target_file", None), kwargs)

                loader = self._default_procedure_worker_class(kwargs)()

                rsh = EasyRSH()
                rsh.connect_s(EasyHostsUtils.get_host(source_host) if rsync_type == "get" else EasyHostsUtils.get_host(target_host))
                    
                parameters = kwargs.copy()
                parameters.update({"rsh": rsh, "type": rsync_type, "source_file": source_file, "source_home": source_home, "target_file": target_file, "target_home": target_home, "procedureID": procedure_id})
                
                if not loader.deal(parameters):
                    all_loaded = False
                    if serial:
                        break
                    
        return all_loaded

    def init_procedures(self, kwargs):
        task_processes = kwargs.get("task_processes")
        stage_config = task_processes.get_stage(kwargs)
        
        rsyncs = stage_config.get("rsyncs")
        rsyncs_config_path = AppContext.get_config_path(rsyncs)

        all_loaded = True
        with open(rsyncs_config_path, encoding="UTF-8") as df:
            rsyncs_config = rapidjson.load(df)
            procedures = []
            rsync_idx = 0
            for rsync_config in rsyncs_config:
                procedure_id = rsync_config.get("id", None)
                procedure_id = procedure_id if procedure_id else f"rsync_{rsync_idx}"
                rsync_idx += 1

                procedure_name = rsync_config.get("title", None)
                procedure_name = procedure_name if procedure_name else procedure_id

                procedures.append([procedure_id, procedure_name])

            process_paras = dict(kwargs, procedures=procedures)
            
            result = task_processes.init_procedures(process_paras)
            return result


def get_procedure_worker():
    return RsyncWorker_Procedure()


def get_stage_worker():
    return RsyncWorker_Stage()