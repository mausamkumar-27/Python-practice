num1=input("Enter 1st numbers: ")
num2=input("Enter 2nd numbers: ")

try:
    result=int(num1)/int(num2)
    print(f"Your ans is {result}")
except ValueError:
    print("Please enter numbers only!")
except ZeroDivisionError:
    print("Division by Zero is impossible")