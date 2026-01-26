class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        avg=sum(self.marks)/3
        print("Hello",self.name,".Your average score is:",avg)
    
marks=Student('Imran',[85,87,89])
marks.get_avg()
