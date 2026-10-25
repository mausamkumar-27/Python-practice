warehouses=["Delhi","Mumbai","Kolkata","Chennai","Bangalore"]
weights=[120,250,180,300,90]
distances=[1200,800,1500,600,450]
transport_modes=["Air","Truck","Air","Train","Truck"]
base_rates=[12,8,15,6,7]
tup_all=list(zip(warehouses,weights,distances,transport_modes,base_rates))
print(tup_all)
ship_cost=list(map(lambda ware,w,d,t,b:w*d*b,warehouses,weights,distances,transport_modes,base_rates))
print(ship_cost)
#ship_cost=[w*d*b for ware,w,d,t,b in tup_all]
'''transport_ship_tup=list(zip(transport_modes,ship_cost))
#surcharge_ship_cost=list(map(lambda t,tc:tc+t if t=="Air" return 3000 or t=="Truck" return 1000 or t=="Train" return 500)
surcharge_ship_cost=list(map(lambda t,tc:tc+(3000 if t=="Air" else (1000 if t=="Truck" else(500 if t=="Train" else 0)))))
tup_final=list(zip(warehouses,surcharge_ship_cost,distances))
my_dict={ware:ssc for ware,ssc,dist in tup_final if ssc>=100000 and dist>=500}
print(my_dict)'''