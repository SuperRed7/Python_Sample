# coding:utf-8
value_1 = int(eval(input('请输入一个四位整数:')))
print(value_1, type(value_1))
print('千位数:', value_1 // 1000)
print('百位数:', value_1 // 100 % 10)
print('十位数:', value_1 // 10 % 10)
print('个位数:', value_1 % 10)

value_2 = eval(input('请输入父亲的身高:'))
value_3 = eval(input('请输入母亲的身高:'))
value_4 = (value_2 + value_3) * 0.54
print('儿子的身高预测为:', round(value_4, 2))
