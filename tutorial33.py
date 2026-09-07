dict={"Name":"Mausam","age":19,"State":"Bihar","Pin":854104}
print(type(dict))
print(dict["Name"])
#print(dict[school])              give Name Error
print(dict.get("Name"))
#print(dict.get("school"))        give None
print(dict.keys())
print(dict.values())
print(dict.items())

for key in dict:
    print(key)
for value in dict:
    print(value)