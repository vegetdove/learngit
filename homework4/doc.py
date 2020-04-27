# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX   

import hashlib

f = open("E:vegetdove/superintendent/learngit/homework4/info.txt","w")

class Student:

    def __init__(self, name, num, password):
        self.name = name
        self.num = num
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        self.password = md5.hexdigest()

    def __str__(self):
        return "%s %s %s" % (self.name, self.num, self.password)

    def writeToFile(self, f):
        f.write(self.__str__())
        f.write('\n')

if __name__ == '__main__':
    a = Student('Tom', 'admin', '123')
    b = Student('Jack', 'root', '145')
    c = Student('a', 'eww', '234')
    d = Student('b', '34fr', '4444')
    e = Student('c', 'rftg', '5588')
    a.writeToFile(f)
    b.writeToFile(f)
    c.writeToFile(f)
    d.writeToFile(f)
    e.writeToFile(f)