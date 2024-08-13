# _*_ coding: utf-8 _*_
# @Time: 2024/5/14 9:53
# @Author: LBJ辉
# @File: 6.字段
# @Project: nxops-01

# 遍历所有的键-值对

user_0 = {
    'username': 'LBJhui',
    'first': 'lee',
    'last': 'hui'
}

for key, value in user_0.items():
    print('\nKey:' + key)
    print('Value:' + value)
