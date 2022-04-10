# coding:utf-8
value_1 = 'helloworld'

# 索引从0开始(start),到5结束(end,不包含5),步长(step)为1
print(value_1[0:5:1])
# 省略开始位置start,默认从0开始
print(value_1[:5:1])
# 省略开始位置start,省略步长step
print(value_1[:5])
# 省略结束位置end
print(value_1[0::1])
# 省略结束位置end和步长
print(value_1[5::])
# 更换一下步长
# 索引从0开始(start),到5结束(end,不包含5),步长(step)为2
print(value_1[0:5:2])
# 0,2,4,6,8
print(value_1[::2])
# 步长可以为负数
print(value_1[::-1])
