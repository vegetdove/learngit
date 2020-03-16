print("请输入一个年份",end=" ")
year = int(input())
if(year % 4 == 0 and year % 400 != 0) :
    print(year,"年是闰年")
else :
    print(year,"年不是闰年")