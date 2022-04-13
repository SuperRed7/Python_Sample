# coding:utf-8
dict_1 = {'hello': 10, 'world': 20, 'python': 30}
# 使用dict[key]访问字典元素
print(dict_1['hello'])
# 使用dict.get(key)访问字典元素
print(dict_1.get('hello'))
# 如果key不存在时,两者之间使用是有区别的
# KeyError: 'java'
# print(dict_1['java'])
# 默认值为None
print(dict_1.get('java'))
# 指定默认值
print(dict_1.get('java', '不存在'))

# 字典的遍历
for item in dict_1.items():
    # 获取key,value组成的一个元组
    print(item)
# 在使用for循环遍历时,分别获取key和value
for key, value in dict_1.items():
    print(key, value)
