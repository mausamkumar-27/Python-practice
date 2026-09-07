name="Mausam"
s=set(name)
print(s)
#dic=dict(s))
#print(dic)
#dic={s:name.count(name)}      cant use set as dict key
dic={}                          #ek empty dictionary banaya taki value is aa ske
for char in s:
    dic[char]=name.count(char)
print(dic.items())
for key,value in dic.items():
    print(f"{key}:{value}")
