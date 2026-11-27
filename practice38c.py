"""from functools import reduce
n=int(input())
l=[float(1/i**2) for i in range(1,n+1)]
b=reduce(lambda x,y:x+float(y),l,0)
print(f"{b:.6f}")"""
s=int(input())
if s>0:
    print(f"{a:.6f}")
else:
    print("n must be positive")
def geometric_sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return ((1/n**2) + geometric_sum(n-1))
a=geometric_sum(s)
