# _*_ coding: utf-8 _*_
# @Time: 2024/5/22 9:24
# @Author: LBJ辉
# @File: code7-4-错误处理
# @Project: nxops-01

# 运行，从错误信息中找到问题
print(11)

# 打印相关信息
for i in range(10):
    print('-'*30)
    print(i)
    for i in range(5):
        print('内层循环')
        print(i)
        print('*' * i)
