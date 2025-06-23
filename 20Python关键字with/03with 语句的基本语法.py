# with 语句的基本语法

# 基础用法

# with 语句的基本形式如下：
'''with expression [as variable]:
'''
'''
expression 返回一个支持上下文管理协议的对象
as variable 是可选的，用于将表达式结果赋值给变量
代码块执行完毕后，自动调用清理方法
'''


# 文件操作示例
with open('./example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件已自动关闭

# 这段代码等价于前面的 try-finally 实现，但更加简洁明了。