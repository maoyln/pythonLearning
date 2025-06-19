# for...else
# 在 Python 中，for...else 语句用于在循环结束后执行一段代码。

for x in range(6):
  print(x)
else:
  print("Finally finished!")

'''
0
1
2
3
4
5
Finally finished!
'''


print('---------黄金分割线-----------')


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)
else:
  print("Finally finished!")

'''
Baidu
Google
Runoob
Taobao
Finally finished!
'''


print('---------黄金分割线-----------')


# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体，不会执行 else 子句：
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
循环数据 Baidu
循环数据 Google
菜鸟教程!
完成循环!
'''