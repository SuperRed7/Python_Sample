# coding:utf-8
sum_1=0
num_1=1
while num_1<11:
    sum_1+=num_1
    if sum_1>20:
        print('累加和大于20的当前数:',num_1)
        break
    num_1+=1

num_2=0
while num_2<3:
    uname_1=input('请输入用户名:')
    pwd_1=input('请输入密码:')
    if uname_1=='zhc' and pwd_1=='123456':
        print('登录中,请稍后...')
        break
    else:
        if num_2<2:
            print('你还有',2-num_2,'次机会!')
    num_2+=1
else:
    print('三次均输入失败!')

for num_3 in range(3):
    uname_2 = input('请输入用户名:')
    pwd_2 = input('请输入密码:')
    if uname_2 == 'zhc' and pwd_2 == '123456':
        print('登录中,请稍后...')
        break
    else:
        if num_3 < 2:
            print('你还有', 2 - num_3, '次机会!')
else:
    print('三次均输入失败!')

for value_1 in 'hello':
    if value_1=='e':
        break
    print(value_1)