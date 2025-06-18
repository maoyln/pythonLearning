# 字典

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

# 注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。


# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 一个简单的字典实例：


print('---------黄金分割线-----------')


# 使用大括号 {} 来创建空字典
emptyDict = {}
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:", len(emptyDict))
 
# 查看类型
print(type(emptyDict))

# {}
# Length: 0
# <class 'dict'>

print('---------黄金分割线-----------')

# 使用内建函数 dict() 创建字典：
emptyDict = dict()
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:",len(emptyDict))
 
# 查看类型
print(type(emptyDict))

print('---------黄金分割线-----------')


# 访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])

# tinydict['Name']:  Runoob
# tinydict['Age']:  7


print('---------黄金分割线-----------')


# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

# tinydict['Age']:  8
# tinydict['School']:  菜鸟教程


print('---------黄金分割线-----------')


# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显式删除一个字典用del命令，如下实例：

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

# 但这会引发一个异常，因为用执行 del 操作后字典不再存在：



# 序号	函数及描述
# 1	dict.clear()
# 删除字典内所有元素
# 2	dict.copy()
# 返回一个字典的浅复制
# 3	dict.fromkeys()
# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 4	dict.get(key, default=None)
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值
# 5	key in dict
# 如果键在字典dict里返回true，否则返回false
# 6	dict.items()
# 以列表返回一个视图对象
# 7	dict.keys()
# 返回一个视图对象
# 8	dict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	dict.update(dict2)
# 把字典dict2的键/值对更新到dict里
# 10	dict.values()
# 返回一个视图对象
# 11	dict.pop(key[,default])
# 删除字典 key（键）所对应的值，返回被删除的值。
# 12	dict.popitem()
# 返回并删除字典中的最后一对键和值。