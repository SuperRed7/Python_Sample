# coding:utf-8
value_1 = 'helloworld'
# 字符串的显示宽度是20,左对齐,空白部分用*填充
print('{0:*<20}'.format(value_1))
# 字符串的显示宽度是20,右对齐,空白部分用*填充
print('{0:*>20}'.format(value_1))
# 字符串的显示宽度是20,居中对齐,空白部分用*填充
print('{0:*^20}'.format(value_1))
# center()也可以实现居中对齐
print(value_1.center(20, '*'))

# 千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(123456789))
print('{0:,}'.format(123456789.123))

# 浮点数小数部分的精度
print('{0:.2f}'.format(3.1415926))
print('{0:.5}'.format(value_1))

# 整数类型
a = 425
# 二进制,unicode符号,十进制,八进制，十六进制,十六进制大写
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(a))

# 浮点数类型
b = 3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))
