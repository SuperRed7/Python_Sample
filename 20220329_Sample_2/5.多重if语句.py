# coding:utf-8
score_1=eval(input('请输入你的成绩:'))
if score_1<0 or score_1>100:
    print('成绩输入有误')
elif 0<=score_1<60:
    print('E')
elif 60<=score_1<70:
    print('D')
elif 70<=score_1<80:
    print('C')
elif 80<=score_1<90:
    print('B')
else:
    print('A')
