# __name__ 属性

# 一个模块被另一个程序第一次引入时，其主程序将运行。

# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。

# Filename: using_name.py

# 方式一
# $ python .\25Python模块\using_name.py
# 程序自身在运行

# 方式二
import using_name # 我来自另一模块