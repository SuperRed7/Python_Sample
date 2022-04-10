# coding:utf-8
"""
字典
通过键(key)从字典中获取指定的项(value),但不能通过索引来获取
字典是无序的,也被称为hash表(散列表)
是python中的可变序列
字典中的键(key)必须唯一,如果出现多次,后出现的将覆盖先出现的
字典中的键(key)要求是不可变序列
"""
# 直接使用{}创建字典
dict_1={10:'cat',20:'dog',30:'pet',20:'zoo'}
# key相同,value覆盖
print(dict_1)

# 使用zip()
list_1=[10,20,30,40]
list_2=['cat','dog','car','zoo','apple']
obj_1=zip(list_1,list_2)
# 映射函数的结果是一个zip对象
print(obj_1)
# 转成列表
# print(list(obj_1))
# 转成元组
# print(tuple(obj_1))
# 转成字典
print(dict(obj_1))

# 使用参数创建字典
# 注意,参数相当于变量，变量的名字不加引号且不能以数字开头
dict_2=dict(cat=10,dog=20)
print(dict_2)

# 元组可以作为key,列表不可以
tuple_1=(10,20,30)
print({tuple_1:10})
# TypeError: unhashable type: 'list'
# list_1=[10,20,30]
# print({list_1:10})

# 字典属于序列类型
print('max:',max(dict_2))
print('min:',min(dict_2))
print('len:',len(dict_2))

# 字典的删除
del dict_2
# NameError: name 'dict_2' is not defined.
# print(dict_2)