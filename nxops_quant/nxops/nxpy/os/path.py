# -*- coding: UTF-8 -*-
# cython: language_level=3

'''
@Author       : yi.mt
@Date         : 2020-06-10 17:42:30
@LastEditTime : 2020-07-22 13:40:02
@LastEditors  : yi.mt
@Description  : 
'''

import os
import platform


class PathUtils:

    @staticmethod
    def get_real_path(file_path):
        system = platform.system()
        if system == "Windows":
            file_path = file_path.replace("${", "%")
            file_path = file_path.replace("}", "%")

        output = os.popen("echo " + file_path)
        return output.readline().replace("\n", "").replace("\r", "")
