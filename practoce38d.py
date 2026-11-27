n=int(input())
c=int(input())
p=int(input())
a=n*c
b=c+(n-p)*5
if p<=n:
    print(f"{a}")
else:
    print(f"{b}")