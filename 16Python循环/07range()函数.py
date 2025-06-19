# range() 函数

# 如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列，例如:

for i in range(5,9) :
    print(i)

'''
5
6
7
8
'''

print('---------黄金分割线-----------')

# 也可以使 range() 以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3) :
    print(i)

'''
0
3
6
9
'''

print('---------黄金分割线-----------')

# 负数：
for i in range(-10, -100, -30) :
    print(i)

'''
-10
-40
-70
'''


print('---------黄金分割线-----------')


# 您可以结合 range() 和 len() 函数以遍历一个序列的索引,如下所示:

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

'''
0 Google
1 Baidu
2 Runoob
3 Taobao
4 QQ
'''

print('---------黄金分割线-----------')


# 还可以使用 range() 函数来创建一个列表：
print(list(range(5)))

'''
[0, 1, 2, 3, 4]
'''