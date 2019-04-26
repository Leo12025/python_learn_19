def hello():
    print('hello python')
    return 0
temp=hello()
print(temp)


def back():
    return (1,'back',3.14)
back()


def discounts(price,rate):
    final_price=price * rate
    return final_price
old_price=float(input('请输入原价'))
rate=float(input('请输入折扣率：'))
new_price =discounts(old_price,rate)
print('打折后价格是：',new_price)


def discounts1(price,rate):
    final_price=price * rate
    old_price = 88 #这里试图修改全局变量
    print('修改后old_price的值是：',old_price)
    return final_price
old_price=float(input('请输入原价'))
rate=float(input('请输入折扣率：'))
new_price =discounts1(old_price,rate)
print('修改后的old_price的值是：',old_price)
print('打折后价格是：',new_price)