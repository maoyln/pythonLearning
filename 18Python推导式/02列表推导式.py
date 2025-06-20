# 列表推导式

# 语法如下
'''
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

'''
# 解释
'''
out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值
'''

# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)
# ['ALICE', 'JERRY', 'WENDY', 'SMITH']


print('---------黄金分割线-----------')


# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0 ]
print(multiples)
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]