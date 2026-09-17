l=[]
for i in range(1,6):
    names=input("Enter names: ")
    #l=list(i)  # in keyword ke andar keval iterable items valid h
    #tup=tuple(i)   same as above reason
    #l=list(tup)      same reason
    l.append(names)

print(l)