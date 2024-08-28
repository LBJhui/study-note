# _*_ coding: utf-8 _*_
# @Time: 2024/5/15 10:05
# @Author: LBJ辉
# @File: code1-3-print
# @Project: nxops-01

# 任务 1：打印数字 2024
print(2024)

# 任务 2：打印字符串 我是Mia
print("我是Mia")

# 任务 3：创建变量 year，值为 2024，打印变量 year
year = 2024
print(year)

"""
逗号的使用
- 想要在一行中打印多个内容，可以在 print() 函数中使用逗号隔开多个内容
- 变量、数字、字符串都可以
- 注意使用英文的逗号

格式化输出
- 如果希望输出文字信息的同时，一起输出数据，就需要使用到格式化操作符
- % 被称为格式化操作符，专门用于处理字符串中的格式
    - 包含 % 的字符串，被称为格式化字符串
    - % 和不同的字符连用，不同类型的数据需要使用不同的格式化字符
%s: 字符串
%d: 有符号十进制整数，%06d 表示输出的整数显示位数，不足的地方使用 0 补全
%f: 浮点数，%.2f 表示小数点后只显示两位
%%: 输出 %
"""
# 任务 4
year = 2024
month = 2
day = 20
week = "一"
weather = "晴"
temp = 19.5
print("我是Mia")
# sep: 设置打印多个内容的分隔符
# end: 设置print命令执行结束后的操作
print(year, "年，我要减肥", sep="", end="\n\n")
print(year, "年，我要读100本书", sep="", end="\n\n")
print(year, "年，我要去10个城市旅游", sep="", end="\n\n")
print("今天是 %d 年 %02d 月 %02d 日，星期%s，天气%s，温度 %.1f 度" % (year, month, day, week, weather, temp))
