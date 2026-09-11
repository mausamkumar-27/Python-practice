list=[5,7,9,11]
name=input("Enter your name: ")
try:
    print(list[5])
    if name=="Mausam":
        print("Your name matches the criteria!")

except IndexError:
    print("Your index is out of range")
finally:
    print("This block will always run !")