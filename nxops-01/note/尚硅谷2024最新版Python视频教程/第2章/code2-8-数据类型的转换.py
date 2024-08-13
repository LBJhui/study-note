# _*_ coding: utf-8 _*_
# @Time: 2024/5/16 14:18
# @Author: LBJ辉
# @File: code2-8-数据类型的转换
# @Project: nxops-01

# 转换为整数 int
# 纯数字的字符串
s = '1024'
print(type(s))
n = int(s)
print(type(n))

# 浮点数 float --> 整数 int
s1 = 2.23
print(int(s1))

# 布尔 bool --> 整数 int
s2, s3 = True, False
print(int(s2), int(s3))

# 转换为浮点数 float
# str --> float
print(float(s))  # 有没有小数点都可以

# int --> float
print(float(n))

# bool --> float
print(float(s2), float(s3))

# 转换为布尔 bool
# str --> bool
# int --> bool
# float --> bool

# 转换为字符串 str

# 进制的转换
s = '1a'
print(int(s, 16))
