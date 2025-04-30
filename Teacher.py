class Teacher:
    def __init__(self, name):
        self.name = name
        self.email = ''

    def getName(self):
        return self.name

    def setEmail(self, email):
        if '@' in email:
            self.email = email
        else:
            raise ValueError("Email格式錯誤，請包含 '@'")

    def getEmail(self):
        return self.email
