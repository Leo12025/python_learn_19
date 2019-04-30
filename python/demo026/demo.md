###字典

拥有关键符号`{}`，也可以使用`dict()`创建字典
与序列不同的是，当你在序列中去更新不存在的项时会产生`索引未找到的`错误，而字典会`自动创建新的项`来存储

`dict()` 实际上是个 `工厂函数(类型)`
例如之前我们学习的`str()` `int()` `list()` `tuple()`都是工厂函数，他们通过`调用`的形式创建一个对`应类型的变量`，本身不属于类型的范围。

###字典的内建方法

**fromkeys()**
创建去返回一个新的字典 
参数名称|参数类型|是否可选|备注
-|-|-|-
S|var||键值
v|var|是|键值对应的值，不提供则为None

```python
dict1={}
dict1.fromkeys((1,2,3))


#返回示例
dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
```

```python
dict1={}
dict1.fromkeys((1,2,3),'number')

#返回示例
dict1.fromkeys((1,2,3),'number')
{1: 'number', 2: 'number', 3: 'number'}
```

`第二个参数只能是一个参数`
`其作用是创建一个字典，并不是修改值`


###访问字典的几个方法

**keys()**
将所有键 作为一个列表 用于输出

```python
dict1={}
dict1 = dict1.fromkeys(range(32),'zan')
dict1
for eachKey in dict1.keys():
    print(eachKey)

#返回示例
0
1
2
……
```

**values()**
将所有值 作为一个列表 用于输出

**items()**
将所有键值 作为一个列表 用于输出
```python
#输出示例
(0,'zan')
(1,'zan')
……
```

`当你去调用一个不存在的项会导致报错`

```python
print(dict1.get(32))

#输出示例
None

print(dict1.get(32,'米有'))
#输出示例
'米有'

print(dict1.get(31,'米有'))
#输出示例
'zan'
```

成员字符操作符 `in` or `not in`
```python
31 in dict1
#输出示例
True
```

`成员操作符在这里查找的是键，而不是值`

**clear()**
清空字典内容

原则上不建议使用`直接赋值空字典`的形式来清空字典，当字典同时被多个名称引用时，使用赋值空字典的形式不会导致彻底清空，而使用`clear()`的形式能够直接清空整个字典对象


**copy()**
浅拷贝，浅拷贝不等于赋值

```python
a={1:'one',2:'two',3:'three'}
b=a.copy
c=a
a
#{1: 'one', 2: 'two', 3: 'three'}
b
#{1: 'one', 2: 'two', 3: 'three'}
c
#{1: 'one', 2: 'two', 3: 'three'}
id(a)
#2710949971072
id(b)
#2710951914448
id(c)
#2710949971072
```
直接赋值的地址是`一致的`，但是copy()得到的是一个新的地址，修改原字典不影响新的字典

**pop()** **popitem()**

给键弹对应的值，给键弹出对应的项(随机!)

```python
a.pop(2)
#'tow'
a.popitem()
#(1,'one')
```

字典没有索引，但是有优先级之分
```python
a.setdefault('小白')
```
第二个参数给默认值(随机插入)

**updata()**
```python
b={'小白':'狗'}
a.update(b)
```
使用另一个字典来更新字典的值