# -*- encoding: utf-8 -*-
'''
@File	  :   Dict.py
@Time	  :	  2020/04/12 19:48:20
@Authur   :	  vegetdove
@Version  :   1.0
'''

class Dictclass :
    dict1 = {}
    def __init__(self, dict1):
        self.dict1 = dict1
    def del_dict(self,key) :
        del self.dict1[key]
    def get_dict(self,key) :
        print(self.dict1.get(key,"not found"))
    def get_key(self) :
        print(list(self.dict1))
    def update_dict(self,dict2):
        self.dict1.update(dict2)
        print(list(self.dict1))

dict1 = Dictclass({"name":"Bob","age":18,"score":100})
dict1.del_dict("score")
dict1.get_dict("name")
dict1.get_dict("score")
dict1.get_key()
dict1.update_dict({"score":100})
