# coding:utf-8
sum_1 = 0
num_1 = 1
while num_1 <= 100:
    if num_1 % 2 == 1:
        num_1 += 1
        continue
    sum_1 += num_1
    num_1 += 1
print('1-100之间的偶数和:', sum_1)

sum_2 = 0
for num_2 in range(1, 101):
    if num_2 % 2 == 1:
        continue
    sum_2 += num_2
print('1-100之间的偶数和:', sum_2)
