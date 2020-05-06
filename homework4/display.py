# 6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 
# 输出格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小


import os

print("名称             时间                类型        大小")

path0 = "E://vegetdove/superintendent/learngit/homework4/"

a = os.listdir(path0)

for i in a :

    path = path0 + i

    size = os.path.getsize(path)
    size = str(size) + "k"

    time = os.path.getatime(path)

    _type = os.path.isfile(path)
    judgement = ""
    if(_type == True) :
        judgement = "File"
    else :
        judgement = "Dir"

    print(i,"   ",time,"   ",judgement,"   ",size)