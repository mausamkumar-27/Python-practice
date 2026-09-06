city1={"Tokyo","Madrid","Berlin","Delhi"}
city2={"Tokyo","Seoul","Kabul","Madrid"}
'''city1.pop("Tokyo")         TypeError bcz tum predict nhi kr skte ki kon sa item poped hoga(unordered,unindexed)
print(city1)'''

city1.pop()
print(city1)

#print(city2.clear())             why return o/p  as None
city2.clear()
print(city2)


del city1
print(city1)