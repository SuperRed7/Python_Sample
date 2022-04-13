# coding:utf-8
year_1 = eval(input('请输入一个四位的正数年份:'))
if (year_1 % 4 == 0 and year_1 % 100 != 0) or year_1 % 400 == 0:
    print(year_1, '年是闰年')
else:
    print(year_1, '是平年')
