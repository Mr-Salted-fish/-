# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 20:17
# @Author : 肖俊
# @File : 麦粒.py
# @Software: PyCharm
x = 0  # 麦子总量
y = 1  # 第一个格子
z = 1  # 下一个格子的麦子是本格子的两倍
# #依次循环X64
while y <= 64:#y为格子次数循环64次
    x += z#第一个格子的麦子
    y += 1#格子数加一
    z = z * 2#麦子x2


print(z)
