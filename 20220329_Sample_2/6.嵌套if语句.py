# coding:utf-8
answer_1=input('请问你喝酒了吗? y/n \n')
if answer_1=='y':
    proof_1=eval(input('请输入酒精含量:'))
    if proof_1<20:
        print('酒精含量不构成酒驾,滚!')
    elif proof_1<80:
        print('酒精含量已构成酒驾标准,你完了!')
    else:
        print('严重酒驾,坐牢吧你!')
else:
    print('没喝酒,滚!')