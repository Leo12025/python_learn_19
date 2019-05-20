'''
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getPeri(self):
        return (self.x+self.y)*2
    def getArea(self):
        return self.x*self.y
rect=Rectangle(3,4)
rect.getPeri()
rect.getArea()

'''
'''
因为 new 传入的 str 是不可修改的值，因此无法使用 __init__ 来对 str 进行修改，
但是我们可以通过继承 str 类并重写 __new__ 函数来对 str 进行优先处理
然后回调 str 的 __new__ 方法进行字符串的构建


class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
a=CapStr("I happy.")
a
'''

'''
析构器 __del__ 并不是 del x 调用的，而是 Python 的垃圾回收机制将其回收时会进行的一个过程

当 对象没有被引用时 该方法才会被触发
'''



type(lem)
#class BIF
type(dir)
#class BIF
type(int)
#class type
class C:
    pass
type(C)
#class type
#类在定义的是时候叫做类 定义完之后叫做类对象

int('123')#现在是实例化一个对象并返回实例后的对象
'''
a+b => a.__add__(self,other=b)

通过改写 __add__ 方法实现 加法 的修改 

建议使用 继承 的形式定义class

'''