from functools import reduce
s=input()
k=int(input())
b=reduce(lambda x,y:x+int(y),s,0)
n=b*k
def sumDigit(q):
    if int(q)<10:
        return int(q)
    else:
        a=reduce(lambda x,y:x+int(y),q,0)
    return sumDigit(str(a))
d=sumDigit(str(n))
print(d)