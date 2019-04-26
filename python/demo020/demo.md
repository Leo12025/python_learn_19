###020 内嵌函数和闭包

`Global关键字`
在整个文件、项目内都可以访问到全局变量，作用域是最大的，在函数内仅仅访问全局变量，不可做修改，否则python会以`屏蔽Shadowing`的方式来保护全局变量

`屏蔽Shadowing`：在函数内创造一个相同名称的局部变量，从而不影响全局变量
```python
count=5
def MyFun():
    count=10
    print(10)
MyFun()
print(count)
```
在函数中修改全局变量：
在 变量定义前 增加`Global`关键字
```python
count=5
def MyFun():
    global count
    count=10
    print(10)
MyFun()
print(count)
```

##内嵌函数
允许在函数内定义新的函数：内置函数
```python
def fun1():
    print('fun1正在被调用...')
    def fun2():
        print('fun2正在被调用...')
    fun2()
fun1()
```

在全局作用域中调用函数内构建的函数会产生一个`函数未定义`的异常

###闭包
函数是编程的一个重要的组成结果，`编程范式（面向对象编程、面对过程编程）`。

从表现形式定义为：**如果在一个内部函数里对外部作用域（但不是在全局作用域的变量进行引用，那么内部函数被称为闭包**

```python
def funX(x):
    def funY():
        return x *y
    return funY
```

funY中的x的作用与在`函数外`但是不在`全局作用域`，那么这个`funY()`即称作为闭包

```python
def funX(x):
    def funY(y):
        return x *y
    return funY
i=funX(8)
type(i) #这里返回的是函数对象，即为funY
i(5) #函数调用
funX(8)(5)
```
```python
def fun1():
    x=5
    def fun2():
        x *=x
        return x
    return fun2
fun1()
```

```python
def fun1():
    x=[5]
    def fun2():
        x[0] *=x[0]
        return x[0]
    return fun2()
fun1()

```
`nonlocal`关键字
```python
def fun1():
    x=5
    def fun2():
        nonlocal x
        x *=x
        return x
    return fun2()
fun1()
```

**函数定义、调用子函数，但是外部无法调用函数内的子函数**