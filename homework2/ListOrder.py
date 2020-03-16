# -*- encoding: utf-8 -*-
'''
@File	  :   ListOrder.py
@Time	  :	  2020/03/16 19:12:49
@Authur   :	  vegetdove
@Version  :   1.0
'''

# here put the import lib
import random

def Order(a) :
    a.sort()
    print("排序后的数组为:",a)

list1 = [0]
list1.clear()
for i in range(0,10) :
    list1.append(random.randint(1,100))
Order(list1)