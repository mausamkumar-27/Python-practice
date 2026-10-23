items=["Laptop","Mouse","Keyboard","Monitor","Headphones",]
prices=[50000,500,1500,12000,2500]
quantities=[10,150,80,25,60]
ratings=[4.5,3.8,4.2,4.6,3.9]
from functools import reduce
combined=zip(items,prices,quantities,ratings)
filterd_tuple=filter(lambda x:x[3]>=4.0,combined)
map_paired=map(lambda x:(x[0],x[1]*x[2]),filterd_tuple)
my_dict=dict(map_paired)
grand_total=reduce(lambda a,b:a+b,my_dict.values())
print("Filtered Dictionary:",my_dict)
print("Grand Total:",grand_total)
