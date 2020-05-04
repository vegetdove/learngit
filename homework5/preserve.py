#3  编写一个装饰器，为多个函数加上认证的功能
# （必须输入用户的账号密码，才能调用这个函数）

import time,random

def outer(func) :
    def inner() :
        name = input("name = ")
        password = input("password = ")
        if(name == "Bob" and password == "123") :
            print("log in successfully!")
            func()
        else :
            print("log in error")
    return inner

@outer
def rantime() :
    t = random.randrange(1,5)
    time.sleep(t)
    print("%ss are used"%t)
rantime()