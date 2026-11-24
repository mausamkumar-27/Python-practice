from functools import reduce
n=input()
k=int(input())
def superDigit(n,k):
    if int(n)<10:
        return n
    else:
        l=[int(i) for i in n]
        s=reduce(lambda x,y:x+y,l)
        total=s*k
    return superDigit(str(total),1)
b=superDigit(n,k)
print(b)