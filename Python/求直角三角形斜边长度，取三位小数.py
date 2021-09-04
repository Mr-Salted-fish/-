# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:14
# @Author : 肖俊
# @File : 求直角三角形斜边长度，取三位小数.py
# @Software: PyCharm
# 求直角三角形斜边长度，取三位小数

import math

a = float(input('1边：'))
b = float(input('2边：'))
c = a ** 2 + b ** 2
print('%.3f' % math.sqrt(c))

