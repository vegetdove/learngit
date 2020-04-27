# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX   

# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
#      系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  
#      如果都正确,打印提示, 您登录成功(失败);


import hashlib

student = []
perstudent = []
with open("E:vegetdove/superintendent/learngit/homework4/info.txt","r") as f :
    for line in f.readlines() :
        perstudent = list(line.strip().split(" ")) #将每行学生信息切分成字符串存入数组
        student.append(list(perstudent))           #存入二维数组

def admin() :
    name = input("请输入姓名：")
    for i in student :
        if(i[0]==name) :
            numr = i[1]
            passr = i[2]
            num = str(input("请输入账号:"))
            if(num == numr) :
                password = input("请输入密码:")
                md5 = hashlib.md5()
                md5.update(password.encode("utf-8"))
                if(md5.hexdigest()==passr):
                    print("登陆成功！")

admin()