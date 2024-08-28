# _*_ coding: utf-8 _*_
# @Time: 2024/5/20 10:09
# @Author: LBJ辉
# @File: code6-1-列表
# @Project: nxops-01

# 创建列表
list1 = []  # 空列表
print(list1)
print(type(list1))

list2 = [1, 2, 4, True, False, 'hello']
print(list2)

list3 = list('12345678')  # 类型转换：str -> list
print(list3)  # ['1', '2', '3', '4', '5', '6', '7', '8']

# 列表的索引
print(list3[1])

# 列表的加法和乘法
print(list3 + list2)
print(list3 * 3)

# 列表的成员运算
print('0' in list3)
print('0' not in list3)

# 内置函数
print(len(list3))
print(max(list3))
print(min(list3))
# del list3

# 列表的遍历
for i in list3:
    print(i, end='  ')

print()

for i, j in enumerate(list3):
    print('i:', i, 'j:', j)

for i in range(len(list2)):
    print(i, list2[i])

# 列表的常用方法
list1.append('666')  # 添加元素 ['666']
list1.extend([1, 2, 3])  # 添加列表 ['666', 1, 2, 3]
list1.insert(2, 'hello')  # 插入元素 ['666', 1, 'hello', 2, 3]
list1.pop(3)  # 根据索引删除元素 ['666', 1, 'hello', 3]
list1.remove(1)  # 根据元素值删除元素 ['666', 'hello', 3]
list1.clear()  # 清空列表

# 计算若干个人的平均年龄
age = [12, 44, 34, 64, 24, 56]
print(sum(age) / len(age))
