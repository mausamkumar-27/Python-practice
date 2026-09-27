from functools import reduce
l=[1,7,13,19]
l1=reduce(lambda x,y:x+y,l)
print(l1)