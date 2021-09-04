# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 16:16
# @Author : 肖俊
# @File : 判断能否构成三角形及面积.py
# @Software: PyCharm
a = int(input('1边：'))
b = int(input('2边：'))
c = int(input('3边：'))
p=(a+b+c)/2     #海伦公式
S=((p-a)*(p-b)*(p-c)*p)**0.5            #海伦公式
if (b + c > a) or (a + b > c and abs(a - b) < c) or (a + b > c and a + c > b and b + c > a):
    print('可以构成三角形')
    print('面积为:%s'% S)
else:
    print('不能构成三角形')

