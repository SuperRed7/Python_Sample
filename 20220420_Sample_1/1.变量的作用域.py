# coding:utf-8
"""
变量的作用域
程序代码能访问该变量的区域
根据变量的有效范围可分为:
1.局部变量
在函数内定于并使用的变量,只在函数内部有效
局部变量使用global声明,这个变量就会变成全局变量
2.全局变量
函数外定义的变量,可作用于函数内外
"""


def fun_1(a, b):
    # c就成为局部变量,因为c是在函数内进行定义的变量,a和b为函数的形参,作用范围也是函数内部,相当于局部变量
    c = a + b
    print(c)


# name为全局变量,作用范围为函数内外都可以使用
name = 'zhc'
print(name)


def fun_2():
    print(name)


def fun_3():
    # 函数内部定义的变量,局部变量,局部变量使用global声明,这个变量实际上就变成了全局变量
    global age
    age = 20
    print(age)


fun_3()
print(age)
