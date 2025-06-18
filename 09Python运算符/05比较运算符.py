# Python 比较运算符

# 运算符	描述	实例
# ==	等于 - 比较对象是否相等	(a == b) 返回 False。
# !=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
# >	大于 - 返回x是否大于y	(a > b) 返回 False。
# <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
# >=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
# <=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。


#!/usr/bin/python3
 
a = 21
b = 10
c = 0
 
if ( a == b ):
   print ("1 - a 等于 b")
else:
   print ("1 - a 不等于 b")
 
if ( a != b ):
   print ("2 - a 不等于 b")
else:
   print ("2 - a 等于 b")
 
if ( a < b ):
   print ("3 - a 小于 b")
else:
   print ("3 - a 大于等于 b")
 
if ( a > b ):
   print ("4 - a 大于 b")
else:
   print ("4 - a 小于等于 b")
 
# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):
   print ("5 - a 小于等于 b")
else:
   print ("5 - a 大于  b")
 
if ( b >= a ):
   print ("6 - b 大于等于 a")
else:
   print ("6 - b 小于 a")

p = 30
if (p > 100):
   print('p大于100')
elif (p > 10):
   print('p在10和100之间')
else:
   print('p小于10')


# 1 - a 不等于 b
# 2 - a 不等于 b
# 3 - a 大于等于 b
# 4 - a 大于 b
# 5 - a 小于等于 b
# 6 - b 大于等于 a
# p在10和100之间