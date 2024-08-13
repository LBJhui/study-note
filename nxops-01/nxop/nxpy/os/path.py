# _*_ coding: utf-8 _*_
# @Time: 2024/4/18 10:01
# @Author: LBJ辉
# @File: path
# @Project: nxops-01
import os
import platform


class PathUtils:
    @staticmethod
    def get_real_path(file_path):
        system = platform.system()  # Windows
        if system == "Windows":
            file_path = file_path.replace("${", "%")
            file_path = file_path.replace("}", "%")

        output = os.popen("echo " + file_path)
        return output.readline().replace("\n", "").replace("\r", "")
