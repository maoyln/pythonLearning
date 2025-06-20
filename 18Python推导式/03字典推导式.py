# 字典推导式

# 字典推导基本格式：

'''
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
'''

# 使用字符串及其长度创建字典：
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)
# {'Google': 6, 'Runoob': 6, 'Taobao': 6}


print('---------黄金分割线-----------')


# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dic = {key: key*key for key in {2, 3, 4}}
print(dic)
# {2: 4, 3: 9, 4: 16}