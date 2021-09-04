# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 17:15
# @Author : 肖俊
# @File : 爱因斯坦阶梯.py
# @Software: PyCharm
i = 1
'''
while True:
    i += 1
    if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(i)
        break
'''
for i in range(1000):
    if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(i)
        break
