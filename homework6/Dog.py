# -*- encoding: utf-8 -*-
'''
@File	  :   Dog.py
@Time	  :	  2020/04/12 17:24:57
@Authur   :	  vegetdove
@Version  :   1.0
'''

class Dog :
    def __init__(self, name, color, num, price):
        self.name = name
        self.color = color
        self.num = num
        self.price = price
    def buy(self) :
        self.num = self.num + 1
    def sell(self) :
        self.num = self.num - 1
    def amount(self) :
        print(self.num)

a = Dog("a","red",13,20)
b = Dog("b","black",10,50)
c = Dog("c","white",9,100)

a.sell()
a.sell()
b.buy()
c.buy()
c.sell()

a.amount()
b.amount()
c.amount()