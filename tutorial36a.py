num1=input("Enter 1st numbers: ")
num2=input("Enter 2nd numbers: ")
division=int(num1)/int(num2)
try:
    print(f"Your ans is {division}")
except ValueError:
    print("Please enter numbers only!")
except ZeroDivisionError:
    print("Division by Zero is impossible")