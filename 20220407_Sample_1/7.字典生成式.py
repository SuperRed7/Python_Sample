# coding:utf-8
import random

# 使用指定范围的数作为key
dict_1={item:random.randint(1,100) for item in range(4)}
print(dict_1)

# 使用映射函数生成字典
list_1=[1001,1002,1003]
list_2=['张三','李四','王五']
dict_2={key:value for key,value in zip(list_1,list_2)}
print(dict_2)

