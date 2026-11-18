class Employee:
    def __init__(self):
        # 1. ASLI DATA BOX (Memory mein tijori)
        self._salary = 25000

    # 2. GATE 1: GETTER (Sirf bahar data bhejne ka darwaza)
    @property
    def salary(self):
        return self._salary

    # 3. GATE 2: SETTER (Sirf andar data daalne aur check karne ka darwaza)
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 10000:
            print("Error: Salary 10000 se kam nahi ho sakti!")
        else:
            self._salary = new_salary
            print("Salary updated!")

# Execution Lines:
emp = Employee()        # Step A
emp.salary = 8000       # Step B
print(emp.salary)       # Step C