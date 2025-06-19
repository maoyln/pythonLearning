# break 和 continue 语句及循环中的 else 子句

## break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
## continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。


# while 中使用 break：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

'''
4
3
循环结束。
'''

print('---------黄金分割线-----------')


# while 中使用 continue：

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

'''
4
3
1
0
循环结束。
'''


print('---------黄金分割线-----------')


for letter in 'Runoob':     # 第一个实例
   if letter == 'n':
      break
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当前变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print ("Good bye!")

'''
当前字母为 : R
当前字母为 : u
当前变量值为 : 10
当前变量值为 : 9
当前变量值为 : 8
当前变量值为 : 7
当前变量值为 : 6
Good bye!
'''

print('---------黄金分割线-----------')


# 以下实例循环字符串 Runoob，碰到字母 o 跳过输出：

for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")

'''
当前字母 : R
当前字母 : u
当前字母 : n
当前字母 : b
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 4
当前变量值 : 3
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
Good bye!
'''


print('---------黄金分割线-----------')


# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
# 如下实例用于查询质数的循环例子:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

'''
2  是质数
3  是质数
4 等于 2 * 2
5  是质数
6 等于 2 * 3
7  是质数
8 等于 2 * 4
9 等于 3 * 3
'''