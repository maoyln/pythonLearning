# 强制位置参数

'''
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
'''

# 在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# 以下使用方法是正确的:

f(10, 20, 30, d=40, e=50, f=60)
# 10 20 30 40 50 60

# 以下使用方法会发生错误:
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
'''
Traceback (most recent call last):
  File "F:\work\myPythonLearning\21Python函数\08强制位置参数.py", line 17, in <module>
    f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
    ~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: f() got some positional-only arguments passed as keyword arguments: 'b'
'''
f(10, 20, 30, 40, e=50, f=60)           # e 必须使用关键字参数的形式
'''
Traceback (most recent call last):
  File "F:\work\myPythonLearning\21Python函数\08强制位置参数.py", line 25, in <module>
    f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
    ~^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: f() takes 4 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
'''

f(10, 20, 30, 40, e=50, f=60)
# 10 20 30 40 50 60