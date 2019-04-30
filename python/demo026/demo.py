dict1={}
#dict1.fromkeys((1,2,3))
dict1.fromkeys((1,2,3),'number')


dict1={}
dict1 = dict1.fromkeys(range(32),'zan')
dict1
for eachKey in dict1.keys():
    print(eachKey)

print(dict1.get(32))

print(dict1.get(32,'米有'))

31 in dict1



a={1:'one',2:'two',3:'three'}
b=a.copy()
c=a
a
b
c
id(a)
id(b)
id(c)


b={'小白':'狗'}
a.update(b)