# coding:utf-8
# 模拟简单的通讯录
set_1 = set()
for i in range(1, 6):
    person_1 = input('请输入第' + str(i) + '位好友的姓名与手机号码:')
    set_1.add(person_1)
print(set_1)
for i in set_1:
    print(i)
