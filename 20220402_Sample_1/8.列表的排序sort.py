# coding:utf-8
# 列表对象的sort()
# 对原列表中的元素进行排序,排序之后原列表中元素的顺序将发生改变
list_1=[22,23124,234,54,564,2,43,543,213]
print('原列表1:',list_1)
# 默认升序排序
list_1.sort()
print('升序排序后:',list_1)
# 降序排序
list_1.sort(reverse=True)
print('降序排序后:',list_1)

list_2=['banana','apple','Cat','Orange']
print('原列表2:',list_2)
list_2.sort()
print('升序排序后:',list_2)
list_2.sort(reverse=True)
print('降序排序后:',list_2)
# 忽略大小写进行排序
list_2.sort(key=str.lower)
print('忽略大小写排序后:',list_2)