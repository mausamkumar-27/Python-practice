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
my_dict={product:(zone,stock,zone in auth_zone_set) for product,stock,zone in combined_data }
#print(my_dict)
total_revenue=reduce(lambda x,y:x+y,[stock for zone,stock,is_authorised in my_dict.values() if is_authorised])
for product,details in my_dict.items():
    zone,stock,is_authorised=details
    print(f"Item:{product.strip().capitalize()} | Zone Autorized:{is_authorised} | Updated Stock:{stock}")
print(f"Total Warehouse Inventory Stock Sum:{total_revenue}")