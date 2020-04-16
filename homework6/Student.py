# -*- encoding: utf-8 -*-
'''
@File	  :   Student.py
@Time	  :	  2020/04/12 19:36:44
@Authur   :	  vegetdove
@Version  :   1.0
'''

class Student :
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self) :
        print(self.name)
    def get_age(self) :
        print(self.age)
    def get_course(self) :
        print(max(self.score))

student1 = Student("张三",19,(44,64,32))
student2 = Student("李四",20,(98,68,87))

student1.get_name()
student1.get_course()
student2.get_age()
student2.get_course()