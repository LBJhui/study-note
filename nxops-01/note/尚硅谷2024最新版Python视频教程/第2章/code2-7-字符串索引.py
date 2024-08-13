# _*_ coding: utf-8 _*_
# @Time: 2024/5/16 14:06
# @Author: LBJ辉
# @File: code2-7-字符串索引
# @Project: nxops-01

s = 'hello world'
print(s[0])
print(s[4])
print(s[-1])
# 切片 变量名[起始索引:结束索引+1:步数]
# 步数默认为 1，可省略不写
# 起始索引默认为 0，可省略不写
# 结束索引默认为 -1，可省略不写
print(s[0:4])  # 包头不包尾
print(s[0:9:2])

# 字符串反转
s2 = '123456789'
print(s2[-1:-10:-1])
print(s2[::-1])
