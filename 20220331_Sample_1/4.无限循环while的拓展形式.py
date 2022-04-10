# coding:utf-8
# 计算1-100之间的累加和
# 1.初始化变量
num_1=1
num_2=0
# 2.条件判断
while num_1<=100:
    # 3.语句块
    num_2+=num_1
    # 4.改变变量
    num_1+=1
else:
    print('1-100之间的累加和:',num_2)