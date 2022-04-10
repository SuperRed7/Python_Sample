# coding:utf-8
list_1=['hello','world','zhc','tzr']
for value_1 in list_1:
    print(value_1)

for num_1 in range(len(list_1)):
    print(num_1,list_1[num_1])

# 使用for循环与enumerate(),进行遍历
# 默认序号从0开始
for index_1,value_1 in enumerate(list_1):
    print(index_1,value_1)
# 序号从10开始
for index_1,value_1 in enumerate(list_1,10):
    print(index_1,value_1)
