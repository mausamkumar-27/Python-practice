'''n=[2,5,8,11,14,17,20]
a=filter(lambda x:x%2==0,n)
b=list(map(lambda x:x**2,a))
print(b)

group1 = [45, 60, 75, 90, 82]
group2 = [75, 90, 33, 50, 60]
group3 = [90, 12, 75, 45, 88]

a=set(group1)
b=set(group2)
c=set(group3)

d=a.intersection(b)
e=d.intersection(c)
print(e)'''

from functools import reduce
n=[5,15,8,25,10,30]
a=filter(lambda x:x>10,n)
b=reduce(lambda x,y:x+y,a)
print("Total sum:",b)