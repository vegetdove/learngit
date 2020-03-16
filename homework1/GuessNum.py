import random
num = random.randint(1,50)
print("请输入最大猜数字次数")
N = int(input())
for i in range(1,N) :
    print("请输入你猜的数字")
    a = int(input())
    if(a == num) :
        print("猜对啦！")
        break
    elif (a < num) :
        print("猜小啦")
    elif (a > num) :
        print("猜大啦")
else :
    a = int(input())
    if(a == num) :
        print("猜对啦！")
    else :
        print("失败啦，下次加油")