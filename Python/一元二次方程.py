# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 21:18
# @Author : 肖俊
# @File : 一元二次方程.py
# @Software: PyCharm
import math

a = int(input('请输入：'))
b = int(input('请输入：'))
c = int(input('请输入：'))

try:
    delta = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
except ValueError:
    print('无解')
