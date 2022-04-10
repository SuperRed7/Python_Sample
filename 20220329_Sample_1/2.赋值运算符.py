# coding:utf-8
x=20
y=10
x=x+y
print(x)
x+=y
print(x)
x-=y
print(x)
x*=y
print(x)
x/=y
print(x)
x%=y
print(x)
z=3
y//=z
print(y)
y**=z
print(y)

# python支持链式赋值
a=b=c=100
print(a,b,c)
# python支持系列解包赋值
a,b=10,20
print(a,b)

# 如何交换两个变量的值
# 其它语言的方法
# temp=0
# temp=a
# a=b
# b=temp
# print(a,b)
# python的方法
a,b=b,a
print(a,b)