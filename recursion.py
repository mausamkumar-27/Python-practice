'''def fun(n):
    if n<1:
        return 
    else:
        print(n,end=" ")
        fun(n-1)
fun(5)
print()'''
'''def asc(n):
    if n<1:
        return
    asc(n-1)
    print(n,end=" ")
asc(5)
print()'''
'''def total(n):
    if n<1:
        return 0
    elif n==0:
        return 0
    else:
        total(n-1)
        return n+total(n-1)
a=total(5)
print(a)'''
'''def total(n):
    if n<1 or n==0:
        return 0
    else:
        return n+total(n-1)
        total(n-1)
a=total(5)
print(a)'''
'''def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
c=gcd(4,15)
print(c)'''

'''def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
c=gcd(42,9)
print(c)'''

'''def gcd(a,b):
    if a==0:
        return b
    else:
        return gcd (b%a,a)
c=gcd(8,69)
print(c)'''
n=int(input())
for i in range (n,0,-2):
    print(i,end=" ")
print()