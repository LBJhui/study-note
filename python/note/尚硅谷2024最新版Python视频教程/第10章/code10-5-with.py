# _*_ coding: utf-8 _*_
# @Time: 2024/5/24 10:46
# @Author: LBJ辉
# @File: code10-5-with
# @Project: nxops-01

with open('test.txt', mode='r', encoding='utf-8') as f:
    context = f.read()
    print(context)
print('hello')
