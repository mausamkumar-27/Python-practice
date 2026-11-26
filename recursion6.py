from functools import reduce
s=input()
k=int(input())
b=reduce(lambda x,y:x+int(y),s,0)
c=b*k
def sumDigit(n):
    if n<10:
        return n
    else:
        a=reduce(lambda x,y:x+int(y),n,0)
    return sumDigit(a)
sumDigit(c)