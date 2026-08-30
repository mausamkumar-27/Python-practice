x=int(input("Enter a No.: "))
match x:
    case 0:
        print("x is Zero")
    case 4:
        print("x is four")
    case _ if x<0:
     print("x is Negative")
    case _ if x%2==0:
     print("x is Even") 
    case _ :
     print("x is odd & not matching above")

    
    
