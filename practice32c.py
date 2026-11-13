n=[2,5,8,11,14,17,20]
a=filter(lambda x:x%2==0,n)
b=list(map(lambda x:x**2,a))
print(b)