# 一行中赋多个不同值

# 你可以在同一行中给多个变量分别赋不同的值：
x, y, z = "chengzi", "xiangjiao", "yingtao"
print(x)
print(y)
print(z)

# 注意：变量数量必须与要赋的值数量匹配，否则会出现错误。

# 一行中赋值相同
x = y = z = 'myl'
print(x)
print(y)
print(z)

# 解包集合

# 当你有一个列表、元组等集合时，可以使用“解包”将其中的元素依次赋给多个变量：

mf = ['myl-jh','fj-jh','tt-jh','gg-jh']
x,y,z,t = mf

print(x)
print(y)
print(z)
print(t)

a, b, c = 1, 2, "runoob"

print(a)
print(b)
print(c)