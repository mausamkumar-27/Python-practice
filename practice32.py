'''class student:
    name="Aman"
    branch="CSE"
s1=student()
print(f"{s1.name} is studying {s1.branch}")

class car:
    def start(self):
        print(f"Car is starting...")
my_car=car()
my_car.start()'''

class student:
    def study(self):
        print(f'Student is studying...')
    def sleep(self):
        print(f"Student is sleeping...")
s1=student()
s1.study()
s1.sleep()