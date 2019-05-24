'''
类的定制：基本要求
 - 定制一个计时器的类
 - start和stop方法代表启动计时和停止计时
 - 鸡舍定时器对象t1，print(t1)和直接调用t1均显示结果
 - 当计时器未启动或已经停止计时，调用stop方法会给予提示
 - 两个计时器对象可以进行相加：t1 + t2
 - 只能使用提供的有限资源完成
使用time模块的localtime方法获取时间
time.localtime返回struct_time的时间格式
表现你的类：__str__ 和 __repr__
__str__ ： 被print打印的时候调用
__repr__ ： 直接输出时候调用

一、不带括号时，调用的是这个函数本身 ，是整个函数体，是一个函数对象，不须等该函数执行完成
二、带括号（参数或者无参），调用的是函数的执行结果，须等该函数执行完成的结果
'''


import time as t

class MyTimer():
    def __init__(self):
        self.unit=['年','月','天','小时','分钟','秒']
        self.prompt="未开始计时！"
        self.lasted=[]
        self.starttime=0 #属性会覆盖方法！！
        self.stoptime=0

    def __str__(self):
        return self.prompt
    __repr__ =__str__

    def __add__(self,other):
        prompt = "总共运行了"
        result=[]
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+self.unit[index])
        return prompt

    # 开始计时
    def start(self):
        self.starttime = t.localtime()
        self.prompt="请先调用 stop() 停止计时！"
        print("计时开始...")

    # 停止计时
    def stop(self):
        if not self.starttime:
            print("提示：请先调用 start() 进行计时！")
        else:
            self.stoptime = t.localtime()
            self._calc()
            print("计时停止")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.stoptime[index] - self.starttime[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])+ self.unit[index])
        # 为下一轮计时初始化变量
        self.starttime=0 #属性会覆盖方法！！
        self.stoptime=0

