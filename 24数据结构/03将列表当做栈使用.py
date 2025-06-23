# 将列表当做栈使用
# 在 Python 中，可以使用列表（list）来实现栈的功能。栈是一种后进先出（LIFO, Last-In-First-Out）数据结构，意味着最后添加的元素最先被移除。
# 列表提供了一些方法，使其非常适合用于栈操作，特别是 append() 和 pop() 方法。

# 用 append() 方法可以把一个元素添加到栈顶，用不指定索引的 pop() 方法可以把一个元素从栈顶释放出来。

'''
栈操作
压入（Push）: 将一个元素添加到栈的顶端。
弹出（Pop）: 移除并返回栈顶元素。
查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
检查是否为空（IsEmpty）: 检查栈是否为空。
获取栈的大小（Size）: 获取栈中元素的数量。
'''

# 1、创建一个空栈
stack = []

# 2、压入（Push）操作
# 使用append()方法将元素添加到栈的顶端
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # 输出: [1, 2, 3]

# 3、弹出（Pop）操作
# 使用 pop() 方法移除并返回栈顶元素：
top_element = stack.pop()
print(top_element)  # 输出: 3
print(stack)        # 输出: [1, 2]

# 4、查看栈顶元素（Peek/Top）
# 直接访问列表的最后一个元素（不移除）：
top_element = stack[-1]
print(top_element)  # 输出: 2

# 5、检查是否为空（IsEmpty）
is_empty = len(stack) == 0
print(is_empty)  # 输出: False

# 6、获取栈的大小（Size）
# 使用 len() 函数获取栈中元素的数量：
size = len(stack)
print(size)  # 输出: 2

# 实例

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())  # 输出: 栈顶元素: 3
print("栈大小:", stack.size())    # 输出: 栈大小: 3

print("弹出元素:", stack.pop())  # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())    # 输出: 栈大小: 2

# 以上代码中，我们定义了一个 Stack 类，封装了列表作为底层数据结构，并实现了栈的基本操作。