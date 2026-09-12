analyze_text=input("Enter something: ")
b=analyze_text.lower().replace(' ','')
d={}
for i in b:
   #if i!=' ':
       d[i]=d.get(i,0)+1
print(d)