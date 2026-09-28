n=int(input())
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=" ")
    for k in range(i,i+1):
        print("*",end=" ")
    for l in range(1,2*(i-1)):
        if i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for m in range(i,i+1):
        if i==1:
            print("",end=" ")
        else:
            print("*",end=" ")
    print()
