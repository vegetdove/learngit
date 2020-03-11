# -*- encoding: utf-8 -*-
'''
@File	  :   test.py
@Time	  :	  2020/02/22 12:04:57
@Authur   :	  vegetdove
@Version  :   1.0
'''

# here put the import lib

# def TotalPrice(amount,price):
#     print(amount * price) 
# amount = int(input("请输入苹果总量"))
# price = int(input("请输入苹果单价"))
# print("苹果的总价为",end=" ")
# TotalPrice(amount,price)

# def ChangeList( a ):
#     print("a重新赋值之前的地址:",id(a))
#     a.append([1,2,3])
#     print("a重新赋值后的值:",a)
#     print("a重新赋值后的地址:",id(a))
# b = [20,30]
# print('b的地址:',id(b))
# ChangeList(b)
# print('传了参数后的b的地址:',id(b))
# print('b的值:', b )


# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# odd = filter(lambda x:x%2 == 1 , list1)
# print(list(odd))

def printinfo(argv,*vartuple):
    print(argv)
    print(vartuple)
    return

def printin(argv,**vardict):
    print(argv)
    print(vardict)
    return

printinfo(12,23,43,54)
printin(33,a=22,b=6)