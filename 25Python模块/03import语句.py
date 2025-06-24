# import 语句

# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
'''
import module1[, module2[,... moduleN]
'''

# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

# 搜索路径时一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：

# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("maoyln")
# 输出： Hello :  maoyln


'''
一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？

这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。
'''

# 模块的搜索路径
# 当导入一个模块时，Python 会按照以下顺序查找模块：
'''
当前目录。
环境变量 PYTHONPATH 指定的目录。
Python 标准库目录。
.pth 文件中指定的目录。
'''
# 搜索路径是在 Python 编译或安装的时候确定的，安装新的库应该也会修改。
# 搜索路径被存储在 sys 模块中的 path 变量，做一个简单的实验，在交互式解释器中，输入以下代码：

import sys
print(sys.path)
'''
['F:\\work\\myPythonLearning\\25Python模块', 'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313', 'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
'''

# sys.path 输出是一个列表，其中第一项是空串 ''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），亦即我们执行 python 解释器的目录（对于脚本的话就是运行的脚本所在的目录）。

# 因此若像我一样在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。

# 了解了搜索路径的概念，就可以在脚本中修改 sys.path 来引入一些不在搜索路径中的模块。

# 现在，在解释器的当前目录或者 sys.path 中的一个目录里面来创建一个 fibo.py 的文件，代码如下：

import fibo

fibo.fib(1000) # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
fib2n = fibo.fib2(100)
print(fib2n) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
# >>> fib = fibo.fib
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377