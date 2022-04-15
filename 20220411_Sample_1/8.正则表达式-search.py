# coding:utf-8
import re

"""
re.search(pattern,string,flags=0)
用于在整个字符串中搜索第一个匹配的值
如果匹配成功,结果为match对象
否则为None
"""

pattern = r'\d\.\d+'
value_1 = 'I study Python3.10 every day Python2.10 I love you'
value_2 = '4.10Python I study every day'
value_3 = 'I study Python every day'
search_1 = re.search(pattern, value_1)
print(search_1)
print(search_1.group())
search_2 = re.search(pattern, value_2)
print(search_2)
print(search_2.group())
search_3 = re.search(pattern, value_3)
print(search_3)
# AttributeError: 'NoneType' object has no attribute 'group'
# print(search_3.group())
