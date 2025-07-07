
# 打开文件
fo = open("./100maoyln.txt", "wb")
print ("文件名为: ", fo.name) # 文件名为:  ./100maoyln.txt

# 刷新缓冲区
fo.flush()

# 关闭文件
fo.close()