name=input("Enter Something Here: ")
name=name.replace(' ','')
d={}
s=set()
for i in name:
    d[i]=d.get(i,0)+1
    #s=s.add(i)
    s.add(i)
print(s)
print(d)