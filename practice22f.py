def print_car_details(**details):
    for key,value in details.items():
        print(key,value)
print_car_details(Brand="Toyota",Model="Fortuner",Year=2026,Color="Black")