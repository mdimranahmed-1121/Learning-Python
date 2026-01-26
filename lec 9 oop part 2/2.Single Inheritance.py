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

Car1=ToyotaCar("Fortuner")
Car2=ToyotaCar("Pious")
print(Car1.name)
Car1.stop()
Car2.start()

        