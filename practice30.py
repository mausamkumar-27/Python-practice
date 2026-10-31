from functools import reduce
products="laptop,phone,tablet,headphone"
prices="50000,30000,20000,5000"
categories="Electronics,Electronics,Electronics,Accessories"
discounts=10
list_products=products.split(",")
list_prices=list(map(int,prices.split(",")))
list_categories=categories.split(",")

z_pro_price=list(zip(list_products,list_prices,list_categories))
#print(z_pro_price)
my_dict={product:(cat,(price * 90)/100) for product,price,cat in z_pro_price}
#print(my_dict)
dis_price=list(map(lambda x:(x*90)/100,list_prices))
total_revenue=reduce(lambda x,y:x+y,dis_price)
#print(total_revenue)
for product,details in my_dict.items():
    cat,final_price=details
    print(f"Product:{product.strip().capitalize()} | Category:{categories.strip().capitalize()} | Prices:{final_price}")
print(f"Total Revenue:{total_revenue}")