# -*- encoding: utf-8 -*-
'''
@File	  :   LengthJudge.py
@Time	  :	  2020/03/16 16:24:15
@Authur   :	  vegetdove
@Version  :   1.0
'''

def LengthJudge(a) :
    if isinstance(a,list) :
        return(len(a))
    elif isinstance(a,tuple) :
        return(len(a))
    elif isinstance(a,str) :
        return(len(a))
a = [1,2,"fd",4,8]
l1 = LengthJudge(a)
print("列表对象长度为：",l1)
b = (1,3,5,7)
l2 = LengthJudge(b)
print("元组对象长度为：",l2)
c = "swioqedufrw"
l3 = LengthJudge(c)
print("字符串对象长度为：",l3)
