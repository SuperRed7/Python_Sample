# coding:utf-8
# 输出九九乘法表
for x in range(1, 10):
    for y in range(1, x + 1):
        print(str(y) + '*' + str(x) + '=' + str(x * y), end='\t')
    # 换行
    print()
