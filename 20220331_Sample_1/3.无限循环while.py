# coding:utf-8
# 1.初始化变量
answer_1 = input('今天要测核酸吗?y/n\n')
# 2.条件判断
while answer_1 != 'n':
    # 3.语句块
    print('走,去做核酸!')
    # 4.改变变量
    answer_1 = input('今天要测核酸吗?y/n\n')

# 计算1-100之间的累加和
# 1.初始化变量
num_1 = 1
num_2 = 0
# 2.条件判断
while num_1 <= 100:
    # 3.语句块
    num_2 += num_1
    # 4.改变变量
    num_1 += 1
print('1-100之间的累加和:', num_2)
