class Employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name:{self.name}")
emp=Employee("Mausam")
print(emp.name)
emp.display()