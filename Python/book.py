# -*- codeing = utf-8 -*-
# @Time : 2021/9/2 5:32
# @Author : 肖俊
# @File : book.py
# @Software: PyCharm

# 求矩形面积
'''

def rectangle (x,y):
    area = x * y
    return area

if __name__=='__main__':
    lenth=float(input('长度：'))
    high=float(input('宽度：'))
    area=rectangle(lenth,high)
    print('面积为：',area)



# 求圆的周长和面积

import math

r = float(input('半径：'))
perimeter = 2 * math.pi * r
rectangle = math.pi * r * r
print('%.3f' % perimeter)
print('%.3f' % rectangle)



# 求两点之间的距离，取两位小数

import math

x1 = float(input('x1的坐标：'))
y1 = float(input('y1的坐标：'))
x2 = float(input('x2的坐标：'))
y2 = float(input('y2的坐标：'))
print('%.2f' % math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)))


# 求梯形的面积，取整数

a = float(input('上底：'))
b = float(input('下底：'))
h = float(input('高：'))
s = (a + b) * h / 2
print(int(s))


# 求直角三角形斜边长度，取三位小数

import math

a = float(input('1边：'))
b = float(input('2边：'))
c = a ** 2 + b ** 2
print('%.3f' % math.sqrt(c))


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
'''