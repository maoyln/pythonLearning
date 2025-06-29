# 列表推导式

'''
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，
或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。
'''

# 这里我们将列表中每个数值乘三，获得一个新的列表：
vec = [2, 4, 6]
newVec = [3*x for x in vec]
print(newVec) # [6, 12, 18]


print('---------黄金分割线-----------')


# 现在我们玩一点小花样：
newVec2 = [[x, x**2] for x in vec]
print(newVec2) # [[2, 4], [4, 16], [6, 36]]


print('---------黄金分割线-----------')


# 这里我们对序列里每一个元素逐个调用某方法：
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit2 = [weapon.strip() for weapon in freshfruit]
print(freshfruit2) # ['banana', 'loganberry', 'passion fruit']


print('---------黄金分割线-----------')


# 我们可以用 if 子句作为过滤器：

a = [3*x for x in vec if x > 3]
print(a)
b = [3*x for x in vec if x < 2]
print(b)


print('---------黄金分割线-----------')



# 以下是一些关于循环和其它技巧的演示：

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
c = [x*y for x in vec1 for y in vec2]
d = [x+y for x in vec1 for y in vec2]
e = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(c) # [8, 6, -18, 16, 12, -36, 24, 18, -54]
print(d) # [6, 5, -7, 8, 7, -5, 10, 9, -3]
print(e) # [8, 12, -54]


print('---------黄金分割线-----------')


# 列表推导式可以使用复杂表达式或嵌套函数：
e = [str(round(355/113, i)) for i in range(1, 6)]
print(e) # ['3.1', '3.14', '3.142', '3.1416', '3.14159']