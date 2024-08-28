# _*_ coding: utf-8 _*_
# @Time: 2024/5/23 10:04
# @Author: LBJ辉
# @File: code9-3-random
# @Project: nxops-01

import random

# 随机小数
a = random.random()
# 随机整数
a = random.randint(1, 100)
print(a)

# 获取列表中的随机元素
list1 = [1, 2, 3, 4, 5, 6]
print(list1[random.randint(0, len(list1) - 1)])
print(random.choice(list1))
print(random.choice('hello'))
print(ord('A'), ord('Z'))  # 65 90

random.shuffle(list1)
print(list1)

# 生成一个随机字母组成的列表
from my_package import my_tools

print(my_tools.random_string(5))
