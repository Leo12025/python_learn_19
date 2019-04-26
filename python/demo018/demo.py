def MyFirstFunction(name):
    "函数定义过程中的name是叫形参"
    #因为Ta只是一个形式，表示占据一个参数位置
    print('传递进来的'+name+'叫做实参，因为Ta是具体的参数值')
MyFirstFunction('测试')

MyFirstFunction.__doc__
help(MyFirstFunction)

def saySame(name="system",words="null value"):
    print(name+"->"+words)
saySame()#能正确输出 system->null value
saySame('ceshi')#能正确输出 ceshi->null value
saySame(words="测试语句",name="系统")

def test(*params):
    print('参数的长度是',len(params))
    print('第二个参数是',params[1])
test(1,'test',2,3,4,5)

def test1(*params,name):
    print('参数的长度是',len(params))
    print('第二个参数是',params[1])
    print('name参数是',name)
test1(1,'test',2,3,4,5,name='1')