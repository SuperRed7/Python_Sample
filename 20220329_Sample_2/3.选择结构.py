# coding:utf-8
num_1 = eval(input('请输入你购买的六位数号码:'))
# 使用比较运算符,即比较表达式
if num_1 == 123456:
    print('恭喜你,中奖了!')
if num_1 != 123456:
    print('很遗憾,你未中奖!')

num_2 = 98
# 0的布尔值为False,非0的布尔值为True
if num_2 % 2:
    print(num_2, '为奇数')
if not num_2 % 2:
    print(num_2, '为偶数')

value_1 = input('请输入一段文字:')
# 空字符串的布尔值为False,非空字符串的布尔值为True
if value_1:
    print(value_1, '是一个非空字符串')
if not value_1:
    print(value_1, '是一个空字符串')

value_2 = eval(input('请输入一个布尔类型的值:True或False'))
# 表达式也可以是一个单纯的变量
if value_2:
    print(value_2, '的值为True')
if not value_2:
    print(value_2, '的值为False')

# 使用if语句时,如果语句块只有一句代码,可以将语句块直接写在冒号的后面
num_3 = 10
num_4 = 20
if num_3 > num_4:
    max_num = num_3
else:
    max_num = num_4
print('最大值为:', max_num)
