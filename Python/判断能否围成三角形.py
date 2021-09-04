# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:15
# @Author : 肖俊
# @File : 判断能否围成三角形.py
# @Software: PyCharm
# 判断能否围成三角形
a = float(input('1边：'))
b = float(input('2边：'))
c = float(input('3边：'))
if b + c > a:
    print('可以构成三角形')
elif a + b > c and abs(a - b) < c:
    print('可以构成三角形')
elif a + b > c and a + c > b and b + c > a:
    print('可以构成三角形')
else:
    print('不能构成三角形\n三角形构成公式为：\n1.b+c>a\n2.a+b>c和|a-b|<c\n3.a+b>和a+c>b和b+c>a')
