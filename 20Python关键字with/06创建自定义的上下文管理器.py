# 创建自定义的上下文管理器
# 类实现方式
# 我们可以通过实现 __enter__ 和 __exit__ 方法创建自定义的上下文管理器：

class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
   
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False

# 使用示例
with Timer() as t:
    # 执行一些耗时操作
    sum(range(1000000))

print(range(1000000))
print(sum(range(1000000)))