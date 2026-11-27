n=int(input())
c=int(input())
p=int(input())
a=n*c
b=a+(p-n)*5
if p<=n:
    print(f"{a}")
else:
    print(f"{b}")