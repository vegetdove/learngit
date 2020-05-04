# 1  编写一个装饰器，能计算其他函数的运行时间；

import time,random

def outer(func) :
    def inner() :
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间为%ss"%(end_time-start_time))
    return inner

@outer
def rantime() :
    time.sleep(random.randrange(1,5))

rantime()