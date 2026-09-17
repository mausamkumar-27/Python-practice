d={}
for i in range(1,6):
    fruits=input("Enter fruits name: ")
    quantity=float(input("Enter quantity in kg: "))
    d[fruits]=d.get(quantity,0)
print(d)