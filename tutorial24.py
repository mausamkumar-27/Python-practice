a=(1,"Mausam",True,9,11,34)
print(type(a))
b=(1,)
print(type(b))

name=("Mausam","Harry","Mansi","Aman","India",2,4,3,2,2,2,)
if "Mausam" in name:
    print("Yes,Mausam is Present")
else:
    print("No,Mausam is absent")    
short=name.count("Mausam") 
print(short) 

star=name.index(2,8,9)
print(star)

