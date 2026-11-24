from functools import reduce
n=input()
k=int(input())
def superDigit(n):
    if int(n)<10:
        return n
    else:
        l=[int(i) for i in n]
        s=reduce(lambda x,y:x+y,l)
        total=s*k
    return total
b=superDigit(n)
print(b)