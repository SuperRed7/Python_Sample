# coding:utf-8
# 大小写转换
value_1='HelloWorld'
value_2=value_1.lower()
value_3=value_1.upper()
print(value_1,value_2,value_3)

# 字符串的分隔,返回一个列表
value_4='123@qq.com'
list_1=value_4.split('@')
print(list_1,type(list_1))
print('邮箱名:',list_1[0],'邮箱服务器域名:',list_1[1])

# 统计子串在指定字符串中出现的次数
print(value_1.count('o'))

# 检索操作(查询)
print(value_1.find('o'))
print(value_1.find('p'))

print(value_1.index('o'))
# ValueError: substring not found
# print(value_1.index('p'))

# 判断前缀与后缀
print(value_1.startswith('H'))
print(value_1.startswith('P'))

print('sample.py'.endswith('.py'))
print('sample.txt'.endswith('.py'))

# 字符串的替换
value_5=value_1.replace('o','你好')
print(value_1,value_5)

# 字符串在指定的宽度范围内居中
print(value_1.center(20))
print(value_1.center(20,'*'))

# 去除字符串左右的空格
value_6='    Hello World    '
print(value_6.strip())
# 去除字符串左侧的空格
print(value_6.lstrip())
# 去除字符串右侧的空格
print(value_6.rstrip())

# 去除指定的字符
value_7='dl-HelloWorld'
# 注意:不管dl或ld,只要左右包含l或d,就去除
print(value_7.strip('ld'))
# 去除左侧指定的字符
print(value_7.lstrip('ld'))
# 去除右侧指定的字符
print(value_7.rstrip('ld'))