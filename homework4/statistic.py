# 7 使用python代码统计一个文件夹中所有文件的总大小

import os


path0 = "E://vegetdove/superintendent/learngit/homework4/"

a = os.listdir(path0)
count = 0

for i in a :
    path = path0 + i
    size = os.path.getsize(path)
    count += size

print(f"文件夹{path0}中文件总大小为",count,"KB")