#age=int(input("Enter your age: "))          hmesha input try block ke andar lo,yahan if string("a","b") daal diya to program try block ke pehle hi crash ho jaayega
try:
    age=int(input("Enter your age: "))
    if age<0 or age>120:
        raise ValueError("age in between 0 to 120!")
except:
    print(f"Please entered valid age!")