# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:13
# @Author : 肖俊
# @File : 求两点之间的距离，取两位小数.py
# @Software: PyCharm
# 求两点之间的距离，取两位小数

import math

x1 = float(input('x1的坐标：'))
y1 = float(input('y1的坐标：'))
x2 = float(input('x2的坐标：'))
y2 = float(input('y2的坐标：'))
print('%.2f' % math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)))
