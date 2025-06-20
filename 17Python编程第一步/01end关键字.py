# end关键字
# python的基本写法上述都已经讲了，下面只补充一下end关键字

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b