def sorted_list(*tup):
    l1=list(tup)
    l1.sort(reverse=True)
    return l1
l2=sorted_list(45,12,89,23,67,9)
l3=max(l2)
l4=min(l2)
print(l2)
print("Maximum:",l3)
print("Minimum:",l4)