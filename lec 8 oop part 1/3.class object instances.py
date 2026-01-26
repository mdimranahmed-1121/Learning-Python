class Student:
    college_name='Savar Cantonment Public School & College' #class attributes

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("Imran",95)
s2=Student("Ashik",85)
print(s1.name,s1.marks,s1.college_name)
print(s2.name,s2.marks,s2.college_name)
        