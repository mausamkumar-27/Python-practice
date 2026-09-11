num1=input("Enter 1st no. ")
num2=input("Enter 2nd no. ")
try:
    result=int(num1)/int(num2)
    print(f"Your ans:{result}")
except ValueError:
    print("Please enter integers only!")
except ZeroDivisionError:
    print("Impossible to divide by Zero")
else:
    print("Result matches successfully!")