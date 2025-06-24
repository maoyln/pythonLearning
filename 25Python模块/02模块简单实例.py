# 下面是一个使用 python 标准库中模块的例子。
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')

# 执行命令：python .\25Python模块\02模块实例.py '你好' 'maoyl'
# 输出
'''
你好
maoyl

Python 路径为： ['F:\\work\\myPythonLearning\\25Python模块', 
'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 
'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 
'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 
'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313', 
'C:\\Users\\maoyl\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages'] 
'''

# 关键词
# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。