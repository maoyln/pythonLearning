# 类装饰器

'''
除了函数装饰器，Python 还支持类装饰器。

类装饰器（Class Decorator）是一种用于动态修改类行为的装饰器，它接收一个类作为参数，并返回一个新的类或修改后的类。

类装饰器可以用于：

添加/修改类的方法或属性

拦截实例化过程
实现单例模式、日志记录、权限检查等功能

类装饰器有两种常见形式：

函数形式的类装饰器（接收类作为参数，返回新类）
类形式的类装饰器（实现 __call__ 方法，使其可调用）
'''


# 函数形式的类装饰器

# 以下实例给类添加日志功能：
def log_class(cls):
    """类装饰器，在调用方法前后打印日志"""
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)  # 实例化原始类
        
        def __getattr__(self, name):
            """拦截未定义的属性访问，转发给原始类"""
            return getattr(self.wrapped, name)
        
        def display(self):
            print(f"调用 {cls.__name__}.display() 前")
            self.wrapped.display()
            print(f"调用 {cls.__name__}.display() 后")
    
    return Wrapper  # 返回包装后的类

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display()

'''
调用 MyClass.display() 前
这是 MyClass 的 display 方法
调用 MyClass.display() 后
'''

print('---------黄金分割线-----------')


# 类形式的类装饰器（实现 __call__ 方法）
# 以下实例实现单例模式（Singleton）：
class SingletonDecorator:
    """类装饰器，使目标类变成单例模式"""
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        """拦截实例化过程，确保只创建一个实例"""
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True，说明是同一个实例
'''
Database 初始化
True
'''
