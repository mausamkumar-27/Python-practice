
drivers=["Ramesh","Suresh","Amit","Vikram","Priya"]
distances=[450,300,600,250,500]
hours=[9,8,10,6,9]
fuel_used=[35,30,45,20,38]
ratings=[4.2,3.5,4.6,4.0,4.4]
tup_drivers=list(zip(drivers,distances,hours,fuel_used,ratings))
filtered_drivers={name:dist/fuel_use for name,dist,hrs,fuel_use,rat in tup_drivers if dist/hrs>=45 and rat>=4.0}
filtered_values=list(filtered_drivers.values())