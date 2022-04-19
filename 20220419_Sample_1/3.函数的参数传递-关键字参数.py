# coding:utf-8
"""
关键字参数
函数调用时,使用"形参名称=值"的方式进行传参
传参顺序可以与定义时参数的顺序不同
"""


def happy_birthday(name, age):
    print('祝{0}{1}岁生日快乐'.format(name, age))


# 关键字传参
happy_birthday(name='zhc', age=30)
happy_birthday(age=30, name='zhc')
happy_birthday('zhc', age=30)
