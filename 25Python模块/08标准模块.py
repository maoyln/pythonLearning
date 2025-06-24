# 标准模块
# Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。

'''
模块名	功能描述
math	数学运算（如平方根、三角函数等）
os	操作系统相关功能（如文件、目录操作）
sys	系统相关的参数和函数
random	生成随机数
datetime	处理日期和时间
json	处理 JSON 数据
re	正则表达式操作
collections	提供额外的数据结构（如 defaultdict、deque）
itertools	提供迭代器工具
functools	高阶函数工具（如 reduce、lru_cache）
'''
# 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。

# 这些组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。

# 应该注意到这有一个特别的模块 sys ，它内置在每一个 Python 解析器中。变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:

import sys
ps1 = sys.ps1
print(ps1)