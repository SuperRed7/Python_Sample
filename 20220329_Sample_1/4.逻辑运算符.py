# coding:utf-8
print('--------逻辑与--------')
print(True and True)
print(8>7 and 7>6)

print(True and False)
print(8>7 and 7<6)

print(False and False)
# 当第一个表达式为False时,不计算第二个表达式
print(8<7 and 10/0)

print(False and True)
print(8<7 and 7>6)

print('--------逻辑或--------')
print(True or True)
print(8<7 or 7>6)

print(True or False)
# 当第一个表达式为False时,不计算第二个表达式
print(8>7 or 10/0)

print(False or False)
print(8<7 or 7<6)

print(False or True)
print(8<7 or 7>6)

print('--------逻辑非--------')
print(not True)
print(not (8>7))

print(not False)
print(not (8<7))