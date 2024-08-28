# _*_ coding: utf-8 _*_
# @Time: 2024/5/24 9:58
# @Author: LBJ辉
# @File: code10-1-文件读取
# @Project: nxops-01

import os

# 打开文件
f = open('test.txt')  # 相对路径 <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp936'>
path = os.getcwd()  # D:\Desktop\note-docsify\nxops-01\note\尚硅谷2024最新版Python视频教程\第10章
filename = path + '/test.txt'
f = open(filename, mode='r', encoding='utf-8')  # 绝对路径
# 读取文件
context = f.read(5)  # LBJhu
print(context)
context = f.readline()
print('context', context)
context = f.readlines()
print(context)
# 关闭文件
f.close()
