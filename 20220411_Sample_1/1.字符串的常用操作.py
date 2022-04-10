# coding:utf-8
# 大小写转换
value_1='HelloWorld'
value_2=value_1.lower()
value_3=value_1.upper()
print(value_1,value_2,value_3)

# 字符串的分隔
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