##018 函数

###形参(parameter) 和实参(argument)

```python
def MyFirstFunction(name):
    "函数定义过程中的name是叫形参"
    #因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的'+name+'叫做实参，因为Ta是具体的参数值')
MyFirstFunction('测试')
```
**注意：函数必须先`定义`再调用，否则会产生 `not define` 错误**

###函数文档
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
`"函数_文档字符串"`
函数文档可以使用`MyFirstFunction.__doc__`来进行打印，也可以通过`help(MyFirstFunction)`打印

###关键字参数
主要处理多参数时候的顺序等
```python
def saySame(name,words):
    print(name+"->"+words)
saySame(words="测试语句",name="系统")
```

###默认参数
**定义了默认值的参数**
```python
def saySame(name="system",words="null value"):
    print(name+"->"+words)
saySame() #能正确输出 system->null value
saySame('ceshi') #能正确输出 ceshi->null value
saySame(words="测试语句",name="系统")
```

###收集参数 可变参数
```python
def test(*params):
    print('参数的长度是',len(params))
    print('第二个参数是',params[1])
test(1,'test',2,3,4,5)
```
将可变参数打包成一个`元组`，如果在可变参数后还有参数的话需要使用关键字参数进行传递，否则会合并在可变参数内
```python
def test(*params,name):
    print('参数的长度是',len(params))
    print('第二个参数是',params[1])
    print('name参数是',name)
test(1,'test',2,3,4,5,name='1')
```
也可以在定义的时候给与默认参数，这样即使没有按照关键字参数传值也不会导致异常