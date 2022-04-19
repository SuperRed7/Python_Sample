# coding:utf-8
"""
默认值参数
函数定义时,直接形式参数进行赋值,在调用时如果该参数不传递,
将使用默认值,如果该参数传值,则使用传递的值
"""


def happy_birthday(name='zhc', age=30):
    print('祝{0}{1}岁生日快乐'.format(name, age))


# 默认值传参
happy_birthday()
happy_birthday('tzr')
happy_birthday(age=20)


# 函数定义是,同时存在位置参数和默认值参数时,默认值参数放后面
def happy_birthday1(a, b=20):
    print('祝{0}{1}岁生日快乐'.format(a, b))
