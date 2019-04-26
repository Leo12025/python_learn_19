###020 递归

`普通程序员使用迭代，天才程序员使用递归`

属于**算法**范畴而不属于Python的范畴

在生活中的例子：汉诺塔游戏、树结构的定义、谢尔宾斯基三角形

`递归就是函数调用自身`

```python
def recursion():
    return recursion()
```
如果我们不Ctrl+C的话会出错，Python3的递归深度默认是100层

设置python3的递归深度
```python
import sys
sys.setrecursionlimit(100)
```

递归求阶层
写一个求阶乘的函数
 - 正整数阶乘指从1乘以2乘以3乘以4一直乘以所要求的数
 - 例如给的数是5，则阶乘式是1X2X3X4X5，得到的积是120，所以120就是4的阶乘

 `非递归版本`

```python
#factoroal_1.py
 def factoroal(n):
    result=n
    for i in range(1,n):
        result *=1
    return result
    
number = int(input('请输入一个正整数：'))
result=factoroal(number)
print("%d 的阶层是： %d" % (number,result))
```

`递归版本`

```python
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
```

`递归的两个特点：1)自己调用自身 2)设置了正确的返回值(当n=1时，会正确返回结果而不继续调用自身)`


```
假设我们n的值传入是5，那么：
    factorial(5) = 5 * factorial(4)
        factorial(4) = 4 * factorial(3)
            factorial(3) = 3 * factorial(2)
                factorial(2) = 2 * factorial(1)
                    factorial(1) = 1(return)
```

**递归具有危险性**

不能片面的认为递归比迭代好，递归消耗大量的栈空间和内存资源，并且自身调用自身容易产生危险性

求阶层建议不使用递归，汉诺塔可使用递归更加的精简


