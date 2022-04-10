# coding:utf-8
import random
# 生成指定范围的数值列表
list_1=[item for item in range(1,11)]
print(list_1)

list_1=[item*item for item in range(1,11)]
print(list_1)

list_1=[random.randint(1,100) for _ in range(10)]
print(list_1)

# 从列表中选择符合条件的元素组成新的列表
list_2=[item for item in range(10) if item%2==0]
print(list_2)