empty_dic={}
print(type(empty_dic))

empty_set=set()
print(type(empty_set))

#l=["Mausam",2,4,3,9,2]
#s={2,3,5,6,"Mausam",9,[8,4,5,"Mausam"]}
s={2,4,5,3,5,"Mausam"}
print(s)

#s[2]

#accessing set element
for i in s:
   # print(s)
    print(i)
if "Mausam" in s:
    print("yes")

s.add(20)
print(s)

