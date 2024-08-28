# _*_ coding: utf-8 _*_
# @Time: 2024/5/17 9:55
# @Author: LBJ辉
# @File: code4-4-match
# @Project: nxops-01

x = 10
match x:
    case 1:
        print('x is 1')
    case 2:
        print('x is 2')
    case _:
        print('x is not 1 or 2')
