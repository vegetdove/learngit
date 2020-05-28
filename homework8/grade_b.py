# 1  有100个同学的分数：数据请用随机函数生成；
#      B 利用线程池来实现；

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from random import randint

count = 0


def work(n):
    global count
    for i in range(20):
        grade = randint(0, 100)
        count += 1
        print(f"----线程{n}:同学{count}的成绩为{grade}分---")


if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=5)
    futures = []
    for i in range(5):
        future = executor.submit(work, i+1)
        futures.append(future)
    executor.shutdown(True)