'''n=[2,5,8,11,14,17,20]
a=filter(lambda x:x%2==0,n)
b=list(map(lambda x:x**2,a))
print(b)'''

group1 = [45, 60, 75, 90, 82]
group2 = [75, 90, 33, 50, 60]
group3 = [90, 12, 75, 45, 88]

b=group1.intersection(group2)
c=b.intersection(group3)
print(c)