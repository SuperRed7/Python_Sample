# coding:utf-8
x = 10
y = 3

# 隐式转换:通过运算隐式地转换了结果的数据类型
z = x / y
print(z, type(z))

# float类型转换成int类型,只保留整数部分
print(int(3.1))
print(int(3.9))
# str类型转换成int类型
print(int('100') + int('100'))
# int类型转换成float类型
print(float(10))
# str类型转换成float类型
print(float('3.1'))
# str类型转换成float类型再转换成int类型
print(int(float(3.1)))

# chr()与ord()
# chr()将整数转换成一个字符
# ord()将字符转换成一个整数值
print(chr(25105))
print(ord('我'))

# 进制之间的转换操作
# 十进制与其他进制之间的转换
print('十进制转换成二进制:' + bin(25205))
print('十进制转换成八进制:' + oct(25205))
print('十进制转换成十六进制:' + hex(25205))
