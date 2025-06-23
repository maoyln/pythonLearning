# 使用装饰器
# 装饰器通过 @ 符号应用在函数定义之前，例如：

'''
@time_logger
def target_function():
    pass
'''

# 等同于：
'''
def target_function():
    pass
target_function = time_logger(target_function)
'''

'''
这会将 target_function 函数传递给 decorator 装饰器，并将返回的函数重新赋值给 target_function。从而，每次调用 target_function 时，实际上是调用了经过装饰器处理后的函数。

通过装饰器，开发者可以在保持代码整洁的同时，灵活且高效地扩展程序的功能。

以下是一个简单的装饰器示例，它会在函数执行前后打印日志：
'''

