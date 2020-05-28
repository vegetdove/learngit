# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；

from threading import Thread
import time
from random import randint

count = 0


def work1():
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程1:同学{count}的成绩为{grade}---")


def work2():
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程2:同学{count}的成绩为{grade}---")


def work3():
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程3:同学{count}的成绩为{grade}---")


def work4():
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程4:同学{count}的成绩为{grade}---")


def work5():
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程5:同学{count}的成绩为{grade}---")


t1 = Thread(target=work1)
t1.start()

t2 = Thread(target=work2)
t2.start()

t3 = Thread(target=work3)
t3.start()

t4 = Thread(target=work4)
t4.start()

t5 = Thread(target=work5)
t5.start()
