# coding:utf-8
"""
集合
python中的集合与数学中集合的概念一致
集合可分为可变集合set与不可变集合frozenset
集合与字典的key一致,都是无序的
集合中的元素要求唯一
集合中只能存储不可变数据类型(字符串,整数,浮点数,元组)
集合使用{}定义,元素之间使用逗号进行分隔
"""
# 使用{}直接创建集合
set_1 = {10, 20, 30, 40}
print(set_1, type(set_1))
# TypeError: unhashable type: 'list'
# set_1={[10,20],[30,40]}
# print(set_1)
# TypeError: unhashable type: 'list'
# set_1={([10,20]),([30,40])}
# print(set_1)

# 直接使用空{}创建的是<class 'dict'>字典
dict_1 = {}
print(dict_1, type(dict_1))

# 使用set(可迭代对象)创建集合
# 创建空集合
set_2 = set()
print(set_2, type(set_2), bool(set_2))

set_3 = set('helloworld')
print(set_3)
set_4 = set([10, 20, 30])
print(set_4)
set_5 = set(range(1, 11))
print(set_5)

# 集合属于序列
print('max:', max(set_5))
print('min:', min(set_5))
print('len:', len(set_5))
print('9在集合中存在:', (9 in set_5))
print('9在集合中不存在:', (9 not in set_5))

# 删除集合
del set_5
# NameError: name 'set_5' is not defined.
# print(set_5)
