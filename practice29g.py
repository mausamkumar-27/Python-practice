class employee:
    def data(self,name,salary):
        self.name=name
        self.salary=12*salary
    def annual(self):
        print(f"Employee {self.name} Annual Salary:{self.salary}")
emp1=employee()
emp2=employee()
emp1.data("Mausam",150000)
emp2.data("Hardik",120000)
emp1.annual()
emp2.annual()