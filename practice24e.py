cities=["Delhi","Mumbai","Shimla"]
celcius_temps=[35,32,18]
dictionary={cc:(c*9/5)+32 for cc,c in zip(cities,celcius_temps)}
print(dictionary)