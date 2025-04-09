'''class Teacher:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name  # 改為返回名稱'''



import os
from Person import Person

class Teacher(Person):
    def __init__(self, name,id):
        super().__init__(name,id)
    def getName(self):
        print(self.name)

if __name__ == "__main__":
    teacher1=Teacher('chris',123)
    teacher2=Teacher('Tom',124)
    teacher1.getName()