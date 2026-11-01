from functools import reduce
products="charger,battery,adapter,cable"
stocks="150,200,120,300"
zones="zoneA,zoneB,zoneA,zoneC"
Authorized_zones="zoneA,zoneB,zoneD"
surge_Add=25

product_list=products.split(",")
stock_list=list(map(int,stocks.split(",")))
zone_list=zones.split(",")
Auth_z_list=Authorized_zones.split(",")
updated_stock=list(map(lambda x:x+surge_Add , stock_list))
combined_data=list(zip(product_list,updated_stock,zone_list))
auth_zone_set=set(Auth_z_list)
my_dict={product:(zone,stock) for product,stock,zone in combined_data if zone in auth_zone_set}
#print(my_dict)
total_revenue=reduce(lambda x,y:x+y,list(my_dict.values()))
for product,details in my_dict.items():
    zone,stock=details
    print(f"Item:{product.strip().capitalize()} | Zone Autorized:{zone} | Updated Stock:{stock}")
print(f"Total Warehouse Inventory Stock Sum:{total_revenue}")