# coding:utf-8
import re

"""
re.sub(pattern,repl,string,count,flags=0)
使用正则表达式实现字符串的替换
re.split(pattern,string,maxsplit,flags=0)
功能与字符串的split()相同
"""

pattern_1 = r'黑客|破解|反爬'
repl_1 = 'XXX'
value_1 = '我想学习Python,想破解一些黑客视频,Python可以实现无底线反爬吗?'
sub_1 = re.sub(pattern_1, repl_1, value_1, count=2)
print(sub_1)

pattern_2 = r'[?|&]'
value_2 = 'https://www.baidu.com/' \
          's?wd=shshs&rsv_spt=1&rsv_iqid=0x83a8dbc500018d7d' \
          '&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1' \
          '&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100' \
          '&rsv_sug2=0&rsv_btype=i&inputT=1058' \
          '&rsv_sug4=5037'
list_1 = re.split(pattern_2, value_2, maxsplit=5)
print(list_1)
