city1={"Tokyo","Madrid","Berlin","Delhi"}
city2={"Tokyo","Seoul","Kabul","Madrid"}
#print(city1.intersection(city2))
#print(city1.intersection_update(city2)).        why return o/p as None
city1.intersection_update(city2)
print(city1)