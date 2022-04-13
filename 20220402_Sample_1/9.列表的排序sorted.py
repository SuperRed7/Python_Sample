# coding:utf-8
# 内置的sorted()
# 使用sorted()函数排序后,原列表元素顺序不变,排序后产生一个新的列表对象
list_1 = [22, 23124, 234, 54, 564, 2, 43, 543, 213]
print('原列表1:', list_1)
# 升序
list_2 = sorted(list_1)
print('升序:', list_2)
print('原列表1:', list_1)
# 降序
list_3 = sorted(list_1, reverse=True)
print('降序:', list_3)
print('原列表1:', list_1)

list_4 = ['banana', 'apple', 'Cat', 'Orange']
print('原列表2:', list_4)
# 忽略大小写进行排序
list_5 = sorted(list_4, key=str.lower)
print('忽略大小写排序后:', list_5)
print('原列表2:', list_4)
