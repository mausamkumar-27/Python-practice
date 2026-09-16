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
    total=0         #tumhen vaiable define krna pdega loop se pehle
    if j%2!=0:
        total+=j
print(total)