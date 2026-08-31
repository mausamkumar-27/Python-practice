n=int(input("Enter the Number: "))
if n>0 :
    print("Positive")
    if n%2==0:
        print("Positive even")
    else:
        print("Positive odd")  
elif n==0:
    print("Zero",n)
else:
    print("Negative")    

             