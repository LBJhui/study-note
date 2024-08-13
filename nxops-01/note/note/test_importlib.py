# _*_ coding: utf-8 _*_
# @Time: 2024/3/28 9:39
# @Author: LBJ辉
# @File: test_importlib
# @Project: nxops
import importlib

# 创建模块规范
spec = importlib.util.spec_from_file_location("module_name", "module_path")

# 根据规范创建模块
module = importlib.util.module_from_spec(spec)

# 执行模块
spec.loader.exec_module(module)

# 动态导入模块
module = importlib.import_module("module_name")
