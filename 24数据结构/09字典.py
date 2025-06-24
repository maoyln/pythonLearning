# 字典

'''
另一个非常有用的 Python 内建数据类型是字典。
序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
一对大括号创建一个空的字典：{}。
'''

# 这是一个字典运用的简单例子：
tel = {'myl': 4098, 'fj': 4139}
tel['mtt'] = 4127
tel['xr'] = 9027
print(tel) # {'myl': 4098, 'fj': 4139, 'mtt': 4127, 'xr': 4127}

del tel['xr']
print(tel) # {'myl': 4098, 'fj': 4139, 'mtt': 4127}

tel['irv'] = 4127
print(tel) # {'myl': 4098, 'fj': 4139, 'mtt': 4127, 'irv': 4127}


sort_tel = sorted(tel.keys())
print(sort_tel) # ['fj', 'irv', 'mtt', 'myl']
print(tel) # {'myl': 4098, 'fj': 4139, 'mtt': 4127, 'irv': 4127}

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
d_tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d_tel) # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 此外，字典推导可以用来创建任意键和值的表达式词典：
d_tel1 = dict(sape=4139, guido=4127, jack=4098)
print(d_tel1) # {'sape': 4139, 'guido': 4127, 'jack': 4098}