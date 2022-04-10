# coding:utf-8
# 模拟简单的购物流程
list_1 = []
for i in range(5):
    goods = input('商品入库--请输入商品编号和名称,每次只能输入一件商品:')
    list_1.append(goods)
print('----------------------------')
print('入库商品信息:')
# print(list_1)
for i in list_1:
    print(i)
print('----------------------------')
list_2 = []
while True:
    flag = False  # 代表库存里没有商品信息
    num = input('请输入你要购买的商品编号:')
    for i in list_1:
        # 取字符串元素前4位的切片
        if num == i[0:4]:
            flag = True  # 代表库存里有商品信息
            list_2.append(i)
            print('商品已成功添加到购物车')
            # 退出的是for循环
            break
    # if flag==False and num!='q':
    #     print('库存里没有该商品编号!')
    if num == 'q':
        # 退出的是while循环
        print('退出简单的购物流程!')
        break
    # if flag==False:
    if not flag:
        print('库存里没有该商品编号!')

print('----------------------------')
print('你购物车里已选择的商品为:')
# 反向
list_2.reverse()
for i in list_2:
    print(i)
