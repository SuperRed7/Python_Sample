# coding:utf-8
# 猜数游戏
import random

num_1 = random.randint(1, 100)
# print(num_1)
num_2 = 0
while num_2 <= 9:
    num_3 = eval(input('请输入一个1-100之间的整数:'))
    if num_3 == num_1:
        print('bingo!')
        if num_2 <= 3:
            print('猜数大神,一共猜了', num_2 + 1, '次')
        elif num_2 <= 6:
            print('猜数高手,一共猜了', num_2 + 1, '次')
        else:
            print('猜数菜鸟,一共猜了', num_2 + 1, '次')
        break
    elif num_3 > num_1:
        if num_2 <= 8:
            print('大了,你还有', 9 - num_2, '次机会!')
    else:
        if num_2 <= 8:
            print('小了,你还有', 9 - num_2, '次机会!')
    num_2 += 1
else:
    print('猜数', num_2, '次均失败!正确数字是:', num_1)
