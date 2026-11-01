from functools import reduce
panel="panel_alpha,panel_beta,panel_gamma,panel_delta"
energy="450,380,520,290"
sector="SectorA,SectorB,SectorA,SectorC"
approved_sector="SectorA,SectorB,SectorD"
bonus=50
panel_list=panel.split(",")
energy_list=list(map(int,energy.split(",")))
sector_list=sector.split(",")
approved_s_list=approved_sector.split(",")
updated_energy=list(map(lambda x: x+bonus,energy_list))
combined_data=list(zip(panel_list,sector_list,updated_energy))
approved_s_set=set(approved_s_list)
my_dict={name:(approved,u_energy, approved in approved_s_set) for name,approved,u_energy in combined_data}
#print(my_dict)
for p_name,details in my_dict.items():
    a,e,is_authorised = details
    print(f"Panel:{p_name.strip().capitalize()} | Sector Approved:{is_authorised} | Final Energy:{e}")
total_revenue=reduce(lambda x,y :x+y,[e for a,e,is_authorised in my_dict.values() if is_authorised])
print(f"Total Revenue:{total_revenue}")