'''class student:
    name="Aman"
    branch="CSE"
s1=student()
print(f"{s1.name} is studying {s1.branch}")

class car:
    def start(self):
        print(f"Car is starting...")
my_car=car()
my_car.start()

class student:
    def study(self):
        print(f'Student is studying...')
    def sleep(self):
        print(f"Student is sleeping...")
s1=student()
s1.study()
s1.sleep()'''

class BankAccount:
    def deposit(self,account_holder,amount):
        print(f"{account_holder} deposited {amount}")
    def withdraw(self,account_holder,amount):
            print(f"{account_holder} withdrew {amount}")
b1=BankAccount()
b1.deposit("Mausam",50000)
b1.withdraw("Rahul",10000)