# -*- encoding: utf-8 -*-
'''
@File	  :   Fibo.py
@Time	  :	  2020/03/16 18:34:11
@Authur   :	  vegetdove
@Version  :   1.0
'''

def fibo(n) : 
    a,b = 0,1
    print(a,end=" ")
    print(b,end=" ")  
    for i in range(1,n+1) :
        a,b = b,a+b
        if(b<=n) :
            print(b,end=" ")

print("请输入n作为斐波那契数列的限制")
a = input()
print("n以内的斐波那契数列为")
fibo(int(a))