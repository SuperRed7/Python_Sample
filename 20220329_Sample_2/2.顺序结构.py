# coding:utf-8
# 赋值运算符的执行顺序,从右到左
name_1 = '张三'
age_1 = 20
print(name_1, age_1)

# 链式赋值
a = b = c = d = 100

# 系列解包赋值
# 元祖分解赋值
name_2, age_2 = '李四', 22
print(name_2, age_2)
# 列表分解赋值
[name_3, age_3] = ['王五', 30]
print(name_3, age_3)
# 字符串分解赋值
a, b, c, d = 'room'
print(a, b, c, d)
# 拓展的字符串解包赋值
a, *b = 'room'
print(a, b)

# 输入、输出语句,也是典型的顺序结构
name_4 = input('请输入姓名:')
age_4 = eval(input('请输入年龄:'))
luck_num_1 = eval(input('请输入幸运数字:'))
print('姓名:', name_4)
print('年龄:', age_4)
print('幸运数字:', luck_num_1)
