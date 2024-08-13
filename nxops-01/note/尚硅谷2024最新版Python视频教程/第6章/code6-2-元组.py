# _*_ coding: utf-8 _*_
# @Time: 2024/5/20 14:02
# @Author: LBJ辉
# @File: code6-2-元组
# @Project: nxops-01

tuple1 = (1, 2, 3, True, 'hello')
print(tuple1)
print(type(tuple1))
tuple2 = (1,)  # 元组里只有一个元素时，加一个逗号
tuple3 = tuple()  # tuple():类型转换
tuple4 = ()
tuple5 = tuple('hello')  # ('h', 'e', 'l', 'l', 'o')
tuple6 = tuple([1, 2, 3, 4])  # (1, 2, 3, 4)
list1 = list(tuple6)  # [1, 2, 3, 4]
str1 = str(tuple6)  # '(1, 2, 3, 4)'

# 索引
print(tuple1[-1])
# 切片
print(tuple1[::-1])
# len
print(len(tuple1))
print(max(tuple6), min(tuple6))
del tuple5

print(tuple1 + tuple6)
print(tuple1 * 3)

print(1 in tuple1)

# 元组的常用方法
a = tuple1.count('hellwwwo')
print(a)
print(tuple1)
a = tuple1.index(2)
print(a)

# 元组的遍历
for i in tuple1:
    print(i)

for index, value in enumerate(tuple1):
    print(index, value)

for i in range(len(tuple1)):
    print(i, tuple1[i])
