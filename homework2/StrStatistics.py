# -*- encoding: utf-8 -*-
'''
@File	  :   StrStatistics.py
@Time	  :	  2020/03/16 17:24:45
@Authur   :	  vegetdove
@Version  :   1.0
'''

def StrStatistics(a) :
    m,n,j,k = 0,0,0,0
    for char in a :
        if(char>="A" and char<="z") :
            m+=1          
        elif(char>="0" and char<="9") :
            n+=1
        elif(char == " ") :
            j+=1
        else :
            k+=1
    print(f"字母有{m}个")  
    print(f"数字有{n}个")
    print(f"空格有{j}个")
    print(f"其他字符有{k}个")
    
print("请输入要统计的字符串")
a = input()
StrStatistics(a)