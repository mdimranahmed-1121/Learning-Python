class Student:
    college_name="SCPSC" #class attributes
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

s1=Student("Imran",85)
s2=Student("Sajib",95)
print(s1.name,s1.marks,s2.name,s2.marks,sep="\n")
print(s1.college_name)