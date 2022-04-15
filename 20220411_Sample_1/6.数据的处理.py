# coding:utf-8
# 字符串的拼接
value_1 = 'hello'
value_2 = 'world'
# 使用+进行拼接
print(value_1 + value_2)
# 使用join方法进行拼接
print(''.join([value_1, value_2]))
print('*'.join([value_1, value_2, 'python', 'java']))
print('你好'.join([value_1, value_2, 'python', 'java']))
# 直接拼接
print('hello''world')
# 使用格式化字符串进行拼接
print('%s%s' % (value_1, value_2))
print(f'{value_1}{value_2}')
print('{0}{1}'.format(value_1, value_2))

# 字符串的去重
value_3 = 'awrisfhaeuhsajfhwiwqapofqwb'
# 1.字符串的拼接及not in
value_4 = ''
for i in value_3:
    if i not in value_4:
        value_4 += i
print(value_4)
# 2.使用索引及not in
value_4 = ''
for i in range(len(value_3)):
    if value_3[i] not in value_4:
        value_4 += value_3[i]
print(value_4)
# 3.通过集合去重及列表的排序
value_4 = set(value_3)
list_1 = list(value_4)
# 排序的关键字
list_1.sort(key=value_3.index)
print(''.join(list_1))

# 列表元素的去重
list_2 = ['金星', '木星', '水星', '火星', '金星', '木星', '水星', '火星']
list_3 = []
# 1.遍历及not in
for i in list_2:
    if i not in list_3:
        list_3.append(i)
print(list_3)
# 2.使用索引及not in
for i in range(len(list_2)):
    if list_2[i] not in list_3:
        list_3.append(list_2[i])
print(list_3)
# 3.通过集合去重及列表的排序
value_5 = set(list_2)
list_4 = list(value_5)
list_4.sort(key=list_2.index)
print(list_4)
