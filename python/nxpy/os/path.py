# _*_ coding: utf-8 _*_
# @Time: 2024/8/13 14:44
# @Author: LBJ辉
# @File: path
# @Project: python
import os
import platform


class PathUtils:
    @staticmethod
    def get_real_path(file_path):
        system = platform.system()
        if system == 'Windows':
            file_path = file_path.replace("${", "%")
            file_path = file_path.replace("}", "%")

        output = os.popen('echo ' + file_path)
        return output.readline().replace('\n', '').replace("\r", "")
