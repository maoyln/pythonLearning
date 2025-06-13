# Python支持三种主要的数值类型：

# int（整数）
# float（浮点数）
# complex（复数）

# 创建数值类型变量
# 当你给变量赋予数值时，Python会自动为其分配对应的数据类型：

x = 1       # 整数
y = 2.5     # 浮点数
z = 3j      # 复数

print(x) # 1
print(y) # 2.5
print(z) # 3j

print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'complex'>


print('---------黄金分割线-----------')

# 整数（int）
# 整数是正数或负数，不带小数点，长度不受限制：
x = 5
y = 12345678901234567890
z = -256

print(x) # 5
print(y) # 12345678901234567890
print(z) # -256

print(type(x)) # <class 'int'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'int'>



print('---------黄金分割线-----------')

# 浮点数（float）
# 浮点数是带小数点的数，或者使用科学计数法表示：
x = 1.5
y = -3.6
z = 35e3  # 表示35000.0

print(x) # 1.5
print(y) # -3.6
print(z) # 35000.0

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>


print('---------黄金分割线-----------')

# 复数（complex）
x = 3+5j
y = 5j
z = -3j

print(x) # (3+5j)
print(y) # 5j
print(z) # (-0-3j)

print(type(x))
print(type(y))
print(type(z))

print('---------黄金分割线-----------')
