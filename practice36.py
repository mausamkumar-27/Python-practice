class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_details(self):
        print(f"Employee Name:{self.name},ID:{self.id}")
class Programmer(Employee):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language=language
    def show_language(self):
        print(f"{self.name} codes in {self.language}")
p1=Programmer("Mausam",101,"Python")
p1.show_details()
p1.show_language()