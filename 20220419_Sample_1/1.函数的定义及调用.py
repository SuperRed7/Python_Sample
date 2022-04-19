# coding:utf-8
"""
函数的定义:
函数是将一段实现功能的完整代码,使用函数名称进行封装,通过
函数名称进行调用。以此达到一次编写,多次调用的目的。
使用函数可以实现代码的重用性。
Python中函数定义使用def关键字。
语法结构:
def 函数名称(参数列表):
    函数体
    [return 返回值列表]
"""


# 函数的定义
def get_sum(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    print(f'1到{num}之间的和为:{s}')
    # return s


# 函数的调用
get_sum(100)
get_sum(1000)
