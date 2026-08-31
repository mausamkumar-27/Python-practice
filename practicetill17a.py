n=input("Enter the Number: ")
print(int(n))
if n>0 :
    print("Positive",n)
    if n%2==0:
        print("Positive even",n)
    else:
        print("Positive odd",n)  
elif n==0:
    print("Zero",n)
else:
    print("Negative",n)             