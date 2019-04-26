def recursion():
    return recursion()

import sys
sys.setrecursionlimit(100)

def a(x):
    i=1
    num=1
    while i <= x:
        num=num * i
        i=i+1
    return num
a(5)

#factoroal_1.py

def factoroal(n):
    result=n
    for i in range(1,n):
        result *=1
    return result

number = int(input('请输入一个正整数：'))
result=factoroal(number)
print("%d 的阶层是： %d" % (number,result))



#factoroal_2.py
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
#number = int(input('请输入一个正整数：'))
number = int("10")
result=factorial(number)
print("%d 的阶层是： %d" % (number,result))
