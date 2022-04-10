# coding:utf-8
num_1=eval(input('请输入你的6位数号码:'))
if num_1==123456:
    print('恭喜你,中奖了!')
else:
    print('很遗憾,你未中奖!')

# 使用条件表达式简化
result_1='恭喜你,中奖了!' if num_1==123456 else '很遗憾,你未中奖!'
print(result_1)
# 再次简化
print('恭喜你,中奖了!' if num_1==123456 else '很遗憾,你未中奖!')