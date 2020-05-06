# 5  通过Python来模拟实现一个txt文件的拷贝过程;


import sys

path0 = "E://vegetdove/superintendent/learngit/homework4/txt0.txt"
path1 = "E://vegetdove/superintendent/learngit/homework4/txt1.txt"

def copy(path0,path1) :

    content = ""
    with open(path0,"r") as f :
        content = f.read()

    with open(path1,"w") as f :
        f.write(content)
    
copy(path0,path1)