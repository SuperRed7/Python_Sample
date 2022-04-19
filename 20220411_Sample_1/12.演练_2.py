# coding:utf-8
# 统计字符串中出现指定字符的次数(不区分大小写)
value_1 = 'HelloPython,HelloJava,HelloPhp'
value_2 = input('请输入要统计的字符:')
print('{0}在{1}中一共出现了{2}次'.format(value_2, value_1, value_1.upper().count(value_2.upper())))
