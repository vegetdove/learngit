def fibo(n) :
    a, b = 0, 1
    print(0,end=" ")
    print(1,end=" ")
    for i in range(1,n+1) :
        while (a+b <= n) :
            a, b = b, a+b
            print(b,end=" ")
print("100 以内的斐波那契数列为")
fibo(100)