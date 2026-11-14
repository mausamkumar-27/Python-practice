'''class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print(f"This car is a {self.brand} and its color is {self.color}.")
car1=car("Toyota","Red")
car2=car("Honda","Black")
car1.display()
car2.display()'''

def intro(name,dept,salary):
    print(f"Hi {name},Dept:{dept},Salary:{salary}")
emp_data={'name':'Rohit','dept':"Engineering",'salary':55000}
intro(**emp_data)
