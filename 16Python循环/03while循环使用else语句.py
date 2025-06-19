# while 循环使用 else 语句
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")


'''
0  小于 5
1  小于 5
2  小于 5
3  小于 5
4  小于 5
5  大于或等于 5
'''