# coding:utf-8
# 统计循环执行的次数
num_1 = 0
while num_1 < 3:
    uname_1 = input('请输入你的用户名:')
    pwd_1 = input('请输入你的密码:')
    if uname_1 == 'zhc' and pwd_1 == '123456':
        print('系统正在登录,请稍后...')
        num_1 = 4
    else:
        if num_1 < 2:
            print('输入错误,你还有', 2 - num_1, '次机会')
        num_1 += 1
if num_1 == 3: print('用户已被锁定,无法操作!')
