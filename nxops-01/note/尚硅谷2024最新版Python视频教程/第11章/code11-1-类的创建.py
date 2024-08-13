# _*_ coding: utf-8 _*_
# @Time: 2024/5/28 9:10
# @Author: LBJ辉
# @File: code11-1-类的创建
# @Project: nxops-01

class Player(object):  # object 基类
    pass


tom = Player()  # 类的实例化（创建对象）
print(type(tom))
print(isinstance(tom, object))
print(isinstance(tom, Player))
