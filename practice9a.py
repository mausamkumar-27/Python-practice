list=[5,7,9,11]
name=input("Enter your name: ")
try:
    print(list[2])             #if tu list me out of range index daalta to if name wala code run hi nhi krta bcz direct except pr chal jaata
    if name=="Mausam":
        print("Your name matches the criteria!")
except ValueError:
    print("This is not your name!")

except IndexError:
    print("Your index is out of range")
finally:
    print("This block will always run !")