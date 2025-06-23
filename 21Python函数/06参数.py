# 参数

'''
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
'''

# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# 调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
# printme() # 本行代码放开报错如下

'''
Traceback (most recent call last):
  File "F:\work\myPythonLearning\21Python函数\06参数.py", line 23, in <module>
    printme()
    ~~~~~~~^^
TypeError: printme() missing 1 required positional argument: 'str'
'''


print('---------黄金分割线-----------')


# 关键字参数
'''
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''
# 以下实例在函数 printme() 调用时使用参数名：
# 
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str = "教程")
# 教程
printme("教程01")
# 教程01


print('---------黄金分割线-----------')


# 以下实例中演示了函数参数的使用不需要使用指定顺序：

def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=30, name="myl" )
# 名字:  myl
# 年龄:  30
printinfo( age=31, name="myln" )
# 名字:  myln
# 年龄:  31


print('---------黄金分割线-----------')


# 默认参数
def printinfo( name, age = 31 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=30, name="maoyl" )
# 名字:  maoyl
# 年龄:  30
print ("------------------------")
printinfo( name="maoyl01" )
# 名字:  maoyl01
# 年龄:  31


print('---------黄金分割线-----------')


# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下
'''
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
# 以上实例输出结果：
# 70
# (60, 50)

print('---------黄金分割线-----------')

# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
# 输出:
# 10
# 输出:
# 70
# 60
# 50


print('---------黄金分割线-----------')


# 还有一种就是参数带两个星号 **基本语法如下：
'''
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''

# 加了两个星号 ** 的参数会以字典的形式导入。
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)
# 输出:
# 1
# {'a': 2, 'b': 3}


print('---------黄金分割线-----------')

# 声明函数时，参数中星号 * 可以单独出现，例如:
'''
def f(a,b,*,c):
    return a+b+c
'''

# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入：
def f(a,b,*,c):
   return a+b+c
# f(1,2,3)   # 报错
'''
Traceback (most recent call last):
  File "F:\work\myPythonLearning\21Python函数\06参数.py", line 182, in <module>
    f(1,2,3)   # 报错
    ~^^^^^^^
TypeError: f() takes 2 positional arguments but 3 we
'''

dd = f(1,2,c=3) # 正常
print(dd)
# 6