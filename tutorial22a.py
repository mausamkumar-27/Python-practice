n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:5])
print(n[::-1])
print(n[::-2])
print(n[1:8:2])
squares=[l*l for l in range(6)]
print(squares)
evens=[i for i in range(11) if i%2==0]
print(evens)
all_students=["Mausam","Harry","Ali","Shubham"]
short_list=[item for item in all_students if len(item)<4]
print(short_list)