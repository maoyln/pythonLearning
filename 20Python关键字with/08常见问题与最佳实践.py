# 常见问题与最佳实践
# 常见错误

# 1、错误地认为 with 只能用于文件
# 错误：认为只有文件需要with
conn = sqlite3.connect('db.sqlite')
# 应该使用with语句

# 2、忽略__exit__的返回值：
class MyContext:
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 忘记返回True/False可能导致异常处理不符合预期
        pass


# 最佳实践

'''
优先使用 with 管理资源：对于文件、网络连接、锁等资源，总是优先考虑使用 with 语句
保持上下文简洁：with 块中的代码应该只包含与资源相关的操作
合理处理异常：在自定义上下文管理器中，根据需求决定是否抑制异常
利用多个上下文：Python 允许在单个 with 语句中管理多个资源
'''