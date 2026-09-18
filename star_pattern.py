'''n=int(input())
for i in range(1,n+1):
    #print("*"*i,end=" ")
    print("* " * i)'''


n=int(input())
for i in range(1,n+1):
    star=2*i-1
    space=2*n-star
    print(space*" ", end=" ")
    #print(star*"* ")
    print("* "*star)