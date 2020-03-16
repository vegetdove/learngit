# -*- encoding: utf-8 -*-
'''
@File	  :   LengthControl.py
@Time	  :	  2020/03/16 17:42:21
@Authur   :	  vegetdove
@Version  :   1.0
'''

# here put the import lib

def LengthControl(a) :
    for i in a :
        if(len(a[i]) > 2) :
            a[i] = a[i][0:2]
    return a

a = {"eue" : "iuke", "uoiy" : "0823", "ewuef":"9"}
a = LengthControl(a)
print(a)   