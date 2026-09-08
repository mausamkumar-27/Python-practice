numbers=[12,7,19,24,33,46,51,68]
evens=[]
odds=[]
for no in numbers:
    if(no%2==0):
        no.append(evens)
    else:
        no.append(odds)
print(evens)
print(odds)