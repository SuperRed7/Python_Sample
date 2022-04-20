# coding:utf-8
def fun_1(n):
    if n == 1:
        return 1
    else:
        result = n * fun_1(n - 1)
        return result


print(fun_1(6))
