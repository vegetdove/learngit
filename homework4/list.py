# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#     提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)

from collections import deque
from datetime import datetime,timedelta

l = [1,2,3,4,5,6,7,8,9,"a"]
a = datetime.now()
l.append(2)
l.insert(0,"v")
b = datetime.now()
print((b-a).seconds)

q = deque([1,2,3,4,5,6,7,8,9,"a"])
c = datetime.now()
q.append(2)
q.appendleft("v")
d = datetime.now()
print((d-c).microseconds)