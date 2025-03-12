import os

class Teacher:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)
        
if __name__ == "__main__":
    teacher = Teacher()
    teacher.getName()