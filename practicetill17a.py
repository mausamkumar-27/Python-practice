'''n=int(input("Enter the Number: "))
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

for i in range(10,2,-2):
    print(i)
'''
x=int(input("Enter the No: "))
match x:
    case 2:
        print("x is two")
    case 3:
        print("x is Three")  
    case _ if x<0:
        print("x is Negative") 
    case _ if x%2==0:
            print("x is Even") 
    case _ :
        print("Not Matching")              