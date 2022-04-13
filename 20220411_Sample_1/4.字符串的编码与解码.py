# coding:utf-8
"""
字符串的编码
将str类型转成bytes类型
str.encode(encoding='',errors='strict/ignore/replace')
字符串的解码
将bytes类型转成str类型
bytes.decode(encoding='',errors='strict/ignore/replace')
"""
# 编码
value_1 = '伟大的中国梦'
# 默认为 UTF-8 编码
# 英文占一个字节,中文占三个字节
value_1_utf8_1 = value_1.encode()
print(value_1_utf8_1)
value_1_utf8_2 = value_1.encode('utf-8')
print(value_1_utf8_2)
# GBK和GB2312编码
# 英文占一个字节,中文占两个字节
value_1_gbk_1 = value_1.encode('gbk')
print(value_1_gbk_1)
value_1_gbk_2 = value_1.encode('gb2312')
print(value_1_gbk_2)
# 编码中的errors处理
value_2 = '耶✌'
value_2_1 = value_2.encode('gbk', errors='replace')
print(value_2_1)
value_2_2 = value_2.encode('gbk', errors='ignore')
print(value_2_2)
# 默认报错类型为strict
# value_2_3=value_2.encode('gbk',errors='strict')
# UnicodeEncodeError: 'gbk' codec can't encode character '\u270c' in position 1: illegal multibyte sequence
# print(value_2_3)

# 解码
# 默认为UTF-8解码
print(bytes.decode(value_1_utf8_2))
print(bytes.decode(value_1_utf8_2, 'utf-8'))
print(bytes.decode(value_1_gbk_1, 'gbk'))
print(bytes.decode(value_2_2, 'gbk', errors='ignore'))
