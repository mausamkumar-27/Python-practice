"""from functools import reduce
n=int(input())
l=[float(1/i**2) for i in range(1,n+1)]
b=reduce(lambda x,y:x+float(y),l,0)
print(f"{b:.6f}")"""
s=int(input())
def geometric_sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return geometric_sum(1/(n-1)**2)+geometric_sum(1/(n-2)**2)
a=geometric_sum(s)
b=a+(1/s**2)
print(f"{b:.6f}")