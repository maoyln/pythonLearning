# from … import 语句

# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下
# from modname import name1[, name2[, ... nameN]]

# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
'''
>>> from fibo import fib, fib2
>>> fib(500)
1 1 2 3 5 8 13 21 34 55 89 144 233 377
'''
# 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

# 给模块起别名
# 使用 as 关键字为模块或函数起别名：
'''
import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root
'''

# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
# from modname import *
# 这提供了一个简单的方法来导入一个模块中的所有项目。
# 不推荐，容易引起命名冲突。