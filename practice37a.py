n=int(input("Enter a no.: "))
if n<1:
    print("Not Composite")
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("Composite No")
            break
    else:
        print("Not Composite")