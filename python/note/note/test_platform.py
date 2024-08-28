# _*_ coding: utf-8 _*_
# @Time: 2024/3/27 10:22
# @Author: LBJ辉
# @File: test_platform
# @Project: nxops

import platform

# 获取操作系统名称
os_name = platform.system()
print(f'操作系统名称: {os_name}')  # 操作系统名称: Windows

# 获取操作系统版本
os_version = platform.version()
print(f'操作系统版本: {os_version}')  # 操作系统版本: 10.0.19041

# 获取计算机的处理器名称
processor_name = platform.processor()
print(f'处理器名称: {processor_name}')  # 处理器名称: AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD

# 获取计算机的处理器架构
processor_architecture = platform.architecture()
print(f'处理器架构: {processor_architecture}')  # 处理器架构: ('64bit', 'WindowsPE')

# 获取Python版本
python_version = platform.python_version()
print(f'Python版本: {python_version}')  # Python版本: 3.8.8rc1

# 获取Python解释器名称
python_implementation = platform.python_implementation()
print(f'Python解释器名称: {python_implementation}')  # Python解释器名称: CPython

# 获取Python解释器实现名称
python_implementation_name = platform.python_implementation()
print(f'Python解释器实现名称: {python_implementation_name}')  # Python解释器实现名称: CPython

'''
报错：partially initialized module 'platform' has no attribute 'system' (most likely due to a circular import)

解决方法：将文件名改为其他非类名、包名。
'''
