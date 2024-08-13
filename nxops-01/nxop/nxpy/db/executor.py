# _*_ coding: utf-8 _*_
# @Time: 2024/4/18 11:13
# @Author: LBJ辉
# @File: executor
# @Project: nxops-01
import importlib
import importlib.util
import os
import platform
import re
import uuid

import rapidjson
from nxpy.db.datasource import DataSourceUtils
from nxpy.os.path import PathUtils
from nxpy.security.realm import Securable, SecurityRealm

sql_pattern = re.compile(r"(\$\{[\[\]\.a-zA-Z0-9_]+\})|(#\{[\[\]\.a-zA-Z0-9_]+\})")
if_cases_pattern = re.compile(r"<if\s+.+</if>")
if_items_pattern = re.compile(r"(<if\s+test=\")(.+)(\"\s*>)(.+)(</if>)")


def replace_has_expr(matched):
    var_name = str(matched.group('var_name'))
    return f"'{var_name}' in dir()"


def parse_has_expr(expr):
    a = re.compile(r"has\((?P<var_name>[^\)]+)\)")
    return re.sub(r"has\((?P<var_name>[^\)]+)\)", replace_has_expr, expr)


class EasyDBStatement(Securable):
    # 这个函数是一个类的构造函数，用于初始化类的属性。该类表示一个数据库操作语句，包含了一些基本信息，如id、ware_id、executor_id、module、stmt等。其中，stmt可以是一个列表，如果是一个列表，则会逐个遍历子语句，创建多个子数据库操作语句对象，并将它们保存在一个列表中。此外，该函数还设置了某些属性的默认值，并调用了父类的构造函数。如果该对象没有父对象，则会调用bind_rules方法。
    def __init__(self, id, ware_id, executor_id, module, stmt, realm=None, parent=None):
        self.id = id  # init_task_stages
        self.ware_id = ware_id  # task_process
        self.executor_id = executor_id  # task
        self.module = module
        self.config = stmt
        '''
        ("""INSERT IGNORE INTO task.t_TaskStage(TaskID, RunID, StageID, StageTag, StageName, UpdateDate, UpdateTime, Status, Remark)
                                VALUES(#{taskID}, #{runID}, #{stageID}, #{stageTag}, #{stageName}, DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(), '%H:%i:%S'), #{stageStatus}, #{stageRemark})""",
                         {"many": True})
        '''
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
                sub_statement = EasyDBStatement(f"{id}.{idx}", ware_id, self.executor_id, self.module, sub_stmt, realm,
                                                parent=self)
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
            self.realm = SecurityRealm(auth_id=realm.get("auth_id", None), auth_level=realm.get("auth_level", None),
                                       auth_token=realm.get("auth_token", None), roles=realm.get("roles", None))

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
                    sub_id = (self.id + "." + sub_stmt.get("id")) if isinstance(sub_stmt,
                                                                                dict) and "id" in sub_stmt else f"{self.id}.{idx}"
                    sub_statement = EasyDBStatement(sub_id, self.ware_id, self.executor_id, self.module, sub_stmt,
                                                    parent=self)
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
                self.cases_if.append({"holder": raw_case_if, "when": parse_has_expr(raw_case_items_if[0][1]),
                                      "then": raw_case_items_if[0][3]})

    def _push_preload_parameter(self, parameter):
        self.preloads.append(parameter)

    def _push_runtime_parameter(self, parameter):
        self.runtimes.append(parameter)


class EasyDBExecutor:
    executors = {}

    def __init__(self, eid, *args, **kwargs):
        super().__init__()

        '''
        `.pyd` 文件是 Python 在 Windows 平台上用于扩展模块的动态链接库（Dynamic-Link Library）文件。这些文件通常包含用 C、C++ 或其他语言编写的 Python 扩展，它们被编译成二进制格式，以便 Python 解释器可以加载和使用它们。
        Python 的扩展模块允许开发者使用比纯 Python 更快或更底层的语言来实现某些功能，并将其作为 Python 模块导入和使用。`.pyd` 文件就是这些扩展模块的二进制形式。
        例如，如果你有一个用 C 或 C++ 编写的 Python 扩展，你可以使用 Python 的 C API 将其编译成一个 `.pyd` 文件，然后就可以在 Python 脚本中像导入普通 Python 模块一样导入它。
        在 Python 的 `site-packages` 目录下，你可能会找到许多 `.pyd` 文件，这些都是 Python 的第三方库或扩展模块的一部分。
        需要注意的是，`.pyd` 文件是特定于 Windows 平台的。在其他操作系统（如 Linux 或 macOS）上，Python 扩展通常被编译为共享对象文件（如 `.so` 文件在 Linux 上）或动态库文件（如 `.dylib` 文件在 macOS 上）。
        '''

        self.lib_ware_suffix = ".so"
        if platform.system() == "Windows":
            self.lib_ware_suffix = ".pyd"  # 如果是Windows系统，则设置为.pyd，否则设置为.so。
        self.lib_ware_suffix_rpos = -1 * len(self.lib_ware_suffix)

        '''
        "task"(eid): {
            "datasource": "simrun",(datasource_id)
            "package": "nxpy.task.easymodules"(package)
        }
        '''
        self.eid = eid
        self.datasource_id = kwargs.get("datasource", None)
        self._datasource = None
        self.package = kwargs.get("package", None)
        self.home = kwargs.get("home", None)
        self.recursive = kwargs.get("recursive", None)
        self.fixes = kwargs.get("fixes", None)
        self._wares = kwargs.get("wares", None)

        if self.datasource_id:
            self._datasource = DataSourceUtils.get_datasource(datasource_id=self.datasource_id)

        # 如果home存在，则将其转换为一个包含路径和包名的元组列表，并存储在home属性中。
        if self.home:
            self.home = [(PathUtils.get_real_path(item), None) for item in self.home] if isinstance(self.home,
                                                                                                    list) else [
                PathUtils.get_real_path(self.home)]
        # 如果package存在，则使用importlib.import_module()方法导入指定的模块，并获取其路径，然后将其转换为一个包含路径和包名的元组，并存储在home属性中。
        elif self.package:
            self.home = [(importlib.import_module(item).__path__[0], item) for item in self.package] if isinstance(
                self.package, list) else [(importlib.import_module(self.package).__path__[0], self.package)]
        # self.home [('D:\\Desktop\\note-docsify\\nxops-01\\nxop\\nxpy\\task\\easymodules', 'nxpy.task.easymodules')]
        self.wares = {}

        # 遍历home属性中的每个路径，加载所有以.py或.so（或.pyd）结尾的文件，并将其作为组件加载到wares字典中。
        if self.home:
            for (ware_home, package_name) in self.home:
                for root, dirs, files in os.walk(ware_home):
                    # root D:\Desktop\note-docsify\nxops-01\nxop\nxpy\task\easymodules
                    # dirs []
                    # files ['task_process.py']
                    if not self.recursive and root != ware_home:
                        continue
                    for file_name in files:
                        if file_name[-3:] == ".py" or file_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
                            self._load_ware(file_name, ware_home=ware_home, package_name=package_name,
                                            is_lib=True if file_name[
                                                           self.lib_ware_suffix_rpos:] == self.lib_ware_suffix else False,
                                            file_path=None if root == ware_home else os.path.join(root, file_name))

        self.executors.update({self.eid: self})

    # 该函数用于从文件中导入ware，根据是否修复标志is_fix和ware_home进行不同的操作。如果is_fix为False且ware_home存在，则根据file_path替换ware_home、去除扩展名和lib_ware_suffix后导入模块，返回导入的模块及其别名、ware和realm。否则，生成随机模块名，根据file_path或ware_home和ware_name构建模块位置，通过spec_from_file_location和module_from_spec导入模块并执行，返回导入的模块及其别名、ware和realm。
    def _import_ware_from_file(self, ware_id, ware_name, ware_home, package_name, is_fix=False, file_path=None):
        # ware_id task_process
        # ware_name task_process.py
        # ware_home D:\Desktop\note-docsify\nxops-01\nxop\nxpy\task\easymodules
        # package_name nxpy.task.easymodules
        # is_fix False
        # file_path None
        if not is_fix and ware_home:
            module_ware_id = ware_id
            if file_path:
                module_ware_id = file_path.replace(ware_home, "").replace(".py", "").replace(self.lib_ware_suffix,
                                                                                             "").replace(os.path.sep,
                                                                                                         ".")
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

    # 该函数用于加载一个名为ware_name的仓库，根据参数的不同，可以加载为库文件或普通文件，并进行一系列处理和导入操作。具体步骤包括：根据ware_name后缀判断其类型，更新ware_id；检查是否已经加载过该仓库，如果是则直接返回；通过_import_ware_from_file方法导入仓库，并得到相关数据；根据导入的数据，创建并更新easy_stmt，最后更新wares字典。
    def _load_ware(self, ware_name, ware_home, package_name, is_lib=False, is_fix=False, file_path=None):
        # ware_name task_process.py
        # ware_home  D:\Desktop\note-docsify\nxops-01\nxop\nxpy\task\easymodules
        # package_name nxpy.task.easymodules
        # is_lib False
        # file_path None
        ware_id = ware_name  # task_process.py
        if ware_name[-3:] == ".py":
            ware_id = ware_id[:-3]  # task_process
        elif ware_name[self.lib_ware_suffix_rpos:] == self.lib_ware_suffix:
            ware_id = ware_id[:self.lib_ware_suffix_rpos]
        else:
            ware_name += self.lib_ware_suffix if is_lib else ".py"

        if self._wares and ware_id not in self._wares:
            return

        module, n_ware_id, raw_ware, raw_realm = self._import_ware_from_file(ware_id, ware_name, ware_home,
                                                                             package_name, is_fix=is_fix,
                                                                             file_path=file_path)
        well_ware = self.wares.get(n_ware_id, {})
        for stmt_id, stmt in raw_ware.items():
            easy_stmt = EasyDBStatement(stmt_id, ware_id, self.eid, module, stmt, raw_realm)
            well_ware.update({stmt_id: easy_stmt})

        self.wares.update({ware_id: well_ware, n_ware_id: well_ware})


class EasyDBExecutorUtils:
    # 加载数据库 executor 配置
    @staticmethod
    def load_executors(config_file_path):
        with open(config_file_path, encoding="UTF-8") as cf:
            config = rapidjson.load(cf)

            for (execuotr_id, execuotr_config) in config.items():
                EasyDBExecutor(execuotr_id, **execuotr_config)
