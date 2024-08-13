# _*_ coding: utf-8 _*_
# @Time: 2024/5/16 13:41
# @Author: LBJ辉
# @File: code2-5-浮点数
# @Project: nxops-01

# 浮点数的计算
n1 = 0.1
n2 = 0.2
print(n1 + n2)  # 0.30000000000000004

# 四舍五入 round def round(number: SupportsRound[_T], ndigits: SupportsIndex)
n3 = round(n1 + n2, 2)
print(n3)

import math

# 向上取整 ceil
n4 = math.ceil(n1 + n2)
print(n4)

# 向下取整 floor
n5 = math.floor(n1 + n2)
print(n5)
