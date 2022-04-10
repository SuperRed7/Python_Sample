# coding:utf-8
answer_1='y'
while answer_1=='y':
    print('--------欢迎使用10086查询功能--------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话时长')
    print('4.退出程序')
    answer_2=input('请输入你要执行的操作:')
    if answer_2=='1':
        print('当前余额为:60.22元')
    elif answer_2=='2':
        print('当前剩余流量:234.33MB')
    elif answer_2=='3':
        print('当前剩余通话时长:300分钟')
    elif answer_2=='4':
        break
    else:
        print('对不起,数字输入有误,请重新输入你要执行的操作!')
        # continue
    answer_1=input('还要继续使用吗?y/n\n')
print('程序退出,感谢你的使用!')
