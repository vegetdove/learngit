from random import randint

args = {
    'Human': 0,
    'Dog': 1,
}

class Base(object):
    role = int()
    name = str()
    force = int()
    blood = int()

    def __init__(self, role:int, name:str, force:int, blood:int):
        self.role = args[role]
        self.name = name 
        self.force = force
        self.blood = blood   

    def attack(self, target):
        return target.injured(self.force) 
              
    def injured(self, value):
        self.blood -= value
        return self.blood
