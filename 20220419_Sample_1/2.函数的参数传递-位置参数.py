# coding:utf-8
"""
位置参数
调用时的参数个数和顺序必须与定于的参数个数和顺序相同
"""


def happy_birthday(name, age):
    print('祝{0}{1}岁生日快乐'.format(name, age))


happy_birthday('zhc', 30)
