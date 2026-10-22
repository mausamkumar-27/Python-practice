items=["Pen","Notebook","Bag"]
prices=[20,100,800]
quantities=[50,30,10]
dictionary={r:p*q for r,p,q in zip(items,prices,quantities)}
print(dictionary)