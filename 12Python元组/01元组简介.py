# 元组

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号 ( )，列表使用方括号 [ ]。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。


tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"   #  不需要括号也可以
print(type(tup3))

# <class 'tuple'>


print('---------黄金分割线-----------')

tup1 = (50)
print(type(tup1))     # 不加逗号，类型为整型
# <class 'int'>

tup1 = (50,)
print(type(tup1))     # 加上逗号，类型为元组
# <class 'tuple'>


print('---------黄金分割线-----------')


# 访问元组

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

# tup1[0]:  Google
# tup2[1:5]:  (2, 3, 4, 5)


print('---------黄金分割线-----------')


# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

# (12, 34.56, 'abc', 'xyz')


print('---------黄金分割线-----------')


# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

tup = ('Google', 'Runoob', 1997, 2000)
 
print (tup)
del tup
print ("删除后的元组 tup : ")
# print (tup)

'''
删除后的元组 tup : 
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (tup)
NameError: name 'tup' is not defined
'''

print('---------黄金分割线-----------')


# 元组索引，截取

tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo','Weixin')

print(tup[1])
print(tup[-2])
print(tup[1:])
print(tup[1:4])

'''
Runoob
Weibo
('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
('Runoob', 'Taobao', 'Wiki')
'''