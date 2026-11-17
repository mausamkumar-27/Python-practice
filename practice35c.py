'''class person:
    def __init__(self,name):
        self.name=name
p1=person("Mausam")
p1.name="   "
print(f"{p1.name}")'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if new_age<0:
            print("Error: Age cant be negative!")
        else:
            self._age=new_age
            print("Age updated successfully!")
p1=Person("Mausam",20)
#print(p1.age)
p1.age=-5
print(p1.age)
