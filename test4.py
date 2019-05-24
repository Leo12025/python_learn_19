class Nint(int):
    def __radd__(self,other):
        return int.__sub__(self,other)
a=Nint(5)
b=Nint(3)
a+8 #8
1+b #2 (由于 1 没有 __add__ 方法，因此调用了b的 __radd__ 方法来实现
#因为上面我们重写了 __radd__  的方法实现，因此此处结果与实际情况不符
#  传值时候 __radd__ 的self指的是 第二个参数，而other指的是第一个参数
# 特别注重参数位置的运算，例如减法，可以在 第3行 重写时候将参数调整为 other,self来实现


'''
定义赋值加法行为：+=
__iadd__
eg. a = a + b  => a += b => 加上后面的值并赋值给前面
'''

'''
一元操作符
'''