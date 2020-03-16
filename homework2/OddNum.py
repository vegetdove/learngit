# -*- encoding: utf-8 -*-
'''
@File	  :   OddNum.py
@Time	  :	  2020/03/16 17:11:26
@Authur   :	  vegetdove
@Version  :   1.0
'''

# here put the import lib
import random

def OddNum(list1) :
    for i in range(len(list1)) :
        if list1[i] % 2 == 1 :
            print(list1[i],end=" ")

a = [0]
a.clear()
for i in range(0,10) :
    a.append(random.randint(1,100))

OddNum(a)