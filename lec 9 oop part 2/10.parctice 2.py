class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showdetails(self):
        print("Role:",e1.role)
        print("Department:",e1.department)
        print("Salary:",e1.salary)

        
class Engineer(Employee):
    def __init__(self,name, age):
        super().__init__(input("Role:"), input("Department:"), int(input("Salary:")))
e1=Engineer(input("Name:"),input("age:"))
e1.showdetails()
