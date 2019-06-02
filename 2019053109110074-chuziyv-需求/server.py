from urllib.parse import urlencode
import requests as req
import re
import os,sys
from configparser import ConfigParser
import time

class Msg():
    skey=""
    text=""
    desp=""
    def __init__(self,text,*desp):
        try:
            f = open(r'skey.txt')
            self.skey=f.readline()
            f.close()
        except FileNotFoundError:
            self.skey="File is not found, write your skey from server in skey.txt please."
        self.text = text
        if len(self.desp) != 0:
           self.desp = desp[0]
        pass
    def send(self):
        url="https://sc.ftqq.com/"+self.skey+".send"
        print(url)
        parmars = {}
        parmars.update(text=self.text)
        parmars.update(desp=self.desp)
        print(parmars)
        getDate = urlencode(parmars)# 不需要自己处理编码信息
        print(getDate)
        reqs = req.get(url,getDate)
        print(reqs.status_code,reqs.content)
        pass
    @property
    def setText(self,text):
        self.text = text
    @property
    def setDesp(self,desp):
        self.desp = desp
class NewGuildMsg(Msg):
    def __init__(self,guildName,guildUid,guildArea,cTime):
        super().__init__("","")#初始化，你懂的，这里不需要啥东西
        self.text="新的公会入驻："+guildName
        self.desp="合作品类:"+guildArea+"  \n"+"公会Uid:"+guildUid+"  \n"+"入驻时间:"+cTime
        #换行遵循 MarkDown 语法，使用 [空格]+[空格]+[\n] 的形式完成空格，也可以在处理过程中分行加入此格式处理
        

def ServerInit():
    skey=''
    try:
        f = open(r'skey.txt')
        skey=f.readline()
        f.close()
    except FileNotFoundError:
        skey="File is not found, write your skey from server in skey.txt please."
    return skey

def SendMsg(skey,text,*desp):
    url="https://sc.ftqq.com/"+skey+".send"
    print(url)
    parmars = {}
    parmars.update(text=text)
    print(parmars)
    if len(desp) != 0:
        parmars.update(desp=desp[0])
    getDate = urlencode(parmars)# 不需要自己处理编码信息
    print(getDate)
    reqs = req.get(url,getDate)
    print(reqs.status_code,reqs.content)


def GetMCNHistory():
    #先获取在线列表，然后分解各个数据，倒conf表
    print('start GetMCNHistory in '+time.asctime())
    mcnList = ReadMcnList()
    if len(mcnList) == 0:
        print('mcnList is null value, check your internet connect please!')
        pass
    cfg = ConfigParser()
    cfg.read("mcnlist.ini")
    for list in mcnList:
        list1 = list
        #guildId = list1[0]
        guildName = list1[1]
        guildUid = list1[2]
        guildArea = list1[3]
        if cfg.has_section(guildName) == False:
            cfg.add_section(guildName)
            cfg.set(guildName, 'area', guildArea)
            cfg.set(guildName, 'uid', guildUid)
            cfg.set(guildName,'ctime',time.asctime())
            m1 = NewGuildMsg(
                guildName,
                cfg.get(guildName,'uid'),
                cfg.get(guildName,'area'),
                cfg.get(guildName,'ctime')
            )
            m1.send()
        else:
            #检查是否存在更改：
            if(cfg.get(guildName,'area') != guildArea):
                cfg.set(guildName, 'area', guildArea)
            if(cfg.get(guildName,'uid') != guildUid):
                cfg.set(guildName, 'uid', guildUid)
            #print(list1,guildName,guildUid,guildArea)
    with open('mcnlist.ini', 'w') as fw:
        cfg.write(fw)
    pass

def ReadMcnList():
    '''
    在线获取 MCN 机构列表
    来源：694号公告
    返回数据：    [['1', '娱加文化传媒', '253529768', '娱乐、电台、游戏'], ['2', '超电文化', '373856133', '游戏'], ['3', '大鹅文化', '304834208 ', '游戏、电台'], ['4', 'H6工作室', '111600803', '娱乐'], ['5', 'YS愈声', '388144512', '电台'], ['6', '炫石互娱','247182', '娱乐、游戏'], ['7', 'SG笙歌工作室', '411910114', '电台'], ['8', 'CX初心娱乐', '411912450', '电台'], ['9', 'TMG', '68493287', '娱乐、游戏、电台'], ['10', '初音', '412079264', '电台'], ['11', '王朝娱乐', '2083196', '电台'], ['12','FP互娱', '41147414', '娱乐'], ['13', 'GY文化', '266779856', '娱乐'], ['14', '花田文化', '222137749', '娱乐、电台'], ['15', '星灵传媒', '94475674', '电台'], ['16', '渝元文化', '4388187', '娱乐、电台'], ['17', '蜜橘文化', '25008516', '娱乐、电台、游戏'], ['18', '喵游', '24142421', '游戏'], ['19', '轩云文化', '270734246', '游戏'], ['20', '橘子传媒', '313835198', '游戏'], ['21', '星嘉文化', '15747663', '娱乐、游戏']]
    '''
    url="https://api.vc.bilibili.com/news/v1/notice/info?platform=pc&id=694"
    reqs=req.get(url)
    resourceData=reqs.json()
    content=resourceData['data']['content']
    #print(content)
    content = GetMiddleText(content,"<table","</table>")
    #print(content[0])
    content = content.replace("</td></tr>","nn")
    content = content.replace("</td>","mm")
    content = GetNotHTMLContent(content)
    content = GetMiddleText(content,"合作品类nn","nn1）")
    content = content.replace("&nbsp;","")
    mcnList=[]
    list = content.split('nn')
    for _ in list:
        list2 = _.split('mm')
        mcnList.append(list2)
        #for _1 in list2:
        #    print(_1)
        #print(_)
    #print(mcnList)
    '''
    [['1', '娱加文化传媒', '253529768', '娱乐、电台、游戏'], ['2', '超电文化', '373856133', '游戏'], ['3', '大鹅文化', '304834208 ', '游戏、电台'], ['4', 'H6工作室', '111600803', '娱乐'], ['5', 'YS愈声', '388144512', '电台'], ['6', '炫石互娱','247182', '娱乐、游戏'], ['7', 'SG笙歌工作室', '411910114', '电台'], ['8', 'CX初心娱乐', '411912450', '电台'], ['9', 'TMG', '68493287', '娱乐、游戏、电台'], ['10', '初音', '412079264', '电台'], ['11', '王朝娱乐', '2083196', '电台'], ['12','FP互娱', '41147414', '娱乐'], ['13', 'GY文化', '266779856', '娱乐'], ['14', '花田文化', '222137749', '娱乐、电台'], ['15', '星灵传媒', '94475674', '电台'], ['16', '渝元文化', '4388187', '娱乐、电台'], ['17', '蜜橘文化', '25008516', '娱乐、电台、游戏'], ['18', '喵游', '24142421', '游戏'], ['19', '轩云文化', '270734246', '游戏'], ['20', '橘子传媒', '313835198', '游戏'], ['21', '星嘉文化', '15747663', '娱乐、游戏']]
    '''
    
    return mcnList

def GetMiddleText(text,last,last2):
    pat = re.compile(last+'(.*?)'+last2,re.S)
    result = pat.findall(text)
    return result[0]

def GetNotHTMLContent(text):
    dr = re.compile(r'<[^>]+>',re.S)
    content = dr.sub('',text)
    return content

if __name__ == '__main__':
    ServerInit()

