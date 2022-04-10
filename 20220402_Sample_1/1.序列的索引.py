# coding:utf-8
"""
序列:用于存储多个值的连续空间,每个值都对应一个整数的编号,称为索引。
序列结构主要有列表、元组、集合、字典和字符串
"""
value_1 = 'hello world!'
# 正向递增索引
for value_2 in range(0, len(value_1)):
    print(value_2, value_1[value_2])
# 反向递减索引
for value_3 in range(-12,0):
    print(value_3, value_1[value_3])
