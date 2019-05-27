class Celsius:
    def __init__(self,value=26.0):
        self.value=float(value)

    def __get__(self,instance,owner):# 自身，所属实例对象，所属类
        return self.value

    def __set__(self,instance,value):
        self.value = float(value)
    

class Fahenheit:
    def __get__(self,instance,owner):
        return instance.cel *1.8 +32 #在获取华氏度时，调用 类实例对象（Teamperature）的cel属性来进行计算
    def __set__(self,instance,value):
        instance.cel=(float(value)-32) /1.8#调用描述符去定义

class Teamperature:
    #以下两个都时描述符属性（自身是个特殊类，有set、set、delect方法来实现读取与赋值、删除）
    cel =Celsius()
    fah=Fahenheit()