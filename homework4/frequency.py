# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.0/24段的ip;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip


import os
import random


path0 = "E://vegetdove/superintendent/learngit/homework4/ip.txt"

path1 = "172.25.254."

with open(path0,"w") as f :
    for i in range(1200) :
        num = str(random.randint(1,254))
        path = path1 + num
        f.write(path)
        f.write("\n")

with open(path0,"r") as f :
    content = f.read()

print("频率前10的IP为")
result = {ip:content.split().count(ip) for ip in set (content.split())}
result1 = sorted(result,key = lambda k : result[k])
result1.reverse()
i = 0
for j in result1 :
    if(i<10) :
        print(j)
        i += 1