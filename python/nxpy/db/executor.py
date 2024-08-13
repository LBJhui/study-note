# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 15:42
# @Author: LBJ辉
# @File: executor
# @Project: python
import importlib
import os
import platform
import uuid

import rapidjson

from nxpy.db.datasource import DataSourceUtils
from nxpy.os.path import PathUtils
from nxpy.security.realm import  Securable

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

class EasyDBExecutor:
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
            # [('D:\\Desktop\\study-note\\python\\nxpy\\task\\easymodules', 'nxpy.task.easymodules')]
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
class EasyDBExecutorUtils:
    @staticmethod
    def load_executors(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)
            for (executor_id, executor_config) in config.items():
                EasyDBExecutor(executor_id, **executor_config)
