# 2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

count = 1
with open("E:vegetdove/superintendent/learngit/homework3/input.txt","r") as f :
    for line in f.readlines() :
        print("line",count,":",line.strip())
        count += 1