# coding:utf-8
"""
元组
由一系列按特定顺序排列的元素组成
python中的不可变序列
使用()定义,元素之间用逗号分隔
元组中的元素可以是任意数据类型
"""
# 直接使用()创建元组
tuple_1 = ('hello', [10, 20, 30], 'python', 'world')
print(tuple_1, type(tuple_1))

# 使用内置函数tuple()创建元组
tuple_2 = tuple('helloworld')
print(tuple_2)

tuple_3 = tuple([10, 20, 30, 40])
print(tuple_3)

tuple_4 = tuple(range(10))
print(tuple_4)

# 元组的相关操作
tuple_5 = tuple(range(50, 60))
print(tuple_5)
print('60在元组中存在:', (60 in tuple_5))
print('60在元组中不存在:', (60 not in tuple_5))
print('最大元素:', max(tuple_5))
print('最小元素:', min(tuple_5))
print('长度:', len(tuple_5))
print('索引:', tuple_5.index(54))
print('元素个数:', tuple_5.count(54))

# 元组中只有一个元素,逗号不能省略
tuple_6 = (10)
print(tuple_6, type(tuple_6))
tuple_7 = (10,)
print(tuple_7, type(tuple_7))

# 元组的删除
tuple_8 = ('你好',)
print(tuple_8, type(tuple_8))
del tuple_8
# NameError: name 'tuple_8' is not defined.
# print(tuple_8,type(tuple_8))
