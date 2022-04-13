# coding:utf-8
set_1 = {10, 20, 30}
# 向集合中添加元素
set_1.add('你好')
print(set_1)
# 删除元素
set_1.remove('你好')
print(set_1)

# 遍历集合
for item in set_1:
    print(item, type(item))

# 10表示的是元素的序号,不是索引,可以自定义
for index, item in enumerate(set_1, 10):
    print(index, '--->', item)

# 集合生成式
set_2 = {item for item in range(10)}
print(set_2, type(set_2))
set_3 = {item for item in range(10) if item % 2}
print(set_3)

# 清除集合所有元素
set_1.clear()
print(set_1, '空集合的布尔值:', bool(set_1))
