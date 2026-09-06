s1={"Mausam",2,4,2,4,5,6,65,20}
s2={"Kumar",2,4,3,4,6,5,65,19,76}
print(s1.union(s2))
#print(s1.update(s2)).       Sir why return o/p as None
s1.update(s2)
print(s1)

print(s1.intersection(s2))