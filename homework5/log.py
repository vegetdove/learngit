# 2  编写一个装饰器，
#    能记录其他函数调用的日志，将日志写入到文件中；

import time

def log(text) :
    def decorator(func) :
        def wrapper(*args,**kw) :
            print("%s %s():"%(text,func.__name__))
            with open("D://CodeProjects/PythonProjects/homework5/log.txt","w") as f :
                f.write("%s %s()"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("execute")
def now() :
    print("%s"%time.time())

now()