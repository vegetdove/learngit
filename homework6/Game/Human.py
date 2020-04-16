from Base import Base

class Human(Base):
    def __init__(self, name):
        super().__init__('Human', name, 10, 100)

    def injured(self, value):
        res = super().injured(value)
        self.force -= 2
        if self.force <= 0:
            self.force = 1
        return res