count=5
def MyFun():
    global count
    count=10
    print(10)
MyFun()
print(count)


def fun1():
    print('fun1正在被调用...')
    def fun2():
        print('fun2正在被调用...')
    fun2()
fun1()

def funX(x):
    def funY(y):
        return x *y
    return funY
i=funX(8)
type(i)
i(5)
funX(8)(5)

def fun1():
    x=5
    def fun2():
        x *=x
        return x
    return fun
fun1()


def fun1():
    x=[5]
    def fun2():
        x[0] *=x[0]
        return x[0]
    return fun2()
fun1()

def fun1():
    x=5
    def fun2():
        nonlocal x
        x *=x
        return x
    return fun2()
fun1()