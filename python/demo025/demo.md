###字典
键(`Key`)值(`Value`)对应 - 映射类型

###创建和访问字典

`使用 列表 创建 伪键值对应`
```python
brand = ['BiliBili','AcFun','Dig']
slogan=['干杯','==','Why']
#值跟索引值没有对应关系，即 bilibili 与 0 没有关系
print('BiliBili的口号是：',slogan[brand.index('BiliBili')])
```

`使用字典来实现上面的代码`

```python
dict1={'bilibili':'干杯','AcFun':'被各种收买'}
print('B站的口还是:',dict1['bilibili'])
```

键值组合称之为`项`,即 `'bilibili':'干杯'` 就是一个项

`键 可以是字符串类型，也可以是整形或者变量`
```python
dict2={1:'one',2:'two',3:'three'}
dict2[2]
```

`跟其他类型一样，可以创建空字典`

```python
dict3={}
dict3
```

`因为字典只有一个参数 meeping 因此在直接创建字典时候需要使用多重括号包含起来，其中可以是元组或者列表`
```python
dict3 =dict((('F',70),('i',105),('s',115)))
dict3
```

```python
dict4=dict(bilibili='干杯',acfun='acfun~')
#注意： 此处的键不需要加引号，方便识别键、值
dict4
```


`可以直接通过键值对应修改他的值，如果没有找到该值的话会自动创建新的项来存放，不会产生错误`

```python
dict4=dict(bilibili='干杯',acfun='acfun~')
#注意： 此处的键不需要加引号，方便识别键、值
dict4
dict4['acfun']='我是a站'
dict4
```