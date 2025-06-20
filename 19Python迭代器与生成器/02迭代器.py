# 字符串，列表或元组对象都可用于创建迭代器：

# 列表

list = [1,2,3,4]
it = iter(list) # 创建迭代器对象
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # 4


print('---------黄金分割线-----------')


# 迭代器对象可以使用常规for语句进行遍历：

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
# 1 2 3 4


print('---------黄金分割线-----------')


# 也可以使用 next() 函数：

import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
'''
1
2
3
4
'''