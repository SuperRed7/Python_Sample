# coding:utf-8
# 千年虫
list_1 = [88, 89, 90, 98, 00, 99]
print('原列表:', list_1)

# 1.使用for循环遍历列表
# for index in range(len(list_1)):
#     if str(list_1[index])!='0':
#         list_1[index]='19'+str(list_1[index])
#     else:
#         list_1[index] = '200' + str(list_1[index])
# print('修改后的年份列表:',list_1)

# 2.使用enumerate()遍历列表
for index, value in enumerate(list_1):
    if str(value) != '0':
        list_1[index] = '19' + str(value)
    else:
        list_1[index] = '200' + str(value)
print('修改后的年份列表:', list_1)
