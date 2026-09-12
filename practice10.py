analyze_text=input("Enter something: ")
b=analyze_text.lower()
d={}
for i in b:
   d[i]=d.get(i,0)+1
print(d)