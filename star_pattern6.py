n=int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        if j==n+i-1 or j==n-i+1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    for k in range(n+1,2*n):
        if k==n+1 or k==2*n-1 or i==2*n-1:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()