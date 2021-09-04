# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:11
# @Author : 肖俊
# @File : 求矩形面积.py
# @Software: PyCharm
# 求矩形面积


def rectangle (x,y):
    area = x * y
    return area

if __name__=='__main__':
    lenth=float(input('长度：'))
    high=float(input('宽度：'))
    area=rectangle(lenth,high)
    print('面积为：',area)