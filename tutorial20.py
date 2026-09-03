def name(first_name,last_name):
    print("Hello",first_name,last_name)
name(last_name="Kumar",first_name="Mausam")


a=int(input("Enter a No. "))
b=int(input("Enter  No. "))

def average(a=9,b=7):
    print("The averaage is: ",(a+b)/2)
average(a,b)
average(a,b=5)
average(a=5,b=9)
average()

