# 全局变量是在函数外部定义的变量，所有函数都能访问并使用它们。相对于局部变量只能在函数内部被访问，灵活度更高。

# 基本用法
x = 'myl'
def myFunc():
    print(x + '-python')
myFunc()
# 这里的 x 被视为全局变量，因此能在函数内直接调用。如果在函数内定义同名变量，则那个变量为局部变量，不会影响外部的全局变量。

# 同名局部变量
# 以下示例在函数内创建了和全局变量同名的变量，但只在函数内有
def myFunc():
    x = 'new-myl'
    print(x + '-python')
myFunc()
print(x + '-python')

# 运行结果中，函数内部输出的是 new-myl-python，函数外部输出的仍然是全局变量 x 原本的值 myl-python。


# global关键字
# 通常来说，在函数内部定义的变量只能在该函数内使用。然而，如果想在函数内部创建或修改全局变量，需要使用 global 关键字：

def myfunc():
    global x
    x = "new---python"
    print("new---python == " + x)
myfunc()
print("new---python == " + x)

# 如果已存在同名全局变量，使用 global 也能在函数内部对其进行修改：
def myfunc():
    global x
    x = "这是第二次修改的最终值"
    print("第二次修改全局： " + x)

myfunc()

print("第二次修改全局： " + x)
# 这样便成功改变了原本全局变量 x 的值。