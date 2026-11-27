from functools import reduce
n=int(input())
l=[float(1/i**2) for i in range(1,n+1)]
b=reduce(lambda x,y:x+float(y),l,0)
print(f"{b:.6f}")