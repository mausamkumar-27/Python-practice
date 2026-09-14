'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")        #Horizontally cursor ko rok rha hu according to inner loop condition
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


