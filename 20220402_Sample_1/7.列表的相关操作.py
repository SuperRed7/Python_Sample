# coding:utf-8
list_1 = ['hello', 'world']
print('原:', list_1, id(list_1))

# 可变:对应的内存地址不会发生改变
list_1.append(123)
print('增加元素:', list_1, id(list_1))

list_1.insert(1, 100)
print('插入元素:', list_1, id(list_1))

list_1.remove('world')
print('删除元素:', list_1, id(list_1))

# pop(index)根据索引取出元素,先将元素取出,再将元素删除
print(list_1.pop(1))
print(list_1, id(list_1))

list_1.reverse()
print('列表反向:', list_1, id(list_1))

# 列表拷贝,将产生一个新的列表对象
list_2 = list_1.copy()
print('先前列表:', list_1, id(list_1))
print('列表拷贝:', list_2, id(list_2))

list_1[1] = 'mysql'
print('修改元素:', list_1, id(list_1))

list_1.clear()
print('清除元素:', list_1, id(list_1))
