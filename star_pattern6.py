n=int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        if j==n+i-1 or j==n-i+1:
            print("*", end=" ")
        else:
            print(" ",end=" ")