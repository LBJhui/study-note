# _*_ coding: utf-8 _*_
# @Time: 2024/5/9 9:36
# @Author: LBJ辉
# @File: 3.列表
# @Project: nxops-01

bicycles = ['trek', 'cannon dale', 'redline', 'specialized']
print(bicycles)  # ['trek', 'cannon dale', 'redline', 'specialized']
print(bicycles[-1])  # specialized
bicycles[0] = 'feige'
print(bicycles)  # ['feige', 'cannon dale', 'redline', 'specialized']
# 在列表末尾添加元素
bicycles.append('trek')
print(bicycles)  # ['feige', 'cannon dale', 'redline', 'specialized', 'trek']

# 在列表中插入元素
bicycles.insert(0, '雅迪')
print(bicycles)  # ['雅迪', 'feige', 'cannon dale', 'redline', 'specialized', 'trek']

# 从列表中删除元素
del bicycles[-1]
print(bicycles)  # ['雅迪', 'feige', 'cannon dale', 'redline', 'specialized']

# 使用方法pop()删除元素
popped_bicycle = bicycles.pop()
print(bicycles)  # ['雅迪', 'feige', 'cannon dale', 'redline']
print(popped_bicycle)  # specialized
popped_bicycle = bicycles.pop(2)
print(bicycles)  # ['雅迪', 'feige', 'redline']
print(popped_bicycle)  # cannon dale

# 根据值删除元素
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
bicycles.remove('雅迪')
print(bicycles)  # ['feige', 'redline']

# 使用方法sort()对列表进行永久性排序
cars = ['shenlan', 'byd', 'xiaopeng', 'lixiang', 'weilai']
cars.sort()
print(cars)  # ['byd', 'lixiang', 'shenlan', 'weilai', 'xiaopeng']
cars.sort(reverse=True)
print(cars)  # ['xiaopeng', 'weilai', 'shenlan', 'lixiang', 'byd']

# 使用函数sorted()对列表进行临时排序
cars = ['shenlan', 'byd', 'xiaopeng', 'lixiang', 'weilai']
print(cars)  # ['shenlan', 'byd', 'xiaopeng', 'lixiang', 'weilai']
print(sorted(cars))  # ['byd', 'lixiang', 'shenlan', 'weilai', 'xiaopeng']
print(sorted(cars, reverse=True))  # ['xiaopeng', 'weilai', 'shenlan', 'lixiang', 'byd']
print(cars)  # ['shenlan', 'byd', 'xiaopeng', 'lixiang', 'weilai']

cars.reverse()
print(cars)  # ['weilai', 'lixiang', 'xiaopeng', 'byd', 'shenlan']

print(len(cars))  # 5
