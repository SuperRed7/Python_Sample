# coding:utf-8
# 计算1-10之间的累加和
num_2=0
for num_3 in range(1,11):
    print(num_2,'+',num_3,'=',num_2+num_3)
    num_2+=num_3
else:
    print('1-10之间的累加和:',num_2)
