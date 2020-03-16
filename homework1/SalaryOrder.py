import operator
imployee = [
    [1,"张三",10,9000],
    [2,"李四",8,6000],
    [3,"小王",9,8000],
    [4,"小赵",5,6000],
    [5,"小刘",10,8000],
    [6,"小孙",12,4000],
    [7,"小杨",4,2000],
    [8,"小朱",2,10000],
    [9,"小飞",10,3000],
    [10,"小周",15,500]]
imployee.sort(key = operator.itemgetter(3),reverse=True)
print("10 名员工的员工信息按工资从高到低排列如下:")
print("[工号，姓名，工龄，工资]")
for i in range(len(imployee)) :
    print(imployee[i])