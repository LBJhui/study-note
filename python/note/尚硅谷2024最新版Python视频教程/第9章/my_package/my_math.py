# _*_ coding: utf-8 _*_
# @Time: 2024/5/23 9:59
# @Author: LBJ辉
# @File: my_math
# @Project: nxops-01

author = 'mia'


def add(a, b):
    return a + b


def total(*args):
    '''
    参数args:接收一个列表
    return：a列表中每个元素的平方和
    '''
    result = 0
    for i in args:
        result = result + i ** 2
    return result
