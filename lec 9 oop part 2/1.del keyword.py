class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

s1=Student('Imran',1814037)
print(s1)
print(s1.name)        
print(s1.roll)
del s1.roll
del s1
print(s1.roll)
print(s1)