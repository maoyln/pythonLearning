# 基本语法

'''
Python 装饰允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能，
装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。
'''
# 语法
def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # 这里是在调用原始函数前添加的新功能
        before_call_code()
       
        result = original_function(*args, **kwargs)
       
        # 这里是在调用原始函数后添加的新功能
        after_call_code()
       
        return result
    return wrapper

# 使用装饰器
@decorator_function
def target_function(arg1, arg2):
    pass  # 原始函数的实现

'''

解析：decorator 是一个装饰器函数，它接受一个函数 func 作为参数，并返回一个内部函数 wrapper，
在 wrapper 函数内部，你可以执行一些额外的操作，然后调用原始函数 func，并返回其结果。

decorator_function 是装饰器，它接收一个函数 original_function 作为参数。
wrapper 是内部函数，它是实际会被调用的新函数，它包裹了原始函数的调用，并在其前后增加了额外的行为。
当我们使用 @decorator_function 前缀在 target_function 定义前，
Python会自动将 target_function 作为参数传递给 decorator_function，然后将返回的 wrapper 函数替换掉原来的 target_function。
'''