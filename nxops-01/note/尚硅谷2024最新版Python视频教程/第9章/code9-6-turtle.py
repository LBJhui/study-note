# _*_ coding: utf-8 _*_
# @Time: 2024/5/23 14:31
# @Author: LBJ辉
# @File: code9-6-turtle
# @Project: nxops-01

import time
import turtle

from my_package import my_tools

pen = turtle.Turtle()
pen.backward(100)
pen.speed(0)
while True:
    time.sleep(1)
    times = my_tools.get_time()
    pen.clear()
    pen.write(times, font=("Arial", 40, "normal"))
input()
