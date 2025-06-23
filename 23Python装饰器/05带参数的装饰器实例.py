# 带参数的装饰器
# 如果原函数需要参数，可以在装饰器的 wrapper 函数中传递参数：

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("myl")

'''
在原函数之前执行
Hello, myl!
在原函数之后执行
'''

# 以上代码代码定义了一个装饰器 my_decorator，它会在被装饰的函数执行前后分别打印一条消息。
# 装饰器通过 wrapper 函数包裹原函数，并在调用原函数前后添加额外操作。


print('---------黄金分割线-----------')


# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数：
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()

'''
Hello!
Hello!
Hello!
'''

'''
repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。decorator 接受一个函数 func，
并返回一个 wrapper 函数。wrapper 函数会调用 func 函数 num_times 次。
使用 @repeat(3) 装饰s ay_hell 函数后，调用 say_hello 会打印 "Hello!" 三次。
'''