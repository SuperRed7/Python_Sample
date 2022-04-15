# coding:utf-8
import re

"""
re.match(pattern,string,flags=0)
用于从字符串的开始位置进行匹配
如果起始位置匹配成功,结果为match对象
否则为None
"""

pattern = r'\d\.\d+'
value_1 = 'I study Python3.10 every day'
match_1 = re.match(pattern, value_1, re.IGNORECASE)
print(match_1)
value_2 = '3.10Python I study every day 4.15'
match_2 = re.match(pattern, value_2, re.IGNORECASE)
print(match_2)
print('匹配值的起始位置:', match_2.start())
print('匹配值的结束位置:', match_2.end())
print('匹配区间的位置元组:', match_2.span())
print('待匹配的字符串:', match_2.string)
print('匹配的数据:', match_2.group())
