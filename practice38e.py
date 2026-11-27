p=int(input())
def no(n):
    if n==1:
        return 1
    else:
        return (-1)**(n+1)*(n**n)+no(n-1)
a=no(p)
print(a)