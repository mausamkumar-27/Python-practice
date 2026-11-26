from functools import reduce
s=input()
k=int(input())
b=reduce(lambda x,y:x+int(y),s,0)
n=b*k
def sumDigit(n):
    if int(n)<10:
        return int(n)
    else:
        a=reduce(lambda x,y:x+int(y),n,0)
    return sumDigit(str(a))
d=sumDigit(str(n))
print(d)