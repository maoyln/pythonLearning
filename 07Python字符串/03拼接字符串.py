# Python字符串拼接基础操作
# 在Python中，我们经常需要将多个字符串连接成一个字符串，这个操作称为“字符串拼接”，常用的方式是使用加号（+）操作符。

# 拼接字符串基础示例
# 下面是一个简单的示例，将变量a和b拼接成新的变量c：
a = "Nihao"
b = "Maoyl"
c = a + b
print(c)  # 输出 NihaoMaoyl


print('---------黄金分割线-----------')


# 添加空格拼接
# 很多时候，你可能需要在两个字符串之间插入空格或其他符号，方法很简单：
a = "Nihao"
b = "Maoyl"
c = a + " " + b
print(c)  # 输出：Nihao Maoyl

# 注意事项
# 请注意，如果尝试将字符串与数字直接用+连接，会导致类型错误（TypeError）。你可以将数字转换成字符串后再拼接：

print('---------黄金分割线-----------')

age = 25
txt = "Wo jinnian " + str(age) + " sui."
print(txt)  # 输出：Wo jinnian 25 sui.

# 了解这些拼接技巧可以帮助你更灵活地组合文本数据，轻松应对日常开发中的字符串处理需求。