class marks:
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
    @property
    def avg(self):
        return str((self.phy+self.che+self.math)/3)
    
student1=marks(98,94,90)
print(student1.avg)
student1.math=93
print(student1.avg)
