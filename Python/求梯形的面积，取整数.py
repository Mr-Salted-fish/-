# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:14
# @Author : 肖俊
# @File : 求梯形的面积，取整数.py
# @Software: PyCharm
# 求梯形的面积，取整数

a = float(input('上底：'))
b = float(input('下底：'))
h = float(input('高：'))
s = (a + b) * h / 2
print(int(s))
