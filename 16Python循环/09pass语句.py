# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。

# pass 不做任何事情，一般用做占位语句，如下实例

# while True:
#     pass  # 等待键盘中断 (Ctrl+C)


print('---------黄金分割线-----------')

# 以下实例在字母为 o 时 执行 pass 语句块:
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")

'''
当前字母 : R
当前字母 : u
当前字母 : n
执行 pass 块
当前字母 : o
执行 pass 块
当前字母 : o
当前字母 : b
Good bye!
'''