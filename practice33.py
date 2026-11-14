class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(f"This car is a {self.brand} and its color is {self.color}.")
car1=car("Toyota","Red")
car2=car("Honda","Black")
car1.display()
car2.display()