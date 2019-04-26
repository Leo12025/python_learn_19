**匿名函数**`lambda关键字`

```python
def ds(x):
    return 2 * x +1
ds(5)
```

```python
lambda x:2*x+1
```
`冒号前面是原函数的参数，右边则是原函数的返回值`

lambda 其实是构建了一个函数对象，那么可以直接将其赋值给一个变量作为函数使用

```python
g=lambda x:2*x+1
g(5)
```

冒号前面的参数可以使用逗号隔开

```python
lambda x,y:x+y
a=lambda x,y:x+y
g(3,4)
```

####作用
Python写一些执行脚本时，使用`lambda`就可以省下定义函数过程，比如说我们周四hi需要写歌简单的脚本来管理服务器时间，我们就不需要专门去定义一个函数然后再写调用，使用`lambda`就可以使得代码更加精简。

对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，有时候给函数起个名字也是比较头疼的问题，使用`lambda`就不需要考虑命名的问题了。

简化代码的可读性，由于初学者函数阅读经常要跳到开头`def`定义部分，使用`lambda`函数就可以省去这样的步骤。

##两个牛逼的BIF

`filter()`
过滤器：filter(function, iterable)

```python
list(filter(None,[1,0,False,True]))
```
可以筛选出`[1, True]`

创建一个可以过滤出奇数的过滤器

```python
def odd(x): #定义一个函数 求余=1也为True(见上方)
    return x%2
temp=range(10) #获的一个0-10的列表
show=filter(odd,temp) #给出函数的名称，python会自行寻找
list(show)
```
可以筛选出`[1, 3, 5, 7, 9]`

上述代码也可以使用`lambda`关键字来构建
```python
list(filter(lambda x:x%2,range(10)))
```

`map()`
映射：
参数：一个函数和一个可迭代的序列（参数）

```python
list(map(lambda x:x*2,range(10)))
```

`[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]`

将可迭代参数的各个数据放进函数里面去加工，然后返回一个新的可迭代序列

