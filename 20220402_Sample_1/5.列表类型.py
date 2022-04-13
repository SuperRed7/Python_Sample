# coding:utf-8
# 可以直接使用[]创建
list_1 = ['hello', 'world', 100, 123.4]
print(list_1)

# 可以使用内置函数list()创建
list_2 = list('helloworld')
list_3 = list(range(1, 10, 2))
print(list_2)
print(list_3)

# 列表是序列的一种,对序列操作的运算符,操作符,函数就可以使用
print(list_1 + list_2 + list_3)
print(list_1 * 3)
print(len(list_1))
print(max(list_3))
print(min(list_2))
print(list_2.count('o'))
print(list_2.index('o'))

list_4 = [10, 20, 30]
print(list_4)
# 删除列表
del list_4
# NameError: name 'list_4' is not defined.
print(list_4)
