# coding:utf-8
height_1=179.5
print(height_1)
print(type(height_1))

# 浮点数不确定的尾数问题
# 0.30000000000000004
print(0.1+0.2)
# 使用内置函数round()限定运算结果需要保留的小数位数
print(round(0.1+0.2,1))