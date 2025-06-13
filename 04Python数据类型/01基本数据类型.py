# 在编程中，数据类型是非常重要的概念。变量可以存储不同类型的数据，每种类型都有它特定的用途。

# Python中内置的数据类型包括：

# 文本类型：str
# 数值类型：int, float, complex
# 序列类型：list, tuple, range
# 映射类型：dict
# 集合类型：set, frozenset
# 布尔类型：bool
# 二进制类型：bytes, bytearray, memoryview
# 空值类型：NoneType


# 使用内置的 type() 函数可以快速确定变量的数据类型，例如：
x = 10
print(type(x))  # 输出: <class 'int'>

# 设置具体的数据类型
# 如果你希望在创建变量时明确指定数据类型，可以使用对应的构造函

# str() 创建字符串
# int() 创建整数
# float() 创建浮点数
# bool() 创建布尔类型变量

# 示例代码：
x = str("nihao shijie")      # 字符串(str)
y = int(20)                  # 整数(int)
z = float(20.5)              # 浮点数(float)
a = list(("pingguo", "li"))  # 列表(list)
b = tuple(("pingguo", "li")) # 元组(tuple)
c = range(6)                 # 范围(range)
d = dict(name="zhangsan", age=30)  # 字典(dict)
e = set(("pingguo", "li"))   # 集合(set)
f = frozenset(("lanmei", "yingtao")) # 不可变集合(frozenset)
g = bool(5)                  # 布尔(bool)
h = bytes(5)                 # 字节(bytes)
i = bytearray(5)             # 字节数组(bytearray)
j = memoryview(bytes(5))     # 内存视图(memoryview)
k = None                     # NoneType类型

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)