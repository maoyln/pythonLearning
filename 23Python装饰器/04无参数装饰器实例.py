def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

wp = say_hello()

# print(wp) # None
'''
在原函数之前执行
Hello!
在原函数之后执行
'''

'''
my_decorator 是一个装饰器函数，它接受 say_hello 作为参数，并返回 wrapper 函数。
@my_decorator 将 say_hello 替换为 wrapper。
'''
