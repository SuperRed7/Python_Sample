# coding:utf-8
tuple_1 = ('hello', 'python', 'world')
# 根据索引访问
print(tuple_1[0])
# 元组支持切片操作
tuple_2 = tuple_1[0:3:2]
print(tuple_2)
# 元组的遍历
for item in tuple_1:
    print(item)
# 组合遍历
for item in range(len(tuple_1)):
    print(item, tuple_1[item])
# 使用enumerate()
for index, item in enumerate(tuple_1, 1):
    print(index, '--->', item)
