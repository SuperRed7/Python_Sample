# coding:utf-8
# 遍历字符串
for value_1 in 'hello':
    print(value_1)

# 内置函数range(),产生一个[n,m)的整数序列,包含n,不包含m
for num_1 in range(1,11):
    if num_1%2==0:
        print(num_1,'是偶数')
    # else:
    #     print(num_1,'是奇数')

# 计算1-10之间的累加和
num_2=0
for num_3 in range(1,11):
    print(num_2,'+',num_3,'=',num_2+num_3)
    num_2+=num_3
print('1-10之间的累加和:',num_2)

# 计算100-1999之间的水仙花数
for num_4 in range(100,1000):
    # 个位数
    num_4_1=num_4%10
    # 十位数
    num_4_2=num_4//10%10
    # 百位数
    num_4_3=num_4//100%10
    if num_4_1**3+num_4_2**3+num_4_3**3==num_4:
        print('水仙花数有:',num_4)
