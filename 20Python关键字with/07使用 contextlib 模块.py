# 使用 contextlib 模块
# Python 的 contextlib 模块提供了更简单的方式来创建上下文管理器：

from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例
with tag("h1"):
    print("这是一个标题")

'''
<h1>
这是一个标题
</h1>
'''