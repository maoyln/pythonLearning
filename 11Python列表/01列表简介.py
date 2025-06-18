# 列表

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )

# red
# green
# blue


print('---------黄金分割线-----------')


list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[-1] )
print( list[-2] )
print( list[-3] )

# black
# white
# yellow


print('---------黄金分割线-----------')


nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])

# [10, 20, 30, 40]


print('---------黄金分割线-----------')


list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])

# list[1]:  Runoob
# list[1:-2]:  ['Runoob', 'Zhihu']


print('---------黄金分割线-----------')


# 更新列表
list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

# 第三个元素为 :  1997
# 更新后的第三个元素为 :  2001
# 更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']


# 删除列表元素

list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)

# 原始列表 :  ['Google', 'Runoob', 1997, 2000]
# 删除第三个元素 :  ['Google', 'Runoob', 2000]