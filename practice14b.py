s1=set()
s2=set()
for i in range(1,6):
    n1=int(input("Enter n1: "))
    n2=int(input("Enter n2: "))
    s1.add(n1)
    s2.add(n2)
s=s1.intersection(s2)
t=tuple(s)
for j in t:
    if j%2!=0:
     #sum+=j
     sum=sum+j
    print(sum)