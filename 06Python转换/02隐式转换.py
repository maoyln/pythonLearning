# 隐式类型转换

# 在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
# 以下实例中，我们对两种不同类型的数据进行运算，较低数据类型（整数）就会转换为较高数据类型（浮点数）以避免数据丢失。

num_int = 123
num_flo = 1.23

print(num_int)
print(num_flo)

num_new = num_int + num_flo

print(num_new)

# num_int 数据类型为: <class 'int'>
# num_flo 数据类型为: <class 'float'>
# num_new: 值为: 124.23
# num_new 数据类型为: <class 'float'>


print('---------黄金分割线-----------')


num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("num_str 数据类型为:",type(num_str))

print(num_int+num_str)

# 输出
# num_int 数据类型为: <class 'int'>
# num_str 数据类型为: <class 'str'>
# Traceback (most recent call last):
#   File "F:\work\myPythonLearning\06Python转换\02隐式转换.py", line 32, in <module>
#     print(num_int+num_str)
#           ~~~~~~~^~~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# 从输出中可以看出，整型和字符串类型运算结果会报错，输出 TypeError。 Python 在这种情况下无法使用隐式转换。

# 但是，Python 为这些类型的情况提供了一种解决方案，称为显式转换。

print('---------黄金分割线-----------')
