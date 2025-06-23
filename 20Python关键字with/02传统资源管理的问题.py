file = open('example.txt', 'r')
try:
    content = file.read()
    print(contecnt)
    # 处理文件内容
finally:
    file.close()


'''
这种写法存在几个问题：

容易忘记关闭资源：如果没有 try-finally 块，可能会忘记调用 close()
代码冗长：简单的文件操作需要多行代码
异常处理复杂：需要手动处理可能出现的异常
'''