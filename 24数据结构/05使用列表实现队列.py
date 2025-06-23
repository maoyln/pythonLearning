# 使用列表实现队列
# 虽然 deque更高效，但如果坚持使用列表来实现队列，也可以这么做。以下是如何使用列表实现队列的示例：

# 1. 创建队列
queue = []

# 2. 向队尾添加元素
# 使用 append() 方法将元素添加到队尾：
queue.append('a')
queue.append('b')
queue.append('c')
print("队列状态:", queue)  # 输出: 队列状态: ['a', 'b', 'c']

# 3. 从队首移除元素
# 使用 pop(0) 方法从队首移除元素：
first_element = queue.pop(0)
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)            # 输出: 队列状态: ['b', 'c']

# 4. 查看队首元素（不移除）
# 直接访问列表的第一个元素：
front_element = queue[0]
print("队首元素:", front_element)    # 输出: 队首元素: b

# 5. 检查队列是否为空
# 检查列表是否为空：
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)     # 输出: 队列是否为空: False

# 6. 获取队列大小
# 使用 len() 函数获取队列的大小：
size = len(queue)
print("队列大小:", size)            # 输出: 队列大小: 2


print('---------黄金分割线-----------')


# 实例（使用列表实现队列）
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# 使用示例
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("队首元素:", queue.peek())    # 输出: 队首元素: a
print("队列大小:", queue.size())    # 输出: 队列大小: 3

print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False
print("队列大小:", queue.size())    # 输出: 队列大小: 2

# 虽然可以使用列表来实现队列，但使用 collections.deque 会更高效和简洁。它提供了 O(1) 时间复杂度的添加和删除操作，非常适合队列这种数据结构。