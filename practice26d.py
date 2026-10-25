from functools import reduce
restaurants=["Spicy Hut","Burger King","Pizza Oven","Tandoori Nights","South Spice"]
categories=["Fast Food","Fast Food","Italian","North Indian","South Indian"]
avg_prices=[250,180,400,350,200]
items_sold=[120,200,90,70,150]
ratings=[4.6,3.8,4.4,3.5,4.7]
final_revenue=list(map(lambda price,sold,cat:(price*sold)+(2000 if cat=="Italian" else (1500 if cat=="North Indian" else (1000 if cat=="Fast Food" else 800))),avg_prices,items_sold,categories))
#print(final_revenue)
res_fv_r=list(zip(restaurants,final_revenue,ratings,items_sold))
filtered_dict={name:f_rev for name,f_rev,r,i_s in res_fv_r if r >=4.0 and i_s >=100}
print("Eligible Restaurants Revenue Dict:",filtered_dict)
#reduce_dict=reduce(lambda x,y:x>y,filtered_dict.values())
reduce_dict=reduce(lambda x,y:x if x>y else y,filtered_dict.values())
print("Maximum Final Revenue among Eligible:",reduce_dict)