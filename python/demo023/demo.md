###递归

斐波那契数列

我们可以用数学函数来定义：
```
f(n) => 当 n=1 ，=1
        当 n=2 ，=1
        当 n>2 ，f(n-1)+f(n-2)
```

课间练习：假设我们需要求出经历了20个月后，总共有多少对小兔崽子？（迭代 vs 递归）

通过迭代实现的代码
```python
def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('input error')
        return -1
    while (n-2) > 0:
        n3 = n2+n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
result = fab(20)
if result != -1:
    print('=>%d' % result)
```

通过递归实现的代码
```python
def fab2(n):
    if n <1:
        print('input error')
    if n==1 or n==2:
        return 1
    else:
        return fab2(n-1) + fab2(n-2)
result = fab2(20)
if result != -1:
    print('=>%d' % result)
```

这在算法中叫做`分治思想`：将问题分解成较小问题，多层处理
