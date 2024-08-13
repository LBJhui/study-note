# _*_ coding: utf-8 _*_
# @Time: 2024/5/21 10:59
# @Author: LBJ辉
# @File: code7-1-异常处理
# @Project: nxops-01

# NameError
print('hello world')
# prlnt('hello world')  # 函数名拼写错误
a = '111'
print(a)
# print(aa)  # 变量名拼写错误
# print(b)   # 使用一个不存在的变量

# SyntaxError  IndentationError
# if 'he' == 'hi':
# print('hello')
# TypeError
# print(3+'2')
# AttributeError
tp = (1, 3, 5)
# tp[2]=4
# print(tp)
# tp.append(2)
# print(tp)
# KeyError
d = {1: 2, 3: 4}
# print(d[2])
# IndexError
print(tp[4])
