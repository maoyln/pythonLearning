# 算数运算符

# 运算符	描述	实例
# +	加 - 两个对象相加	a + b 输出结果 31
# -	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -11
# *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 210
# /	除 - x 除以 y	b / a 输出结果 2.1
# %	取模 - 返回除法的余数	b % a 输出结果 1
# **	幂 - 返回x的y次幂	a**b 为10的21次方
# //	取整除 - 往小的方向取整数	 >>> 9//2 得 4 >>> -9//2 得-5


a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)
 
c = a - b
print ("2 - c 的值为：", c)
 
c = a * b
print ("3 - c 的值为：", c)
 
c = a / b
print ("4 - c 的值为：", c)
 
c = a % b
print ("5 - c 的值为：", c)
 
# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b 
print ("6 - c 的值为：", c)
 
a = 10
b = 5
c = a//b 
d = 10 // 3
e = -10 // 3
f = -10 // -3
print ("7 - c 的值为：", c)
print ("7 - d 的值为：", d)
print ("7 - e 的值为：", e)
print ("7 - f 的值为：", f)

# 1 - c 的值为： 31
# 2 - c 的值为： 11
# 3 - c 的值为： 210
# 4 - c 的值为： 2.1
# 5 - c 的值为： 1
# 6 - c 的值为： 8
# 7 - c 的值为： 2
# 7 - d 的值为： 3
# 7 - e 的值为： -4
# 7 - f 的值为： 3