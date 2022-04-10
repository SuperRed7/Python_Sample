# coding:utf-8
print('输出一个三行四列的长方形:')
for x_1 in range(1, 4):
    for y_1 in range(1, 5):
        print('*', end='')
    # 换行
    print()

print('输出一个直角三角形:')
for x_2 in range(1, 7):
    for y_2 in range(1, x_2 + 1):
        print('*', end='')
    print()

print('输出一个倒直角三角形:')
for x_3 in range(1, 7):
    for y_3 in range(1, 7 - x_3 + 1):
        print('*', end='')
    print()

print('输出一个等腰三角形:')
for x_4 in range(1, 7):
    # 倒三角形
    for y_4 in range(1, 7 - x_4):
        print(' ', end='')
    # 1,3,5,7,9,11的三角形
    for k_4 in range(1, 2 * x_4):
        print('*', end='')
    print()

print('输出一个菱形:')
x_5 = eval(input('请输入菱形的行数:'))
while x_5 % 2 == 0:
    print('行数必须为奇数！')
    x_5 = eval(input('请输入菱形的行数:'))
# 上半部分
x_5_1 = (x_5 + 1) // 2
# 下半部分
x_5_2 = x_5 // 2
for x_6 in range(1, x_5_1 + 1):
    for y_6 in range(1, x_5_1 + 1 - x_6):
        print(' ', end='')
    for k_6 in range(1, 2 * x_6):
        print('*', end='')
    print()
for x_7 in range(1, x_5_2 + 1):
    # 直角三角形
    for y_7 in range(1, x_7 + 1):
        print(' ', end='')
    for k_7 in range(1, 2 * x_5_2 - 2 * x_7 + 2):
        print('*', end='')
    print()

print('输出一个空心菱形:')
for x_6 in range(1, x_5_1 + 1):
    for y_6 in range(1, x_5_1 + 1 - x_6):
        print(' ', end='')
    for k_6 in range(1, 2 * x_6):
        # 在此加一个判断即可
        if k_6 == 1 or k_6 == 2 * x_6 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
for x_7 in range(1, x_5_2 + 1):
    # 直角三角形
    for y_7 in range(1, x_7 + 1):
        print(' ', end='')
    for k_7 in range(1, 2 * x_5_2 - 2 * x_7 + 2):
        # 在此加一个判断即可
        if k_7 == 1 or k_7 == 2 * x_5_2 - 2 * x_7 + 2 - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
