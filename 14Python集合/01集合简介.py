# 集合

# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

print('---------黄金分割线-----------')

# 创建格式

'''
parame = {value01,value02,...}
或者
set(value)
'''

set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
print(set1)
print(type(set1))
print(set2)
print(type(set2))


print('---------黄金分割线-----------')


# 添加元素
# s.add( x )
# s.update( x )
myset01 = {1,2,3,4,5}
myset01.add('aadd')
myset01.add('3')
myset01.add(2)
print(myset01)

myset01.update({'批量添加1', '批量添加2'})
print(myset01)


print('---------黄金分割线-----------')


# 移除元素
# s.remove( x )  # 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
# s.discard( x ) # 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

# 随机删除使用s.pop()  我们也可以设置随机删除集合中的一个元素，语法格式如下：

mre =  set(("mmm", "yyy", "lll", "nnn"))
print(mre)
mre.remove("yyy")
# mre.remove("yyy") # Traceback (most recent call last):File "F:\work\myPythonLearning\14Python集合\01集合简介.py", line 53, in <module> mre.remove("yyy")
print(mre)
mre.discard("yyy")

print(mre)


thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(thisset)
print(x)


print('---------黄金分割线-----------')


# 计算集合元素个数

# len(thisset)
print(len(thisset))


print('---------黄金分割线-----------')


# 清空集合
# s.clear()

mylthisset = set(("Google", "Runoob", "Taobao"))
mylthisset.clear()
print(mylthisset)


print('---------黄金分割线-----------')


# 判断元素是否在集合中存在

hissetfj = set(("Google", "Runoob", "Taobao"))

print("Runoob" in hissetfj)
print("myl" in hissetfj)


'''
方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
len()	计算集合元素个数
'''