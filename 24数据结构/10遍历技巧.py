# 遍历技巧

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave


print('---------黄金分割线-----------')



for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe


print('---------黄金分割线-----------')


# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
     print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

print('---------黄金分割线-----------')


# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# apple
# banana
# orange
# pear