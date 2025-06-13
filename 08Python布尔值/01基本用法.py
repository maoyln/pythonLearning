# Python布尔值及bool()函数用法解析
# 在Python中，布尔类型（Boolean）只有两个值：True 和 False。布尔值在条件判断和逻辑运算中起着至关重要的作用。

# 基本用法与比较运算
# 你可以通过比较运算符来获得布尔结果：

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False


print('---------黄金分割线-----------')


# 在条件语句中的布尔值
# 在if条件语句中，Python会自动评估表达式，并返回对应的布尔值：
if 10 > 9:
    print("Shi de, 10 dayu 9!")
else:
    print("Bu, 10 budayu 9!")


print('---------黄金分割线-----------')


# bool()函数评估数据类型
# 使用内置的bool()函数可以评估变量或值的布尔状态：

print(bool("nihao"))  # 输出 True
print(bool(15))       # 输出 True

x = ""
y = 0
print(bool(x))  # 输出 False (空字符串为False)
print(bool(y))  # 输出 False (0为False)


print('---------黄金分割线-----------')


# 哪些值在Python中被评估为True？
# 在Python中，几乎所有非空或非零的值都被评估为True：
print(bool("nihao"))
print(bool(123))
print(bool(["apple", "banana"]))


print('---------黄金分割线-----------')


# 哪些值会被视为False？
# 只有少数特定的值会被Python视为False，包括：
# False
# None
# 数值 0
# 空字符串 ""
# 空列表 []
# 空元组 ()
# 空字典 {}

# 示例代码：
print(bool(False))    # 输出 False
print(bool(None))     # 输出 False
print(bool(0))        # 输出 False
print(bool(""))       # 输出 False
print(bool([]))       # 输出 False


print('---------黄金分割线-----------')


# 函数返回布尔值
# 你还可以定义函数，让它们返回布尔值：
def myFunction():
    return True

if myFunction():
    print("Hanshu fanhui le True")
else:
    print("Hanshu fanhui le False")


print('---------黄金分割线-----------')


# 使用 isinstance() 检测类型
# Python内置的 isinstance() 函数也返回布尔值，可判断变量是否属于某个特定的数据类型：

x = 200
print(isinstance(x, int))  # 输出 True
print(isinstance(x, str))  # 输出 False


# 熟悉布尔类型的用法和特点，可以帮助你更清晰地表达逻辑关系，更轻松地编写出高质量的代码。