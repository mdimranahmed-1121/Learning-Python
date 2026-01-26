class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stoped...")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type

car1=Fortuner("Petrol")
print(car1.type)
car1.start()


        