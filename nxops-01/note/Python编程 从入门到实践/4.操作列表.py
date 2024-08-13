# _*_ coding: utf-8 _*_
# @Time: 2024/5/9 10:19
# @Author: LBJ辉
# @File: 4.操作列表
# @Project: nxops-01

cars = ['shenlan', 'byd', 'xiaopeng', 'lixiang', 'weilai']
for car in cars:
    print(car)
# shenlan
# byd
# xiaopeng
# lixiang
# weilai

# 函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）
for value in range(1, 5):
    print(value)
# 1
# 2
# 3
# 4

# 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]

# range(start, stop[, step])
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 0
print(max(digits))  # 9
print(sum(digits))  # 45

squares = [value ** 2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 切片

# 不可变的列表被称为元组