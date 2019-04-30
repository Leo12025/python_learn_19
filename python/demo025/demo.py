brand = ['BiliBili','AcFun','Dig']
slogan=['干杯','==','Why']
#值跟索引值没有对应关系，即 bilibili 与 0 没有关系
print('BiliBili的口号是：',slogan[brand.index('BiliBili')])

dict1={'bilibili':'干杯','AcFun':'被各种收买'}
print('B站的口还是:',dict1['bilibili'])

#键值组合：项  'bilibili':'干杯'

dict2={1:'one',2:'two',3:'three'}
dict2[2]

#创建空字典
dict3={}
dict3

dict3 =dict((('F',70),('i',105),('s',115)))
dict3

dict4=dict(bilibili='干杯',acfun='acfun~')
#注意： 此处的键不需要加引号，方便识别键、值
dict4
dict4['acfun']='我是a站'
dict4