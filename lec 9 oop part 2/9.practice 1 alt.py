import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return math.pi*self.r*self.r
    def perimeter(self):
        return 2*math.pi*self.r
    
c1=Circle(int(input("Enter the radius of circle:")))
print("Area:",c1.area())
print("Perimeter:",c1.perimeter())