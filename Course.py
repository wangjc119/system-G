import os

class Course:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)
        
if __name__ == "__main__":
    course = Course()
    course.getName()