# coding:utf-8
import re

"""
re.findall(pattern,string,flags=0)
用于在整个字符串中搜索所有符合正则表达式的值
如果匹配成功,结果为列表
否则为[]
"""

pattern = r'\d\.\d+'
value_1 = 'I study Python3.10 every day Python2.10 I love you'
value_2 = '4.10Python I study every day'
value_3 = 'I study Python every day'
findall_1 = re.findall(pattern, value_1)
print(findall_1, type(findall_1))
findall_2 = re.findall(pattern, value_2)
print(findall_2, type(findall_1))
findall_3 = re.findall(pattern, value_3)
print(findall_3, type(findall_1))
