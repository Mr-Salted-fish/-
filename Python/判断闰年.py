# -*- codeing = utf-8 -*-
# @Time : 2021/9/3 15:40
# @Author : 肖俊
# @File : 判断闰年.py
# @Software: PyCharm
year=int(input('请输入年份:'))
if ((year%4 ==0 and year%100 !=0)) or (year%400 ==0):
    print('%d是闰年'%year)
else:
    print('%d不是闰年'%year)

