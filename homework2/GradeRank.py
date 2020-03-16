# -*- encoding: utf-8 -*-
'''
@File	  :   GradeRank.py
@Time	  :	  2020/03/16 18:41:32
@Authur   :	  vegetdove
@Version  :   1.0
'''

# here put the import lib
import random

def RankJudge(grade) :
    if(grade >= 90) :
        return "A"
    elif(80 <= grade < 90) :
        return "B"
    elif(70 <= grade < 80) :
        return "C"
    else :
        return "D"

for i in range(0,20) :
    a = random.randint(0,100)
    print(a , RankJudge(a))