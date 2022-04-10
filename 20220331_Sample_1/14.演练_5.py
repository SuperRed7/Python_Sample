# coding:utf-8
# 实现一个人机对战的小游戏:石头剪刀布
import random

print('----加载程序,请稍等----')
uname_1 = input('请输入你的姓名:\n')
num_1 = input('请选择电脑角色:1<-->美国队长 2<-->钢铁侠 3<-->绿巨人\n')
while True:
    if num_1 == '1':
        uname_2 = '美国队长'
        break
    elif num_1 == '2':
        uname_2 = '钢铁侠'
        break
    elif num_1 == '3':
        uname_2 = '绿巨人'
        break
    else:
        num_1 = input('输入有误,请重新选择电脑角色:\n')
print(uname_1, 'VS', uname_2)
sum_1 = 0
sum_2 = 0
sum_3 = 0
while True:
    print('----实时战绩', uname_1, sum_1, ':', uname_2, sum_2, '----')
    num_2 = input('请出拳:1<-->石头 2<-->剪刀 3<-->布\n')
    while True:
        if num_2 == '1':
            uname_3 = '石头'
            break
        elif num_2 == '2':
            uname_3 = '剪刀'
            break
        elif num_2 == '3':
            uname_3 = '布'
            break
        else:
            num_2 = input('输入有误,请重新出拳:1<-->石头 2<-->剪刀 3<-->布\n')
    num_3 = random.randint(1, 3)
    if num_3 == 1:
        uname_4 = '石头'
    elif num_3 == 2:
        uname_4 = '剪刀'
    else:
        uname_4 = '布'
    print(uname_1, ':', uname_3)
    print(uname_2, ':', uname_4)
    if uname_3 == uname_4:
        print('平局!')
    elif (uname_3 == '石头' and uname_4 == '剪刀') or (uname_3 == '剪刀' and uname_4 == '布') or (
            uname_3 == '布' and uname_4 == '石头'):
        print(uname_1, '赢了!')
        sum_1 += 1
    else:
        print(uname_2, '赢了!')
        sum_2 += 1
    uname_5 = input('再来一局?y/n\n')
    sum_3 += 1
    if uname_5 == 'n':
        print('----退出程序,正计算最终战绩----')
        print('总对局数:', sum_3, '胜率:', str(round(sum_1 / sum_3, 4) * 100) + '%')
        print(uname_1, sum_1, ':', uname_2, sum_2)
        print('胜局数:', sum_1)
        print('负局数:', sum_2)
        print('平局数:', sum_3 - sum_1 - sum_2)
        if sum_1 == sum_2:
            print('打成平手,卧龙凤雏!')
        elif sum_1 > sum_2:
            print('你赢了,天才!')
        else:
            print('你输了,废物!')
        break
