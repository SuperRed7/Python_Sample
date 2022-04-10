# coding:utf-8
# 创建一个整型类型变量
luck_num_1=7
# 创建一个字符串类型变量
my_name_1='我就住在江边路'
print(my_name_1,'的幸运数字是:',luck_num_1)
# 通过内置函数type()查看变量的数据类型
print(type(luck_num_1))
print(type(my_name_1))
# Python允许多个变量指向同一个值
no_1=number_1=1024
# 通过内置函数id()查看变量的内存地址
print(id(no_1))
print(id(number_1))

