name="Mausam"
s=set(name)
print(s)
#dic=dict(s))
#print(dic)
#dic={s:name.count(name)}      cant use set as dict key
dic={}
for char in s:
    print(char)

dic={char:name.count(char)}
print(dic)

