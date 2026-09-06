city1={"Tokyo","Madrid","Berlin","Delhi"}
city2={"Tokyo","Seoul","Kabul","Madrid"}
print(city1.isdisjoint(city2))
print(city1.issuperset(city2))
print(city1.issubset(city2))

city1.add("Channai")
print(city1)
#city1.remove("Kolkata")          Keyerror dega bcz use removeand kolkata absent in city1
#print(city1)

city1.remove("Tokyo")
print(city1)

city1.discard("Kolkata")
print(city1)                 #No KeyError bcz use discard

city1.discard("Berlin")
print(city1)
