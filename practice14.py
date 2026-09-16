name=input()
d={}
s=set()
for i in name:
    d[i]=d.get(i,0)+1
    t=s.add(i)
print(t)
print(d)