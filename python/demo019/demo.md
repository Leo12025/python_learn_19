##018 函数与过程

`函数function具有返回值、而过程procedure是简单的并且没有返回值`
**注意：python只有函数，没有过程**

```python
def hello():
    print('hello python')
temp=hello()
print(temp)
```

###返回值
```python
def back():
    return (1,'back',3.14)
    #return 1,'back',3.14 打包成一个元组并返回数据
back()
```

###函数的作用域问题

一般的编程语言都有`局部变量Local Variable`和`全局变量Global Variable`两种变量作用类型

||Global|Loacl|LocalA
:-|:-|:-|:-|
Global|Y|Y|Y
Local|Y|Y|
LocalA||Y|Y

`Local Variable`的作用域是单个函数内，无法在函数外进行调用
`Global Variable`的作用域是整个程序，在函数内外均可使用
前提是该函数已定义，全局变量的使用要小心

在函数内试图修改全局变量时，会自动创建一个局部变量替代原全局变量来替代，与全局变量互不影响。

`可以在函数内部访问全局变量但是不能修改`

```python
def discounts1(price,rate):
    final_price=price * rate
    old_price = 88 #这里试图修改全局变量
    print('修改后old_price的值是：',old_price)
    return final_price
old_price=float(input('请输入原价'))
rate=float(input('请输入折扣率：'))
new_price =discounts1(old_price,rate)
print('修改后的old_price的值是：',old_price)
print('打折后价格是：',new_price)
```
