class C:
    def __init__(self,size=10):
        self.size= size
    def getSize(self):
        return self.size
    def setSize(self,value):
        self.size=value
    def delSize(self):
        del self.size
    x=property(getSize,setSize,delSize) #使用 property 使得 x 与 size 挂钩


    class Rectangle():
        def __init__(self,width=0,height=0):
            self.width=width
            self.height=height
        def __setattr__(self,name,value):
            if name=='square':
                self.width=value
                self.height=value
            else:
                super().__setattr__(name.value) # 调用基类的方法
                # self.__dict__[name]=value 调用 __dict__ 的方式来实现
        def gatArae(self):
            return self.width * self.height
    


