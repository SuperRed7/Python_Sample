# coding:utf-8
tuple_1=(i for i in range(1,4))
# 结果是一个生成器对象
print(tuple_1)

# 使用内置函数tuple()转换生成器对象为元组或列表
# tuple_1=tuple(tuple_1)
# print(tuple_1)

# 使用for遍历转换生成器对象为元组或列表
# for item in tuple_1:
#     print(item)

# 使用__next__()转换生成器对象为元组或列表
print(tuple_1.__next__())
print(tuple_1.__next__())
print(tuple_1.__next__())
# 生成器遍历之后,原生成器对象已经不存在了
# 再想重新遍历必须重新创建一个生成器对象
for item in tuple_1:
    print(item)
