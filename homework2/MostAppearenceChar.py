# -*- encoding: utf-8 -*-
'''
@File	  :   MostAppearenceChar.py
@Time	  :	  2020/03/16 18:48:30
@Authur   :	  vegetdove
@Version  :   1.0
'''

def MostAppearence(string) :
    string1 = ",".join(string)
    result = {word:string1.split(",").count(word) for word in set(string1.split(","))}
    result1 = sorted(result, key = lambda k : result[k])
    result1.reverse()
    for j in result1 :
        print(j, ":", result[j])
        break

a = "iwuyrfwiiucydfyvbniuwyiiefvdcdewseweeeee"
MostAppearence(a)