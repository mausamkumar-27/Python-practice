
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
print(my_dict)