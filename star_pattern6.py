n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n):
        if j==n+i-1 or j==n-i+1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n):
    for k in range(1,2*n):
        if k==1 or k==2*n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()