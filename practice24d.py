items=["Pen","Notebook","Bag"]
prices=[20,100,800]
quantities=[50,30,10]
dictionary={items:p*q for p,q in zip(prices,quantities)}
print(dictionary)