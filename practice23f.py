def original_tup(*tup):
    return tup
t1=original_tup(5,10,15,20,25)
l1=list(t1)
l1.pop(2)
l1.insert(2,99)
t2=tuple(l1)
print(f"Original Tuple :,{t1}")
print(f"Modified Tuple :,{t2}")