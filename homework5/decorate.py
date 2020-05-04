# 4  编写装饰器来实现，对目标函数进行装饰，分3种情况：
# 目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；


def decorate0(func) :
    def inner() :
        func()
    return inner

def decorate1(func) :
    def inner(*args,**kwargs) :
        func(*args,**kwargs)
    return inner

def decorate2(func) :
    def inner(*args,**kwargs) :
        res = func(*args,**kwargs)
        return res
    return inner

def prime(i) :
    if(i == 2) :
        return 1
    else :
        for j in range(2,i) :
            if(i%j == 0) :
                return 0
        else :
            return 1

@decorate0
def judge0() :
    for i in range(2,20000) :
        if(prime(i)) :
            print(i)

@decorate1
def judge1(m,n) :
    count = 0
    for i in range(m,n) :
        if(prime(i)) :
            count += 1
    print(count)

@decorate2
def judge2(m,n) :
    count = 0
    for i in range(m,n) :
        if(prime(i)) :
            count += 1
    return count

judge0()
judge1(2,10000)
k = judge2(2,5000)
print(k)