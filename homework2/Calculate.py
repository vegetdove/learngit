# -*- encoding: utf-8 -*-
'''
@File	  :   Calculate.py
@Time	  :	  2020/03/16 19:18:06
@Authur   :	  vegetdove
@Version  :   1.0
'''

def Calculate(a,b,c) :
    result = 0
    if(c == "+") :
        result = a + b
    elif(c == "-") :
        result = a - b
    elif(c == "*") :
        result = a * b
    elif(c == "/") :
        result = a / b
    return result
print("请输入第一个数：")
a = int(input())
print("请输入第二个数：")
b = int(input())
print("请输入运算符：")
c = input()
result = Calculate(a,b,c)
print("运算式为",end=" ")
print(f"{a}{c}{b} = {result}")