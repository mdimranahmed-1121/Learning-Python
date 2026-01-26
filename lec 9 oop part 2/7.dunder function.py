class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def ShowNumber(self):
        print(self.real,'i+',self.img,'j')
    def __add__(self,num2):
        Newreal=self.real+num2.real
        Newimg=self.img+num2.img
        return Complex(Newreal,Newimg)

s1=Complex(4,5)
num2=Complex(6,5)
s1.ShowNumber()
num2.ShowNumber()
num3=s1+num2
num3.ShowNumber()

