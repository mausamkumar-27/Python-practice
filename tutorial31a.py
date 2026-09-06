'''s1={"Mausam",2,4,2,4,5,6,65,20}
s2={"Kumar",2,4,3,4,6,5,65,19,76}
print(s1.union(s2))
#print(s1.update(s2)).       Sir why return o/p as None
s1.update(s2)
print(s1)

#print(s1.intersection(s2)).      ye 'Kumar',19'76 etc. dega bcz s2 ka sara item uodate kr s1 me daal chuka hai'''

city1={"Delhi","Mumbai","Londan","Hydrabad","Kota"}
city2={"Patna","Indore","Wizag","Kota","Londan"}
'''print(city1.intersection(city2))   
city=city1.intersection(city2)
print(city)'''

print(city1.intersection_update(city2))        #why again return o/p as None
