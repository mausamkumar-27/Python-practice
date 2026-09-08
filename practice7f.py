numbers=[12,7,19,24,33,46,51,68]
evens=[]
odds=[]
for no in numbers:
    if no%2==0:
        #no.append(evens)       beta list.append() hota hai
        evens.append(no)
    else:
        #no.append(odds)         beta list.append() hota hai
        odds.append(no)
print(evens)
print(odds)
#sum+=evens                aise sum nhhi hoga kyuki sum Python ka in-built function h & tu variable bhi usi naam se rakh diya to dono overwrite ho jaayega
print("Sum is: ",sum(evens))
print("Sum is: ",sum(odds))