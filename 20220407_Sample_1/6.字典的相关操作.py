# coding:utf-8
dict_1={1001:'李梅',1002:'王华',1003:'张峰'}
print(dict_1,type(dict_1))
# 向字典中添加数据
# 直接使用赋值运算符 =
dict_1[1004]='张丽'
print(dict_1)

# 获取字典中所有的key
# dict_keys,python中的一种内部数据结构,专用于表示字典的key
keys_1=dict_1.keys()
print(keys_1)
# 如果希望更好地显示数据,可以使用list或tuple转成相应的数据类型
print(list(keys_1))
print(tuple(keys_1))

# 获取字典中所有的value
# dict_values,python中的一种内部数据结构,专用于表示字典的value
values_1=dict_1.values()
print(values_1)
# 如果希望更好地显示数据,可以使用list或tuple转成相应的数据类型
print(list(values_1))
print(tuple(values_1))

# 字典遍历时用到的items()
# dict_items,python中的一种内部数据结构,专用于表示字典的key-value对
items_1=dict_1.items()
print(items_1)
print(list(items_1))
print(tuple(items_1))

# 将字典中的数据转成键-值对的形式,以元组的方式进行显示
list_1=list(items_1)
print(list_1)
# 直接可以使用dict()将[(1001, '李梅'), (1002, '王华'), (1003, '张峰'), (1004, '张丽')]转成字典
dict_2=dict(list_1)
print(dict_2)

# 使用pop()
print(dict_2.pop(1001))
print(dict_2)
# 如果key不存在,结果输出默认值'不存在'
print(dict_2.pop(1008,'不存在'))
print(dict_2)

# 随机删除
# 先获取键-值对
print(dict_2.popitem())
print(dict_2)

# 清空字典的所有元素
dict_2.clear()
print(dict_2)

# python中一切皆对象,而每一个对象都有一个布尔值
# 空字典/空元组/空列表/空字符串/空集合的bool值为False
print(bool(dict_2))

# 删除字典
del dict_2
# NameError: name 'dict_2' is not defined.
# print(dict_2)