# -*- encoding: utf-8 -*-
'''
@File	  :   StudentPack.py
@Time	  :	  2020/04/12 20:48:02
@Authur   :	  vegetdove
@Version  :   1.0
'''
class Student :
    def __init__(self, name, age, sex, English, math, Chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.English = English
        self.math = math
        self.Chinese = Chinese
    def result(self) :
        a = self.English + self.math + self.Chinese
        b = a/3
        print("总分为:",a)
        print("平均分为：",b)
        print(f"""
        学生基本信息为：
        姓名：{self.name}
        年龄：{self.age}
        性别：{self.sex}
        英语成绩：{self.English}
        数学成绩：{self.math}
        语文成绩：{self.Chinese}
        """)

a = Student("Bob",19,"男",100,98,20)
a.result()
