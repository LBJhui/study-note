# _*_ coding: utf-8 _*_
# @Time: 2024/5/21 9:38
# @Author: LBJ辉
# @File: code6-4-字符串
# @Project: nxops-01

s1 = 'hello world'

# 序列的通用操作
print(s1 + ' LBJhui')
print(s1 * 3)
print(len(s1))
print(max(s1), min(s1))
# del s1
print('s' in s1)
print('abcd' < 'abce')

# 字符串的遍历
for i in s1:
    print(i)

for index, value in enumerate(s1):
    print(index, value)

for i in range(len(s1)):
    print(i, s1[i])

# 类型转换
print(str(12), type(str(12)))
print(str([1, 2, 3, 4]), type(str([1, 2, 3, 4])))
print(str((12,)), type(str((12,))))

# 常用方法
print(s1.islower())
print(s1.isupper())
print(s1.count('o'))
print(s1.strip())
print(s1.split(' '))
print(s1.find('o'))
print('#'.join(['111', '222', '333']))
