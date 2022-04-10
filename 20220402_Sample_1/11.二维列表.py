# coding:utf-8
# 创建二维列表
list_1=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',98,85],
    ['广州',155,133],
    ['深圳',222,333]
]
print(list_1)

for row in list_1:
    for col in row:
        print(col,end='\t')
    print('')

# 列表生成一个四行五列
list_2=[[j for j in range(5)]for i in range(4)]
print(list_2)