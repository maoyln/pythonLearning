# 下面示例演示了列表的大部分方法：

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x')) # 2  1  0

a.insert(2, -1)
a.append(555)

print(a) # [66.25, 333, -1, 333, 1, 1234.5, 555]

print(a.index(333)) # 1

a.remove(333)

print(a) # [66.25, -1, 333, 1, 1234.5, 555]

a.reverse()

print(a) # [555, 1234.5, 1, 333, -1, 66.25]

a.sort()

print(a) # [-1, 1, 66.25, 333, 555, 1234.5]

# 注意：类似 insert, remove 或 sort 等修改列表的方法没有返回值。