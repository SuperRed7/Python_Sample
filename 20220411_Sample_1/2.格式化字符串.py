# coding:utf-8
# 使用占位符进行格式化
name = '张三'
age = 18
score = 98.5
print('姓名:%s,年龄:%d,成绩:%.1f' % (name, age, score))

# f-string格式化字符串
print(f'姓名:{name},年龄:{age},成绩:{score}')

# 使用字符串的format()
print('姓名:{0},年龄:{1},成绩:{2}'.format(name, age, score))
print('姓名:{2},年龄:{0},成绩:{1}'.format(age, score, name))
