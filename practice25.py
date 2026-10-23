items=["Laptop","Mouse","Keyboard","Monitor","Headphones",]
prices=[50000,500,1500,12000,2500]
quantities=[10,150,80,25,60]
ratings=[4.5,3.8,4.2,4.6,3.9]
a=list(zip(prices,quantities))
#print(a)
b=[p*q for p,q in a]
#print(b)
c=list(zip(items,b,ratings))
#print(c)
from functools import reduce
my_dict={i:j for i,j,k in c if k >=4.0}
grand_total=reduce(lambda x,y : x+y,my_dict.values())
print("Filtered Dictionary:",my_dict)
print("Grand total:",grand_total)