l=[]

for i in range(1,6):
    names=input("Enter names: ")
    #l=list(i)  # in keyword ke andar keval iterable items valid h
    #tup=tuple(i)   same as above reason
    #l=list(tup)      same reason
    l.append(names)
    tup=tuple(l)
vowel_list=[]
consonent_list=[]
for j in tup:
    if j[0].lower() in ('a','e','i','o','u'):
        vowel_list.append(j)
    else:
        consonent_list.append(j)

print(consonent_list)