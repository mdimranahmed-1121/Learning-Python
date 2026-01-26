class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r * self.r   
    def perimeter(self):
        return 2 * 3.1416 * self.r       

c1 = Circle(int(input("Enter radius of circle:")))
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())
