from functools import reduce
products=["Laptop","Smartphone","Wireless Earbuds","Smartwatch","Tablet"]
product_types=["Electronics","Electronics","Accessories","Gadgets","Electronics"]
unit_prices=[60000,25000,2500,4500,18000]
quantities_sold=[3,8,12,4,6]
ratings=[4.7,3.8,4.5,4.2,4.1]
final_revenue=list(map(lambda prices,quantities,products:(prices*quantities)+(2000 if products=="Electronics" else(1000 if products=="Gadgets" else 300)),unit_prices,quantities_sold,product_types))
#print(final_revenue)
my_dict=dict(map(lambda product,f_r,rat,sold:(product,f_r) if rat >=4.0 and sold >=5 else(product,0) ,products,final_revenue,ratings,quantities_sold))
reduce_dict=reduce(lambda x,y:x if x>y else y,my_dict.values())
print("Eligible Products Revenue Dict:",my_dict)
print("Maximum Final Order Amount among Eligible:",reduce_dict)