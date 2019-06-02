from server import GetMCNHistory,time
import threading

#skey=""
status = True

def init():
    pass
    #global skey
    #skey=ServerInit()
def test():
    #print(skey)
    #sendmsg(skey,'代码部署正确，可以进行第二阶段','')
    #ReadMcnList()# 代码部署正确，可以进行第二阶段
    GetMCNHistory()
class myTheard(threading.Thread):
    def __init__(self,function,time):
        super().__init__()
        self.function = function
        self.time = time
    def run(self):
        global status
        while status:
            if self.function == "mcnlist":
                GetMCNHistory()
            time.sleep(self.time)

if __name__ == "__main__":
    init() # 这里把key初始化掉，并给skey赋值
    t1 = myTheard("mcnlist",30)
    t1.start()
    a = input("input:")
    while True:
        if a == "exit":
            status = False
            print('wait other theard with running')
            exit()
        a=input("input:")



            


