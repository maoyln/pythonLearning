file = open('./example.txt', 'r')
try:
    content = file.read()
    print(content)
    # 处理文件内容
finally:
    file.close()


'''
这种写法存在几个问题：

容易忘记关闭资源：如果没有 try-finally 块，可能会忘记调用 close()
代码冗长：简单的文件操作需要多行代码
异常处理复杂：需要手动处理可能出现的异常
'''

# with 语句的优势

'''
with 语句通过上下文管理协议（Context Management Protocol）解决了这些问题：

自动资源释放：确保资源在使用后被正确关闭
代码简洁：减少样板代码
异常安全：即使在代码块中发生异常，资源也会被正确释放
可读性强：明确标识资源的作用域
'''