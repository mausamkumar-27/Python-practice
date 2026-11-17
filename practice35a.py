class car:
    def __init__(self,brand,price,wheels="2"):
        self.brand=brand
        self.price=price
        self.wheels=wheels
    def display(self):
        print(f"Brand:{self.brand} | Price:{self.price} | Wheels:{self.wheels}")
car1=car("Tata",800000)
car2=car("Tesla",4500000,4)
car1.display()
car2.display()