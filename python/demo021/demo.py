def ds(x):
    return 2 * x +1
ds(5)

lambda x:2*x+1

g=lambda x:2*x+1
g(5)

lambda x,y:x+y
a=lambda x,y:x+y
a(3,4)

help(filter)

list(filter(None,[1,0,False,True]))

def odd(x):
    return x%2
temp=range(10)
show=filter(odd,temp)
list(show)

list(filter(lambda x:x%2,range(10)))


list(map(lambda x:x*2,range(10)))