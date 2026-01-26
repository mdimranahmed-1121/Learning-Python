class Student:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def greet():
        return 'hello'
s1=Student("Imran")
print(s1.greet(),s1.name)