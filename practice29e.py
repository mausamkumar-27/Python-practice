class student:
    def set_name(self,name):
        self.name=name
    def greet(self):
        print(f"Hello,my name is {self.name}")
s1=student()
s2=student()
s1.set_name("Mausam")
s2.set_name("Rahul")
s1.greet()
s2.greet()