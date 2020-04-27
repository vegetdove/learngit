# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX   

import hashlib

s = []
def stu() :
    name = input("name?")
    num = input("number?")
    password = input("password?")
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    s.append([name,num,md5.hexdigest()])
    with open ("E:vegetdove/superintendent/learngit/homework4/info.txt","w") as f :
        for i in s :
            f.write(str(i))
            f.write("\n")

for i in range(0,5) :
    stu()