def modified_list(*tup):
    l1=list(tup)
    last_item=l1.pop()
    l1.insert(0,last_item)
    return l1
l3=modified_list("Apple","Banana","Cherry","Mango")
print(l3)