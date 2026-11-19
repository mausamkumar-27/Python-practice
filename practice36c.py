'''class Employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name:{self.name}")
emp=Employee("Mausam")
print(emp.name)
emp.display()'''
class student:
    def __init__(self,name,roll_no):
        self._roll_no=roll_no
class LPUstudent(student):
    def show_roll(self):
        print(f"Roll Number:{self._roll_no}")
s=LPUstudent("Mausam",101)
s.show_roll()
print(s._roll_no)