items=["Laptop","Mouse","Keyboard","Monitor","Headphones",]
prices=[50000,500,1500,12000,2500]
quantities=[10,150,80,25,60]
ratings=[4.5,3.8,4.2,4.6,3.9]
a=list(zip(prices,quantities))
b=[p*q for p,q in a]
c=list(zip(items,b,ratings))
my_dict={i:j for i,j,k in c if ratings >=4.0}
print(my_dict)