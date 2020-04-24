# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 
# 然后按照分数从高到低进行排序输出

student = []
perstudent = []
with open("E:vegetdove/superintendent/learngit/homework3/student.txt","r") as f :
    for line in f.readlines() :
        perstudent = list(line.strip().split(" ")) #将每行学生信息切分成字符串存入数组
        perstudent[0] = int(perstudent[0])         #把字符串转化成整型
        perstudent[2] = int(perstudent[2])
        student.append(list(perstudent))           #存入二维数组

student = sorted(student,key = (lambda x:x[2]),reverse=True)
print(student)