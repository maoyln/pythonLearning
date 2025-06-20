# 元组推导式（生成器表达式）
# 元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

# 元组推导式基本格式：

'''
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
'''

# 元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。


# 例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：
a = (x for x in range(1,10))
print(a)
# <generator object <genexpr> at 0x7faf6ee20a50>  # 返回的是生成器对象
b = tuple(a)       # 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(b)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)