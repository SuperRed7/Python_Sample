# coding:utf-8
value_1='helloworld'

print('e' in value_1)
print('v' in value_1)
print('e' not in value_1)
print('v' not in value_1)

# 内置函数
print(len(value_1))
print(max(value_1))
print(min(value_1))

# 序列对象的方法,使用序列的名称,打点调用
# 字符第一次出现的索引位置
print(value_1.index('o'))
print(value_1.count('o'))