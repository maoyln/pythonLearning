# StopIteration

'''
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
'''

# 在 20 次迭代后停止执行：
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
print(myclass) # <__main__.MyNumbers object at 0x00000218FA3F6A50>
myiter = iter(myclass)
print(myiter) # <__main__.MyNumbers object at 0x00000218FA3F6A50>
 
for x in myiter:
  print(x)

'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
'''