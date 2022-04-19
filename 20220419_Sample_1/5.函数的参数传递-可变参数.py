# coding:utf-8
"""
可变参数
1.个数可变的位置参数:
在参数前加一个星(*para)
函数调用时可接收任意个数的实际参数,并放到一个元组中
2.个数可变的关键字参数:
在参数前加两个星(**para)
函数调用时可接收任意个数"参数=值"形式的实际参数,并放到一个字典中
"""


def fun_1(*args):
    print(args, type(args))
    for i in args:
        print(i)


def fun_2(**kwargs):
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, '-->', value)


fun_1(10, 'zhc', 20, 'tzr')
fun_1(10)
fun_1(20, 30)
fun_1([11, 22, 33, 44])
# 调用时参数前加一个星(*),会将列表进行解包
fun_1(*[11, 22, 33, 44])

fun_2(name='zhc', age=18, height=178)
fun_2(name='zhc', age=18)
dict_1 = {'name': 'zhc', 'age': 18, 'height': 178}
# TypeError: fun_2() takes 0 positional arguments but 1 was given
# fun_2(dict_1)
# 调用时参数前加两个星(*),会将字典进行解包
fun_2(**dict_1)


# 从*之后的参数,在函数调用时,只能采用关键字参数传递
# *称为关键字传参
def fun_3(a, b, *, c, d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# TypeError: fun_3() takes 2 positional arguments but 4 were given
# fun_3(10,20,30,40)
fun_3(10, 20, c=30, d=40)
