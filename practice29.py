class Employee:
    name="Mausam"
    language="Python"
    salary=120000
    def getinfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}.")
    def greet(self):
        print("Good morning!")
Mausam=Employee()
Mausam.getinfo()
Mausam.greet() 
   