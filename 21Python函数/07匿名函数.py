# 匿名函数
'''
Python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度。
'''

# 语法
# lambda 函数的语法只包含一个语句，如下：
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''

# 设置参数 a 加上 10:

x = lambda a : a + 10
print(x(5))
# 15


print('---------黄金分割线-----------')


# 以下实例匿名函数设置两个参数：

# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
# 相加后的值为 :  30
print ("相加后的值为 : ", sum( 20, 20 ))
# 相加后的值为 :  40


print('---------黄金分割线-----------')


# 我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。

# 以下实例将匿名函数封装在 myfunc 函数中，通过传入不同的参数来创建不同的匿名函数：

def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
# 22
print(mytripler(11))
# 33