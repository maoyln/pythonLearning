# 在其他语言中，缩进通常只是为了提高可读性，而在Python中，缩进却是划分代码块的关键。例如：
if 5 > 2:
    print('这是一个正确语句')

# 如果你省略了必要的缩进，Python会抛出错误：
if 5 > 3:
 print('zhengque') # 必须有缩进


if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")

# 如果同一个代码块里出现如下不一致的缩进，将会导致错误：