# 4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.

path0 = "E:vegetdove/superintendent/learngit/homework3/"
import os
os.mkdir(path0+"img")                 # 创建目录
path1 = "E:vegetdove/superintendent/learngit/homework3/img/"
with open(path1+"X4G5.png","w") as f: # 创建文件
    pass
with open(path1+"A2S3.png","w") as f:
    pass
with open(path1+"D3F4.png","w") as f:
    pass
with open(path1+"G5H6.png","w") as f:
    pass
with open(path1+"J7K8.png","w") as f:
    pass
with open(path1+"K8L9.png","w") as f:
    pass
with open(path1+"V4B5.png","w") as f:
    pass
with open(path1+"N6M7.png","w") as f:
    pass
with open(path1+"C3V4.png","w") as f:
    pass
with open(path1+"X2C3.png","w") as f:
    pass


files = os.listdir(path1)

for filename in files:
    portion = os.path.splitext(filename)

    if portion[1] == ".png":          # 如果后缀是.png
        
        newname = portion[0] + ".jpg" # 重新组合文件名和后缀名
        filenamedir=path1 +filename
        newnamedir=path1+newname

        os.rename(filenamedir,newnamedir)