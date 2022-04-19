# coding:utf-8
# 格式化输出商品的名称和单价
list_1 = [
    ['01', '电风扇', '美的', 500],
    ['02', '洗衣机', 'TCL', 1000],
    ['03', '微波炉', '松下', 600],
    ['04', '电饭煲', '美的', 300]
]
print('编号\t名称\t\t品牌\t单价')
for i in list_1:
    for j in i:
        print(j, end='\t')
    # 换行
    print()

print('------格式化操作-----')
for i in list_1:
    i[0] = '0000' + i[0]
    i[3] = '￥{0:.2f}'.format((i[3]))
print('编号\t\t名称\t\t品牌\t单价')
for i in list_1:
    for j in i:
        print(j, end='\t')
    # 换行
    print()
