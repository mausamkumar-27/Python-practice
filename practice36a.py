class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show_info(self):
        print(f"Brand:{self.brand},Top speed:{self.speed} km/h")
    class ElectricCar(Vehicle):
        def __init__(self,brand,speed,battery_range):
            super().__init__(brand,speed)
        def show_battery(self):
            print(f"{self.brand} has range of {self.battery_range} km/h")
car1=ElectricCar("Tata Nexon EV",150,450)
car1.show_info()
car1.show_baterry()