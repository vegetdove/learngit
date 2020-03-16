print("0~50间的奇数为",end=" ")
for i in range(0,50) :
    if i % 2 == 1 :
        print(i,end=" ")
print("\n")

print("0~50间的偶数为",end=" ")
for i in range(0,50) :
    if i % 2 == 0 :
        print(i,end=" ")
print("\n")

print("0~50间的质数为",end=" ")
for i in range(2,51) :
    for j in range(2,i) :
        if (i % j == 0) :
            break
    else :
        print(i,end=" ")
print("\n")

print("0~50间能被2、3同时整除的数为",end=" ")
for i in range(0,50) :
    if i % 6 == 0 :
        print(i,end=" ")
print("\n")