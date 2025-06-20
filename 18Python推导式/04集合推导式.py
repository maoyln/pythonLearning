# 集合推导式
# 集合推导式基本格式：

'''
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
'''

# 计算数字 1,2,3 的平方数：

setNew = {i**2 for i in (3,4,5)  }
print(setNew)


print('---------黄金分割线-----------')


# 判断不是 abc 的字母并输出：

noABC = {x for x in 'asdfwqweasrqwrasdvccdasdcasd' if x not in 'abc'}
print(noABC)
# {'w', 'f', 'q', 'v', 'e', 'd', 'r', 's'}