def modified_tup(*tup):
    return tup
t1=modified_tup(10,20,30,20,40,20,50)
t2=t1.count(20)
t3=t1.index(20)
print("Count of 20: ",t2)
print("First Index of 20: ", t3)