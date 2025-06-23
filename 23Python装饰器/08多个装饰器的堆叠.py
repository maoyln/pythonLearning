# 多个装饰器的堆叠
# 你可以将多个装饰器堆叠在一起，它们会按照从下到上的顺序依次应用。例如：

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
'''
Decorator 1
Decorator 2
Hello!
'''