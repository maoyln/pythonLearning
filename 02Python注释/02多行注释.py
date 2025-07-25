# Python本身没有专门的多行注释语法，如果想写多行注释，常见做法是在每一行前都加上#：

# 这是一个注释
# 可以写在
# 多行上
print("Hello, World!")


# 或者，利用多行字符串（用三重引号引起来）来实现类似多行注释的效果，只要这一段字符串没有被赋值给变量，解释器就会自动忽略它：

# 双引号注释
"""
这是一段看似多行注释的字符串
因为没有赋值给变量
所以不会被执行
"""
print('上面是多行注释（双引号）')


# 单引号注释
'''
这是一段看似多行注释的字符串
因为没有赋值给变量
所以不会被执行
'''
print('上面是多行注释（单引号）')