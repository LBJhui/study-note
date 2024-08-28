# _*_ coding: utf-8 _*_
# @Time: 2024/5/15 10:40
# @Author: LBJ辉
# @File: code1-4-input
# @Project: nxops-01

# input() 的使用

name = input("请输入你的名字：")
print(name)

age = input("请输入你的年龄：")
year = 2024
# 类型转换
age = int(age)
birth = year - age
print("你的出生年份是", birth)
