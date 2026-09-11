#age=int(input("Enter your age: "))          
try:
    if age<0 or age>120:
        raise ValueError("age in between 0 to 120!")
except:
    print(f"Your age is {age}.")