# _*_ coding: utf-8 _*_
# @Time: 2024/5/21 9:55
# @Author: LBJ辉
# @File: code6-5-字典
# @Project: nxops-01

# 字典的创建
d = {
    'name': 'LBJhui',
    'gender': 'male'
}
print(d)
print(type(d))
# d = {}
# d = dict()

# 新增键值对
d['height'] = 170
print(d)

# 获取键值对
print(d['height'])

# 修改键值对
d['height'] = 180
print(d)
# del d

print('height' in d)

# 字典的遍历
for i in d:
    print(i, d[i])

print(d.items())
for k, v in d.items():
    print(k, v)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)

# 字典的常用方法
d.pop('name')
a = d.copy()
print('a 的键值对：', a)
print(d.get('height'))
d.popitem()
d.update({'age': 18})
print(d)
d.clear()
