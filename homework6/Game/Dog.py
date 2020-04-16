from Base import Base

class Dog(Base):
    def __init__(self, name):
        super().__init__('Dog', name, 15, 80)

    def injured(self, value):
        res = super().injured(value)
        self.force -= 3
        if self.force <= 0:
            self.force = 1
        return res