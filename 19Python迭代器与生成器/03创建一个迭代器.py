# 创建一个迭代器

'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
更多内容查阅：Python3 面向对象

__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
'''

# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
1
2
3
4
5
'''

print('---------黄金分割线-----------')


