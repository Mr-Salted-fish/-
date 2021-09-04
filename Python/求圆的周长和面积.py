# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:13
# @Author : 肖俊
# @File : 求圆的周长和面积.py
# @Software: PyCharm
# 求圆的周长和面积

import math

r = float(input('半径：'))
perimeter = 2 * math.pi * r
rectangle = math.pi * r * r
print('%.3f' % perimeter)
print('%.3f' % rectangle)
