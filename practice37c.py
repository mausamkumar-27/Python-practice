from functools import reduce 
n=int(input())
l=[int(i) for i in range(1,n+1)]
a=reduce(lambda x,y:x+y,l)
print("Total Sum:",a)