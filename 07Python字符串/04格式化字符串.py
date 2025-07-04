# Python中优雅的字符串拼接方法
# 在 Python 中，我们无法直接使用加号+拼接字符串和数字，否则会出现错误：
# 但你可以通过使用f-strings或format()方法来轻松实现字符串与数字的拼接。

# f-strings（推荐方法）
# f-strings 是 Python 3.6 引入的新特性，现已成为格式化字符串的主流方式，语法简洁易读：
age = 36
txt = f"Wo jinnian {age} sui"
print(txt)  # 输出: Wo jinnian 36 sui


print('---------黄金分割线-----------')


# f-strings占位符与修饰符
# 在f-strings中，占位符内不仅可以放变量，也可以包含函数调用、表达式甚至数学运算：
price = 59
txt = f"Jiage shi {price} yuan"
print(txt)  # 输出: The price is 59 dollars


print('---------黄金分割线-----------')


# 你也可以在占位符中加入数学运算或其他Python代码：
txt = f"Zong jine wei {20 * 59} yuan"
print(txt)  # 输出: Zong jine wei 1180 yuan


print('---------黄金分割线-----------')


# 使用 format() 方法
# 除了 f-strings，你还可以使用 format() 方法来格式化字符串：

age = 36
txt = "Wo jinnian {} sui".format(age)
print(txt)  # 输出: Wo jinnian 36 sui


# 使用f-strings（推荐）或format方法，可以使字符串拼接更加清晰、高效，避免类型错误。


print ("我叫 %s 今年 %d 岁!" % ('小明', 10))



# python字符串格式化符号:

# 符   号	描述
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址


# 三引号

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)