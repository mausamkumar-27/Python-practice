analyze_text=input("Enter something: ")
b=analyze_text.lower()
d={}
for i in b:
    d[i]=i.count(i)
    print(d)


