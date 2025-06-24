# del 语句
'''
使用 del 语句可以从一个列表中根据索引来删除一个元素，而不是值来删除元素。这与使用 pop() 返回一个值不同。
可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。
'''

# 例如：
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a) # [1, 66.25, 333, 333, 1234.5]


print('---------黄金分割线-----------')


# 元组和序列
t = 12345, 54321, 'hello!'
print(t) # (12345, 54321, 'hello!')
u = t, (1, 2, 3, 4, 5)
print(u) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# 如你所见，元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。


print('---------黄金分割线-----------')


# 集合

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # {'pear', 'banana', 'orange', 'apple'} # 删除重复的
inBaskT = 'orange' in basket
print(inBaskT) # True
inBaskF = 'crabgrass' in basket
print(inBaskF) # False

print('---------黄金分割线-----------')

# 以下演示了两个集合的操作
a = set('abracadabra') # {'c', 'r', 'd', 'b', 'a'}
b = set('alacazam') # {'a', 'm', 'l', 'c', 'z'}
print(a) # a 中唯一的字母
print(b)

c = a - b # 在 a 中的字母，但不在 b 中
print(c) # {'d', 'r', 'b'}

d = a | b # # 在 a 或 b 中的字母
print(d) # {'d', 'a', 'l', 'c', 'm', 'r', 'b', 'z'}

f = a & b # 在 a 和 b 中都有的字母
print(f) # {'a', 'c'}

g = a ^ b # 在 a 或 b 中的字母，但不同时在 a 和 b 中
print(g) # {'b', 'd', 'z', 'r', 'l', 'm'}