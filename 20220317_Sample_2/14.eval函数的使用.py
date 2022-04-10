# coding:utf-8
value_1='3.14+3'
print(value_1,type(value_1))

# eval()将去掉字符串最外侧的引号,并按照python语句方式执行去掉引号后的字符串
value_2=eval(value_1)
print(value_2,type(value_2))

# eval()经常和input()一起使用,用来获取用户输入的数值
age_1=input('请输入你的年龄:')
print(age_1,type(age_1))
height_1=input('请输入你的身高:')
print(height_1,type(height_1))

age_2=eval(input('请再次输入你的年龄:'))
print(age_2,type(age_2))
height_2=eval(input('请再次输入你的身高:'))
print(height_2,type(height_2))

value_3='我就住在江边路'
print(eval('value_3'))
