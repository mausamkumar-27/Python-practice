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
s=input()
l=s.split(" ")
d={int(i):i.count() for i in l}
print(d)

