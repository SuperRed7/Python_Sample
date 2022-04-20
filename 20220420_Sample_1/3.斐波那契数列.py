# coding:utf-8
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        result=fun(n-1)+fun(n-2)
        return result
print('-----输出斐波那契数列第6位上的数字-----')
print(fun(6))

print('-----1.输出斐波那契数列前6位上的数字-----')
for i in range(1,7):
    print(fun(i))

i=1
n=eval(input('请输入一个整数:\t'))
print('-----2.输出斐波那契数列前'+str(n)+'位上的数字-----')
while i<n+1:
    print(fun(i))
    i+=1
