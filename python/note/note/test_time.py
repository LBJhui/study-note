# _*_ coding: utf-8 _*_
# @Time: 2024/3/26 10:08
# @Author: LBJ辉
# @File: time
# @Project: nxops

# 时间模块time是python自带的模块，它内部封装了一些获取时间戳和字符串形式时间的函数。
import time

# 获取当前时间戳。时间戳是指从计算机元年到现在经过的秒数。
print(time.time())  # 1711419003.4450874

# 获取格式化时间对象，返回值是当前格林尼治时间。
print(time.gmtime())
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=26, tm_hour=2, tm_min=11, tm_sec=13, tm_wday=1, tm_yday=86, tm_isdst=0)

# 获取格式化时间对象，返回值是当地时间(也就是北京时间，比格林尼治时间+8小时)。
print(time.localtime())
# time.struct_time(tm_year=2024, tm_mon=3, tm_mday=26, tm_hour=10, tm_min=12, tm_sec=2, tm_wday=1, tm_yday=86, tm_isdst=0)

'''
tm_mon=3，表示当前是3月
tm_mday=25，表示当前是25日
tm_hour=2，表示当前是2时(注意是格林尼治时间,加8小时才是北京时间)
tm_min=9，表示当前是9分
tm_sec=43，表示当前是43秒
tm_wday=0，取值范围是 0~6，0 表示星期一，6 表示星期日。
tm_yday=85，表示当前是一年的第85天
tm_isdst=0，表示不是夏令时(=1表示是夏令时)
'''

# 获取格式化的时间
print(time.asctime())  # Tue Mar 26 10:12:48 2024

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-03-26 10:12:48
